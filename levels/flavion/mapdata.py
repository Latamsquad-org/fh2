# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    teamSPs,
    spawnerCondition,
    neighPush,
)

kitlimits_64 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GW_SMGAssault_mp28_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="FA_active_RiflemanGL",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_LMG_early_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="FA_active_LMG",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_AntitankPzb770_Limited",
        limit=0.1,
    ),
    plugin(limitKit, team=2, slot=5, kit="FA_active_antitank", limit=0.2),
]

spawnerConditions32 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_flavion_battery_h39a",
        we_dont_own="CP_32_flavion_east",
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=25, ticketLoss2=25)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_early", "FA_active_NCO"),
        soldiers=("gw_heer_unteroffizier_early", "fg_chasseur_nco"),
    ),
]

push_32 = [
    plugin(
        neighPush,
        sources="CP_32_flavion_axismain",
        targets="CP_32_favion_outskirts,CP_32_flavion_east",
    ),
    plugin(
        neighPush,
        sources="CP_32_favion_outskirts",
        targets="CP_32_flavion_east",
    ),
    plugin(
        neighPush,
        sources="CP_32_flavion_east",
        targets=(
            "CP_32_flavion_garage,CP_32_flavion_church,CP_32_flavion_chapel"
        ),
    ),
    plugin(
        neighPush,
        sources="CP_32_flavion_garage",
        targets="CP_32_flavion_battery,CP_32_flavion_church",
    ),
    plugin(
        neighPush,
        sources="CP_32_flavion_church",
        targets=(
            "CP_32_flavion_battery,CP_32_flavion_west,CP_32_flavion_chapel,"
            "CP_32_flavion_garage"
        ),
    ),
    plugin(
        neighPush,
        sources="CP_32_flavion_chapel",
        targets="CP_32_flavion_west,CP_32_flavion_church",
    ),
    plugin(
        neighPush,
        sources="CP_32_flavion_west",
        targets="CP_32_flavion_battery",
    ),
    plugin(
        neighPush,
        sources="CP_32_flavion_battery",
        targets="CP_32_flavion_west",
    ),
]

gpm_cq = {
    64: tickets_64 + kitlimits_64 + rifleNCO + spawns,
    32: (
        tickets_64
        + kitlimits_64
        + rifleNCO
        + spawns
        + push_32
        + spawnerConditions32
    ),
    16: tickets_16 + kitlimits_64 + rifleNCO + spawns,
}

gpm_coop = {
    64: tickets_64 + spawns + rifleNCO,
    32: push_32 + spawns + rifleNCO,
    16: tickets_16 + spawns + rifleNCO,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
