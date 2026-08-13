# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0301
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    push,
    spawnerCondition,
    teamSPs,
    linkCPs,
    dynamicOOB,
    timeCP,
)


kit_limits = [
    plugin(
        limitKit,
        team=1,
        kit="IA_Limited_Assault_Beretta38_K98",
        slot=1,
        limit=0.05,
    ),
    plugin(limitKit, team=2, kit="RE_SMGAssault_Limited", slot=1, limit=0.2),
    plugin(
        limitKit, team=1, kit="IA_Limited_Support_MG34_K98", slot=3, limit=0.1
    ),
    plugin(limitKit, team=2, kit="RE_LMG_Limited", slot=3, limit=0.15),
    plugin(limitKit, team=1, kit="IA_AntiTank_carcano", slot=5, limit=0.1),
    plugin(
        limitKit,
        team=2,
        kit="RE_AntitankAssault_RPG40_Limited",
        slot=5,
        limit=0.1,
    ),
]

kit_limits_16 = [
    plugin(
        limitKit,
        team=1,
        kit="IA_Limited_Assault_Beretta38_K98",
        slot=1,
        limit=0.05,
    ),
    plugin(limitKit, team=2, kit="RE_SMGAssault_Limited", slot=1, limit=0.1),
    plugin(
        limitKit, team=1, kit="IA_Limited_Support_MG34_K98", slot=3, limit=0.1
    ),
    plugin(limitKit, team=2, kit="RE_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="IA_AntiTank_carcano", slot=5, limit=0.05),
    plugin(
        limitKit,
        team=2,
        kit="RE_AntitankAssault_RPG40_Limited",
        slot=5,
        limit=0.05,
    ),

    plugin(limitKit, team=1, kit="IA_RifleAssault_SVT40_Limited", slot=4, limit=0.05),
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("IA_NCOBeretta38", "RE_NCO_43early"),
        soldiers=("ia_heavy_soldier", "re_nco_soldier_telogrieka"),
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=500, ticketLoss2=14)]

spawndelay_64 = [
    plugin(
        timeCP,
        team="-1",
        target="cp_64_little_saturn_dummy_forward_spawns",
        time=90,
    ),
]


linkCPs_64 = [
    plugin(
        linkCPs,
        target="cp_64_little_saturn_sectorlockdummy",
        source="cp_64_little_saturn_windmill, cp_64_little_saturn_hill_203, cp_64_little_saturn_gadyuchiye_north",
    ),
]


push_64 = [
    plugin(
        push,
        source="cp_64_little_saturn_windmill, cp_64_little_saturn_hill_203, cp_64_little_saturn_gadyuchiye_north",
        target="cp_64_little_saturn_sectorlockdummy",
        attacker=2,
    ),
    plugin(
        push,
        source="cp_64_little_saturn_sectorlockdummy",
        target="cp_64_little_saturn_west_farm, cp_64_little_saturn_trenches, cp_64_little_saturn_east_farm",
        attacker=2,
        delay=120,
    ),
    plugin(
        push,
        source="cp_64_little_saturn_trenches, cp_64_little_saturn_west_farm, cp_64_little_saturn_east_farm",
        target="cp_64_little_saturn_gadyuchiye_south",
        attacker=2,
        force=True,
        count=2,
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "cp_64_little_saturn_sectorlockdummy": {
                "allies": {
                    "creates": ["CombatArea_yesgoB"],
                    "destroys": ["CombatArea_yesgo1"],
                },
            },
        },
        inactive_at_start=["CombatArea_yesgoB"],
        delay_allies=120,
        delay_axis=120,
    )
]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_64_little_saturn_ARMIR_stug_01_0",
        we_dont_own="cp_64_little_saturn_sectorlockdummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_64_little_saturn_ARMIR_stug_02",
        we_dont_own="cp_64_little_saturn_sectorlockdummy",
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]


spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_32_little_saturn_axismain_fiat_01",
        we_dont_own="cp_32_little_saturn_sectorlockdummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_32_little_saturn_axismain_fiat_02",
        we_dont_own="cp_32_little_saturn_sectorlockdummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_32_little_saturn_axismain_semovente",
        we_dont_own="cp_32_little_saturn_sectorlockdummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_32_little_saturn_axismain_Stug",
        we_dont_own="cp_32_little_saturn_sectorlockdummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_32_little_saturn_axismain_MarderIII",
        we_dont_own="cp_32_little_saturn_sectorlockdummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_32_little_saturn_2nd_line_east_MarderIII",
        we_own="cp_32_little_saturn_sectorlockdummy",
    ),

    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_32_little_saturn_2nd_line_west_Stug",
        we_own="cp_32_little_saturn_sectorlockdummy",
    ),
]

linkCPs_32 = [
    plugin(
        linkCPs,
        target="cp_32_little_saturn_sectorlockdummy",
        source="cp_32_little_saturn_1st_line_west, cp_32_little_saturn_1st_line_east, cp_32_little_saturn_1st_line_middle",
    ),
]

push_32 = [
    plugin(
        push,
        source="cp_32_little_saturn_1st_line_west, cp_32_little_saturn_1st_line_east, cp_32_little_saturn_1st_line_middle",
        target="cp_32_little_saturn_sectorlockdummy",
        attacker=2,
    ),
    plugin(
        push,
        source="cp_32_little_saturn_sectorlockdummy",
        target="cp_32_little_saturn_2nd_line_west, cp_32_little_saturn_2nd_line_east",
        attacker=2,
        delay=120,
    ),
]

dynamicoob_32 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "cp_32_little_saturn_sectorlockdummy": {
                "allies": {
                    "creates": ["CombatArea_yesgoB_32"],
                    "destroys": ["CombatArea_yesgo1_32"],
                },
            },
        },
        inactive_at_start=["CombatArea_yesgoB_32"],
        delay_allies=120,
        delay_axis=120,
    )
]

spawndelay_32 = [
    plugin(
        timeCP,
        team=-1,
        target="cp_32_little_saturn_italian_forward_spawns",
        time=45,
    ),
]

tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

gpm_cq = {
    64: (
        kit_limits
        + rifleNCO
        + tickets_64
        + linkCPs_64
        + push_64
        + spawnerConditions
        + spawns
        + dynamicoob_64
        + spawndelay_64
    ),
    32: (
        kit_limits
        + rifleNCO
        + tickets_64
        + linkCPs_32
        + push_32
        + spawnerConditions_32
        + spawns
        + dynamicoob_32
	+ spawndelay_32
    ),
    16: (
        kit_limits_16
        + rifleNCO
        + tickets_16
    ),

}
