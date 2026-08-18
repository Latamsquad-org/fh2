# -*- coding: utf-8 -*-
# latamadmin.py - comandos de admin LatamSquad para FH2 (Python 2).
# AutoBalance: max diferencia 2. !ab on / !ab off / !ab (estado).
# !info: ronda (mapa, siguiente, tickets, jugadores). !info nombre: ficha admin.
# El motor BF2 no dispara PlayerChangeTeams al usar setTeam, se puede revertir.

import os
import sys
import time

try:
    import bf2
    import host
    _IN_GAME = True
except Exception:
    bf2 = None
    host = None
    _IN_GAME = False

# Max jugadores de diferencia entre equipos (10 vs 8 ok, 11 vs 8 no).
MAX_TEAM_DIFF = 2
TEAM_1 = 1
TEAM_2 = 2
# Delay para recontar despues de un disconnect (el jugador puede seguir en la lista).
REBALANCE_DELAY_SEC = 1.5
AB_CMD_COOLDOWN_SEC = 2
INFO_CMD_COOLDOWN_SEC = 3

GAMEMODE_LABELS = {
    'gpm_cq': 'Conquest',
    'gpm_coop': 'Coop',
    'sp1': 'SP1',
    'sp2': 'SP2',
    'sp3': 'SP3',
}

HUD_CHAT_PREFIXES = (
    'HUD_TEXT_CHAT_TEAM',
    'HUD_TEXT_CHAT_SQUAD',
    'HUD_TEXT_CHAT_DEADPREFIX',
    'HUD_CHAT_DEADPREFIX',
    '* ',
)


def strip_chat_hud_prefix(msg_text):
    """Quita prefijos HUD de chat BF2/FH2."""
    text = '' if msg_text is None else str(msg_text)
    for prefix in HUD_CHAT_PREFIXES:
        if text.startswith(prefix):
            text = text[len(prefix):].lstrip()
    return text


def parse_ab_command(msg_text):
    """
    Parsea !ab / !ab on / !ab off.
    Retorna None, 'status', 'on' o 'off'.
    """
    text = strip_chat_hud_prefix(msg_text).strip()
    if not text.startswith('!'):
        return None
    parts = text[1:].split()
    if len(parts) < 1:
        return None
    if parts[0].lower() != 'ab':
        return None
    if len(parts) == 1:
        return 'status'
    arg = parts[1].lower()
    if arg in ('on', '1', 'true', 'enable'):
        return 'on'
    if arg in ('off', '0', 'false', 'disable'):
        return 'off'
    return 'status'


def parse_bang_command(msg_text):
    """Separa !comando y argumentos. Retorna (cmd, args) o None."""
    text = strip_chat_hud_prefix(msg_text).strip()
    if not text.startswith('!'):
        return None
    parts = text[1:].split()
    if len(parts) < 1:
        return None
    cmd = parts[0].lower()
    if cmd == '':
        return None
    return (cmd, parts[1:])


def parse_info_args(args):
    """
    !info -> ('round', None, False)
    !info nombre -> ('player', nombre, False)
    !info nombre last -> ('player', nombre, True)
    !info #12 -> ('player', '#12', False)
    """
    if args is None:
        args = []
    parts = [str(x) for x in list(args)]
    last = False
    if parts and parts[-1].lower() == 'last':
        last = True
        parts = parts[:-1]
    if not parts:
        return ('round', None, last)
    return ('player', ' '.join(parts), last)


def pretty_map_name(map_id):
    """hurtgen_forest -> Hurtgen Forest."""
    text = str(map_id or '').replace('\\', '/').split('/')[-1].strip()
    if text == '':
        return '?'
    return text.replace('_', ' ').title()


def pretty_gamemode(mode):
    """gpm_cq -> Conquest."""
    key = str(mode or '').strip().lower()
    if key in GAMEMODE_LABELS:
        return GAMEMODE_LABELS[key]
    if key == '':
        return '?'
    return str(mode)


def parse_maplist_append_text(text):
    """Lee lineas mapList.append name mode layer."""
    entries = []
    if not text:
        return entries
    for line in str(text).splitlines():
        raw = line.strip()
        if raw.lower().startswith('rem '):
            continue
        parts = raw.split()
        if len(parts) < 4:
            continue
        if parts[0].lower() != 'maplist.append':
            continue
        entries.append({
            'name': parts[1],
            'mode': parts[2],
            'layer': parts[3],
        })
    return entries


def parse_maplist_list_output(text):
    """Parsea salida de mapList.list (N: name mode layer)."""
    entries = []
    if not text:
        return entries
    for line in str(text).splitlines():
        raw = line.strip()
        if ':' not in raw:
            continue
        _idx, rest = raw.split(':', 1)
        rest = rest.strip().replace('"', '')
        parts = rest.split()
        if len(parts) < 3:
            continue
        name = parts[0].replace('\\', '/').split('/')[-1]
        entries.append({
            'name': name,
            'mode': parts[1],
            'layer': parts[2],
        })
    return entries


def map_entry_at(entries, index):
    """Entrada de rotacion por indice, o None."""
    try:
        idx = int(index)
    except (TypeError, ValueError):
        return None
    if idx < 0 or idx >= len(entries):
        return None
    return entries[idx]


def format_map_entry(entry):
    """Ramelle (Conquest, 16) o ? si falta."""
    if not entry:
        return '?'
    return '%s (%s, %s)' % (
        pretty_map_name(entry.get('name')),
        pretty_gamemode(entry.get('mode')),
        entry.get('layer') or '?',
    )


def format_round_info_lines(data):
    """Lineas de !info (ronda). data es un dict con claves opcionales."""
    if data is None:
        data = {}
    lines = []
    server = data.get('server_name') or '?'
    lines.append('Servidor: %s' % server)
    lines.append('Mapa: %s' % (data.get('current') or '?'))
    lines.append('Siguiente: %s' % (data.get('next') or '?'))
    players = data.get('players')
    max_players = data.get('max_players')
    t1 = data.get('team1')
    t2 = data.get('team2')
    if players is None:
        players = '?'
    if max_players is None:
        max_players = '?'
    if t1 is None:
        t1 = '?'
    if t2 is None:
        t2 = '?'
    lines.append('Jugadores: %s/%s | equipos %s vs %s' % (
        players, max_players, t1, t2
    ))
    tk1 = data.get('tickets1')
    tk2 = data.get('tickets2')
    n1 = data.get('team1_name') or '1'
    n2 = data.get('team2_name') or '2'
    if tk1 is None:
        tk1 = '?'
    if tk2 is None:
        tk2 = '?'
    lines.append('Tickets: %s %s | %s %s' % (n1, tk1, n2, tk2))
    return lines


def player_name_matches(full_name, query):
    """True si query esta en el nombre completo o sin tag [CLAN]."""
    q = str(query or '').strip().lower()
    n = str(full_name or '').strip().lower()
    if q == '' or n == '':
        return False
    if n.find(q) != -1:
        return True
    if n.startswith('['):
        end = n.find(']')
        if end != -1:
            n2 = n[end + 1:].lstrip()
            if n2.find(q) != -1:
                return True
    return False


def format_player_info_lines(data):
    """Lineas de !info nombre (ficha). Equivalente FH2 de PR commandPlayerInfo."""
    if data is None:
        data = {}
    name = data.get('name') or '?'
    line1 = '%s:' % name
    extra = []
    team = data.get('team')
    if team not in (None, ''):
        extra.append('Equipo %s' % team)
    score = data.get('score')
    kills = data.get('kills')
    deaths = data.get('deaths')
    if score is not None or kills is not None or deaths is not None:
        extra.append('Score %s K %s D %s' % (
            score if score is not None else '?',
            kills if kills is not None else '?',
            deaths if deaths is not None else '?',
        ))
    ping = data.get('ping')
    if ping not in (None, ''):
        extra.append('Ping %s' % ping)
    if extra:
        line1 = '%s %s' % (line1, ' | '.join(extra))
    lines = [line1]
    ip = data.get('ip') or '?'
    lines.append('----->%s' % ip)
    if data.get('show_last'):
        lines.append('Historial last: no disponible en FH2 (sin bans PR).')
    return lines


def other_team(team):
    """Equipo contrario (1 <-> 2). Otro valor -> 0."""
    if int(team) == TEAM_1:
        return TEAM_2
    if int(team) == TEAM_2:
        return TEAM_1
    return 0


def counts_after_switch(t1, t2, from_team, to_team):
    """Simula el recuento si un jugador pasa de from_team a to_team."""
    nt1 = int(t1)
    nt2 = int(t2)
    if from_team == TEAM_1:
        nt1 -= 1
    elif from_team == TEAM_2:
        nt2 -= 1
    if to_team == TEAM_1:
        nt1 += 1
    elif to_team == TEAM_2:
        nt2 += 1
    if nt1 < 0:
        nt1 = 0
    if nt2 < 0:
        nt2 = 0
    return (nt1, nt2)


def is_switch_allowed(t1, t2, from_team, to_team, max_diff=MAX_TEAM_DIFF):
    """
    True si el cambio no empeora el balance por encima de max_diff.
    Permitido si el nuevo abs <= max_diff, o si mejora el abs actual.
    """
    from_team = int(from_team)
    to_team = int(to_team)
    if to_team not in (TEAM_1, TEAM_2):
        return False
    if from_team == to_team:
        return True
    old_diff = abs(int(t1) - int(t2))
    nt1, nt2 = counts_after_switch(t1, t2, from_team, to_team)
    new_diff = abs(nt1 - nt2)
    if new_diff <= int(max_diff):
        return True
    if new_diff < old_diff:
        return True
    return False


def smaller_team(t1, t2):
    """Equipo con menos jugadores, o 0 si empate."""
    t1 = int(t1)
    t2 = int(t2)
    if t1 < t2:
        return TEAM_1
    if t2 < t1:
        return TEAM_2
    return 0


def larger_team(t1, t2):
    """Equipo con mas jugadores, o 0 si empate."""
    t1 = int(t1)
    t2 = int(t2)
    if t1 > t2:
        return TEAM_1
    if t2 > t1:
        return TEAM_2
    return 0


def target_team_if_illegal(t1, t2, current_team, max_diff=MAX_TEAM_DIFF):
    """
    Si current_team deja el recuento ilegal, devuelve el equipo al que mover.
    t1/t2 YA incluyen al jugador en current_team.
    None si no hay que moverlo.
    """
    current_team = int(current_team)
    if current_team not in (TEAM_1, TEAM_2):
        weak = smaller_team(t1, t2)
        if weak == 0:
            return TEAM_1
        return weak
    if abs(int(t1) - int(t2)) <= int(max_diff):
        return None
    big = larger_team(t1, t2)
    if current_team != big:
        return None
    return other_team(current_team)


def _debug_log(message):
    try:
        print('latamadmin: %s' % message)
    except Exception:
        pass


def _player_valid_human(player):
    """True si el jugador existe, es humano y es valido."""
    if player is None:
        return False
    try:
        if not player.isValid():
            return False
        if player.isAIPlayer():
            return False
    except Exception:
        return False
    return True


def _safe_team(player):
    try:
        return int(player.getTeam())
    except Exception:
        return 0


def _safe_alive(player):
    try:
        return bool(player.isAlive())
    except Exception:
        return False


def _safe_commander(player):
    try:
        return bool(player.isCommander())
    except Exception:
        return False


def _safe_squad_leader(player):
    try:
        return bool(player.isSquadLeader())
    except Exception:
        return False


def _is_immune(player):
    try:
        return bool(getattr(player, 'immune_to_autobalance', False))
    except Exception:
        return False


def _player_name(player):
    try:
        return str(player.getName() or '')
    except Exception:
        return ''


def _load_admin_checker():
    """Carga get_admin_level_by_name + listas de python/admins.toml."""
    admin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'admin')
    if admin_dir not in sys.path:
        sys.path.append(admin_dir)
    from nameauth import get_admin_level_by_name, normalize_admin_list
    import toml
    adm_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'admins.toml')
    adm_conf = toml.load(adm_path)
    users = adm_conf.get('users', {})
    high = normalize_admin_list(users.get('admins_high'))
    mid = normalize_admin_list(users.get('admins_mid'))
    low = normalize_admin_list(users.get('admins_low'))
    return get_admin_level_by_name, high, mid, low


class AutoBalanceSystem(object):
    """Equilibra equipos 1/2 y bloquea cambios que desbalanceen."""

    def __init__(self):
        self.enabled = True
        self._moving = False
        self._rebalance_timer = None
        self._cmd_cooldown = {}
        self._admin_fn = None
        self._admin_high = frozenset()
        self._admin_mid = frozenset()
        self._admin_low = frozenset()
        try:
            fn, high, mid, low = _load_admin_checker()
            self._admin_fn = fn
            self._admin_high = high
            self._admin_mid = mid
            self._admin_low = low
        except Exception as exc:
            _debug_log('admins.toml no cargado: %s' % exc)
        if _IN_GAME:
            host.registerHandler('ChatMessage', self.on_chat_message, 1)
            host.registerHandler('PlayerChangeTeams', self.on_player_change_teams, 1)
            host.registerHandler('PlayerDisconnect', self.on_player_disconnect, 1)
            host.registerHandler('PlayerDeath', self.on_player_death, 1)
            host.registerHandler('PlayerConnect', self.on_player_connect, 1)
            _debug_log('AutoBalance ON (max diff %d)' % MAX_TEAM_DIFF)

    def _is_admin(self, player):
        if self._admin_fn is None:
            return False
        try:
            level = self._admin_fn(
                _player_name(player),
                self._admin_high,
                self._admin_mid,
                self._admin_low,
            )
        except Exception:
            return False
        return level in ('high', 'mid', 'low')

    def _pm(self, player, msg):
        if not _IN_GAME or player is None or host is None:
            return
        if not _player_valid_human(player):
            return
        try:
            text = '\xc2\xa7C1001' + str(msg)
            if len(text) > 240:
                text = text[:239]
            host.sgl_sendTextMessage(player.index, 14, 1, text, 0)
        except Exception:
            pass

    def _say_all(self, msg):
        if not _IN_GAME or host is None:
            return
        try:
            safe = str(msg).replace('"', "'")
            host.rcon_invoke('game.sayall "%s"' % safe)
        except Exception:
            pass

    def _list_humans(self, exclude=None):
        if not _IN_GAME or bf2 is None:
            return []
        out = []
        try:
            players = bf2.playerManager.getPlayers()
        except Exception:
            return []
        exclude_idx = None
        if exclude is not None:
            try:
                exclude_idx = int(exclude.index)
            except Exception:
                exclude_idx = None
        for player in players:
            if not _player_valid_human(player):
                continue
            if exclude_idx is not None:
                try:
                    if int(player.index) == exclude_idx:
                        continue
                except Exception:
                    pass
            out.append(player)
        return out

    def _team_counts(self, exclude=None):
        t1 = 0
        t2 = 0
        for player in self._list_humans(exclude=exclude):
            team = _safe_team(player)
            if team == TEAM_1:
                t1 += 1
            elif team == TEAM_2:
                t2 += 1
        return (t1, t2)

    def _status_text(self):
        t1, t2 = self._team_counts()
        state = 'ON' if self.enabled else 'OFF'
        return 'AutoBalance %s | equipos %d vs %d | max diferencia %d' % (
            state, t1, t2, MAX_TEAM_DIFF
        )

    def _move_player(self, player, to_team, reason):
        """Cambia de equipo con setTeam. PlayerChangeTeams no se dispara."""
        if not _player_valid_human(player):
            return False
        to_team = int(to_team)
        if to_team not in (TEAM_1, TEAM_2):
            return False
        if _safe_team(player) == to_team:
            return False
        if not _IN_GAME:
            return False
        self._moving = True
        try:
            player.setTeam(to_team)
        except Exception as exc:
            _debug_log('setTeam error: %s' % exc)
            self._moving = False
            return False
        self._moving = False
        if reason == 'switch_denied':
            self._pm(
                player,
                'No puedes cambiarte: desbalancearia los equipos (max %d).' % MAX_TEAM_DIFF,
            )
        elif reason == 'rebalance':
            self._pm(player, 'Te movieron de equipo para equilibrar la partida.')
        elif reason == 'join':
            self._pm(player, 'Entraste al equipo con menos jugadores.')
        return True

    def _candidate_score(self, player):
        """Menor puntaje = mejor candidato para mover. Protege cmd/SL y vivos."""
        score = 0
        if _safe_alive(player):
            score += 100
        if _safe_commander(player):
            score += 50
        if _safe_squad_leader(player):
            score += 20
        if _is_immune(player):
            score += 1000
        return score

    def _pick_move_candidate(self, team_num, exclude=None):
        """Elige a quien pasar del equipo grande al chico."""
        team_num = int(team_num)
        candidates = []
        for player in self._list_humans(exclude=exclude):
            if _safe_team(player) != team_num:
                continue
            if _is_immune(player):
                continue
            candidates.append(player)
        if not candidates:
            return None
        candidates.sort(key=self._candidate_score)
        best = candidates[0]
        # No mover comandante/SL vivos si hay otra opcion peor pero segura.
        if _safe_commander(best) or _safe_squad_leader(best):
            for player in candidates:
                if not _safe_commander(player) and not _safe_squad_leader(player):
                    return player
            return None
        return best

    def _rebalance(self, exclude=None):
        """Mueve jugadores del equipo grande hasta abs <= MAX_TEAM_DIFF."""
        if not self.enabled:
            return
        guard = 0
        while guard < 8:
            guard += 1
            t1, t2 = self._team_counts(exclude=exclude)
            if abs(t1 - t2) <= MAX_TEAM_DIFF:
                return
            big = larger_team(t1, t2)
            if big == 0:
                return
            small = other_team(big)
            player = self._pick_move_candidate(big, exclude=exclude)
            if player is None:
                return
            if not self._move_player(player, small, 'rebalance'):
                return

    def _schedule_rebalance(self, exclude=None):
        if not self.enabled or not _IN_GAME or bf2 is None:
            return
        try:
            if self._rebalance_timer is not None:
                self._rebalance_timer.destroy()
        except Exception:
            pass
        self._rebalance_timer = None
        try:
            timer = bf2.Timer(self._on_rebalance_timer, REBALANCE_DELAY_SEC, 1, exclude)
            self._rebalance_timer = timer
        except Exception as exc:
            _debug_log('timer error: %s' % exc)
            self._rebalance(exclude=exclude)

    def _on_rebalance_timer(self, data=None):
        self._rebalance_timer = None
        self._rebalance(exclude=data)

    def _rcon(self, cmd):
        if not _IN_GAME or host is None:
            return ''
        try:
            out = host.rcon_invoke(str(cmd))
        except Exception:
            return ''
        if out is None:
            return ''
        return str(out).strip()

    def _rcon_int(self, cmd):
        text = self._rcon(cmd)
        try:
            return int(text.split()[0])
        except Exception:
            return None

    def _maplist_entries(self):
        listed = parse_maplist_list_output(self._rcon('mapList.list'))
        if listed:
            return listed
        path = os.path.join(
            os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),
            'settings',
            'maplist.con',
        )
        try:
            handle = open(path, 'r')
            try:
                text = handle.read()
            finally:
                handle.close()
        except Exception:
            return []
        return parse_maplist_append_text(text)

    def _team_label(self, team_num):
        try:
            name = bf2.gameLogic.getTeamName(int(team_num))
            if name:
                return str(name)
        except Exception:
            pass
        return str(team_num)

    def _tickets(self, team_num):
        try:
            return int(bf2.gameLogic.getTickets(int(team_num)))
        except Exception:
            return None

    def _server_name(self):
        try:
            name = bf2.serverSettings.getServerName()
            if name:
                return str(name)
        except Exception:
            pass
        text = self._rcon('sv.serverName')
        if text:
            return text.strip().strip('"')
        return '?'

    def _max_players(self):
        try:
            return int(bf2.serverSettings.getMaxPlayers())
        except Exception:
            pass
        val = self._rcon_int('sv.maxPlayers')
        if val is not None:
            return val
        return '?'

    def _build_round_info(self):
        entries = self._maplist_entries()
        cur_idx = self._rcon_int('admin.currentLevel')
        next_idx = self._rcon_int('admin.nextLevel')
        current = map_entry_at(entries, cur_idx)
        nxt = map_entry_at(entries, next_idx)
        if current is None:
            try:
                raw = bf2.gameLogic.getMapName()
                current = {'name': raw, 'mode': 'gpm_cq', 'layer': '?'}
            except Exception:
                pass
        t1, t2 = self._team_counts()
        humans = self._list_humans()
        return {
            'server_name': self._server_name(),
            'current': format_map_entry(current),
            'next': format_map_entry(nxt),
            'players': len(humans),
            'max_players': self._max_players(),
            'team1': t1,
            'team2': t2,
            'tickets1': self._tickets(TEAM_1),
            'tickets2': self._tickets(TEAM_2),
            'team1_name': self._team_label(TEAM_1),
            'team2_name': self._team_label(TEAM_2),
        }

    def _pm_lines(self, player, lines):
        for line in lines:
            self._pm(player, line)

    def _player_ip(self, player):
        try:
            addr = str(player.getAddress() or '')
        except Exception:
            return '?'
        if addr.count(':') == 1:
            addr = addr.split(':', 1)[0]
        if addr == '':
            return '?'
        return addr

    def _player_ping(self, player):
        try:
            return int(player.getPing())
        except Exception:
            return None

    def _player_score_tuple(self, player):
        try:
            return (
                int(player.score.score),
                int(player.score.kills),
                int(player.score.deaths),
            )
        except Exception:
            return (None, None, None)

    def _find_players(self, query):
        """Busca por #id o substring de nombre. Lista vacia si 0 o varios."""
        q = str(query or '').strip()
        if q.startswith('#'):
            num = q[1:].strip()
            try:
                idx = int(num)
            except ValueError:
                return ('bad_id', [])
            try:
                found = bf2.playerManager.getPlayerByIndex(idx)
            except Exception:
                found = None
            if not _player_valid_human(found):
                return ('not_found', [])
            return ('ok', [found])
        matches = []
        for player in self._list_humans():
            if player_name_matches(_player_name(player), q):
                matches.append(player)
        if len(matches) == 0:
            return ('not_found', [])
        if len(matches) > 1:
            return ('many', matches)
        return ('ok', matches)

    def _handle_info(self, player, args):
        kind, query, show_last = parse_info_args(args)
        if kind == 'round':
            lines = format_round_info_lines(self._build_round_info())
            self._pm_lines(player, lines)
            return
        if not self._is_admin(player):
            self._pm(player, 'No tienes permiso para !info jugador')
            return
        status, matches = self._find_players(query)
        if status == 'bad_id':
            self._pm(player, 'ID invalido. Usa !info #12')
            return
        if status == 'not_found':
            self._pm(player, 'No se encontraron jugadores con el nombre %s' % query)
            return
        if status == 'many':
            self._pm(player, 'Multiples jugadores encontrados con el nombre %s:' % query)
            shown = matches[:4]
            for other in shown:
                try:
                    idx = int(other.index)
                except Exception:
                    idx = '?'
                self._pm(player, '#%s: %s' % (idx, _player_name(other)))
            return
        target = matches[0]
        score, kills, deaths = self._player_score_tuple(target)
        data = {
            'name': _player_name(target),
            'team': _safe_team(target),
            'score': score,
            'kills': kills,
            'deaths': deaths,
            'ping': self._player_ping(target),
            'ip': self._player_ip(target),
            'show_last': show_last,
        }
        self._pm_lines(player, format_player_info_lines(data))

    def _handle_ab(self, player, action):
        if action == 'status':
            self._pm(player, self._status_text())
            return
        if not self._is_admin(player):
            self._pm(player, 'No tienes permiso para usar !ab on/off')
            return
        now = time.time()
        last = self._cmd_cooldown.get(player.index, 0)
        if now - last < AB_CMD_COOLDOWN_SEC:
            return
        try:
            self._cmd_cooldown[player.index] = now
        except Exception:
            pass
        if action == 'on':
            self.enabled = True
            self._say_all('AutoBalance: ON (max diferencia %d)' % MAX_TEAM_DIFF)
            self._pm(player, self._status_text())
            self._schedule_rebalance()
            return
        if action == 'off':
            self.enabled = False
            self._say_all('AutoBalance: OFF')
            self._pm(player, self._status_text())

    def on_chat_message(self, player_id, msg_text, channel, flags):
        if player_id == -1:
            return
        parsed = parse_bang_command(msg_text)
        if parsed is None:
            return
        cmd, args = parsed
        if cmd not in ('ab', 'info'):
            return
        try:
            player = bf2.playerManager.getPlayerByIndex(player_id)
        except Exception:
            return
        if not _player_valid_human(player):
            return
        if cmd == 'info':
            now = time.time()
            last = self._cmd_cooldown.get('info:%s' % player_id, 0)
            if now - last < INFO_CMD_COOLDOWN_SEC:
                return
            self._cmd_cooldown['info:%s' % player_id] = now
            self._handle_info(player, args)
            return
        action = parse_ab_command(msg_text)
        if action is None:
            return
        self._handle_ab(player, action)

    def on_player_change_teams(self, player, humanHasSpawned=None):
        if not self.enabled or self._moving:
            return
        if not _player_valid_human(player):
            return
        if _is_immune(player):
            return
        t1, t2 = self._team_counts()
        current = _safe_team(player)
        dest = target_team_if_illegal(t1, t2, current, MAX_TEAM_DIFF)
        if dest is None:
            return
        self._move_player(player, dest, 'switch_denied')
        self._schedule_rebalance()

    def on_player_connect(self, player):
        if not self.enabled:
            return
        self._schedule_rebalance()

    def on_player_disconnect(self, player):
        if not self.enabled:
            return
        self._schedule_rebalance(exclude=player)

    def on_player_death(self, player, vehicle=None):
        if not self.enabled or self._moving:
            return
        t1, t2 = self._team_counts()
        if abs(t1 - t2) > MAX_TEAM_DIFF:
            self._rebalance()


def init():
    """Registra AutoBalance al iniciar el mod."""
    if _IN_GAME:
        AutoBalanceSystem()


if _IN_GAME:
    init()
