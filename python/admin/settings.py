# Embedded file name: python/admin/settings.py
"""
settings
"""
from os import pardir
from os.path import join, dirname, abspath, exists
from random import seed
import toml
from nameauth import normalize_admin_list, get_admin_level_by_name
MOD_DIR = abspath(join(dirname(__file__), pardir, pardir))
LEVEL_DIR = join(MOD_DIR, 'levels')
CONF_FNAME = 'config.toml'
CONFIG_FILE = join(MOD_DIR, CONF_FNAME)
if not exists(CONFIG_FILE):
    CONFIG_FILE = abspath(join(dirname(__file__), pardir, CONF_FNAME))
ADMINS_FNAME = 'admins.toml'
ADMINS_FILE = join(MOD_DIR, ADMINS_FNAME)
if not exists(ADMINS_FILE):
    ADMINS_FILE = abspath(join(dirname(__file__), pardir, ADMINS_FNAME))
BADNAMES_FNAME = 'badnames.toml'
BADNAMES_FILE = join(MOD_DIR, BADNAMES_FNAME)
if not exists(BADNAMES_FILE):
    BADNAMES_FILE = abspath(join(dirname(__file__), pardir, BADNAMES_FNAME))
BANLIST_FNAME = 'banlist.toml'
BANLIST_FILE = join(MOD_DIR, BANLIST_FNAME)
if not exists(BANLIST_FILE):
    BANLIST_FILE = abspath(join(dirname(__file__), pardir, BANLIST_FNAME))
try:
    adm_conf = toml.load(ADMINS_FILE)
    ADMINS_HIGH = normalize_admin_list(adm_conf['users']['admins_high'])
    ADMINS_MID = normalize_admin_list(adm_conf['users']['admins_mid'])
    ADMINS_LOW = normalize_admin_list(adm_conf['users']['admins_low'])
except (IOError, KeyError, TypeError):
    ADMINS_LOW = frozenset()
    ADMINS_MID = frozenset()
    ADMINS_HIGH = frozenset()


def get_admin_level(name):
    """Resolve admin level for a raw player name (with or without [TAG])."""
    return get_admin_level_by_name(name, ADMINS_HIGH, ADMINS_MID, ADMINS_LOW)

DEFAULTS = {'general': {'debug': False,
             'beta': False,
             'enable_beta_commands': False,
             'random_seed': None},
 'messages': {'welcome': '',
              'rules': 'For Rules visit https://playfh2.com/stats/?go=server-rules',
              'announce': [],
              'announce_interval': 300,
              'show_disconnect': False,
              'show_connect': True},
 'janitor': {'enable_afk_tracking': False,
             'min_players_for_kick': 50,
             'balance_afks_before_minplayers': True,
             'max_idle_time': 600,
             'idle_check_interval': 30,
             'idle_yaw_threshold': 0.5,
             'ban_duration': 1209600},
 'maps': {'randomize_maps': False,
          'favorites': [],
          'favorite_weight': 10,
          'n_last_played': 12,
          'n_last_fronts': 1,
          'n_last_gameplay_tags': 1,
          'save_last_played': False},
 'balance': {'enable_autobalance': False,
             'swap_on_start': True,
             'scramble_on_start': False,
             'scramble_interval': 4,
             'protect_commander': True,
             'protect_squadmembers': True,
             'protect_squadleader': True,
             'smb_difference': 1,
             'block_self_switch': False},
 'hud': {'use_new_format': True},
 'stats_api': {'enabled': False,
               'backend_url': None,
               'token': None},
 'voting': {'vote_runnext_allowed': False,
            'vote_reroll_allowed': False,
            'notify_period': 14,
            'vote_duration': 60}}
try:
    CONFIG = toml.load(CONFIG_FILE)
except IOError:
    CONFIG = DEFAULTS

def grab(key, subkey, type_ = None):
    try:
        val = CONFIG[key][subkey]
        if type_ is not None:
            val = ensure_type(val, type_)
    except (TypeError, KeyError, ValueError):
        val = DEFAULTS[key][subkey]

    return val


def ensure_type(key, type_):
    if not isinstance(key, type_):
        raise ValueError
    return type_(key)


IS_BETA = grab('general', 'beta', bool)
ENABLE_BETA_COMMANDS = grab('general', 'enable_beta_commands', bool)
DEBUG = grab('general', 'debug', bool)
RANDOM_SEED = grab('general', 'random_seed')
WELCOME_MSG = grab('messages', 'welcome')
RULES_MSG = grab('messages', 'rules')
ANNOUNCE_MSGS = grab('messages', 'announce')
ANNOUNCE_INTERVAL = grab('messages', 'announce_interval', int)
SHOW_DISCONNECT = grab('messages', 'show_disconnect', bool)
SHOW_CONNECT = grab('messages', 'show_connect', bool)
MAPS_RANDOMIZE = grab('maps', 'randomize_maps', bool)
MAPS_FAVORITES = grab('maps', 'favorites', list)
FAVORITE_WEIGHT = grab('maps', 'favorite_weight', float)
N_LAST_PLAYED = grab('maps', 'n_last_played', int)
N_LAST_FRONTS = grab('maps', 'n_last_fronts', int)
N_LAST_GAMEPLAY_TAGS = grab('maps', 'n_last_gameplay_tags', int)
SAVE_LAST_PLAYED = grab('maps', 'save_last_played', bool)
ENABLE_AUTOBALANCE = grab('balance', 'enable_autobalance', bool)
SWAP_ON_START = grab('balance', 'swap_on_start', bool)
SCRAMBLE_ON_START = grab('balance', 'scramble_on_start', bool)
SCRAMBLE_INTERVAL = grab('balance', 'scramble_interval', int)
PROTECT_COMMANDER = grab('balance', 'protect_commander', bool)
PROTECT_SQUADMEMBERS = grab('balance', 'protect_squadmembers', bool)
PROTECT_SQUADLEADER = grab('balance', 'protect_squadleader', bool)
SMB_DIFFERENCE = grab('balance', 'smb_difference', int)
BLOCK_SELF_SWITCH = grab('balance', 'block_self_switch', bool)
ENABLE_AFK_TRACKING = grab('janitor', 'enable_afk_tracking', bool)
MIN_PLAYERS_FOR_KICK = grab('janitor', 'min_players_for_kick', int)
BALANCE_AFKS_BEFORE_MINPLAYERS = grab('janitor', 'balance_afks_before_minplayers', bool)
MAX_IDLE_TIME = grab('janitor', 'max_idle_time', int)
IDLE_CHECK_INTERVAL = grab('janitor', 'idle_check_interval', int)
IDLE_YAW_THRESHOLD = grab('janitor', 'idle_yaw_threshold', float)
BAN_DURATION = grab('janitor', 'ban_duration', int)
USE_NEW_FORMAT = grab('hud', 'use_new_format', bool)
STATS_API_ENABLED = grab('stats_api', 'enabled', bool)
STATS_BACKEND_URL = grab('stats_api', 'backend_url')
STATS_API_TOKEN = grab('stats_api', 'token')
VOTE_RUNNEXT_ALLOWED = grab('voting', 'vote_runnext_allowed', bool)
VOTE_REROLL_ALLOWED = grab('voting', 'vote_reroll_allowed', bool)
NOTIFY_PERIOD = grab('voting', 'notify_period', int)
VOTE_DURATION = grab('voting', 'vote_duration', int)
if RANDOM_SEED in {'',
 'none',
 'None',
 'nil',
 'NIL'}:
    RANDOM_SEED = None
seed(RANDOM_SEED)
MAP_RECHECK_DURATION = 120