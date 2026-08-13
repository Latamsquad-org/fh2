# uncompyle6 version 3.9.3
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)]
# Embedded file name: python/admin/bf2_tools.py
# Compiled at: 2026-03-10 19:07:22
"""Utilities that need the BF2 python bindings"""
import sys
from math import pi, cos, sin, ceil
from random import choice, randrange
from os.path import exists, join
import re
from textwrap import wrap
from docopt import docopt, DocoptExit
import toml, bf2, bf2.Timer
from host import sgl_sendTextMessage, sgl_getModDirectory
from game.constants import SGL_TEXT_ARG2NUM
from game.gamemodes.gpm_cq import updateTicketLoss, updateCPTakeOverState
from game.gameplayPlugin import setDefaultTicketLossPerMin, g_hooker
from game.localize import localize_message
from game.utilities import TEAM2NUM, get_fullname, get_position, get_rotation, get_team_tickets, is_internet, rcon, read_maplist, root_object, getObjectsOfTemplate, deleteObject, player_in_closed_vehicle, player_in_vehicle
from admin.constants import MAX_LINE_LEN, BIPOD_MGS
from admin.globals import TeamKillHistory, AfkList, MapMetaCache
from admin.log import logger_admin
from admin.util import format_message, normed_3vec, num_to_team, team_to_num, parse_reason
from admin.settings import LEVEL_DIR, ADMINS_HIGH, ADMINS_MID, ADMINS_LOW, BAN_DURATION, BLOCK_SELF_SWITCH, IS_BETA
HAS_HUD_TICKETS = False
try:
    from game.plugins.hudTickets import hudTickets
    from game.plugins.chat import BangBang
    HAS_HUD_TICKETS = True
except ImportError:
    HAS_HUD_TICKETS = False

LOG = logger_admin

def hierarchy(bf2_obj):
    """Find object hierarchy

    Parameters
    ----------
    bf2_obj

    Returns
    -------
    list(str)
    """
    out = []
    while True:
        name = bf2_obj.templateName
        out.append(name)
        try:
            parent = bf2_obj.getParent()
        except AttributeError:
            break

        if not parent:
            break
        if parent == bf2_obj:
            break
        bf2_obj = parent

    out.reverse()
    return out


def is_valid(ply):
    """Check if isValid and if is not None (might happen with bots)"""
    return ply and ply.isValid()


def is_alive(ply):
    """Check if valid and alive"""
    return is_valid(ply) and ply.isAlive()


def is_connected(ply):
    """Check if valid and connected"""
    return is_valid(ply) and ply.isConnected()


def is_nobot(ply):
    """Check if not a bot"""
    return is_valid(ply) and not ply.isAIPlayer()


def is_human(ply):
    """Check if human (not a bot)"""
    return is_nobot(ply)


def is_alive_human(ply):
    """Check if human and alive"""
    return is_valid(ply) and not ply.isAIPlayer() and ply.isAlive()


def is_dead_human(ply):
    """Check if human and dead"""
    return is_valid(ply) and not ply.isAIPlayer() and not ply.isAlive()


def find_type(t):
    """Find type of template

    Parameters
    ----------
    t: str

    Returns
    -------
    str
    """
    from game.utilities import active, getType
    active(t)
    return getType(lower=False)


try:
    from game.utilities import walk_children
except ImportError:

    def walk_children(bf2_obj):
        """Yield all children of an object

        Note that it also yields ``bf2_obj`` itself, as 0th element.

        Parameters
        ----------
        bf2_obj

        Yields
        ------
        child
        """
        yield bf2_obj
        for child in bf2_obj.getChildren():
            for sub_child in walk_children(child):
                yield sub_child

        return


class FH2Player(object):
    """Connected FH2Player

    Parameters
    ----------
    key_hash: str
    name: str
    clan: str

    Attributes
    ----------
    name: str
    key_hash: str
    clan: str
    idx: int
        enumeration index. As players connect to the server they
        are assigned playerID numbers from "0" up.
    is_alive: bool
    is_squadleader: bool
    is_in_squad: bool
    is_commander: bool
    is_admin: bool
    admin_level: str
        'high', 'mid', 'low'
    squad_number: int
        numerical ID of the squad the player is a member of
    team: str
        'axis' or 'allies'
    ip: str
    gsid: int
        gamespy profile ID
    """
    instances = {}

    def __new__(cls, idx, name, key_hash, gsid, **kwargs):
        try:
            found_ply = FH2Player.instances[gsid]
        except KeyError:
            found_ply = None

        if found_ply is not None and found_ply.name == name:
            self = found_ply
        else:
            sup = super(FH2Player, cls)
            self = sup.__new__(cls, idx=idx, name=name, key_hash=key_hash, gsid=gsid, **kwargs)
            FH2Player.instances[gsid] = self
        return self

    def __del__(self):
        gsid = self.gsid
        if gsid in self.instances:
            del self.instances[gsid]
        return

    def __init__(self, idx, name, key_hash, gsid, clan=''):
        self.key_hash = key_hash
        self.name = name
        self.clan = clan
        self.idx = idx
        self.gsid = gsid
        self._bf2_ply = None
        self._is_bot = None
        self._is_admin = None
        self._admin_level = None
        return

    @classmethod
    def from_bf2(cls, bf2_ply):
        """Create from `bf2.playerManager.Player` instance

        Parameters
        ----------
        bf2_ply: bf2.playerManager.Player
        """
        idx = bf2_ply.index
        try:
            clan, name = get_fullname(bf2_ply)
        except (ValueError, IndexError):
            rcon('admin.banPlayer %d %s' % (idx, BAN_DURATION))
            clan = ''
            name = 'NOTSET'

        try:
            key_hash = str(cls._get_hash(idx))
        except ValueError:
            key_hash = 'NOTSET'

        gsid = int(bf2_ply.getProfileId())
        ply = cls(key_hash=key_hash, name=name, idx=idx, gsid=gsid, clan=clan)
        ply._bf2_ply = bf2_ply
        return ply

    @property
    def is_connected(self):
        bf2_ply = self._bf2_ply
        return bool(bf2_ply.isConnected())

    def _get_bf2_ply(self):
        try:
            bf2_ply = self._bf2_ply
        except AttributeError:
            bf2_ply = find_player_by_index(self.idx)

        return bf2_ply

    @property
    def is_alive(self):
        bf2_ply = self._get_bf2_ply()
        return bool(bf2_ply.isAlive())

    @property
    def is_squadleader(self):
        bf2_ply = self._get_bf2_ply()
        return bool(bf2_ply.isSquadLeader())

    @property
    def is_commander(self):
        bf2_ply = self._get_bf2_ply()
        return bool(bf2_ply.isCommander())

    @property
    def ip(self):
        bf2_ply = self._get_bf2_ply()
        return str(bf2_ply.getAddress())

    @property
    def is_bot(self):
        if self._is_bot is not None:
            return self._is_bot
        else:
            bf2_ply = self._get_bf2_ply()
            out = bool(bf2_ply.isAIPlayer())
            self._is_bot = out
            return out

    @property
    def admin_level(self):
        if self._admin_level is not None:
            return self._admin_level
        else:
            kh = self.key_hash
            kh = kh.encode('utf-8')
            if kh in ADMINS_HIGH:
                out = 'high'
            elif kh in ADMINS_MID:
                out = 'mid'
            elif kh in ADMINS_LOW:
                out = 'low'
            else:
                out = None
            self._admin_level = out
            return out

    @property
    def gamespy_id(self):
        bf2_ply = self._bf2_ply
        return int(bf2_ply.getProfileId())

    @property
    def is_admin(self):
        if self._is_admin is not None:
            return self._is_admin
        else:
            if self.admin_level:
                out = True
            elif IS_BETA:
                out = True
            else:
                out = False
            self._is_admin = out
            return out

    @property
    def squad_number(self):
        bf2_ply = self._bf2_ply
        return int(bf2_ply.getSquadId())

    @property
    def team(self):
        bf2_ply = self._bf2_ply
        return num_to_team(int(bf2_ply.getTeam()))

    def get_position(self):
        bf2_ply = self._bf2_ply
        return get_position(bf2_ply)

    def get_rotation(self):
        bf2_ply = self._bf2_ply
        return get_rotation(bf2_ply)

    def get_vehicle_rotation(self):
        if self._bf2_ply is None:
            LOG.warning('(fh2player.get_vehicle_rotation) bf2 player none, PANIC!')
            return (0, 0, 0)
        else:
            bf2_ply = self._bf2_ply
            veh = bf2_ply.getVehicle()
            root_veh = root_object(veh)
            return get_rotation(root_veh)

    def _set_team(self, team):
        """Move player to a team

        Parameters
        ----------
        team: str
        """
        if team not in ('allies', 'axis'):
            return
        else:
            curteam = self.team
            if curteam == team:
                return
            bf2_ply = self._bf2_ply
            if bf2_ply is None:
                LOG.warning('(fh2player._set_team) bf2 player none, PANIC!')
                return
            team_num = team_to_num(team)
            bf2_ply.setTeam(team_num)
            return

    def switch(self, force=False, invoker=None, quiet=False):
        """Move player to the other team"""
        if self._bf2_ply is None:
            LOG.warning('(fh2player.switch) bf2 player none, PANIC!')
            return
        else:
            if invoker is None:
                invoker_name = '<admin>'
            else:
                invoker_name = invoker.name
            self._bf2_ply.immune_to_autobalance = True
            if not self.is_alive:
                if not quiet:
                    personal_message(self, 'Switched by admin!', color='green')
                    admin_message('Switched %s  -- %s' % (self.name, invoker_name))
                curteam = self.team
                if curteam == 'allies':
                    self._set_team('axis')
                elif curteam == 'axis':
                    self._set_team('allies')
                return
            if not quiet:
                personal_message(self, 'Marked for Teamswitch by admin!', color='green')
            self.mark_switch(force=force)
            if not force:
                if not quiet:
                    admin_message("Marked '%s' for Switch -- %s" % (self.name, invoker_name))
                return
            if player_in_vehicle(self._bf2_ply):
                if not quiet:
                    admin_message("Will murder and switch '%s' on vehicle exit -- %s" % (
                     self.name, invoker_name))
                return
            if not quiet:
                personal_message(self, 'Force Switched by admin!', color='green')
                admin_message('Force Switched %s  -- %s' % (self.name, invoker_name))
            success = self.kill()
            if not success:
                return
            return

    def mark_switch(self, force=False):
        if self._bf2_ply is None:
            LOG.warning('(fh2player.unmark_switch) bf2 player none, PANIC!')
            return
        else:
            if force:
                self._bf2_ply.force_switch = True
            curteam = self.team
            if curteam == 'allies':
                self._bf2_ply.switch_on_death_to = 'axis'
                LOG.debug("(fh2player.mark_switch) marking 'switch to axis'!")
                return
            if curteam == 'axis':
                self._bf2_ply.switch_on_death_to = 'allies'
                LOG.debug("(fh2player.mark_switch) marking 'switch to allies'!")
                return
            return

    def unmark_switch(self):
        if self._bf2_ply is None:
            LOG.warning('(fh2player.unmark_switch) bf2 player none, PANIC!')
            return
        else:
            LOG.debug('(fh2player.unmark_switch) unmarking switch!')
            self._bf2_ply.switch_on_death_to = None
            return

    def move_to_axis(self, force=False):
        curteam = self.team
        if curteam == 'axis':
            return
        self.switch(force=force)
        return

    def move_to_allies(self, force=False):
        curteam = self.team
        if curteam == 'allies':
            return
        self.switch(force=force)
        return

    def kill(self):
        """Murder the player"""
        bf2_ply = self._bf2_ply
        if player_in_closed_vehicle(bf2_ply):
            return False
        vehic = bf2_ply.getDefaultVehicle()
        if not vehic:
            return False
        vehic.setDamage(1e-07)
        return True

    def is_in_vehicle(self):
        return player_in_vehicle(self._bf2_ply)

    def resign(self):
        """Resign player from squad/commander position

        Weird hack to resign by double-switching, don't ask me.
        """
        curteam = self.team
        if curteam == 'allies':
            self._set_team('axis')
            self._set_team('allies')
        elif curteam == 'axis':
            self._set_team('allies')
            self._set_team('axis')
        return

    @property
    def is_in_squad(self):
        return bool(self.squad_number)

    @staticmethod
    def _get_hash(ply_index):
        plyrs = rcon('admin.listplayers')
        expr = '^Id:\\s*%s -.*\\s*CD-key hash: (?P<Hash>[0-9a-f]*)' % ply_index
        match = re.search(expr, plyrs, re.MULTILINE)
        if match and len(match.group('Hash')) == 32:
            key_hash = match.group('Hash')
        else:
            raise ValueError("Can't determin hash of player #%s" % ply_index)
        return key_hash


def find_player_by_index(idx, return_bf2=False):
    """Find player by index

    Parameters
    ----------
    idx: int
    return_bf2: bool
        skip wrapping in FH2Player and just return

    Returns
    -------
    admin.core.FH2Player or None
    """
    bf2_ply = bf2.playerManager.getPlayerByIndex(idx)
    if return_bf2:
        return bf2_ply
    else:
        if bf2_ply is None:
            return
        ply = FH2Player.from_bf2(bf2_ply)
        return ply


def find_player_by_name(query):
    """Find player by (partial) name

    Parameters
    ----------
    query: str
        (partial) player name, without clantag

    Returns
    -------
    admin.core.FH2Player or None or dict
        player on success. None on failure. dict on multiple matches.
    """
    query = query.lower()
    matches = {}
    for bf2_ply in bf2.playerManager.getPlayers():
        if not is_nobot(bf2_ply):
            continue
        try:
            ply_name = get_fullname(bf2_ply)[1].lower()
        except (ValueError, IndexError):
            rcon('admin.banPlayer %d %s' % (bf2_ply.index, BAN_DURATION))
            return

        fh_ply = FH2Player.from_bf2(bf2_ply)
        if query == ply_name:
            return fh_ply
        if query in ply_name:
            matches[ply_name] = fh_ply

    if not matches:
        return
    else:
        if len(matches) > 1:
            return matches
        if len(matches) != 1:
            raise ValueError('PANIC: Somehow not exactly 1 match, but not caught.')
        found = matches.values()[0]
        return found


def parse_playername(invoker, words):
    """Try to find a playername from the words array

    Parameters
    ----------
    invoker: admin.core.FH2Player
        player who executed the command
    words: list(str)
        playername to find

    Returns
    -------
    admin.core.FH2Player
    """
    if not words:
        personal_message(invoker, 'Error: No playername specified!', color='red')
        return
    else:
        query = words[0]
        res = find_player_by_name(query=query)
        if res is None:
            personal_message(invoker, "No player found for '%s'" % query, color='red')
            return
        if isinstance(res, dict):
            matches_str = (', ').join(res.keys())
            personal_message(invoker, "Multiple players found for '%s': %s" % (query, matches_str), color='green')
            return
        return res


def global_message(message, team=None, **fmtargs):
    """Send ingame message

    Parameters
    ----------
    message: str
    team: str
        either 'allies' or 'axis'
    **fmtargs:
        color, big
    """
    if not message.strip():
        return
    if team in ('axis', 'allies'):
        cmd = 'game.sayteam %d' % team_to_num(team)
    else:
        cmd = 'game.sayall'
    messages = wrap(message, width=MAX_LINE_LEN)
    messages = [format_message(msg, latin=False, **fmtargs) for msg in messages]
    LOG.info('(global_message) %s', message)
    for msg in messages:
        rcon('%s "%s"' % (cmd, msg))

    return


def personal_message(target, message, channel='Player', **fmtargs):
    """Send message to target player only

    If not possible to send player messages (on local games),
    falls back to sending global message instead

    Parameters
    ----------
    target: admin.core.FH2Player
    message: str
    **fmtargs:
        color, big
    """
    if not message.strip():
        return
    else:
        if not target:
            return
        try:
            if target.is_bot:
                return
        except AttributeError:
            pass

        if not is_internet():
            global_message(message, team=None, **fmtargs)
            return
        messages = wrap(message, width=MAX_LINE_LEN)
        messages = [format_message(msg, latin=False, **fmtargs) for msg in messages]
        magic_channel_number = SGL_TEXT_ARG2NUM[channel]
        try:
            for msg in messages:
                sgl_sendTextMessage(target.idx, magic_channel_number, 1, msg, 0)

        except AttributeError:
            LOG.info('(personal_message) could not send message!')

        return


def admin_message(message, **fmtargs):
    """Send message to ingame admins only

    Parameters
    ----------
    message: str
    **fmtargs:
        big, color
    """
    admins = admins_online()
    LOG.info('(admin_message) %s', message)
    if not is_internet():
        global_message(message, **fmtargs)
        return
    if not admins:
        return
    for admin in admins:
        personal_message(admin, message, **fmtargs)

    return


def cache_all_metas():
    mapnames = [nam for _i, (nam, _ly, _gm) in read_maplist().items()]
    for mapname in mapnames:
        meta = read_metadata(mapname)
        MapMetaCache.add_meta(mapname, meta)

    return


def get_meta(mapname):
    if MapMetaCache.has_meta(mapname):
        return MapMetaCache.read_meta(mapname)
    meta = read_metadata(mapname)
    MapMetaCache.add_meta(mapname, meta)
    return meta


def admins_online():
    """List all admins currently connected

    Returns
    -------
    list(str)
    """
    onl = []
    for bf2_ply in bf2.playerManager.getPlayers():
        if not is_nobot(bf2_ply):
            continue
        ply = FH2Player.from_bf2(bf2_ply)
        if ply.is_admin:
            onl.append(ply)

    return onl


def squad_members(squad_idx, teamname):
    """Get all members of squad #X in a team

    Parameters
    ----------
    squad_idx: int
    teamname: str

    Returns
    -------
    list(admin.core.FH2Player)
    """
    if not 0 < squad_idx < 9:
        return []
    members = []
    for bf2_ply in bf2.playerManager.getPlayers():
        if not is_nobot(bf2_ply):
            continue
        ply = FH2Player.from_bf2(bf2_ply)
        if not ply.team == teamname:
            continue
        if not ply.squad_number == squad_idx:
            continue
        members.append(ply)

    return members


def swap_teams(players=None):
    """Assign each player to the opposite team

    Parameters
    ----------
    players: list or None
        if not specified, load players from bf2
    """
    if players is None:
        players = [FH2Player.from_bf2(bf2_ply) for bf2_ply in bf2.playerManager.getPlayers() if is_valid(bf2_ply)]
    for ply in players:
        ply.switch(quiet=True)

    return


def scramble_teams(players=None):
    """Assign each player to a random team, but keep them balanced

    Parameters
    ----------
    players: list or None
        if not specified, load players from bf2
    """
    LOG.debug('Scrambling teams!')
    if players is None:
        players = [FH2Player.from_bf2(bf2_ply) for bf2_ply in bf2.playerManager.getPlayers() if is_valid(bf2_ply)]
    cur_teams = [p.team for p in players]
    n_players = len(players)
    LOG.debug('N players: %d', n_players)
    LOG.debug('current teams: %s', str(cur_teams))
    max_per_team = ceil(n_players / 2.0)
    n_axis = 0
    n_allies = 0
    new_teams = []
    for i in range(n_players):
        if n_axis >= max_per_team:
            new_teams.append('allies')
            n_allies += 1
            continue
        if n_allies >= max_per_team:
            new_teams.append('axis')
            n_axis += 1
            continue
        idx = randrange(2)
        if idx == 1:
            n_allies += 1
            new_teams.append('allies')
        elif idx == 0:
            n_axis += 1
            new_teams.append('axis')

    LOG.debug('NEW teams: %s', str(new_teams))
    for i, ply in enumerate(players):
        ct = cur_teams[i]
        nt = new_teams[i]
        if ct != nt:
            LOG.debug('Switching player idx %d', i)
            ply.switch(quiet=True)

    return


def pick_random_player_from_team(teamname):
    teamnum = TEAM2NUM[teamname]
    plys = [ply for ply in bf2.playerManager.getPlayers() if ply.getTeam() == teamnum]
    if not plys:
        return None
    else:
        return choice(plys)


def read_metadata(mapname):
    """Read the metadata from a map

    Parameters
    ----------
    mapname: str
        all lowercase, with underscores

    Returns
    -------
    dict
    """
    mapdir = join(LEVEL_DIR, mapname)
    if not exists(mapdir):
        mapdir_low = join(LEVEL_DIR, mapname.lower())
        if exists(mapdir_low):
            mapdir = mapdir_low
        else:
            LOG.warning('(read_metadata) mapdir does not exist!')
            raise IOError("map directory '%s' (and its lowercase version)does not exist!" % mapdir)
    meta_file = join(mapdir, 'meta.toml')
    if not exists(meta_file):
        LOG.warning('(read_metadata) meta file does not exist!')
        raise IOError("metadata file '%s' does not exist!" % meta_file)
    try:
        meta = toml.load(meta_file)
    except toml.decoder.TomlDecodeError as e:
        print "problem with file '%s'" % meta_file
        raise e

    return meta


def kick_player(target, delay=False, delay_time=5):
    """Ban a player

    Parameters
    ----------
    target: FH2Player
    """
    if target is None:
        return
    else:
        name = target.name
        idx = target.idx
        if not delay:
            _kick_bf2_ply(tuple([name, idx]))
            return
        bf2.Timer(_kick_bf2_ply, delta=delay_time, alwaysTrigger=1, data=tuple([name, idx]))
        return


def _kick_bf2_ply(data):
    name, idx = data
    TeamKillHistory.add_kick(name)
    rcon('admin.kickPlayer %d' % idx)
    return


def ban_player(player, permanent=False, duration=None, delay=False, delay_time=5):
    """Ban a player

    Parameters
    ----------
    player: FH2Player
    permanent: bool
    duration: int
    """
    if player is None:
        return
    else:
        if duration is None:
            duration = BAN_DURATION
        if permanent:
            duration = 'perma'
        if not delay:
            _ban_bf2_ply(tuple([player.idx, duration]))
            return
        bf2.Timer(_ban_bf2_ply, delta=delay_time, alwaysTrigger=1, data=tuple([player.idx, duration]))
        return


def _ban_bf2_ply(data):
    idx, duration = data
    rcon('admin.banPlayer %d %s' % (idx, duration))
    rcon('admin.banPlayerKey %d %s' % (idx, duration))
    return


def set_team_tickets(team, tickets):
    """Set teack tickets to desired amount

    Parameters
    ----------
    team: int or str
        1, 2, 'axis, 'allies'
    tickets: int
    """
    if team not in (1, 2):
        team = TEAM2NUM[team]
    if HAS_HUD_TICKETS:
        hudTickets.updateMaxTickets(tickets)
    bf2.gameLogic.setTickets(team, tickets)
    updateTicketLoss()
    return


def add_team_tickets(team, tickets):
    """Set teack tickets to desired amount

    Parameters
    ----------
    team: int or str
        1, 2, 'axis, 'allies'
    tickets: int
        positive or negative

    Returns
    -------
    int
    """
    if team not in (1, 2):
        team = TEAM2NUM[team]
    cur_tickets = get_team_tickets(team)
    set_team_tickets(team, cur_tickets + tickets)
    return


def position_infront(player, distance=3.0):
    """Transform vector to unit length

    Parameters
    ----------
    player: FH2Player
    distance: float
        how many meters infront of the player?

    Returns
    -------
    pos: (float, float, float)
    """
    if player is None:
        return
    else:
        pos = player.get_position()
        yaw = player.get_rotation()[0]
        yaw_rad = yaw / 180.0 * pi
        rot = [sin(yaw_rad), 0, cos(yaw_rad)]
        rot_norm = normed_3vec(rot)
        pos_infront = [pos[i] + distance * rot_norm[i] for i in range(3)]
        pos_infront[1] -= 1
        return pos_infront


def disband_squad(team, squad_num):
    """Resign ALL squad members, destroying the squad

    Parameters
    ----------
    team: str
    squad_num: int
    """
    members = squad_members(squad_num, team)
    msg = localize_message('HUD_TEXT_FH_ADMIN_DISSOLVED')
    for ply in members:
        personal_message(ply, msg, color='red')
        ply.resign()

    return


def fix_squad_bug():
    if 'linux' not in sys.platform:
        raise NotImplementedError('Only available on linux boxes, sorry!')
    from admin.memory import get_squads
    squads = get_squads()
    for team in (1, 2):
        for squad in range(1, 10):
            if squads[team][squad].playercount == 0 and squads[team][squad].currentSL != -1:
                squads[team][squad].currentSL = -1

    for team in (1, 2):
        for squad in range(1, 10):
            sl_idx = squads[team][squad].currentSL
            if sl_idx == -1:
                continue
            sl = bf2.playerManager.getPlayerByIndex(sl_idx)
            if sl is None:
                squads[team][squad].currentSL = -1
            elif sl.getSquadId() != squad or sl.getTeam() != team:
                squads[team][squad].currentSL = -1

    return


def squadless_players(team=None, separate_afk=True):
    if team is not None and not isinstance(team, int):
        team = TEAM2NUM[team]
    out = []
    bf2_players = bf2.playerManager.getPlayers()
    for bf2_ply in bf2_players:
        if not is_nobot(bf2_ply):
            continue
        if bf2_ply.getSquadId():
            continue
        try:
            _, name = get_fullname(bf2_ply)
        except (ValueError, IndexError):
            rcon('admin.banPlayer %d %s' % (bf2_ply.index, BAN_DURATION))
            continue

        if separate_afk and AfkList.has_player(name):
            continue
        if team is None or int(bf2_ply.getTeam()) == team:
            out.append(bf2_ply)
        else:
            continue

    return out


def nuke_all_cameras():
    cams = getObjectsOfTemplate('filmcamera')
    for cam, cam_id in cams:
        if cam.hasArmor:
            try:
                cam.setDamage(0)
            except Exception:
                LOG.info('Could not damage filmcamera!')

        else:
            deleteObject(cam_id)

    return


def capture_flag(cp, new_team, do_event=True):
    """Change control point ownership.

    Parameters
    ----------
    cp
        control point object
    new_team: str
        axis, allies, grey
    """
    new_team_num = team_to_num(new_team)
    if new_team_num in (1, 2):
        top = 1
    else:
        top = 0
    if top:
        cp.cp_setParam('flag', new_team_num)
    cp.cp_setParam('team', new_team_num)
    updateCPTakeOverState(cp)
    updateTicketLoss()
    if do_event:
        caller = g_hooker.registered.get('ControlPointChangedOwner', None)
        if caller:
            caller(cp, top)
    return


def set_team_bleed(teamname, amount):
    """Set team bleedrate

    Parameters
    ----------
    teamname: str
    amount: int
        tickets lost per minute
    """
    team_id = TEAM2NUM[teamname]
    setDefaultTicketLossPerMin(team_id, amount)
    updateTicketLoss()
    return


def mod_dir():
    """Find dir of current mod.

    USUALLY 'mods/fh2' but might differ on a dev version
    """
    return str(sgl_getModDirectory())


def toggle_state(invoker, command, label):
    """Remdul: toggles a state"""
    state = int(rcon(command))
    if state == 0:
        state = 1
    else:
        state = 0
    stateStr = 'Off' if state == 0 else 'On'
    personal_message(invoker, label + ' ' + stateStr, color='blue')
    rcon(command + ' %i' % state)
    return True


def inspect_object(bf2_ply):
    root = root_object(bf2_ply.getVehicle())
    for obj in walk_children(root):
        nam_o = obj.templateName
        path = hierarchy(obj)
        depth = len(path) - 1
        rot = '(%.2f, %.2f, %.2f)' % obj.getRotation()
        pos = '(%.3f, %.3f, %.3f)' % obj.getPosition()
        typ = find_type(nam_o)
        LOG.warning('    ' * depth + "'%s' ['%s'], pos %s, rot %s" % (
         nam_o,
         typ,
         pos,
         rot))

    return


def reboot_server(delay_time=5):
    """Reboot machine"""
    bf2.Timer(_reboot_server, delta=delay_time, alwaysTrigger=1)
    return


def _reboot_server(*_args, **_kwargs):
    import os
    from signal import SIGTERM
    os.kill(os.getpid(), SIGTERM)
    return


def is_blacklisted(query):
    for mg in BIPOD_MGS:
        if query.lower() in mg.lower():
            return True

    return False


def parse_player_docopt(usage, invoker, words):
    """Helper function to parse command line

    Handles error message to invoker and returns None on wrong input

    Parameters
    ----------
    usage: str
        docopt-compatible Usage string. must follow the
        '!CMD PLAYER ... || !CMD -n IDX ...' pattern
    invoker: FH2Player
    words: list(str)

    Returns
    -------
    FH2Player or None
    """
    try:
        args = docopt(usage, argv=words)
    except DocoptExit:
        personal_message(invoker, usage, color='red')
        return

    use_idx = bool(args['-n'])
    if use_idx:
        idx_raw = args['IDX']
        try:
            idx = int(idx_raw)
        except (ValueError, TypeError):
            personal_message(invoker, "Index '%s' is not a number" % idx_raw, color='red')
            return

        res = find_player_by_index(idx)
        if res is None:
            personal_message(invoker, "No player found for index '%d'" % idx, color='red')
            return
        return res
    query = args['PLAYER']
    target = find_player_by_name(query)
    if target is None:
        personal_message(invoker, "No player found for '%s'" % query, color='red')
        return
    else:
        if isinstance(target, dict):
            matches_str = (', ').join(target.keys())
            personal_message(invoker, "Multiple players found for '%s': %s" % (query, matches_str), color='green')
            return
        return target


def parse_reason_docopt(usage, invoker, words):
    """Helper function to parse command line

    Handles error message to invoker and returns None on wrong input

    Parameters
    ----------
    usage: str
        docopt-compatible Usage string. must have a 'REASON' arg
    invoker: FH2Player
    words: list(str)

    Returns
    -------
    str or None
    """
    try:
        args = docopt(usage, argv=words)
    except DocoptExit:
        personal_message(invoker, usage, color='red')
        return

    try:
        reason = args['REASON']
    except KeyError:
        personal_message(invoker, usage, color='red')
        return

    reason = parse_reason(reason)
    return reason


def parse_usage_docopt(usage, invoker, words):
    """Check if command used correctly at all

    Handles error message to invoker and returns None on wrong input

    Parameters
    ----------
    usage: str
        docopt-compatible Usage string. must have a 'REASON' arg
    invoker: FH2Player
    words: list(str)

    Returns
    -------
    str or None
    """
    try:
        docopt(usage, argv=words)
    except DocoptExit:
        personal_message(invoker, usage, color='red')
        return False

    return True


return

# okay decompiling C:\fh2_1\mods\fh2\python\admin\bf2_tools.pyc
