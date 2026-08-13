# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    aiPush,
    disableSPs,
    dynamicOOB,
    limitKit,
    NCOrifleData,
    neighPush,
    spawnerCondition,
    teamSPs,
    ticketLoss,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_m34", "UW_NCO"),
        soldiers=("gb_nco_splittermuster", "uw_29th_sgt"),
    )
]

kit_limits = [
    plugin(
        limitKit,
        team=1,
        kit="GW_Scout_G41_limited",
        slot=0,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GS_SMGAssault_Limited",
        slot=1,
        limit=0.14,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=0.2,
        kit="GW_Engineer_Satchel_limited",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_mk3_Limited",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GS_LMG_FG42_Limited",
        slot=3,
        limit=0.08,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault_Limited",
        slot=5,
        limit=0.04,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankAssault_Limited",
        slot=5,
        limit=0.04,
    ),
]

kit_limits_16 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_Scout_G41_limited",
        slot=0,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GS_SMGAssault_Limited",
        slot=1,
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=0.1,
        kit="GW_Engineer_Satchel_limited",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_mk3_Limited",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GS_LMG_FG42_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault_Limited",
        slot=5,
        limit=0.05,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankAssault_Limited",
        slot=5,
        limit=0.05,
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_brest_fountain": {
                "allies": {
                    "destroys": ["CombatArea_64p_yesgo_axis_fountain"],
                },
            },
        },
        delay_axis=60,
        delay_allies=0,
    )
]
dynamicoob_32 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_32_brest_fountain": {
                "allies": {
                    "destroys": ["CombatArea_32p_yesgo_axis_fountain"],
                },
            },
        },
        delay_axis=60,
        delay_allies=0,
    )
]

push_64 = [
    plugin(
        neighPush,
        main_bases_1="CP_64_brest_harbour",
        main_bases_2="CP_64_brest_industry",
    ),
    plugin(
        neighPush,
        sources="CP_64_brest_industry",
        targets="CP_64_brest_fountain",
    ),
    plugin(
        neighPush,
        sources="CP_64_brest_fountain",
        targets="CP_64_brest_navyhq,CP_64_brest_plaza",
    ),
    plugin(
        neighPush,
        sources="CP_64_brest_navyhq",
        targets="CP_64_brest_flakposition",
    ),
    plugin(
        neighPush,
        sources="CP_64_brest_plaza",
        targets="CP_64_brest_navyhq,CP_64_brest_boulangerie",
    ),
    plugin(
        neighPush,
        sources="CP_64_brest_flakposition",
        targets="CP_64_brest_boulangerie,CP_64_brest_ruins",
    ),
    plugin(
        neighPush,
        sources="CP_64_brest_boulangerie",
        targets="CP_64_brest_flakposition,CP_64_brest_ruins",
    ),
    plugin(
        neighPush,
        sources="CP_64_brest_ruins",
        targets="CP_64_brest_harbour",
    ),
]
push_32 = [
    plugin(
        neighPush,
        main_bases_1="CP_32_brest_harbour",
        main_bases_2="CP_32_brest_industry",
    ),
    plugin(
        neighPush,
        sources="CP_32_brest_industry",
        targets="CP_32_brest_fountain",
    ),
    plugin(
        neighPush,
        sources="CP_32_brest_fountain",
        targets="CP_32_brest_plaza",
    ),
    plugin(
        neighPush,
        sources="CP_32_brest_plaza",
        targets="CP_32_brest_boulangerie",
    ),
    plugin(
        neighPush,
        sources="CP_32_brest_boulangerie",
        targets="CP_32_brest_ruins",
    ),
    plugin(
        neighPush,
        sources="CP_32_brest_ruins",
        targets="CP_32_brest_harbour",
    ),
]


reinforcements_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_brest_harbour_panzer4",
        they_own="CP_64_brest_navyhq or CP_64_brest_plaza",
        they_dont_own=(
            "CP_64_brest_ruins"
            " or CP_64_brest_flakposition"
            " or CP_64_brest_boulangerie"
        ),
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_brest_industry_Stuart",
        we_dont_own=(
            "CP_64_brest_fountain" " or CP_64_brest_navyhq" " or CP_64_brest_plaza"
        ),
    ),
]
spawns_64 = [
    plugin(
        teamSPs,
        team=1,
        sps=(
            "CP_64_brest_fountain_Axis*,"
            " CP_64_brest_navyhq_Axis*,"
            " CP_64_brest_plaza_Axis*,"
            " CP_64_brest_flakposition_Axis*,"
            " CP_64_brest_boulangerie_Axis*,"
            " CP_64_brest_ruins_Axis*"
        ),
    ),
    plugin(
        teamSPs,
        team=2,
        sps=(
            "CP_64_brest_fountain_Allies*,"
            " CP_64_brest_navyhq_Allies*,"
            " CP_64_brest_plaza_Allies*,"
            " CP_64_brest_flakposition_Allies*,"
            " CP_64_brest_boulangerie_Allies*,"
            " CP_64_brest_ruins_Allies*"
        ),
    ),
]
spawns_32 = [plugin(teamSPs)]

tickets_64 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=15)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=10)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]

gpm_cq = {
    64: (
        nco
        + push_64
        + spawns_64
        + kit_limits
        + tickets_64
        + reinforcements_64
        + dynamicoob_64
    ),
    32: (nco + push_32 + spawns_32 + tickets_32 + dynamicoob_32 + kit_limits),
    16: nco + kit_limits_16 + tickets_16,
}


coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=6.0 / 32.0,
        kit="GW_Scout_G41_limited",
        soldier="gb_light_splittermuster",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GS_SMGAssault_Limited",
        soldier="gb_light_sumpfmuster",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=8.0 / 32.0,
        kit="GW_RifleAssault_hurtgen",
        soldier="gb_light_splittermuster",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GS_LMG_FG42_Limited",
        soldier="gb_heavy_splittermuster",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=3.0 / 32.0,
        kit="GW_Engineer_Satchel_limited",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="GW_AntitankAssault_Limited",
        soldier="gw_heer_panzerabwehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=5.0 / 32.0,
        kit="UW_Scout",
        soldier="uw_29th_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="UW_SMGAssault_mk3_Limited",
        soldier="uw_29th_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=10.0 / 32.0,
        kit="UW_RifleAssault_noNadeLauncher",
        soldier="uw_29th_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uw_29th_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="UW_Engineer_Satchel",
        soldier="uw_29th_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="UW_AntitankAssault_Limited",
        soldier="uw_29th_cpl",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_brest_harbour_panzer4",
        they_dont_own=(
            "CP_64_brest_ruins or CP_64_brest_flakposition" " or CP_64_brest_boulangerie"
        ),
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "CP_64_brest_harbour_88," "CP_64_brest_harbour_mg," "CP_64_brest_harbour_mg2"
        ),
        they_own="CP_64_brest_ruins",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_brest_ruins_mg3",
        they_own="CP_64_brest_plaza or CP_64_brest_navyhq",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_brest_ruins_mg,CP_64_brest_ruins_mg2",
        they_own="CP_64_brest_boulangerie or CP_64_brest_flakposition",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_brest_harbour_pak",
        they_own=(
            "CP_64_brest_boulangerie"
            " or CP_64_brest_flakposition"
            " or CP_64_brest_ruins"
        ),
    ),
]
gpm_coop = {
    64: coop_64 + tickets_64 + nco,
    32: nco + push_32 + spawns_32 + tickets_32,
    16: nco + tickets_16,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
