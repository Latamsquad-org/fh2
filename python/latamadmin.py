# -*- coding: utf-8 -*-
# latamadmin.py - comandos de admin LatamSquad para FH2 (Python 2).
# AutoBalance: max diferencia 2. !ab on / !ab off.
# !info: solo admins. !setnext / !sn: parser flexible de mapa y layer.
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

# ---------------------------------------------------------------------------
# Comandos LatamAdmin
# Edita niveles aca (igual que adm_adminPowerLevels en realityconfig_admin.py).
#
# 0   = high (admins_high en admins.toml)
# 1   = admin (admins_mid)
# 2   = mod (admins_low)
# 777 = todos
#
# El numero MAS BAJO tiene MAS poder.
# Si un comando vale 2, high + admin + mod pueden usarlo.
# Si vale 0, solo high.
# Si vale 777, cualquiera.
#
# Comandos actuales:
#   !ab on / !ab off encender/apagar AutoBalance
#   !info            info de ronda
#   !info nombre     ficha de jugador
#   !setnext / !sn   elegir el siguiente mapa
# ---------------------------------------------------------------------------
LEVEL_HIGH = 0
LEVEL_ADMIN = 1
LEVEL_MOD = 2
LEVEL_EVERYONE = 777

COMMAND_ALIASES = {
    'sn': 'setnext',
}

COMMAND_LEVELS = {
    'ab': LEVEL_MOD,
    'info': LEVEL_MOD,
    'setnext': LEVEL_MOD,
}


def resolve_command_name(cmd):
    """Aplica alias (!sn -> setnext)."""
    name = str(cmd or '').strip().lower()
    if name in COMMAND_ALIASES:
        return COMMAND_ALIASES[name]
    return name


def required_command_level(cmd):
    """Nivel pedido por el comando, o None si no existe."""
    name = resolve_command_name(cmd)
    if name not in COMMAND_LEVELS:
        return None
    try:
        return int(COMMAND_LEVELS[name])
    except (TypeError, ValueError):
        return None


def is_chat_command(cmd):
    """True si se escribe en chat (!ab, !info, !setnext, !sn)."""
    return resolve_command_name(cmd) in COMMAND_LEVELS


def admin_tag_to_power(tag):
    """high/mid/low -> 0/1/2. Sin tag -> 777."""
    if tag == 'high':
        return LEVEL_HIGH
    if tag == 'mid':
        return LEVEL_ADMIN
    if tag == 'low':
        return LEVEL_MOD
    return LEVEL_EVERYONE


def can_use_command(cmd, player_power):
    """True si player_power (0/1/2/777) alcanza el nivel del comando."""
    req = required_command_level(cmd)
    if req is None:
        return False
    if req >= LEVEL_EVERYONE:
        return True
    try:
        power = int(player_power)
    except (TypeError, ValueError):
        return False
    if power >= LEVEL_EVERYONE:
        return False
    return power <= req


# Max jugadores de diferencia entre equipos (10 vs 8 ok, 11 vs 8 no).
MAX_TEAM_DIFF = 2
TEAM_1 = 1
TEAM_2 = 2
# Delay para recontar despues de un disconnect (el jugador puede seguir en la lista).
REBALANCE_DELAY_SEC = 1.5
AB_CMD_COOLDOWN_SEC = 2
INFO_CMD_COOLDOWN_SEC = 3
SETNEXT_CMD_COOLDOWN_SEC = 2

GAMEMODE_LABELS = {
    'gpm_cq': 'Conquest',
    'gpm_coop': 'Coop',
    'sp1': 'SP1',
    'sp2': 'SP2',
    'sp3': 'SP3',
}

# PR Inf/Alt/Std/Lrg -> capas FH2 16/32/64/128.
LAYER_ALIASES = {
    '16': '16',
    'inf': '16',
    'small': '16',
    '32': '32',
    'alt': '32',
    'medium': '32',
    'med': '32',
    '64': '64',
    'std': '64',
    'large': '64',
    'lrg': '64',
    'big': '64',
    '128': '128',
    'tiny': '128',
}

MODE_ALIASES = {
    'cq': 'gpm_cq',
    'gpm_cq': 'gpm_cq',
    'conquest': 'gpm_cq',
    'conq': 'gpm_cq',
    'coop': 'gpm_coop',
    'gpm_coop': 'gpm_coop',
    'sp1': 'sp1',
    'sp2': 'sp2',
    'sp3': 'sp3',
}

SETNEXT_USAGE = (
    'Uso: !setnext mapa [modo] layer  |  atajo !sn',
    'Ej: !sn ramelle 16  |  !sn hurtgen forest 64  |  !sn keren cq 32  |  !sn 7',
    'Layers: 16/inf  32/alt  64/std  128/tiny',
)

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
    Parsea !ab on / !ab off.
    Retorna None, 'need_arg', 'on' o 'off'.
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
        return 'need_arg'
    arg = parts[1].lower()
    if arg in ('on', '1', 'true', 'enable'):
        return 'on'
    if arg in ('off', '0', 'false', 'disable'):
        return 'off'
    return 'need_arg'


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


def normalize_map_query(text):
    """Minusculas, _ y espacios unificados."""
    raw = str(text or '').lower().replace('_', ' ')
    return ' '.join(raw.split())


def map_name_matches(map_id, query):
    """True si el query (con o sin _) aparece en el id del mapa."""
    n = normalize_map_query(map_id)
    q = normalize_map_query(query)
    if q == '' or n == '':
        return False
    if n.find(q) != -1:
        return True
    if n.replace(' ', '').find(q.replace(' ', '')) != -1:
        return True
    return False


def score_map_match(map_id, query):
    """0 exacto, 1 prefijo, 2 substring. 99 = no coincide."""
    n = normalize_map_query(map_id)
    q = normalize_map_query(query)
    if q == '' or n == '':
        return 99
    if n == q or n.replace(' ', '') == q.replace(' ', ''):
        return 0
    if n.startswith(q) or n.replace(' ', '').startswith(q.replace(' ', '')):
        return 1
    if map_name_matches(map_id, query):
        return 2
    return 99


def parse_setnext_args(args):
    """
    Parsea !setnext / !sn al estilo PR, pero acepta layer numerico o Inf/Std.
    Retorna dict kind: empty | id | search | error
    """
    if args is None:
        args = []
    parts = [str(x).strip() for x in list(args) if str(x).strip() != '']
    if not parts:
        return {'kind': 'empty'}
    if len(parts) == 1 and parts[0].isdigit():
        return {'kind': 'id', 'map_id': int(parts[0])}
    lowered = [p.lower() for p in parts]
    layer = None
    mode = None
    if lowered and lowered[-1] in LAYER_ALIASES:
        layer = LAYER_ALIASES[lowered[-1]]
        lowered = lowered[:-1]
    if lowered and lowered[-1] in MODE_ALIASES:
        mode = MODE_ALIASES[lowered[-1]]
        lowered = lowered[:-1]
    query = ' '.join(lowered).strip()
    if query == '':
        return {'kind': 'error'}
    return {
        'kind': 'search',
        'query': query,
        'mode': mode,
        'layer': layer,
    }


def filter_setnext_catalog(catalog, query, mode, layer):
    """Lista (score, item) ordenada. item tiene name, mode, layer, index."""
    scored = []
    if catalog is None:
        return scored
    for item in catalog:
        if mode and item.get('mode') != mode:
            continue
        if layer and str(item.get('layer')) != str(layer):
            continue
        sc = score_map_match(item.get('name'), query)
        if sc >= 99:
            continue
        scored.append((sc, item))
    scored.sort(key=lambda row: (
        row[0],
        row[1].get('name') or '',
        str(row[1].get('layer') or ''),
        str(row[1].get('mode') or ''),
    ))
    return scored


def unique_catalog_items(items):
    """Quita duplicados name+mode+layer conservando orden."""
    out = []
    seen = set()
    for item in items:
        key = (
            item.get('name'),
            item.get('mode'),
            str(item.get('layer')),
        )
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def resolve_setnext_target(catalog, parsed, default_mode='gpm_cq'):
    """
    Resuelve un !setnext contra el catalogo.
    Retorna (status, item, extras).
    status: ok | empty | not_found | many | error
    """
    if not parsed or parsed.get('kind') == 'empty':
        return ('empty', None, [])
    if parsed.get('kind') == 'error':
        return ('error', None, [])
    if parsed.get('kind') == 'id':
        map_id = parsed.get('map_id')
        for item in catalog or []:
            if item.get('index') == map_id:
                return ('ok', item, [])
        return ('not_found', None, [])
    query = parsed.get('query')
    mode = parsed.get('mode')
    layer = parsed.get('layer')
    rotation = [x for x in (catalog or []) if x.get('index') is not None]
    search_mode = mode if mode else default_mode
    scored = filter_setnext_catalog(rotation, query, search_mode, layer)
    if not scored:
        scored = filter_setnext_catalog(catalog, query, search_mode, layer)
    if not scored and mode is None:
        scored = filter_setnext_catalog(rotation, query, None, layer)
    if not scored and mode is None:
        scored = filter_setnext_catalog(catalog, query, None, layer)
    if not scored:
        return ('not_found', None, [])
    best = scored[0][0]
    top = [item for sc, item in scored if sc == best]
    uniq = unique_catalog_items(top)
    if len(uniq) == 1:
        return ('ok', uniq[0], [])
    return ('many', None, uniq)


def format_setnext_choice(item):
    """ramelle gpm_cq 16 (id 4)."""
    idx = item.get('index')
    label = format_map_entry(item)
    if idx is None:
        return '%s (no esta en rotacion)' % label
    return '%s (id %s)' % (label, idx)


def scan_spawnpoint_maps(levels_dir):
    """Catalogo name/mode/layer desde levels/*/spawnpoints/*.py."""
    out = []
    if not levels_dir or not os.path.isdir(levels_dir):
        return out
    try:
        maps = os.listdir(levels_dir)
    except Exception:
        return out
    for mapname in maps:
        sp_dir = os.path.join(levels_dir, mapname, 'spawnpoints')
        if not os.path.isdir(sp_dir):
            continue
        try:
            files = os.listdir(sp_dir)
        except Exception:
            continue
        for fname in files:
            low = fname.lower()
            if not low.endswith('.py'):
                continue
            base = low[:-3]
            if '_' not in base:
                continue
            mode, layer = base.rsplit('_', 1)
            if layer not in ('16', '32', '64', '128'):
                continue
            out.append({
                'name': mapname,
                'mode': mode,
                'layer': layer,
                'index': None,
            })
    return out


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
        self._last_setnext = None
        self._disk_maps = []
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
            self._disk_maps = scan_spawnpoint_maps(
                os.path.join(
                    os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),
                    'levels',
                )
            )
            _debug_log('AutoBalance ON (max diff %d)' % MAX_TEAM_DIFF)

    def _admin_tag(self, player):
        """high / mid / low / None segun admins.toml."""
        if self._admin_fn is None:
            return None
        try:
            level = self._admin_fn(
                _player_name(player),
                self._admin_high,
                self._admin_mid,
                self._admin_low,
            )
        except Exception:
            return None
        if level in ('high', 'mid', 'low'):
            return level
        return None

    def _is_admin(self, player):
        return self._admin_tag(player) is not None

    def _player_power(self, player):
        return admin_tag_to_power(self._admin_tag(player))

    def _can_use(self, cmd, player):
        return can_use_command(cmd, self._player_power(player))

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
        if not self._can_use('info', player):
            self._pm(player, 'No tienes permiso para usar !info')
            return
        kind, query, show_last = parse_info_args(args)
        if kind == 'round':
            lines = format_round_info_lines(self._build_round_info())
            self._pm_lines(player, lines)
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
        # Sin permiso: silencio (no avisar a jugadores comunes).
        if not self._can_use('ab', player):
            return
        if action != 'on' and action != 'off':
            self._pm(player, "Debes especificar 'on' u 'off'.")
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

    def _setnext_catalog(self):
        """Rotacion viva + mapas en disco (index None si no estan en maplist)."""
        rotation = self._maplist_entries()
        numbered = []
        rot_keys = set()
        for i, item in enumerate(rotation):
            row = dict(item)
            if row.get('index') is None:
                row['index'] = i
            numbered.append(row)
            rot_keys.add((row.get('name'), row.get('mode'), str(row.get('layer'))))
        extra = []
        for item in self._disk_maps:
            key = (item.get('name'), item.get('mode'), str(item.get('layer')))
            if key in rot_keys:
                continue
            extra.append(dict(item))
        return numbered + extra

    def _append_map_to_rotation(self, item):
        """Agrega el mapa a mapList y devuelve el item con index, o None."""
        name = item.get('name')
        mode = item.get('mode')
        layer = item.get('layer')
        result = self._rcon('mapList.append %s %s %s' % (name, mode, layer))
        listed = self._maplist_entries()
        for i, row in enumerate(listed):
            if row.get('name') == name and row.get('mode') == mode and str(row.get('layer')) == str(layer):
                found = dict(row)
                found['index'] = i
                return found
        if result is not None:
            found = dict(item)
            found['index'] = len(listed)
            return found
        return None

    def _apply_next_level(self, item, admin_player):
        idx = item.get('index')
        if idx is None:
            item = self._append_map_to_rotation(item)
            if item is None or item.get('index') is None:
                self._pm(admin_player, 'No se pudo agregar el mapa a la rotacion.')
                return False
            idx = item.get('index')
        self._rcon('admin.nextLevel %s' % int(idx))
        label = format_map_entry(item)
        admin_name = _player_name(admin_player)
        self._last_setnext = admin_name
        self._say_all('El siguiente mapa es: %s' % label)
        self._pm(admin_player, 'Setnext OK: %s (id %s)' % (label, idx))
        _debug_log('setnext %s by %s' % (label, admin_name))
        return True

    def _handle_setnext(self, player, args):
        if not self._can_use('setnext', player):
            self._pm(player, 'No tienes permiso para usar !setnext')
            return
        parsed = parse_setnext_args(args)
        catalog = self._setnext_catalog()
        status, item, extras = resolve_setnext_target(catalog, parsed)
        if status == 'empty':
            self._pm_lines(player, list(SETNEXT_USAGE))
            nxt_idx = self._rcon_int('admin.nextLevel')
            nxt = map_entry_at(catalog, nxt_idx)
            self._pm(player, 'Siguiente ahora: %s' % format_map_entry(nxt))
            return
        if status == 'error':
            self._pm_lines(player, list(SETNEXT_USAGE))
            return
        if status == 'not_found':
            self._pm(player, 'No se encontro el mapa. Revisa nombre y layer (16/32/64/128).')
            self._pm_lines(player, list(SETNEXT_USAGE))
            return
        if status == 'many':
            self._pm(player, 'Varios mapas. Se mas especifico (agrega layer):')
            shown = extras[:6]
            for row in shown:
                self._pm(player, format_setnext_choice(row))
            return
        self._apply_next_level(item, player)

    def on_chat_message(self, player_id, msg_text, channel, flags):
        if player_id == -1:
            return
        parsed = parse_bang_command(msg_text)
        if parsed is None:
            return
        cmd, args = parsed
        if not is_chat_command(cmd):
            return
        name = resolve_command_name(cmd)
        try:
            player = bf2.playerManager.getPlayerByIndex(player_id)
        except Exception:
            return
        if not _player_valid_human(player):
            return
        if name == 'info':
            if not self._can_use('info', player):
                self._pm(player, 'No tienes permiso para usar !info')
                return
            now = time.time()
            last = self._cmd_cooldown.get('info:%s' % player_id, 0)
            if now - last < INFO_CMD_COOLDOWN_SEC:
                return
            self._cmd_cooldown['info:%s' % player_id] = now
            self._handle_info(player, args)
            return
        if name == 'setnext':
            if not self._can_use('setnext', player):
                self._pm(player, 'No tienes permiso para usar !setnext')
                return
            now = time.time()
            last = self._cmd_cooldown.get('setnext:%s' % player_id, 0)
            if now - last < SETNEXT_CMD_COOLDOWN_SEC:
                return
            self._cmd_cooldown['setnext:%s' % player_id] = now
            self._handle_setnext(player, args)
            return
        if name == 'ab':
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
