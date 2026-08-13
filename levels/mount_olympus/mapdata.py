# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    linkCPs,
    NCOrifleData,
    teamSPs,
    ticketLoss,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40_early", "BA_NCOTommygunS"),
        soldiers=("gw_heer_unteroffizier_early", "ba_nco_soldier"),
    )
]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_Olympus_allies_dummy",
        source=[
            "CP_64_Olymp_monastery",
            "CP_64_Olymp_town_square",
            "CP_64_Olymp_kafeteria",
            "CP_64_Olymp_castle",
            "CP_64_Olymp_leptokaria",
            "CP_64_Olymp_rapsani_station",
        ],
        invert=True,
    ),
]

spawns = [
    plugin(
        teamSPs,
        sps=[
            "CP_64_Olymp_leptokaria_5",
            "CP_64_Olymp_leptokaria_0_6",
            "CP_64_Olymp_leptokaria_0_7",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_Olymp_leptokaria_1",
            "CP_64_Olymp_leptokaria_2",
            "CP_64_Olymp_leptokaria_3",
            "CP_64_Olymp_leptokaria_4",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_Olymp_castle_1",
            "CP_64_Olymp_castle_2",
            "CP_64_Olymp_castle_3",
            "CP_64_Olymp_castle_4",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_Olymp_castle_14_0",
            "CP_64_Olymp_castle_0_5",
            "CP_64_Olymp_castle_16_0",
            "CP_64_Olymp_castle_0_6",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_Olymp_town_square_2_0",
            "CP_64_Olymp_town_square_3_0",
            "CP_64_Olymp_town_square_4_0",
            "CP_64_Olymp_town_square_7_0",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_Olymp_town_square_8_0",
            "CP_64_Olymp_town_square_10_0",
            "CP_64_Olymp_town_square_11_0",
            "CP_64_Olymp_town_square_12_0",
            "CP_64_Olymp_town_square_16_0",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_Olymp_kafeteria_4_0",
            "CP_64_Olymp_kafeteria_6_0",
            "CP_64_Olymp_kafeteria_8_0",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_Olymp_kafeteria_9_0",
            "CP_64_Olymp_kafeteria_13_0",
            "CP_64_Olymp_kafeteria_15_0",
            "CP_64_Olymp_kafeteria_17_0",
        ],
        team=2,
    ),
]

kit_limits_64 = [
    plugin(
        limitKit,
        team=1,
        kit="GM_Limited_Assault_MP40_K98_early",
        slot=1,
        limit=0.18,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Assault_TommygunD_No4",
        slot=1,
        limit=0.18,
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
        limit=0.18,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GM_ATPzB39_Limited",
        slot=5,
        limit=0.05,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_ATBoys_Limited",
        slot=5,
        limit=0.05,
    ),
]

kit_limits_32_16 = [
    plugin(
        limitKit,
        team=1,
        kit="GM_Limited_Assault_MP40_K98_early",
        slot=1,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Assault_TommygunD_No4",
        slot=1,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GM_Limited_Support_MG34_K98",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Support_Bren_No4",
        slot=3,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_Engineer_early_Satchel_Limited",
        slot=4,
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Grenadier_Limited",
        slot=4,
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankPzb770_Limited",
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

tickets_64 = [
    plugin(
        ticketLoss,
        ticketLoss1=20,
        ticketLoss2=20,
    ),
]
tickets_16 = [
    plugin(
        ticketLoss,
        ticketLoss1=1000,
        ticketLoss2=1000,
    ),
]

spawns_AI = [plugin(teamSPs)]

gpm_cq = {
    64: tickets_64 + kit_limits_64 + spawns + links_64 + nco,
    32: kit_limits_32_16 + nco,
    16: kit_limits_32_16 + tickets_16 + nco,
}
gpm_coop = {
    64: tickets_64 + spawns + links_64 + nco,
    32: spawns_AI + tickets_64 + nco,
    16: tickets_16 + spawns_AI + nco,
}
sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
