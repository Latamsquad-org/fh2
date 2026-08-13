# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    DoubleBleed,
    teamSPs,
    limitKit,
    NCOrifleData,
    neighPush,
    ticketLoss,
    FastBleed,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("ga_tunisia_nco_soldier", "bw_nco_soldier_alt"),
    )
]

double_32 = [plugin(DoubleBleed)]

fast_bleed_64 = [
    plugin(
        FastBleed,
        target_flags=[
            "CP_64_mareth_Lower_Gabes",
            "CP_64_mareth_Upper_Gabes",
        ],
        affected_team="axis",
        bleed=720,
    )
]

spawns_64 = [
    plugin(teamSPs),  # Auto-fill
]

spawns_32 = [
    plugin(teamSPs),  # Auto-fill
]

spawns_16 = [
    plugin(teamSPs),  # Auto-fill
]

kit_limits = [
    plugin(limitKit, team=1, kit="GW_SMGAssault_Limited", slot=1, limit=0.16),
    plugin(limitKit, team=2, kit="BA_AssaultTommygunS", slot=1, limit=0.12),
    plugin(limitKit, team=1, kit="GA_Limited_Support_MG34_K98", slot=3, limit=0.08),
    plugin(limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.12),
    plugin(limitKit, team=1, kit="GA_AntiTank_k98_haft", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="BA_TankHunter_hawkin_rifle", slot=5, limit=0.1),
]

kit_limits_16 = [
    plugin(limitKit, team=1, kit="GW_SMGAssault_Limited", slot=1, limit=0.1),
    plugin(limitKit, team=2, kit="BA_AssaultTommygunS", slot=1, limit=0.1),
    plugin(limitKit, team=1, kit="GA_Limited_Support_MG34_K98", slot=3, limit=0.05),
    plugin(limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="GA_AntiTank_k98_haft", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="BA_Grenadier_Limited", slot=5, limit=0.1 ),
]

push_64 = [
    plugin(
        neighPush,
        sources="CP_64_mareth_Medenine",
        targets=[
            "CP_64_mareth_Toujane",
            "CP_64_mareth_Mareth",
        ],
        main_bases_2="CP_64_mareth_Medenine",
    ),
    plugin(
        neighPush,
        sources="CP_64_mareth_Toujane",
        targets=[
            "CP_64_mareth_Matmata",
        ],
    ),
    plugin(
        neighPush,
        sources=[
            "CP_64_mareth_Matmata",
        ],
        targets="CP_64_mareth_Gap_Defense",
    ),
    plugin(
        neighPush,
        sources="CP_64_mareth_Mareth",
        targets="CP_64_mareth_second_line",
    ),
    plugin(
        neighPush,
        sources="CP_64_mareth_Gap_Defense",
        targets="CP_64_mareth_second_line",
    ),
    plugin(
        neighPush,
        sources="CP_64_mareth_Gap_Defense",
        targets="CP_64_mareth_second_line",
    ),
    plugin(
        neighPush,
        sources=[
            "CP_64_mareth_second_line",
        ],
        targets=[
            "CP_64_mareth_Upper_Gabes",
            "CP_64_mareth_Lower_Gabes",
        ],
    ),
    plugin(
        neighPush,
        sources=[
            "CP_64_mareth_Gap_Defense",
        ],
        targets=[
            "CP_64_mareth_Upper_Gabes",
            "CP_64_mareth_Lower_Gabes",
        ],
    ),
]
tickets_64 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20)]


gpm_cq = {
    64: (nco + kit_limits + push_64 + tickets_64 + fast_bleed_64 + spawns_64),
    32: (nco + kit_limits + spawns_32 + double_32),
    16: (nco + kit_limits_16 + spawns_16 + double_32),
}

gpm_coop = {
    64: (nco + push_64 + tickets_64),
    32: (nco + double_32),
    16: (nco),
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
