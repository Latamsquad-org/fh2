# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    aiPush,
    balanceSPs,
    disableSPs,
    limitKit,
    NCOrifleData,
    teamSPs,
    ticketLoss,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GM_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("gm_heavy_soldier", "ba_nco_soldier"),
    )
]


kit_limits_64 = [
    plugin(
        limitKit, team=1, kit="GM_Limited_Assault_MP40_K98_early", slot=1, limit=0.07
    ),
    plugin(
        limitKit, team=2, kit="BA_Limited_Assault_TommygunD_No4", slot=1, limit=0.07,
    ),
    plugin(
        limitKit, team=1, kit="GM_Limited_Support_MG34_K98", slot=3, limit=0.09
    ),
    plugin(
        limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.1
    ),
]


kit_limits_16 = [
    plugin(
        limitKit, team=1, kit="GM_Limited_Assault_MP40_K98_early", slot=1, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="BA_Limited_Assault_TommygunD_No4",  slot=1, limit=0.1,
    ),
    plugin(
        limitKit, team=1, kit="GM_Limited_Support_MG34_K98", slot=3, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.1
    ),
	    plugin(
        limitKit, team=2, kit="BA_Grenadier_Limited", slot=4, limit=0.2
    ),
]


tickets_64 = [plugin(ticketLoss, ticketLoss1=12, ticketLoss2=10)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=8, ticketLoss2=8)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=4, ticketLoss2=4)]

coop_limit = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=3.0 / 32.0,
        kit="GM_ScoutK98Short_early",
        soldier="gm_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GM_Limited_Assault_MP40_K98_early",
        soldier="gm_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=14.0 / 32.0,
        kit="GM_RiflemanK98",
        soldier="gm_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GM_Limited_Support_MG34_K98",
        soldier="gm_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=3.0 / 32.0,
        kit="GM_EngineerK98Short",
        soldier="gm_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=3.0 / 32.0,
        kit="GM_ATPzB39",
        soldier="gm_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=3.0 / 32.0,
        kit="BA_ScoutEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=5.0 / 32.0,
        kit="BA_Limited_Assault_TommygunD_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=16.0 / 32.0,
        kit="BA_RiflemanEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=4.0 / 32.0,
        kit="BA_Limited_Support_Bren_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=3.0 / 32.0,
        kit="BA_EngineerEarly",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=1.0 / 32.0,
        kit="BA_ATBoys",
        soldier="ba_heavy_soldier",
    ),
]
coop_sp = [
    plugin(disableSPs),
    plugin(
        disableSPs,
        cp="CP_64_The_Battle_for_Sfakia_German_Advance_2",
        team=1,
        we_own=(
            "CP_64_The_Battle_for_Sfakia_British_Rearguard "
            "or CP_64_The_Battle_for_Sfakia_Main_Road_West "
            "or CP_64_The_Battle_for_Sfakia_Upper_Town"
        ),
    ),
    plugin(
        disableSPs,
        cp="CP_64_The_Battle_for_Sfakia_Town_Square",
        team=2,
        we_own="CP_64_The_Battle_for_Sfakia_German_Advance_2",
    ),
    plugin(
        disableSPs,
        cp="CP_64_The_Battle_for_Sfakia_The_Monastary",
        team=2,
        we_own="CP_64_The_Battle_for_Sfakia_British_Rearguard and *",
    ),
]
coop_balance = [
    plugin(
        balanceSPs,
        custom_weights=[
            dict(
                cp=(
                    "CP_64_The_Battle_for_Sfakia_German_Advance_1, "
                    "CP_64_The_Battle_for_Sfakia_German_Advance_2"
                ),
                weight=500000,
            ),
            dict(
                cp="CP_64_The_Battle_for_Sfakia_German_Advance_3",
                weight=250000,
            ),
            dict(
                cp="CP_64_The_Battle_for_Sfakia_British_Rearguard",
                team=1,
                weight=333000,
            ),
            dict(
                cp="CP_64_The_Battle_for_Sfakia_British_Rearguard",
                team=2,
                weight=500000,
            ),
            dict(
                cp=(
                    "CP_64_The_Battle_for_Sfakia_Command_Post,"
                    "CP_64_The_Battle_for_Sfakia_Harbour,"
                    "CP_64_The_Battle_for_Sfakia_Main_Road_West,"
                    "CP_64_The_Battle_for_Sfakia_The_Monastary,"
                    "CP_64_The_Battle_for_Sfakia_Town_Square,"
                    "CP_64_The_Battle_for_Sfakia_Upper_Town"
                ),
                weight=1000000,
            ),
        ],
    ),
]
coop_teamsp = [plugin(teamSPs)]
coop_push = [plugin(aiPush)]

gpm_cq = {
    64: tickets_64 + kit_limits_64 + nco,
    32: tickets_32 + kit_limits_64 + nco,
    16: tickets_16 + kit_limits_16 + nco,
}

gpm_coop = {
    64: coop_limit
    + coop_sp
    + coop_balance
    + coop_teamsp
    + coop_push
    + tickets_64
    + nco,
}
sp3 = gpm_coop
