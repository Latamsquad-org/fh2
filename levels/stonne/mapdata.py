# -*- coding: utf-8 -*-
# pylint: disable=W0232,C0103,C0111,F0401
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    limitKit,
    push,
    teamSPs,
    linkCPs,
    NCOrifleData,
    timeCP,
    ticketLoss,
    spawnerCondition,
)

spawns_16 = [plugin(teamSPs)]

NCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_early", "FA_standard_NCO"),
        soldiers=("gw_heer_unteroffizier_early", "fg_nco"),
    ),
]

NCO_16 = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_MP34", "FA_standard_NCO"),
        soldiers=("gw_heer_unteroffizier_early", "fg_nco"),
    ),
]

kit_limits_64 = [
    plugin(
        limitKit, team=1, kit="GW_SMGAssault_mp38_early_Limited", slot=1, limit=0.15),
    plugin(limitKit, team=2, kit="FA_standard_RiflemanGL", slot=1, limit=0.15),
    plugin(limitKit, team=1, kit="GW_LMG_early_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="FA_standard_LMG", slot=3, limit=0.15),
    plugin(limitKit, team=1, kit="GW_AntitankAssault_GeballteLadung", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="FA_active_AntiTank", slot=5, limit=0.13),
]

kit_limits_32 = [
    plugin(limitKit, team=1, kit="GW_SMGAssault_mp38_early_Limited", slot=1, limit=0.15),
    plugin(limitKit, team=2, kit="FA_standard_RiflemanGL", slot=1, limit=0.15),
    plugin(limitKit, team=1, kit="GW_LMG_early_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="FA_standard_LMG", slot=3, limit=0.15),
    plugin(limitKit, team=1, kit="GW_Engineer_early_limited", slot=4, limit=0.12),
    plugin(limitKit, team=2, kit="FA_standard_Engineer_limited", slot=4, limit=0.12),
    plugin(limitKit, team=1, kit="GW_AntitankAssault_GeballteLadung", slot=5, limit=0.08),
    plugin(limitKit, team=2, kit="FA_active_AntiTank", slot=5, limit=0.1),
]

kit_limits_16 = [
    plugin(limitKit, team=1, kit="GW_SMGAssault_mp34_early_Limited", slot=1, limit=0.05),
    plugin(limitKit, team=2, kit="FA_standard_RiflemanGL", slot=1, limit=0.05),
    plugin(limitKit, team=1, kit="GW_LMG_early_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="FA_standard_LMG", slot=3, limit=0.1),  
    plugin(limitKit, team=1, kit="GW_RifleAssault_early_limited", slot=4,limit=0.1),
    plugin(limitKit, team=2, kit="FA_standard_Rifleman_Limited", slot=4,limit=0.1),
    plugin(limitKit, team=1, kit="GW_AntitankAssault_GeballteLadung", slot=5,limit=0.05),
    plugin(limitKit, team=2, kit="FA_active_AntiTank", slot=5, limit=0.05),
]

links_64 = [
    plugin(
        linkCPs,
        target="Stonne_dummy",
        source=["Rue_du_Talus", "Notre_Dame_de_Stonne"],
    ),
    plugin(
        linkCPs,
        target="Stonne_dummy",
        source=["Rue_du_Talus", "Rue_du_Paquis"],
    ),
    plugin(
        linkCPs,
        target="Stonne_dummy",
        source=["Notre_Dame_de_Stonne", "Rue_du_Paquis"],
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_stonne_Route_des_Grandes_Armoises",
        target="CP_32_stonne_Chateau_d_eau",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_stonne_Chateau_d_eau",
        target="CP_32_stonne_Cafe",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_stonne_Chateau_d_eau",
        target="CP_32_stonne_Mairie",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_stonne_Cafe, CP_32_stonne_Mairie",
        target="CP_32_stonne_Route_de_Sedan",
        attacker=2,
        display_arrow=True,
    ),
]

spawns_32 = [
    plugin(
        teamSPs,
        sps=[
            "CP_32_stonne_Chateau_d_eau_Fr1",
            "CP_32_stonne_Chateau_d_eau_Fr2",
            "CP_32_stonne_Chateau_d_eau_Fr3",
            "CP_32_stonne_Cafe_Fr1",
            "CP_32_stonne_Cafe_Fr2",
            "CP_32_stonne_Cafe_Fr3",
            "CP_32_stonne_Mairie_Fr1",
            "CP_32_stonne_Mairie_Fr2",
            "CP_32_stonne_Mairie_Fr3",
            "CP_32_stonne_Route_de_Sedan_Fr1",
            "CP_32_stonne_Route_de_Sedan_Fr2",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_32_stonne_Chateau_d_eau_Ger1",
            "CP_32_stonne_Chateau_d_eau_Ger2",
            "CP_32_stonne_Chateau_d_eau_Ger3",
            "CP_32_stonne_Chateau_d_eau_Ger4",
            "CP_32_stonne_Cafe_Ger1",
            "CP_32_stonne_Cafe_Ger2",
            "CP_32_stonne_Cafe_Ger3",
            "CP_32_stonne_Cafe_Ger4",
            "CP_32_stonne_Mairie_Ger1",
            "CP_32_stonne_Mairie_Ger2",
            "CP_32_stonne_Mairie_Ger3",
            "CP_32_stonne_Mairie_Ger4",
            "CP_32_stonne_Route_de_Sedan_Ger1",
            "CP_32_stonne_Route_de_Sedan_Ger2",
            "CP_32_stonne_Route_de_Sedan_Ger3",
            "CP_32_stonne_Route_de_Sedan_Ger4",
            "CP_32_stonne_Route_de_Sedan_Ger5",
        ],
        team=1,
    ),
]

spawns_64 = [
    plugin(
        teamSPs,
        sps=[
            "French_forwardspawn_dummy_1",
            "French_forwardspawn_dummy_2",
            "French_forwardspawn_dummy_3",
            "Rue_du_Talus_1",
            "Rue_du_Talus_3",
            "Rue_du_Talus_5",
            "Notre_Dame_de_Stonne_2",
            "Notre_Dame_de_Stonne_4",
            "Notre_Dame_de_Stonne_6",
            "Rue_du_Paquis_2",
            "Rue_du_Paquis_4",
            "Rue_du_Paquis_6",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "Pain_De_Sucre_Ger1",
            "Pain_De_Sucre_Ger2",
            "Pain_De_Sucre_Ger3",
            "Pain_De_Sucre_Ger4",
            "Pain_De_Sucre_Ger5",
            "Rue_du_Talus_6",
            "Rue_du_Talus_4",
            "Rue_du_Talus_2",
            "Notre_Dame_de_Stonne_1",
            "Notre_Dame_de_Stonne_3",
            "Notre_Dame_de_Stonne_5",
            "Rue_du_Paquis_1",
            "Rue_du_Paquis_3",
            "Rue_du_Paquis_5",
            "German_forwardspawn_dummy_1",
            "German_forwardspawn_dummy_2",
            "German_forwardspawn_dummy_3",
        ],
        team=1,
    ),
]

spawnerCondition_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_stonne_Route_de_Sedan_pzrIV_2",
        they_own="CP_32_stonne_Chateau_d_eau",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_stonne_Route_de_Sedan_pzjgr",
        they_own="CP_32_stonne_Cafe and CP_32_stonne_Mairie",
    ),
]

spawnerCondition_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "GrossDeutschland_pzrIII_2,GrossDeutschland_PzrIV_1,"
            "GrossDeutschland_PzrIV_2,German_forwardspawn_dummy_pzrII,"
            "German_forwardspawn_dummy_pzrIII,GrossDeutschland_fighter"
        ),
        they_own="Stonne_dummy",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "3e_Division_Cuirassee_H39_2,3e_Division_Cuirassee_B1Bis,"
            "3e_Division_Cuirassee_B1Bis2,3e_Division_Cuirassee_H39_R1,"
            "3e_Division_Cuirassee_H39_R2"
        ),
        they_own="Stonne_dummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="Stonne_dummy_panhard178_sdkfz222",
        we_own="Rue_du_Talus and Notre_Dame_de_Stonne and Rue_du_Paquis",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="Stonne_dummy_panhard178_sdkfz222",
        we_own="Rue_du_Talus and Notre_Dame_de_Stonne and Rue_du_Paquis",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="GrossDeutschland_Sdkfz222",
        we_own="Pain_de_Sucre",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="GrossDeutschland_pzrIII_1",
        we_own="Route_de_Buzancy",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="3e_Division_Cuirassee_panhard178",
        we_own="Route_de_Buzancy",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="3e_Division_Cuirassee_h39",
        they_own="Pain_de_Sucre and Route_de_Buzancy",
    ),
]

spawndelay_64 = [
    plugin(timeCP, team=-1, target="French_forwardspawn_dummy", time=60),
    plugin(timeCP, team=1, target="German_forwardspawn_dummy", time=360),
]

bleed_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

bleed_32 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=11)]

bleed_64 = [plugin(ticketLoss, ticketLoss1=16, ticketLoss2=16)]

gpm_cq = {
    64: (
        links_64
        + spawns_64
        + kit_limits_64
        + spawnerCondition_64
        + bleed_64
        + spawndelay_64
        + NCO
    ),
    32: (
        spawns_32
        + spawnerCondition_32
        + push_32
        + kit_limits_32
        + bleed_32
        + NCO
    ),
    16: kit_limits_16 + bleed_16 + NCO_16 + spawns_16,
}


gpm_coop = {
    64: links_64 + spawns_64 + NCO + spawnerCondition_64 + bleed_64 + spawndelay_64,
    32: spawns_32 + push_32 + bleed_32 + NCO,
    16: bleed_16 + NCO_16 + spawns_16,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
