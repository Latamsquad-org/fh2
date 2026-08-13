# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,R0913
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    teamSPs,
)

kit_limits_64 = [
    plugin(limitKit, kit="JP_SMGAssault_Limited", team=1, slot=1, limit=0.1),
    plugin(
        limitKit,
        kit="BE_Limited_Assault_TommygunD_No4",
        team=2,
        slot=1,
        limit=0.1,
    ),
    plugin(limitKit, kit="JP_LMG_Limited", team=1, slot=3, limit=0.1),
    plugin(
        limitKit, kit="BE_Limited_Support_Bren_No4", team=2, slot=3, limit=0.1
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=12, ticketLoss2=12)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=25, ticketLoss2=25)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("jp_NCO", "BE_NCOTommygunS"),
        soldiers=("jp_rilfe_khaki_sgt", "BE_nco_soldier"),
    ),
]

team_spawns = [
    plugin(teamSPs),  # Auto-fill
]

gpm_cq = {
    64: kit_limits_64 + rifleNCO + tickets_64 + team_spawns,
    32: kit_limits_64 + rifleNCO + tickets_32 + team_spawns,
    16: kit_limits_64 + rifleNCO + tickets_16 + team_spawns,
}
