# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    push,
    linkCPs,
    teamSPs,
    spawnerCondition,
    neighPush,
    dynamicOOB,
)


oob_32 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_32_studienka_sector1": {
                "allies": {
                    "creates": ["CombatArea_32_allies_sw"],
                    "destroys": ["CombatArea_32_axis_ne"],
                },
            },
        },
        inactive_at_start=["CombatArea_32_allies_sw"],
        delay_allies=0,
        delay_axis=120,
    ),
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="RE_LMG_limited", limit=0.15),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="RE_AntitankAssault_ppsh41_limited", limit=0.1, ),
]

kitlimits_16 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="RE_LMG_limited", limit=0.15),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="RE_SMGAssault_pps43_Limited", limit=0.1, ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=30, ticketLoss2=30)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=999, ticketLoss2=15)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=999, ticketLoss2=15)]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "RE_NCO"),
        soldiers=("gw_heer_unteroffizier", "re_nco_soldier_cavalry"),
    ),
]

linkCPs_32 = [
    plugin(
        linkCPs,
        target="CP_32_studienka_sector1",
        source=["CP_32_studienka_berezinacrossing"],
    ),
    plugin(
        linkCPs,
        target="CP_32_studienka_sector2",
        source=["CP_32_studienka_supplydepot", "CP_32_studienka_germanbank"],
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_studienka_alliedmain",
        target="CP_32_studienka_carpenter",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_studienka_carpenter",
        target="CP_32_studienka_studienka",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_studienka_studienka",
        target="CP_32_studienka_berezinacrossing",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_studienka_berezinacrossing",
        target="CP_32_studienka_sector1",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_32_studienka_sector1",
        target="CP_32_studienka_supplydepot",
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_32_studienka_sector1",
        target="CP_32_studienka_germanbank",
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_32_studienka_germanbank",
        target="CP_32_studienka_sector2",
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_32_studienka_supplydepot",
        target="CP_32_studienka_sector2",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_32_studienka_sector2",
        target="CP_32_studienka_napoleonpoint",
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
]

spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_studienka_alliedmain_scout, CP_32_studienka_alliedmain_t34a, CP_32_studienka_alliedmain_t34b, CP_32_studienka_alliedmain_t34c",
        we_dont_own="CP_32_studienka_sector2",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_studienka_napoleonpoint_pziv, CP_32_studienka_napoleonpoint_panther",
        we_dont_own="CP_32_studienka_sector1",
    ),
]

push_16 = [
    plugin(
        push,
        source="CP_16_studienka_alliedmain",
        target="CP_16_studienka_carpenter",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_studienka_carpenter",
        target="CP_16_studienka_studienka",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_studienka_studienka",
        target="CP_16_studienka_berezinacrossing",
        attacker=2,
        display_arrow=True,
    ),
]

gpm_cq = {
    64: tickets_64 + kitlimits_64 + rifleNCO + spawns,
    32: (
        tickets_32
        + kitlimits_64
        + rifleNCO
        + spawns
        + linkCPs_32
        + push_32
        + oob_32
        + spawnerConditions_32
    ),
    16: tickets_16 + kitlimits_16 + rifleNCO + spawns + push_16,
}

kits_AI = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout",
        soldier="gw_heer_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="gw_heer_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GW_LMG_MG42_Limited",
        soldier="gw_heer_maschinengewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer",
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
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="RE_Scout_Cavalry",
        soldier="re_light_soldier_cavalry",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="RE_SMGAssault",
        soldier="re_heavy_soldier_cavalry",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=10.0 / 32.0,
        kit="RE_RifleAssault_Cavalry",
        soldier="re_light_soldier_cavalry",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=5.0 / 32.0,
        kit="RE_LMG_Limited",
        soldier="re_heavy_soldier_cavalry_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="RE_Engineer_pps43",
        soldier="re_light_soldier_cavalry",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="RE_AntitankAssault_ppsh41_limited",
        soldier="re_heavy_soldier_cavalry",
    ),
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "RE_NCO"),
        soldiers=("gw_heer_unteroffizier", "re_nco_soldier_cavalry"),
    ),
]

push_32_AI = [
    plugin(
        neighPush,
        sources="CP_32_studienka_alliedmain",
        targets="CP_32_studienka_carpenter",
    ),
    plugin(
        neighPush,
        sources="CP_32_studienka_carpenter",
        targets="CP_32_studienka_studienka",
    ),
    plugin(
        neighPush,
        sources="CP_32_studienka_studienka",
        targets="CP_32_studienka_berezinacrossing",
    ),
    plugin(
        neighPush,
        sources="CP_32_studienka_berezinacrossing",
        targets="CP_32_studienka_germanbank,CP_32_studienka_supplydepot",
    ),
    plugin(
        neighPush,
        sources="CP_32_studienka_germanbank",
        targets="CP_32_studienka_berezinacrossing,CP_32_studienka_supplydepot",
    ),
    plugin(
        neighPush,
        sources="CP_32_studienka_supplydepot",
        targets="CP_32_studienka_germanbank,CP_32_studienka_berezinacrossing",
    ),
    plugin(
        neighPush,
        sources="CP_32_studienka_supplydepot",
        targets="CP_32_studienka_napoleonpoint",
    ),
    plugin(
        neighPush,
        sources="CP_32_studienka_napoleonpoint",
        targets="CP_32_studienka_supplydepot",
    ),
]

gpm_coop = {
    64: kits_AI + tickets_64 + spawns,
    32: (
        tickets_32
        + kits_AI
        + push_32_AI
        + spawnerConditions_32
        + linkCPs_32
        + spawns
    ),
    16: tickets_16 + rifleNCO + spawns + push_16,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
