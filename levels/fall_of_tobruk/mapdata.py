# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    aiPush,
    balanceSPs,
    disableSPs,
    dynamicOOB,
    limitKit,
    linkCPs,
    NCOrifleData,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("ga_nco_soldier", "ba_nco_soldier"),
    )
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_tobruk_sectorA_locker": {
                "axis": {
                    "creates": ["CombatArea_axis1"],
                    "destroys": ["CombatArea_allies1"],
                },
            },
        },
        inactive_at_start=["CombatArea_axis1"],
        delay_axis=0,
        delay_allies=120,
    )
]

kit_limits = [
    plugin(limitKit, team=2, slot=3, kit="BA_Limited_Support_Bren_No4", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GA_Limited_Support_MG34_K98", limit=0.16),
    plugin(limitKit, team=2, slot=1, kit="BA_Limited_Assault_TommygunD_No4", limit=0.16),
    plugin(limitKit, team=1, slot=1, kit="GA_Limited_Assault_MP40_K98", limit=0.16),
    plugin(limitKit, team=2, slot=5, kit="BA_TankHunter_rifle", limit=0.16),
    plugin(limitKit, team=1, slot=5, kit="GA_ATPzB39_Limited", limit=0.16),
]

kit_limits_16 = [
    plugin(limitKit, team=2, slot=1, kit="BA_Limited_Assault_TommygunS", limit=0.1),
    plugin(limitKit, team=1, slot=1, kit="GA_Limited_Assault_MP40_K98", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="BA_Limited_Support_Bren_No4", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GA_Limited_Support_MG34_K98", limit=0.1),
    plugin(limitKit, team=2, slot=4, kit="BA_Grenadier_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=4, kit="GW_RifleAssault_early_smoke_Limited", limit=0.25),
    plugin(limitKit, team=2, slot=5, kit="BA_TankHunter_rifle", limit=0.16),
    plugin(limitKit, team=1, slot=5, kit="GA_ATPzB39_Limited", limit=0.16),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_tobruk_second_dummy",
        source=["CP_64_tobruk_2"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_tobruk_second_dummy2",
        source=["CP_64_tobruk_2"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_tobruk_sectorA_locker",
        source=["CP_64_tobruk_2", "CP_64_tobruk_3"],
    ),
]

push_64 = [
    plugin(
        push,
        source="CP_64_tobruk_Base1",
        target="CP_64_tobruk_2, CP_64_tobruk_3",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_tobruk_2, CP_64_tobruk_3",
        target="CP_64_tobruk_sectorA_locker",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tobruk_sectorA_locker",
        target="CP_64_tobruk_1, CP_64_tobruk_4, CP_64_tobruk_5",
        attacker=1,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_tobruk_1, CP_64_tobruk_5",
        target="CP_64_tobruk_Base2",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tobruk_4",
        target="CP_64_tobruk_6",
        attacker=1,
        display_arrow=False,
    ),
]

push_16 = [
    plugin(
        push, source="CP_16_tobruk_2", target="CP_16_tobruk_1, CP_16_tobruk_5", attacker=1
    ),
    plugin(
        push,
        source="CP_16_tobruk_1, CP_16_tobruk_5",
        target="CP_16_tobruk_Base2",
        attacker=1,
    ),
]

spawns = [
    plugin(teamSPs),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=11, ticketLoss2=22)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=12, ticketLoss2=12)]

coop_64_kit = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GA_ScoutK98Short",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GA_Limited_Assault_MP40_K98",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GA_RiflemanK98",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GA_Limited_Support_MG34_K98",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=5.0 / 32.0,
        kit="GA_EngineerK98Short",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=3.0 / 32.0,
        kit="GA_ATPzB39_Limited",
        soldier="ga_masked_soldier",
    ),
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
        limit=6.0 / 32.0,
        kit="BA_Limited_Assault_TommygunD_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
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
        kit="BA_TankHunter_rifle",
        soldier="ba_heavy_soldier",
    ),
]
coop_64_aipush = [plugin(aiPush)]
coop_64_disable = [
    plugin(disableSPs),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_tobruk_Base1",
        we_own="CP_64_tobruk_2 or CP_64_tobruk_3",
    ),
]
coop_64_balance = [
    plugin(
        balanceSPs,
        custom_weights=[
            dict(
                cp=(
                    "CP_64_tobruk_1,"
                    "CP_64_tobruk_2,"
                    "CP_64_tobruk_3,"
                    "CP_64_tobruk_4,"
                    "CP_64_tobruk_5,"
                    "CP_64_tobruk_6,"
                    "CP_64_tobruk_Base2"
                ),
                weight=1000000,
            ),
            dict(cp="CP_64_tobruk_2", team=2, weight=1500000, never_disable=True),
            dict(cp="CP_64_tobruk_Base2", team=2, weight=1250000),
            dict(cp="CP_64_tobruk_6", team=2, weight=750000),
        ],
    ),
]
coop_64_sc = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_tobruk_Base1_hanomag_0",
        we_dont_own="CP_64_tobruk_2 or CP_64_tobruk_3",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_tobruk_6_stuart1,CP_64_tobruk_6_stuart2",
        they_own="CP_64_tobruk_2 or CP_64_tobruk_3",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_tobruk_6_mg4",
        they_own="CP_64_tobruk_4",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_tobruk_Base2_at, CP_64_tobruk_5_at",
        we_dont_own="CP_64_tobruk_2 or CP_64_tobruk_3",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_tobruk_4_at, CP_64_tobruk_4_at2, CP_64_tobruk_4_mg3",
        we_dont_own="CP_64_tobruk_3",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_tobruk_Base2_mg, "
            "CP_64_tobruk_Base2_at2, "
            "CP_64_tobruk_6_DE_GB_StaticArtillery, "
            "CP_64_tobruk_6_DE_GB_LightArtillery,"
            "CP_64_tobruk_6_at"
        ),
        we_dont_own="CP_64_tobruk_3",
    ),
]

gpm_cq = {
    64: (
        nco
        + kit_limits
        + push_64
        + spawns
        + linkCPs_64
        + tickets_64
        + dynamicoob_64
    ),
    32: nco + spawns + kit_limits + tickets_32,
    16: nco + spawns + kit_limits_16 + push_16 + tickets_16,
}
gpm_coop = {
    64: coop_64_kit
    + coop_64_aipush
    + coop_64_disable
    + coop_64_balance
    + coop_64_sc
    + spawns
    + nco,
}
sp3 = gpm_coop
