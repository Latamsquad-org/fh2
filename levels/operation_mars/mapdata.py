# -*- coding: utf-8 -*-
# pylint: disable=W0232,C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    push,
    teamSPs,
    spawnerCondition,
    linkCPs,
    dynamicOOB,
    disableSPs,
    aiPush,
)

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_opmars_sector1": {
                "allies": {
                    "creates": ["CombatArea_69_cq_64"],
                    "destroys": ["CombatArea_98_cq_64"],
                },
            },
            "CP_64_opmars_sector2": {
                "allies": {
                    "creates": ["CombatArea_83_cq_64"],
                    "destroys": ["CombatArea_117_cq_64"],
                },
            },
        },
        inactive_at_start=["CombatArea_69_cq_64", "CombatArea_83_cq_64"],
        delay_axis=120,
        delay_allies=0,
    )
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GM_Limited_Assault_MP40_K98", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="RE_SMGAssault_Limited", limit=0.15),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_early_Limited", limit=0.05),
    plugin(limitKit, team=2, slot=3, kit="RE_LMG_limited", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="ga_ATPzB39_Limited", limit=0.1),
    plugin(
        limitKit, team=2, slot=5, kit="RE_Antitank_PTRD_Limited", limit=0.1
    ),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_opmars_sector1",
        source="CP_64_opmars_emelyanovo, CP_64_opmars_toropino",
    ),
    plugin(
        linkCPs, target="CP_64_opmars_sector2", source="CP_64_opmars_forest"
    ),
    plugin(
        linkCPs,
        target="CP_64_opmars_sector3",
        source="CP_64_opmars_hill, CP_64_opmars_pshenichina",
    ),
]

push_64 = [
    plugin(
        push,
        source="CP_64_opmars_6thStalinRifleCorps",
        target="CP_64_opmars_trenchessouth, CP_64_opmars_trenchesnorth",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_opmars_trenchessouth",
        target="CP_64_opmars_emelyanovo",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_opmars_trenchesnorth",
        target="CP_64_opmars_toropino",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_opmars_toropino, CP_64_opmars_emelyanovo",
        target="CP_64_opmars_sector1",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_opmars_sector1",
        target="CP_64_opmars_forest",
        attacker=2,
        display_arrow=False,
        delay=60,
    ),
    plugin(
        push,
        source="CP_64_opmars_forest",
        target="CP_64_opmars_sector2",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_opmars_sector2",
        target="CP_64_opmars_hill, CP_64_opmars_pshenichina",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_opmars_hill, CP_64_opmars_pshenichina",
        target="CP_64_opmars_sector3",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_opmars_alliedmain",
        target="CP_32_opmars_trenches",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_opmars_trenches",
        target="CP_32_opmars_storage",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_opmars_storage",
        target="CP_32_opmars_emelyanovo",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_opmars_emelyanovo",
        target="CP_32_opmars_shelters",
        attacker=2,
        display_arrow=True,
    ),
]

push_16 = [
    plugin(
        push,
        source="CP_16_opmars_germanmain",
        target="CP_16_opmars_shelters",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_opmars_shelters",
        target="CP_16_opmars_emelyanovo",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_opmars_emelyanovo",
        target="CP_16_opmars_storage",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_opmars_storage",
        target="CP_16_opmars_oldhkl",
        attacker=1,
        display_arrow=True,
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=9999, ticketLoss2=15)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=9999)]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40", "RE_NCO_42"),
        soldiers=("GcWhSnow_white_nco_redband", "re_nco_soldier_telogrieka"),
    ),
]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_opmars_6thStalinRifleCorps_t60a, "
            "CP_64_opmars_6thStalinRifleCorps_t34a, "
            "CP_64_opmars_6thStalinRifleCorps_kv1, "
            "CP_64_opmars_6thStalinRifleCorps_t60b, "
            "CP_64_opmars_6thStalinRifleCorps_t34b"
        ),
        we_dont_own="CP_64_opmars_sector2",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_opmars_sector3_stugIIIa",
        we_dont_own="CP_64_opmars_sector1",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_opmars_sector3_stugIIIb",
        we_dont_own="CP_64_opmars_sector2",
    ),
]

gpm_cq = {
    64: tickets_64
    + kitlimits_64
    + rifleNCO
    + spawnerConditions
    + spawns
    + push_64
    + linkCPs_64
    + dynamicoob_64,
    32: tickets_64 + kitlimits_64 + rifleNCO + push_32 + spawns,
    16: tickets_16 + kitlimits_64 + rifleNCO + spawns + push_16,
}

disable_AI_64 = [
    # AI spawn points disabling - Axis
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_opmars_hill",
        we_own="CP_64_opmars_forest",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_opmars_pshenichina",
        we_own="CP_64_opmars_forest",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_opmars_toropino",
        we_own="CP_64_opmars_trenchesnorth",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_opmars_emelyanovo",
        we_own="CP_64_opmars_trenchessouth",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_opmars_forest",
        we_own="CP_64_opmars_emelyanovo and CP_64_opmars_toropino",
    ),
]

disable_AI = [
  plugin(disableSPs),  # Auto-fill
]

Push_AI_64 = [
  plugin(aiPush),  # Push mode
]

gpm_coop = {
    16: (tickets_16 + spawns + push_16 + rifleNCO + disable_AI),
    32: (tickets_64 + rifleNCO + push_32 + spawns + disable_AI),
    64: (
        tickets_64
        + spawns
        + Push_AI_64
        + linkCPs_64
        + rifleNCO
        + spawnerConditions
        + disable_AI_64
    ),
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
