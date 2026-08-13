# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    aiPush,
    balanceSPs,
    disableSPs,
    limitKit,
    linkCPs,
    NCOrifleData,
    neighPush,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    timeCP,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO_GWood", "BW_NCO_GWood"),
        soldiers=("gs_waffen_unteroffizier", "bw_nco_soldier"),
    )
]

kit_limits_16 = [
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_Limited_GWood", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.1),
    plugin(
        limitKit, team=1, slot=5, kit="GS_AntitankAssault_Limited", limit=0.1
    ),
]

kit_limits_32 = [
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.16),
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.16),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_Limited_GWood", limit=0.16),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.1),
    plugin(
        limitKit, team=1, slot=5, kit="GS_AntitankAssault_Limited", limit=0.16
    ),
]

kit_limits_64 = [
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.16),
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.16),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_Limited_GWood", limit=0.16),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.1),
    plugin(
        limitKit, team=1, slot=5, kit="GS_AntitankAssault_Limited", limit=0.16
    ),
]


linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_Goodwood_FirstLine_Dummy",
        source=[
            "CP_64_Goodwood_LeMesnilFrementel",
            "CP_64_Goodwood_LePrieure",
        ],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_Goodwood_Cagny_Dummy",
        source=["CP_64_Goodwood_CagnyEast", "CP_64_Goodwood_CagnyWest"],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_Goodwood_fourflagscombined_dummy",
        source=[
            "CP_64_Goodwood_CagnyEast",
            "CP_64_Goodwood_CagnyWest",
            "CP_64_Goodwood_LeMesnilFrementel",
            "CP_64_Goodwood_LePrieure",
        ],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_Goodwood_Alliedfour_dummy",
        source=[
            "CP_64_Goodwood_CagnyEast",
            "CP_64_Goodwood_CagnyWest",
            "CP_64_Goodwood_LeMesnilFrementel",
            "CP_64_Goodwood_LePrieure",
        ],
        default_zero=True,
    ),
]


push_64 = [
    plugin(
        push,
        source="CP_64_Goodwood_LePrieure",
        target="CP_64_Goodwood_Grentheville",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_Goodwood_LePrieure",
        target="CP_64_Goodwood_LePoirier",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_Goodwood_LeMesnilFrementel",
        target="CP_64_Goodwood_Grentheville",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_Goodwood_LeMesnilFrementel",
        target="CP_64_Goodwood_LePoirier",
        attacker=2,
    ),
]

push_32 = [
    plugin(
        neighPush,
        main_bases_1="CP_32_Goodwood_AxisMain",
        main_bases_2="CP_32_Goodwood_LePrieure",
    ),  # Encirclements
    plugin(
        neighPush,
        sources="CP_32_Goodwood_LePrieure",
        targets="CP_32_Goodwood_CagnyEast, CP_32_Goodwood_CagnyWest",
    ),
    plugin(
        neighPush,
        sources="CP_32_Goodwood_CagnyWest",
        targets="CP_32_Goodwood_CagnyEast, CP_32_Goodwood_LePoirier",
    ),
    plugin(
        neighPush,
        sources="CP_32_Goodwood_CagnyEast",
        targets="CP_32_Goodwood_CagnyWest, CP_32_Goodwood_LePoirier",
    ),
    plugin(
        neighPush,
        sources="CP_32_Goodwood_LePoirier",
        targets="CP_32_Goodwood_CagnyWest, CP_32_Goodwood_CagnyEast, CP_32_Goodwood_Grentheville",
    ),
    plugin(
        neighPush,
        sources="CP_32_Goodwood_Grentheville",
        targets="CP_32_Goodwood_LePoirier",
    ),
    plugin(
        neighPush,
        sources="CP_32_Goodwood_AxisMain",
        targets="CP_32_Goodwood_Grentheville",
    ),
]

bleed_64 = [plugin(ticketLoss, ticketLoss1=29, ticketLoss2=33)]

bleed_32 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]

spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_Goodwood_LePrieure_sherman",
        we_dont_own="CP_32_Goodwood_CagnyWest",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_Goodwood_LePrieure_cromwell1",
        we_dont_own="CP_32_Goodwood_LePoirier",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_Goodwood_LePrieure_sherman5",
        we_dont_own="CP_32_Goodwood_CagnyEast",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_Goodwood_LePrieure_firefly",
        we_dont_own="CP_32_Goodwood_Grentheville",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_Goodwood_AxisMain_panther1",
        we_dont_own="CP_32_Goodwood_CagnyWest",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_Goodwood_AxisMain_panther2",
        we_dont_own="CP_32_Goodwood_LePoirier",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_Goodwood_AxisMain_stug",
        we_dont_own="CP_32_Goodwood_CagnyEast",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_Goodwood_AxisMain_pz4",
        we_dont_own="CP_32_Goodwood_Grentheville",
    ),
]


coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=3.0 / 32.0,
        kit="Gs_Scout",
        soldier="gs_waffen_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=5.0 / 32.0,
        kit="Gs_SMGAssault_Limited",
        soldier="gs_waffen_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault",
        soldier="gw_heer_panzerabwehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GW_LMG_Limited_GWood",
        soldier="gw_heer_maschinengewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="gw_heer_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=6.0 / 32.0,
        kit="GS_AntitankAssault_Limited",
        soldier="gs_waffen_pionier",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="BW_Scout",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=5.0 / 32.0,
        kit="BW_SMGAssault_Limited",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="BW_RifleAssault",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="BW_LMG_Limited",
        soldier="bw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=5.0 / 32.0,
        kit="BW_Engineer_Satchel_GWood",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="BW_Antitank_Limited",
        soldier="bw_heavy_soldier",
    ),
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
    plugin(
        linkCPs,
        target="CP_64_Cagny_sector_dummy",
        source="CP_64_Goodwood_CagnyWest,CP_64_Goodwood_CagnyEast",
        default_zero=True,
    ),
    # AI spawning
    plugin(timeCP, team=-1, target="CP_64_Axis_FirstWave_dummy", time=30),
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Goodwood_LePoirier",
        we_own="CP_64_Axis_FirstWave_dummy or (CP_64_Goodwood_Grentheville and (CP_64_Goodwood_CagnyWest or CP_64_Goodwood_CagnyEast))",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Goodwood_Grentheville",
        we_own="CP_64_Axis_FirstWave_dummy or (CP_64_Goodwood_LePoirier and CP_64_Goodwood_LeMesnilFrementel and (CP_64_Goodwood_CagnyWest or CP_64_Goodwood_CagnyEast))",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Goodwood_LeMesnilFrementel",
        we_own="CP_64_Axis_FirstWave_dummy",
    ),
    plugin(
        balanceSPs,
        custom_weights=[
            dict(
                cp="CP_64_Goodwood_AlliedBase,CP_64_Goodwood_AxisMain",
                weight=500000,
            ),
            dict(cp="CP_64_Goodwood_Grentheville", weight=1000000),
        ],
    ),
    # Reinforcements
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Goodwood_AlliedBase_reinforcements_cromwell, CP_64_Goodwood_AlliedBase_reinforcements_sherman",
        we_own="CP_64_Goodwood_CagnyEast and CP_64_Goodwood_CagnyWest and CP_64_Goodwood_LeMesnilFrementel and CP_64_Goodwood_LePrieure",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Goodwood_AlliedBase_halftrack",
        we_dont_own="CP_64_Goodwood_LeMesnilFrementel or CP_64_Goodwood_LePrieure",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Goodwood_AxisMain_reinforcements1_panther, CP_64_Goodwood_AxisMain_reinforcements1_pziv, CP_64_Goodwood_AxisMain_G43, CP_64_Goodwood_AxisMain_G43_0, CP_64_Goodwood_AxisMain_G43_1, CP_64_Goodwood_AxisMain_G43_2, CP_64_Goodwood_AxisMain_G43_3",
        they_own="CP_64_Goodwood_LeMesnilFrementel and CP_64_Goodwood_LePrieure",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Goodwood_AxisMain_reinforcements2_panther, CP_64_Goodwood_AxisMain_reinforcements2_stug",
        they_own="CP_64_Goodwood_CagnyEast and CP_64_Goodwood_CagnyWest",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Goodwood_AxisMain_reinforcements3_kt, CP_64_Goodwood_AxisMain_reinforcements3_marder",
        they_own="CP_64_Goodwood_LeMesnilFrementel and CP_64_Goodwood_LePrieure and CP_64_Goodwood_CagnyEast and CP_64_Goodwood_CagnyWest",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Goodwood_AxisMain_sdkfz251_0",
        we_dont_own="CP_64_Goodwood_Grentheville",
    ),
]
gpm_cq = {
    64: kit_limits_64 + push_64 + linkCPs_64 + bleed_64 + nco,
    32: kit_limits_32 + push_32 + spawnerConditions_32 + bleed_32 + nco,
    16: kit_limits_16 + nco,
}

gpm_coop = {
    64: coop_64 + bleed_64 + nco,
}

sp3 = gpm_coop
