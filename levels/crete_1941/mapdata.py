# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    teamSPs,
    NCOrifleData,
    DoubleBleed,
)

double_bleed_32 = [plugin(DoubleBleed)]

kit_limits = [
    plugin(
        limitKit,
        team=1,
        kit="GM_Limited_Assault_MP40_K98_para_early",
        slot=1,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Assault_TommygunD_No4",
        slot=1,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GM_Limited_Support_MG34_K98",
        slot=3,
        limit=0.12,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Support_Bren_No4",
        slot=3,
        limit=0.12,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GM_ATPzB39_Limited",
        slot=5,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_ATBoys_Limited",
        slot=5,
        limit=0.1,
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=5, ticketLoss2=20)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]
spawns = [
    plugin(
        teamSPs,
        sps=[
            "CP_16_Crete1941_Olive_axis1",
            "CP_16_Crete1941_Olive_axis2",
            "CP_16_Crete1941_Olive_axis3",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_16_Crete1941_Olive_allies1",
            "CP_16_Crete1941_Olive_allies2",
            "CP_16_Crete1941_Olive_allies3",
        ],
        team=2,
    ),
]

nco = [
    plugin(
        NCOrifleData,
        kits=("GM_NCOMP40_para_early", "BA_NCOTommygunS"),
        soldiers=("gb_nco_grunmeliert", "ba_nco_soldier"),
    ),
]
gpm_cq = {
    64: tickets_64 + kit_limits + nco,
    32: tickets_32 + kit_limits + nco + double_bleed_32,
    16: tickets_16 + kit_limits + spawns + nco,
}

gpm_coop = {
    64: tickets_64 + nco,
    32: tickets_32 + nco,
    16: tickets_16 + nco,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
