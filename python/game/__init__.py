# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,R0913,C0301,W0603,C0302,C0411,E1101,C0209,W0703  # noqa
# vim:set ts=4 sts=4 sw=4 et syntax=python:
"""Gameplay functionality

"""
from __future__ import print_function

import sys

from . import readConfig
if sys.version_info == (2, 7, 12, 'final', 0):
    is_bf2 = True
else:
    is_bf2 = False
    sys.path += ['python', 'python_dummy', '../../python']

config = readConfig.config()

# must be placed AFTER `is_bf2`
from .log import log  # pylint: disable=C0413  # noqa

fhlog = log()
if is_bf2:
    # past spitfire to future spitfire: don't try to add 2.45 config
    # compatibility here. 2.45 doesn't even run config in sandbox env,
    # and isn't using readConfig class at all, so it is totally not
    # compatible and will not work end of the story, don't even think
    # about it.
    config.read('mods/fh2/fh2.cfg')

    fhlog.post_init()

    sublog = fhlog.peon(__name__)

dbg_level = config.get('debug_level')
if dbg_level and dbg_level.lower() == 'debug':  # pylint: disable=R1703
    is_debug = True
else:
    is_debug = False


def newTimerOnTrigger(self):
    try:
        self.targetFunc(self.data)
    except Exception:
        sublog.exception('onTrigger exception')
        self.destroy()


if is_bf2:
    import bf2
    bf2.Timer.onTrigger = newTimerOnTrigger

try:
    import bf2.stats.stats

    # thanks to [poe2]seigman and [dcon]kiff below...
    from game.stats.stats import fh2stats_init  # pylint: disable=C0412

    bf2.stats.stats.init = fh2stats_init

    print('patched stat functions [python/game/__init__.py]')
except Exception:
    pass

# Since some of the HUD buttons got a second game.radioMessage
# understandable by AI and the rest of them got a second dummy
# game.radioMessage, we need to double the ammount of messages which
# triggers chat bans.
if is_bf2:
    import host
    try:
        spam_treshold = float(host.rcon_invoke('sv.radioMaxSpamFlagCount'))
        host.rcon_invoke('sv.radioMaxSpamFlagCount %s' % (spam_treshold * 2.0))
    except Exception:
        pass

# Stats LatamSquad FH2 -> stats.latamsquad.org/api/upload_fh2.php (auto-init al importar)
if is_bf2:
    try:
        import latamstats  # noqa: F401
        print('latamstats loaded [python/game/__init__.py]')
    except Exception:
        print('latamstats failed to load [python/game/__init__.py]')
