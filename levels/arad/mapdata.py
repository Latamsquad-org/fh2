# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    spawnerCondition,
    NCOrifleData,
    limitKit,
    ticketLoss,
    teamSPs,
)

spawns = [plugin(teamSPs)]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GW_STG44Assault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="RE_LMG_limited", limit=0.1),
    plugin(
        limitKit, team=1, slot=5, kit="GW_AntiTankAssault_Limited", limit=0.2
    ),
    plugin(
        limitKit, team=2, slot=5, kit="RE_AntiTankAssault_Limited", limit=0.2
    ),
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO_mp40_g43", "RE_NCO"),
        soldiers=("Gcwhcamo_nco", "re_nco_soldier"),
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]
pco_spawners_64 = [
    # Axis reinforcements
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Arad_23rdPanzerDivision_tiger",
        they_own=(
            "CP_64_arad_westvillage and CP_64_arad_northfield and "
            "CP_64_arad_southfield and CP_64_Arad_EastVillage"
        ),
    ),
    # Allied reinforcements
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Arad_18thTankCorps_su152r",
        they_own=(
            "CP_64_arad_westvillage and CP_64_arad_northfield and "
            "CP_64_arad_southfield and CP_64_arad_crashsite"
        ),
    ),
]
gpm_cq = {
    64: tickets_64 + kitlimits_64 + rifleNCO + pco_spawners_64 + spawns,
    32: tickets_32 + kitlimits_64 + rifleNCO + spawns,
    16: tickets_16 + kitlimits_64 + rifleNCO + spawns,
}


gpm_coop = {
    16: tickets_16 + rifleNCO + spawns,
    32: tickets_32 + rifleNCO + spawns,
    64: tickets_64 + pco_spawners_64 + rifleNCO + spawns,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
