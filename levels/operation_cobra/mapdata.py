# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    delaySpawners,
    disableSPs,
    limitKit,
    NCOrifleData,
    spawnerCondition,
    teamSPs,
    ticketLoss,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO", "UW_NCO"),
        soldiers=("gs_waffen_unteroffizier", "uw_ranger_sgt"),
    )
]

spawns_64 = [
    plugin(
        teamSPs,
        sps=[
            "CP_64_cobra_Hebecrevonairfield_axis1",
            "CP_64_cobra_Hebecrevonairfield_axis2",
            "CP_64_cobra_Hebecrevonairfield_axis3",
            "CP_64_cobra_Hebecrevonairfield_axis4",
            "CP_64_cobra_Hebecrevonairfield_axis5",
            "CP_64_cobra_Hebecrevonairfield_axis6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_cobra_Hebecrevonairfield_allied1",
            "CP_64_cobra_Hebecrevonairfield_allied2",
            "CP_64_cobra_Hebecrevonairfield_allied3",
            "CP_64_cobra_Hebecrevonairfield_allied4",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_cobra_Hebecrevonchurch_axis1",
            "CP_64_cobra_Hebecrevonchurch_axis2",
            "CP_64_cobra_Hebecrevonchurch_axis3",
            "CP_64_cobra_Hebecrevonchurch_axis4",
            "CP_64_cobra_Hebecrevonchurch_axis5",
            "CP_64_cobra_Hebecrevonchurch_axis6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_cobra_Hebecrevonchurch_allies1",
            "CP_64_cobra_Hebecrevonchurch_allies2",
            "CP_64_cobra_Hebecrevonchurch_allies3",
            "CP_64_cobra_Hebecrevonchurch_allies4",
            "CP_64_cobra_Hebecrevonchurch_allies5",
        ],
        team=2,
    ),
]
spawns_16 = [
    plugin(
        teamSPs,
        sps=[
            "CP_16_cobra_church_1_axis",
            "CP_16_cobra_church_2_axis",
            "CP_16_cobra_church_3_axis",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_16_cobra_church_1_allies",
            "CP_16_cobra_church_2_allies",
            "CP_16_cobra_church_3_allies",
            "CP_16_cobra_church_4_allies",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_16_cobra_barn_1_axis",
            "CP_16_cobra_barn_2_axis",
            "CP_16_cobra_barn_3_axis",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=["CP_16_cobra_barn_1_allies", "CP_16_cobra_barn_2_allies"],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_16_cobra_townsquare_1_axis",
            "CP_16_cobra_townsquare_2_axis",
            "CP_16_cobra_townsquare_3_axis",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_16_cobra_townsquare_1_allies",
            "CP_16_cobra_townsquare_2_allies",
            "CP_16_cobra_townsquare_3_allies",
        ],
        team=2,
    ),
]
kitlimits_64 = [
    plugin(limitKit, team=1, kit="GS_SMGAssault_Limited", slot=1, limit=0.25),
    plugin(limitKit, team=2, kit="UW_SMGAssault_Limited", slot=1, limit=0.25),
    plugin(limitKit, team=1, kit="GS_LMG_MG42_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="UW_LMG_Limited", slot=3, limit=0.15),
    plugin(
        limitKit, team=1, kit="GW_AntitankAssault_grenades", slot=5, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="UW_AntitankAssault_Limited", slot=5, limit=0.1
    ),
]
kitlimits_16 = [
    plugin(limitKit, team=1, kit="GS_SMGAssault_Limited", slot=1, limit=0.25),
    plugin(limitKit, team=2, kit="UW_SMGAssault_Limited", slot=1, limit=0.25),
    plugin(limitKit, team=1, kit="GS_LMG_MG42_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="UW_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="GW_RifleAssault_Limited", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="UW_Grenadier_Limited", slot=5, limit=0.1),
]
tickets_64 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=700, ticketLoss2=700)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]
reinforcements_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_cobra_germainbase_pantherg2_0, CP_32_cobra_germainbase_pantherg_0, CP_32_cobra_germainbase_pziv3_0, CP_32_cobra_germainbase_fighterbomber_extra",
        they_own="CP_32_cobra_crossroads",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_cobra_alliedbase_m18_1, CP_32_cobra_alliedbase_m4a1_76_1, CP_32_cobra_alliedbase_m4a1_764, CP_32_cobra_alliedbase_fighterbomber_extra",
        they_own="CP_32_cobra_crossroads",
    ),
]



gpm_cq = {
    64: tickets_64 + kitlimits_64 + spawns_64 + nco,
    32: tickets_32 + reinforcements_32 + nco,
    16: tickets_16 + kitlimits_16 + spawns_16 + nco,
}

gpm_coop = {
    64: tickets_64 + spawns_64 + nco,
    32: tickets_32 + reinforcements_32 + nco,
    16: tickets_16 + spawns_16 + nco,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
