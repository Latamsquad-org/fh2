# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    linkCPs,
    timeCP,
    NCOrifleData,
    push,
    ticketLoss,
    teamSPs,
    disableSPs,
    spawnerCondition,
    aiPush,
    neighPush,
    balanceSPs,
    timeCP,
)

NCO = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("ga_nco_soldier", "ba_nco_soldier"),
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

spawndelay_16 = [
    plugin(
        timeCP,
        team=-1,
        target="CP_16_Alam_Halfa_Allied_forwardspawn",
        time=60,
    ),
]

kit_limits_16 = [
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="BA_Grenadier_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GA_Limited_Assault_MP40_K98",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="BA_Limited_Support_Bren_No4",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GA_Limited_Support_MG34_K98",
        limit=0.2,
    ),
    plugin(limitKit, team=2, slot=5, kit="BA_ATBoys_Limited", limit=0.1),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GA_ATPzB39_Limited",
        limit=0.1,
    ),
]
kit_limits_32 = [
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="BA_Limited_Support_Bren_No4",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GA_Limited_Support_MG34_K98",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="BA_ATBoys_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GA_ATPzB39_Limited",
        limit=0.2,
    ),
]

kit_limits_64 = [
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="BA_Limited_Support_Bren_No4",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GA_Limited_Support_MG34_K98",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="BA_ATBoys_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GA_ATPzB39_Limited",
        limit=0.2,
    ),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_Alam_Sector1_dummy",
        source=("CP_64_AlamHalfa_4th_Light_Armd_Brigade," "CP_64_AlamHalfa_7th_Motor_Brigade"),
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_Alam_Sector2_dummy",
        source=("CP_64_AlamHalfa_22d_Armd_Brigade," "CP_64_AlamHalfa_23d_Armd_Brigade"),
        default_zero=True,
    ),
]

linkCPs_16_cq = [
    plugin(
        linkCPs,
        target="CP_16_Alam_Halfa_Panzer_dummy",
        source="CP_16_Alam_Halfa_7th_Motor_Brigade",
        invert=True,
        never_owned_by=2,
    ),
]
# NOTE: Disabled because doesnt exist anymore in coop. TODO review this.
# linkCPs_16_coop = [
#     plugin(
#         linkCPs,
#         target="CP_16_Alam_Halfa_Panzer_dummy",
#         source="CP_16_Alam_Halfa_7th_Motor_Brigade",
#         invert=True,
#         never_owned_by=2,
#     ),
# ]


push_64 = [
    plugin(
        neighPush,
        sources="CP_64_AlamHalfa_AxisBase",
        targets=("CP_64_AlamHalfa_4th_Light_Armd_Brigade," "CP_64_AlamHalfa_7th_Motor_Brigade"),
    ),
    plugin(
        neighPush,
        sources="CP_64_AlamHalfa_4th_Light_Armd_Brigade",
        targets="CP_64_AlamHalfa_7th_Motor_Brigade",
    ),
    plugin(
        neighPush,
        sources="CP_64_Alam_Sector1_dummy",
        targets=("CP_64_AlamHalfa_Deir_el_Muhafid," "CP_64_AlamHalfa_Samaket_Gabala"),
    ),
    plugin(
        neighPush,
        sources="CP_64_AlamHalfa_Deir_el_Muhafid",
        targets=("CP_64_AlamHalfa_7th_Motor_Brigade," "CP_64_AlamHalfa_22d_Armd_Brigade"),
        two_way_neighboring=False,
    ),
    plugin(
        neighPush,
        sources="CP_64_AlamHalfa_Samaket_Gabala",
        targets=(
            "CP_64_AlamHalfa_4th_Light_Armd_Brigade,"
            "CP_64_AlamHalfa_22d_Armd_Brigade,CP_64_AlamHalfa_23d_Armd_Brigade"
        ),
        two_way_neighboring=False,
    ),
    plugin(
        neighPush,
        sources="CP_64_Alam_Sector2_dummy",
        targets=("CP_64_AlamHalfa_Deir_el_Muhafid," "CP_64_AlamHalfa_Samaket_Gabala"),
    ),
    plugin(
        neighPush,
        sources="CP_64_AlamHalfa_22d_Armd_Brigade",
        targets="CP_64_AlamHalfa_23d_Armd_Brigade",
    ),
    plugin(
        neighPush,
        sources="CP_64_AlamHalfa_8th_Armd_Brigade",
        targets="CP_64_AlamHalfa_23d_Armd_Brigade",
    ),
]

veh_spawning_64 = [
    # Axis
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "CP_64_AxisFirstWave_ComArty,CP_64_AxisFirstWave_PzIII_1,"
            "CP_64_AxisFirstWave_PzIII_2,CP_64_AxisFirstWave_PzIII_3,"
            "CP_64_AxisFirstWave_PzIII_4,CP_64_AxisFirstWave_PzIII_5,"
            "CP_64_AxisFirstWave_PzIII_6,CP_64_AxisFirstWave_PzIII_7,"
            "CP_64_AxisFirstWave_PzIV_1,CP_64_AxisFirstWave_PzIV_2,"
            "CP_64_AxisFirstWave_Sdkfz250"
        ),
        we_dont_own=(
            "CP_64_AlamHalfa_4th_Light_Armd_Brigade or " "CP_64_AlamHalfa_7th_Motor_Brigade"
        ),
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "CP_64_AxisSecondWave_Opel_1,CP_64_AxisSecondWave_Opel_Flak,"
            "CP_64_AxisSecondWave_Pak38,CP_64_AxisSecondWave_PzIII_1,"
            "CP_64_AxisSecondWave_PzIII_2,CP_64_AxisSecondWave_PzIII_3,"
            "CP_64_AxisSecondWave_PzIV_1,CP_64_AxisSecondWave_Sdkfz251_1"
        ),
        we_own="CP_64_AlamHalfa_4th_Light_Armd_Brigade",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "CP_64_AxisSecondWave_88,CP_64_AxisSecondWave_Lefh,"
            "CP_64_AxisSecondWave_PzIII_4,CP_64_AxisSecondWave_PzIII_5,"
            "CP_64_AxisSecondWave_PzIV_2,CP_64_AxisSecondWave_PzIV_3,"
            "CP_64_AxisSecondWave_Sdkfz250,CP_64_AxisSecondWave_Sdkfz251_2,"
            "CP_64_AlamHalfa_4th_Light_Armd_Brigade_Crusader"
        ),
        we_own="CP_64_AlamHalfa_7th_Motor_Brigade",
    ),
    # Allies
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_AlliesFirstWave_ComArty,CP_64_AlliesFirstWave_Crusader_1,"
            "CP_64_AlliesFirstWave_Crusader_2,CP_64_AlliesFirstWave_Daimler,"
            "CP_64_AlliesFirstWave_Grant_1,CP_64_AlliesFirstWave_Grant_2,"
            "CP_64_AlliesFirstWave_Hurricane_1,"
            "CP_64_AlliesFirstWave_Hurricane_2"
        ),
        they_own=(
            "CP_64_AlamHalfa_4th_Light_Armd_Brigade " "and CP_64_AlamHalfa_7th_Motor_Brigade"
        ),
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_AlliesSecondWave_Crusader_1,CP_64_AlliesSecondWave_Grant_1,"
            "CP_64_AlliesSecondWave_Grant_2"
        ),
        they_own=(
            "(CP_64_AlamHalfa_Deir_el_Muhafid "
            "and CP_64_AlamHalfa_Samaket_Gabala) "
            "or CP_64_AlamHalfa_22d_Armd_Brigade "
            "or CP_64_AlamHalfa_23d_Armd_Brigade"
        ),
    ),
]

spawndelay_64 = [
    plugin(timeCP, team=-1, target="CP_64_alam_forward_dummy", time=80),
]

bleed_64 = [plugin(ticketLoss, ticketLoss1=14, ticketLoss2=250)]
bleed_32 = [plugin(ticketLoss, ticketLoss1=14, ticketLoss2=250)]

gpm_cq = {
    64: (
        kit_limits_64
        + push_64
        + linkCPs_64
        + spawndelay_64
        + bleed_64
        + spawns
        + veh_spawning_64
        + NCO
    ),
    32: (kit_limits_32 + bleed_32 + spawns + NCO),
    16: (kit_limits_16 + linkCPs_16_cq + spawns + NCO + spawndelay_16),
}
coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GA_ScoutK98Short",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=0.0 / 32.0,
        kit="GA_TankerP08",
        soldier="ga_masked_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=13.0 / 32.0,
        kit="GA_RiflemanK98",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GA_Limited_Support_MG34_K98",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=6.0 / 32.0,
        kit="ga_EngineerK98Short",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=4.0 / 32.0,
        kit="ga_ATPzB39_Limited",
        soldier="ga_masked_soldier",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="BA_ScoutEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=0.0 / 32.0,
        kit="BA_TankerWebley",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=11.0 / 32.0,
        kit="BA_RiflemanEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="BA_Limited_Support_Bren_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=5.0 / 32.0,
        kit="BA_EngineerEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=7.0 / 32.0,
        kit="BA_ATBoys_Limited",
        soldier="ba_heavy_soldier",
    ),
    # Push mode
    plugin(aiPush),
    plugin(
        linkCPs,
        target="CP_64_sector_1_dummy",
        source=("CP_64_AlamHalfa_4th_Light_Armd_Brigade," "CP_64_AlamHalfa_7th_Motor_Brigade"),
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_sector_2_dummy",
        source=("CP_64_AlamHalfa_22d_Armd_Brigade," "CP_64_AlamHalfa_23d_Armd_Brigade"),
        default_zero=True,
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_AlamHalfa_AxisBase",
        we_own=("CP_64_AlamHalfa_7th_Motor_Brigade " "or CP_64_AlamHalfa_4th_Light_Armd_Brigade"),
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_AlamHalfa_4th_Light_Armd_Brigade",
        we_own="CP_64_alam_forward_dummy",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_AlamHalfa_7th_Motor_Brigade",
        we_own="CP_64_alam_forward_dummy",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_AlamHalfa_Deir_el_Muhafid",
        we_own=(
            "CP_64_AlamHalfa_7th_Motor_Brigade "
            "and (CP_64_AlamHalfa_22d_Armd_Brigade "
            "or CP_64_AlamHalfa_23d_Armd_Brigade)"
        ),
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_AlamHalfa_Samaket_Gabala",
        we_own=(
            (
                "CP_64_AlamHalfa_4th_Light_Armd_Brigade "
                "and (CP_64_AlamHalfa_22d_Armd_Brigade "
                "or CP_64_AlamHalfa_23d_Armd_Brigade)"
            )
        ),
    ),
    plugin(
        balanceSPs,
        custom_weights=[
            dict(
                cp=("CP_64_AlamHalfa_4th_Light_Armd_Brigade, " "CP_64_AlamHalfa_7th_Motor_Brigade"),
                team=1,
                weight=1000000,
            ),
            dict(
                cp=("CP_64_AlamHalfa_Deir_el_Muhafid, " "CP_64_AlamHalfa_Samaket_Gabala"),
                team=1,
                weight=1000000,
            ),
            dict(
                cp=("CP_64_AlamHalfa_22d_Armd_Brigade, " "CP_64_AlamHalfa_23d_Armd_Brigade"),
                team=1,
                weight=1000000,
            ),
            dict(
                cp=("CP_64_AlamHalfa_4th_Light_Armd_Brigade, " "CP_64_AlamHalfa_7th_Motor_Brigade"),
                team=2,
                weight=1000000,
            ),
            dict(
                cp=("CP_64_AlamHalfa_Deir_el_Muhafid, " "CP_64_AlamHalfa_Samaket_Gabala"),
                team=2,
                weight=500000,
            ),
            dict(
                cp=("CP_64_AlamHalfa_22d_Armd_Brigade, " "CP_64_AlamHalfa_23d_Armd_Brigade"),
                team=2,
                weight=700000,
            ),
            dict(
                cp="CP_64_AlamHalfa_8th_Armd_Brigade",
                team=2,
                weight=500000,
            ),
        ],
    ),
    # PCO spawning - Axis
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "FirstWave_pziv2,"
            "FirstWave_pziv1,"
            "FirstWave_pziii1,"
            "FirstWave_pziii2,"
            "FirstWave_pziii3,"
            "FirstWave_pziii4,"
            "FirstWave_pziii5,"
            "FirstWave_pziii6,"
            "FirstWave_pziii7,"
            "FirstWave_comarty_axis,"
            "FirstWave_sdkfz250,"
            "CP_64_AlamHalfa_AxisBase_kubel"
        ),
        we_dont_own=(
            "CP_64_AlamHalfa_4th_Light_Armd_Brigade " "or CP_64_AlamHalfa_7th_Motor_Brigade"
        ),
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_AlamHalfa_4th_Light_Armd_Brigade_Crusader",
        we_own="CP_64_AlamHalfa_7th_Motor_Brigade",
    ),
    # PCO spawning - Allies
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "FirstWave_hurricane1,"
            "FirstWave_hurricane2,"
            "FirstWave_grant1,"
            "FirstWave_grant2,"
            "FirstWave_crusader1,"
            "FirstWave_crusader2,"
            "FirstWave_daimler,"
            "FirstWave_comarty_allies"
        ),
        they_own=(
            "CP_64_AlamHalfa_4th_Light_Armd_Brigade and " "CP_64_AlamHalfa_7th_Motor_Brigade"
        ),
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "SecondWave_grant1,"
            "SecondWave_grant2,"
            "SecondWave_crusader,"
            "CP_64_AlamHalfa_8th_Armd_Brigade_bedford_4"
        ),
        they_own=(
            "(CP_64_AlamHalfa_Deir_el_Muhafid and "
            "CP_64_AlamHalfa_Samaket_Gabala) "
            "or CP_64_AlamHalfa_22d_Armd_Brigade "
            "or CP_64_AlamHalfa_23d_Armd_Brigade"
        ),
    ),
    plugin(ticketLoss, ticketLoss1=12, ticketLoss2=250),
]

coop_16 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GA_ScoutK98Short",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=0.0 / 32.0,
        kit="GA_TankerP08",
        soldier="ga_masked_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=19.0 / 32.0,
        kit="GA_RiflemanK98",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GA_Limited_Support_MG34_K98",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="ga_EngineerK98Short",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=0.0 / 32.0,
        kit="ga_ATPzB39_Limited",
        soldier="ga_masked_soldier",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="BA_ScoutEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=0.0 / 32.0,
        kit="BA_TankerWebley",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=15.0 / 32.0,
        kit="BA_RiflemanEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="BA_Limited_Support_Bren_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="BA_EngineerEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="BA_ATBoys_Limited",
        soldier="ba_heavy_soldier",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    # PzII
    plugin(
        spawnerCondition,
        team=1,
        spawner=("CP_16_Alam_Halfa_Panzer_dummy_PanzerII," "CP_16_Alam_Halfa_Axis_Base_PanzerII"),
        we_dont_own="CP_16_Alam_Halfa_7th_Motor_Brigade",
    ),
    # Note: DISABLED because doesnt exist anymore. TODO review this
    # plugin(
    #     spawnerCondition,
    #     team=1,
    #     spawner=("CP_16_Alam_Halfa_Panzer_dummy_tanker," "CP_16_Alam_Halfa_Axis_Base_tanker"),
    #     we_dont_own="CP_16_Alam_Halfa_7th_Motor_Brigade",
    # ),
    # Push mode
    plugin(
        push,
        source="CP_16_Alam_Halfa_Axis_Base",
        target="CP_16_Alam_Halfa_7th_Motor_Brigade",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_16_Alam_Halfa_7th_Motor_Brigade",
        target="CP_16_Alam_Halfa_trench",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_16_Alam_Halfa_trench",
        target="CP_16_Alam_Halfa_4th_light_armd",
        attacker=1,
    ),
]

gpm_coop = {
    64: coop_64 + spawndelay_64 + spawns + NCO,
    16: (
        coop_16
        # + linkCPs_16_coop
        + spawns
        + NCO
    ),
}

sp1 = gpm_coop
sp3 = gpm_coop
