# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    push,
    neighPush,
    teamSPs,
    spawnerCondition,
    linkCPs,
    dynamicOOB,
)

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_pogostje_sector1": {
                "allies": {
                    "creates": ["CombatArea_186_cq_64"],
                    "destroys": ["CombatArea_225_cq_64"],
                },
            },
            "CP_64_pogostje_sector2": {
                "allies": {
                    "creates": ["CombatArea_244_cq_64"],
                    "destroys": ["CombatArea_258_cq_64"],
                },
            },
        },
        inactive_at_start=["CombatArea_186_cq_64", "CombatArea_244_cq_64"],
        delay_axis=150,
        delay_allies=0,
    )
]

kitlimits_16 = [
    plugin(limitKit, team=1, slot=1, kit="GA_Limited_Assault_MP40_K98_early", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="RE_SMGAssault_ppd40_limited", limit=0.1,),
    plugin(limitKit, team=1, slot=3, kit="GA_Limited_Support_MG34_K98", limit=0.075),
    plugin(limitKit, team=2, slot=3, kit="RE_LMG_dt_Limited", limit=0.075),
    plugin(limitKit, team=1, slot=5, kit="GW_RifleAssault_early_smoke_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="RE_RifleAssault_Early_Limited", limit=0.2),
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GA_Limited_Assault_MP40_K98_early", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="RE_SMGAssault_ppd40_limited", limit=0.1,),
    plugin(limitKit, team=1, slot=3, kit="GA_Limited_Support_MG34_K98", limit=0.08),
    plugin(limitKit, team=2, slot=3, kit="RE_RifleAssault_SVT40_Limited", limit=0.12),
    plugin(limitKit, team=1, slot=5, kit="GA_ATPzB39_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="RE_Antitank_PTRD_Limited", limit=0.2),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_pogostje_sector1",
        source="CP_64_pogostje_henkel, CP_64_pogostje_dubok, CP_64_pogostje_pogostje",
    ),
    plugin(
        linkCPs,
        target="CP_64_pogostje_sector2",
        source="CP_64_pogostje_camp, CP_64_pogostje_rivercrossing",
    ),
    plugin(
        linkCPs,
        target="CP_64_pogostje_sector3",
        source="CP_64_pogostje_vinyagolovo",
    ),
    plugin(
        linkCPs,
        target="CP_64_pogostje_sector4",
        source="CP_64_pogostje_secret_4",
    ),
    plugin(
        linkCPs,
        target="CP_64_pogostje_sector5",
        source="CP_64_pogostje_secret_5",
    ),
    plugin(
        linkCPs,
        target="CP_64_pogostje_secret_6",
        source="CP_64_pogostje_secret_4, CP_64_pogostje_secret_5",
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_pogostje_secret_7",
        source="CP_64_pogostje_secret_6",
        invert=True,
    ),
]

push_64 = [
    plugin(
        push,
        source="CP_64_pogostje_311thStrelkovaja",
        target="CP_64_pogostje_henkel, CP_64_pogostje_dubok, CP_64_pogostje_pogostje",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_pogostje_henkel, CP_64_pogostje_dubok, CP_64_pogostje_pogostje",
        target="CP_64_pogostje_sector1",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_pogostje_sector1",
        target="CP_64_pogostje_camp, CP_64_pogostje_rivercrossing",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_pogostje_camp, CP_64_pogostje_rivercrossing",
        target="CP_64_pogostje_sector2",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_pogostje_sector2",
        target="CP_64_pogostje_vinyagolovo",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_pogostje_vinyagolovo",
        target="CP_64_pogostje_sector3",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
]

push_32SAV = [
    plugin(
        neighPush,
        sources="CP_32_pogostje_pogostje",
        targets="CP_32_pogostje_rivercrossing",
    ),
    plugin(
        neighPush,
        sources="CP_32_pogostje_rivercrossing",
        targets="CP_32_pogostje_waldlager,CP_32_pogostje_winjagolovonorth",
    ),
    plugin(
        neighPush,
        sources="CP_32_pogostje_winjagolovonorth",
        targets="CP_32_pogostje_waldlager,CP_32_pogostje_rivercrossing",
    ),
    plugin(
        neighPush,
        sources="CP_32_pogostje_winjagolovo",
        targets="CP_32_pogostje_winjagolovonorth",
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_pogostje_pogostje",
        target="CP_32_pogostje_rivercrossing, CP_32_pogostje_waldlager",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_32_pogostje_rivercrossing",
        target="CP_32_pogostje_winjagolovonorth",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_32_pogostje_winjagolovonorth, CP_32_pogostje_waldlager",
        target="CP_32_pogostje_winjagolovo",
        attacker=2,
        display_arrow=False,
    ),
]


tickets_64 = [plugin(ticketLoss, ticketLoss1=9999, ticketLoss2=12)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40_early", "RE_NCO_42"),
        soldiers=("GcWhSnow_feldgrau_nco", "re_nco_soldier_telogrieka"),
    ),
]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_pogostje_311thStrelkovaja_kv1a, "
            "CP_64_pogostje_311thStrelkovaja_kv1b, "
            "CP_64_pogostje_311thStrelkovaja_bt7a, "
            "CP_64_pogostje_311thStrelkovaja_t26a, "
            "CP_64_pogostje_311thStrelkovaja_t34a"
        ),
        we_dont_own="CP_64_pogostje_sector1",
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
    16: tickets_16 + kitlimits_16 + rifleNCO,
    32: kitlimits_64 + push_32 + spawns + rifleNCO,
}


gpm_coop = {
    64: tickets_64 + rifleNCO + spawnerConditions + spawns + push_64 + linkCPs_64,
    32: rifleNCO + spawns + push_32,
}


sp2 = gpm_coop
sp3 = gpm_coop