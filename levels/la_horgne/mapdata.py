#!/usr/bin/env python3
# pylint: disable=C0103,F0401,C0415,R0914,W0511,C0114
from game.plugins import (
    plugin,
    limitKit,
    linkCPs,
    teamSPs,
    NCOrifleData,
    ticketLoss,
    spawnerCondition,
    disableSPs,
    push,
    DoubleBleed,
)

NCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_early", "FA_Spahi_NCO"),
        soldiers=("gw_heer_unteroffizier_early", "fg_spahi_sgt"),
    )
]

spawns = [
    plugin(teamSPs),
]

kit_limits_64 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_SMGAssault_mp38_early_Limited",
        slot=1,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_early_Limited",
        slot=3,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_LMG",
        slot=3,
        limit=0.18,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_Engineer_early_limited",
        slot=4,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_Engineer",
        slot=4,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault_GeballteLadung",
        slot=5,
        limit=0.10,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_AntiTank",
        slot=5,
        limit=0.18,
    ),
]

kit_limits_32 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_SMGAssault_mp38_early_Limited",
        slot=1,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_early_Limited",
        slot=3,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_LMG",
        slot=3,
        limit=0.18,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_Engineer_early_limited",
        slot=4,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_Engineer",
        slot=4,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault_GeballteLadung",
        slot=5,
        limit=0.10,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_AntiTank",
        slot=5,
        limit=0.18,
    ),
]

kit_limits_8 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_Scout_early_limited",
        slot=0,
        limit=0.10,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_Scout_limited",
        slot=0,
        limit=0.10,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_SMGAssault_mp38_early_Limited",
        slot=1,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_RiflemanGL",
        slot=1,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_early_Limited",
        slot=3,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_LMG",
        slot=3,
        limit=0.18,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_RifleAssault_early_limited",
        slot=4,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_Rifleman_Limited",
        slot=4,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault_GeballteLadung",
        slot=5,
        limit=0.10,
    ),
    plugin(
        limitKit,
        team=2,
        kit="FA_Spahi_AntiTank",
        slot=5,
        limit=0.18,
    ),
]

spawns_64 = [
    plugin(
        teamSPs,
        sps=[
            "CP_64_la_horgne_3rd_Spahis_Brigade_Fr1",
            "CP_64_la_horgne_3rd_Spahis_Brigade_Fr2",
            "CP_64_la_horgne_3rd_Spahis_Brigade_Fr3",
            "CP_64_la_horgne_3rd_Spahis_Brigade_Fr4",
            "CP_64_la_horgne_3rd_Spahis_Brigade_Fr5",
            "CP_64_la_horgne_3rd_Spahis_Brigade_Fr6",
            "CP_64_la_horgne_3rd_Spahis_Brigade_Fr7",
            "CP_64_la_horgne_La_Tour_Farm_Fr1",
            "CP_64_la_horgne_La_Tour_Farm_Fr2",
            "CP_64_la_horgne_La_Tour_Farm_Fr3",
            "CP_64_la_horgne_Voirin_Farm_Fr1",
            "CP_64_la_horgne_Voirin_Farm_Fr2",
            "CP_64_la_horgne_Voirin_Farm_Fr3",
            "CP_64_la_horgne_Perotin_Farm_Fr1",
            "CP_64_la_horgne_Perotin_Farm_Fr2",
            "CP_64_la_horgne_Perotin_Farm_Fr3",
            "CP_64_la_horgne_Perotin_Farm_Fr4",
            "CP_64_la_horgne_Perotin_Farm_Fr5",
            "CP_64_la_horgne_Perotin_Farm_Fr6",
            "CP_64_la_horgne_Church_Place_Fr1",
            "CP_64_la_horgne_Church_Place_Fr2",
            "CP_64_la_horgne_Church_Place_Fr3",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_la_horgne_La_Tour_Farm_Ger1",
            "CP_64_la_horgne_La_Tour_Farm_Ger2",
            "CP_64_la_horgne_La_Tour_Farm_Ger3",
            "CP_64_la_horgne_La_Tour_Farm_Ger4",
            "CP_64_la_horgne_La_Tour_Farm_Ger5",
            "CP_64_la_horgne_Voirin_Farm_Ger2",
            "CP_64_la_horgne_Voirin_Farm_Ger3",
            "CP_64_la_horgne_Voirin_Farm_Ger4",
            "CP_64_la_horgne_Voirin_Farm_Ger5",
            "CP_64_la_horgne_Perotin_Farm_Ger1",
            "CP_64_la_horgne_Perotin_Farm_Ger2",
            "CP_64_la_horgne_Perotin_Farm_Ger3",
            "CP_64_la_horgne_Church_Place_Ger1",
            "CP_64_la_horgne_Church_Place_Ger2",
            "CP_64_la_horgne_Church_Place_Ger3",
        ],
        team=1,
    ),
]

spawnerCondition_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="Reinforcements_pzIV,Reinforcements_pzIIIe",
        we_own="Reinforcements",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="Reinforcements_h39_1,Reinforcements_h39_2",
        we_own="Reinforcements",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="cp_64_la_horgne_renault_secret_arsenal_an_old_friend",
        they_own="CP_64_la_horgne_Church_Place",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="cp_64_la_horgne_renault_secret_arsenal_another_old_friend",
        we_own="CP_64_la_horgne_Church_Place",
    ),
]



links_64 = [
    plugin(
        linkCPs,
        target="Reinforcements",
        source=[
            "CP_64_la_horgne_Perotin_Farm",
            "CP_64_la_horgne_Church_Place",
        ],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="Reinforcements",
        source=[
            "CP_64_la_horgne_Church_Place",
            "CP_64_la_horgne_La_Tour_Farm",
        ],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="Reinforcements",
        source=["CP_64_la_horgne_Church_Place", "CP_64_la_horgne_Voirin_Farm"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="Reinforcements",
        source=[
            "CP_64_la_horgne_Perotin_Farm",
            "CP_64_la_horgne_Voirin_Farm",
            "CP_64_la_horgne_La_Tour_Farm",
        ],
        invert=True,
    ),
]

spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_la_horgne_1PDZ_pziv",
        we_dont_own="CP_32_La_Horgne_Cemetery, CP_32_La_Horgne_Church_pace, CP_32_La_Horgne_Perotin_Farm",
    ),
]

spawnerConditions_16 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="cp_16_la_horgne_not_my_war_renault",
        we_dont_own="cp_16_la_horgne_perotin_farm, cp_16_la_horgne_church",
    ),
]

push_16 = [
    plugin(
        push,
        source="cp_16_la_horgne_la_tour_farm",
        target="cp_16_la_horgne_perotin_farm, cp_16_la_horgne_church",
        attacker=1,
    ),
]

bleed_64 = [plugin(ticketLoss, ticketLoss1=14, ticketLoss2=12)]

bleed_32 = [plugin(ticketLoss, ticketLoss1=12, ticketLoss2=10)]

bleed_16 = [
    plugin(DoubleBleed),
]

bleed_8 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

gpm_cq = {
    64: spawns_64
    + links_64
    + kit_limits_64
    + spawnerCondition_64
    + bleed_64
    + NCO,
    32: kit_limits_32 + bleed_32 + NCO + spawns,
    16: kit_limits_64 + bleed_64 + NCO + spawns + push_16 + bleed_16,
    128: kit_limits_8 + bleed_8 + NCO + spawns,
}


tickets_coop_64 = [plugin(ticketLoss, ticketLoss1=14, ticketLoss2=12)]

gpm_coop = {
    64: tickets_coop_64 + spawns_64 + NCO + spawnerCondition_64 + links_64,
    32: bleed_32 + NCO + spawns,
    16: NCO + spawns,
}


sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
