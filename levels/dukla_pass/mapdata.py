# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    push,
    teamSPs,
    spawnerCondition,
    disableSPs,
    dynamicOOB,
    linkCPs,
)


kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="RE_LMG_limited", limit=0.1),
    plugin(
        limitKit, team=1, slot=5, kit="GW_AntitankAssault_grenades", limit=0.2
    ),
    plugin(
        limitKit, team=2, slot=5, kit="RE_AntiTankAssault_Limited", limit=0.2
    ),
]


tickets_64 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=9999, ticketLoss2=20)]

push_16 = [
    plugin(
        push,
        source="CP_16_dukla_pass_russianmain",
        target="CP_16_dukla_pass_school",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_16_dukla_pass_school",
        target="CP_16_dukla_pass_bridge",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_16_dukla_pass_bridge",
        target="CP_16_dukla_pass_kruzlova",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_16_dukla_pass_kruzlova",
        target="CP_16_dukla_pass_last_stand",
        attacker=2,
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_dukla_pass_russian_main",
        target="CP_32_dukla_pass_valley_of_death, CP_32_dukla_pass_bridge",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_dukla_pass_valley_of_death, CP_32_dukla_pass_bridge",
        target="CP_32_dukla_pass_sectorlock",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_dukla_pass_sectorlock",
        target="CP_32_dukla_pass_kruzlova_south",
        attacker=2,
    ),
    
    plugin(
        push,
        source="CP_32_dukla_pass_kruzlova_south",
        target="CP_32_dukla_pass_flak",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_dukla_pass_flak",
        target="CP_32_dukla_pass_kruzlova_north",
        attacker=2,
    ),
]

linkCPs_32 = [
    plugin(
        linkCPs,
        target="CP_32_dukla_pass_sectorlock",
        source="CP_32_dukla_pass_valley_of_death, CP_32_dukla_pass_bridge",
    ),
]

dynamicoob_32 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_32_dukla_pass_sectorlock": {
                "allies": {
                    "creates": ["CombatArea_40_32_cq"],
                    "destroys": ["CombatArea_20_32_cq"],
                },
            },
        },
        inactive_at_start=[
            "CombatArea_40_32_cq",
        ],
        delay_axis=120,
        delay_allies=0,
    )
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO_mp40_g43", "RE_NCO"),
        soldiers=("gcwhcamo_nco", "re_nco_soldier_telogrieka"),
    ),
]

spawncond_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_dukla_pass_germanmain_t34, CP_64_dukla_pass_germanmain_pantherI, CP_64_dukla_pass_germanmain_pantherIII, CP_64_dukla_pass_germanmain_StugII",
        we_dont_own="CP_64_dukla_pass_kruzlova_orchard and CP_64_dukla_pass_valley_of_death and CP_64_dukla_pass_kruzlova_south and CP_64_dukla_pass_kruzlova_north",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_dukla_pass_russian_main_t346, CP_64_dukla_pass_russian_main_t347, CP_64_dukla_pass_russian_main_t345, CP_64_dukla_pass_russian_main_t344",
        we_dont_own="CP_64_dukla_pass_valley_of_death and CP_64_dukla_pass_kruzlova_south and CP_64_dukla_pass_kruzlova_north and CP_64_dukla_pass_kruzlova_orchard",
    ),
]

spawncond_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_dukla_pass_kruzlova_north_stugiv",
        we_dont_own="CP_32_dukla_pass_sectorlock",
    ),
]

gpm_cq = {
    64: tickets_64 + kitlimits_64 + rifleNCO + spawncond_64,
    32: tickets_16 + kitlimits_64 + rifleNCO + spawns + push_32 + spawncond_32 + dynamicoob_32 + linkCPs_32,
    16: tickets_16 + kitlimits_64 + rifleNCO + push_16 + spawns,
}


disable_AI = [
    plugin(disableSPs),  # Auto-fill
]


gpm_coop = {
    64: tickets_64 + rifleNCO,
    32: tickets_16 + rifleNCO + spawns + push_32 + disable_AI + spawncond_32 + linkCPs_32,
    16: tickets_16 + rifleNCO + push_16 + spawns + disable_AI,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
