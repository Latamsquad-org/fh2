# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    teamSPs,
    push,
    linkCPs,
    ticketLoss,
    neighPush,
    disableSPs,
    NCOrifleData,
    aiPush,
    timeCP,
)

team_spawns = [
    plugin(teamSPs),  # Auto-fill
]
nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "BW_NCO_StenMk5"),
        soldiers=("gw_heer_unteroffizier", "bjglide_sgt"),
    )
]

nco_16 = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "BW_NCO_StenMk5"),
        soldiers=("gw_heer_unteroffizier", "bjglide_sgt_night"),
    )
]

push_64 = [
    # Sector A
    plugin(
        neighPush,
        sources="CP_64_pegasus_chateau_benouville",
        targets="CP_64_pegasus_benouville",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_benouville, CP_64_pegasus_le_port",
        targets="CP_64_pegasus_crossroads",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_crossroads",
        targets="CP_64_pegasus_le_port",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_reinforcements",
        targets="CP_64_pegasus_le_port",
    ),
    plugin(
        linkCPs,
        target="CP_64_sector_a_locker_dummy",
        source="CP_64_pegasus_benouville, CP_64_pegasus_crossroads, CP_64_pegasus_le_port",
        default_zero=True,
    ),
    plugin(
        neighPush,
        sources="CP_64_sector_a_locker_dummy",
        targets="CP_64_pegasus_pegasus_bridge",
    ),
    # Sector B
    plugin(
        neighPush,
        sources="CP_64_pegasus_le_mariquet",
        targets="CP_64_pegasus_ranville, CP_64_pegasus_ranville_le_bas, CP_64_pegasus_church",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_ranville",
        targets="CP_64_pegasus_church",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_church",
        targets="CP_64_pegasus_ranville_le_bas",
    ),
    plugin(
        linkCPs,
        target="CP_64_sector_b_locker_dummy",
        source="CP_64_pegasus_ranville, CP_64_pegasus_ranville_le_bas, CP_64_pegasus_church",
        default_zero=True,
    ),
    plugin(
        neighPush,
        sources="CP_64_sector_b_locker_dummy",
        targets="CP_64_pegasus_longueville",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_longueville",
        targets="CP_64_pegasus_ranville_le_bas, CP_64_pegasus_church",
        two_way_neighboring=False,
    ),
    # Bridges
    plugin(
        neighPush,
        sources="CP_64_pegasus_pegasus_bridge",
        targets="CP_64_pegasus_crossroads",
        two_way_neighboring=False,
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_horsa_bridge",
        targets="CP_64_pegasus_longueville",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_pegasus_bridge",
        targets="CP_64_pegasus_horsa_bridge",
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_pegasus_chateau_benouville",
        target="CP_32_pegasus_benouville",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_pegasus_benouville",
        target="CP_32_pegasus_crossroads",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_pegasus_benouville",
        target="CP_32_pegasus_timed_locker_dummy",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_32_pegasus_crossroads",
        target="CP_32_pegasus_bridge",
        attacker=1,
        display_arrow=True,
    ),
]

lock_delay_32 = [
    plugin(timeCP, team=1, target="CP_32_pegasus_timed_locker_dummy", time=360),
]

push_16 = [
    plugin(
        push,
        source="CP_16_pegasus_assaultforce",
        target="CP_16_pegasus_germanposition",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_pegasus_germanposition",
        target="CP_16_pegasus_bridge",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_pegasus_bridge",
        target="CP_16_pegasus_crossroads",
        attacker=2,
        display_arrow=True,
    ),
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_mk5", limit=0.3),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG26_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Colt_Limited", limit=0.15),
    plugin(
        limitKit, team=1, slot=5, kit="GW_RifleAssault_G41_Limited", limit=0.1
    ),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.15),
]

tickets = [
    plugin(ticketLoss, ticketLoss1=25, ticketLoss2=10000),
]

tickets_32 = [
    plugin(ticketLoss, ticketLoss1=30, ticketLoss2=10000),
]

tickets_16 = [
    plugin(ticketLoss, ticketLoss1=10000, ticketLoss2=30),
]


push_32_AI = [
  plugin(push, source = 'CP_64_pegasus_le_mariquet', target = 'CP_64_pegasus_ranville, CP_64_pegasus_ranville_le_bas, CP_64_pegasus_church', attacker = 1, display_arrow = False),

  plugin(push, source = 'CP_64_sector_b_locker_dummy', target = 'CP_64_pegasus_longueville', attacker = 1, display_arrow = False, wants_source_marker = False),

  plugin(push, source = 'CP_64_pegasus_longueville', target = 'CP_64_pegasus_horsa_bridge', attacker = 1, display_arrow = False),

  plugin(linkCPs, target = 'CP_64_sector_b_locker_dummy', source = 'CP_64_pegasus_ranville, CP_64_pegasus_ranville_le_bas, CP_64_pegasus_church', default_zero = True),
]

push_64_AI = [
    plugin(
        neighPush,
        sources="CP_64_pegasus_chateau_benouville",
        targets="CP_64_pegasus_benouville",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_benouville, CP_64_pegasus_le_port",
        targets="CP_64_pegasus_crossroads",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_crossroads",
        targets="CP_64_pegasus_le_port",
    ),
    plugin(
        neighPush,
        sources="CP_64_pegasus_reinforcements",
        targets="CP_64_pegasus_le_port",
    ),
    plugin(
        linkCPs,
        target="CP_64_sector_a_locker_dummy",
        source="CP_64_pegasus_benouville, CP_64_pegasus_crossroads, CP_64_pegasus_le_port",
        default_zero=True,
    ),
    plugin(
        neighPush,
        sources="CP_64_sector_a_locker_dummy",
        targets="CP_64_pegasus_pegasus_bridge",
    ),
]

push_16_AI = [
    plugin(
        push,
        source="CP_16_pegasus_assaultforce",
        target="CP_16_pegasus_germanposition",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_pegasus_germanposition",
        target="CP_16_pegasus_bridge",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_pegasus_bridge",
        target="CP_16_pegasus_crossroads",
        attacker=2,
        display_arrow=True,
    ),
]

disable_AI = [
    plugin(disableSPs),  # Auto-fill
]

kit_limits_coop = [
plugin(limitKit, team = 1, slot = 0, limit = 4.0/32.0, kit = "GW_Scout", soldier = "gw_heer_spaher"),
plugin(limitKit, team = 1, slot = 1, limit = 6.0/32.0, kit = "GW_SMGAssault_Limited", soldier = "gw_heer_maschinenpistole"),
plugin(limitKit, team = 1, slot = 2, limit = 9.0/32.0, kit = "GW_RifleAssault", soldier = "gw_heer_gewehr"),
plugin(limitKit, team = 1, slot = 3, limit = 6.0/32.0, kit = "GW_LMG_MG26_Limited", soldier = "gw_heer_maschinengewehr"),
plugin(limitKit, team = 1, slot = 4, limit = 4.0/32.0, kit = "GW_Engineer_Satchel", soldier = "gw_heer_pionier"),
plugin(limitKit, team = 1, slot = 5, limit = 4.0/32.0, kit = "GW_RifleAssault_G41_Limited", soldier = "gw_heer_panzerabwehr"),

plugin(limitKit, team = 2, slot = 0, limit = 4.0/32.0, kit = "BW_Scout", soldier = "bjglide_pvt_night"),
plugin(limitKit, team = 2, slot = 1, limit = 6.0/32.0, kit = "BW_SMGAssault_mk5", soldier = "bj_airborne_cpl"),
plugin(limitKit, team = 2, slot = 2, limit = 9.0/32.0, kit = "BW_RifleAssault", soldier = "bj_airborne_pvt"),
plugin(limitKit, team = 2, slot = 3, limit = 6.0/32.0, kit = "BW_LMG_Colt_Limited", soldier = "bj_airborne_cpl_night"),
plugin(limitKit, team = 2, slot = 4, limit = 4.0/32.0, kit = "BW_Engineer_Satchel", soldier = "bjglide_cpl"),
plugin(limitKit, team = 2, slot = 5, limit = 4.0/32.0, kit = "BW_Antitank_Limited", soldier = "bj_airborne_cpl"),

plugin(NCOrifleData, kits = ('GW_NCO', 'BW_NCO_Stenmk5'), soldiers = ("gw_heer_unteroffizier", "bjglide_sgt")),
]

kit_limits_coop_16 = [
plugin(limitKit, team = 1, slot = 0, limit = 4.0/32.0, kit = "GW_Scout", soldier = "gw_heer_spaher"),
plugin(limitKit, team = 1, slot = 1, limit = 6.0/32.0, kit = "GW_SMGAssault_Limited", soldier = "gw_heer_maschinenpistole"),
plugin(limitKit, team = 1, slot = 2, limit = 9.0/32.0, kit = "GW_RifleAssault", soldier = "gw_heer_gewehr"),
plugin(limitKit, team = 1, slot = 3, limit = 6.0/32.0, kit = "GW_LMG_MG26_Limited", soldier = "gw_heer_maschinengewehr"),
plugin(limitKit, team = 1, slot = 4, limit = 4.0/32.0, kit = "GW_Engineer_Satchel", soldier = "gw_heer_pionier"),
plugin(limitKit, team = 1, slot = 5, limit = 4.0/32.0, kit = "GW_RifleAssault_G41_Limited", soldier = "gw_heer_panzerabwehr"),

plugin(limitKit, team = 2, slot = 0, limit = 4.0/32.0, kit = "BW_Scout", soldier = "bjglide_pvt_night"),
plugin(limitKit, team = 2, slot = 1, limit = 6.0/32.0, kit = "BW_SMGAssault_mk5", soldier = "bjglide_cpl_night"),
plugin(limitKit, team = 2, slot = 2, limit = 9.0/32.0, kit = "BW_RifleAssault", soldier = "bjglide_pvt_night"),
plugin(limitKit, team = 2, slot = 3, limit = 6.0/32.0, kit = "BW_LMG_Colt_Limited", soldier = "bjglide_cpl_night"),
plugin(limitKit, team = 2, slot = 4, limit = 4.0/32.0, kit = "BW_Engineer_Satchel", soldier = "bjglide_cpl_night"),
plugin(limitKit, team = 2, slot = 5, limit = 4.0/32.0, kit = "BW_Antitank_Limited", soldier = "bjglide_cpl_night"),

plugin(NCOrifleData, kits = ('GW_NCO', 'BW_NCO_Stenmk5'), soldiers = ("gw_heer_unteroffizier", "bjglide_sgt_night")),
]

gpm_cq = {
    64: tickets + team_spawns + kitlimits_64 + push_64 + nco,
    32: tickets_32 + team_spawns + kitlimits_64 + push_32 + lock_delay_32 + nco,
    16: tickets_16 + team_spawns + kitlimits_64 + push_16 + nco_16,
}

gpm_coop = {
    64: tickets + team_spawns + kit_limits_coop + push_64_AI,
    32: tickets_32 + team_spawns + kit_limits_coop + push_32_AI,
    16: tickets_16 + team_spawns + kit_limits_coop_16 + push_16_AI + disable_AI,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
