# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    limitKit,
    NCOrifleData,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    DoubleBleed,
    push,
    linkCPs,
)

links_64 = [
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_bridge"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linecentre", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_lineeast", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_linewest", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
plugin(
    linkCPs,
    target="CP_64_event_aa_storm_reinforcements",
    source=["CP_64_event_aa_storm_airfield", "CP_64_event_aa_storm_bridge", "CP_64_event_aa_storm_town", "CP_64_event_aa_storm_axismain"]
),
]

push_64 = [
    plugin(
        push,
        source="CP_64_event_aa_storm_rusmain",
        target="CP_64_event_aa_storm_town, CP_64_event_aa_storm_bridge, CP_64_event_aa_storm_airfield",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_event_aa_storm_town, CP_64_event_aa_storm_bridge, CP_64_event_aa_storm_airfield",
        target="CP_64_event_aa_storm_axismain",
        attacker=2,
    ),
]

kitlimits_64 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GM_Limited_Assault_MP40_K98_para",
        limit=0.15,
    ),
    plugin(limitKit, team=2, slot=1, kit="RE_SMGAssault_Limited", limit=0.15),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GM_Limited_Support_MG34_K98",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="RE_LMG_limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_AntitankAssault_ggp40_haft",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="RE_AntitankAssault_pps42_limited",
        limit=0.2,
    ),
]

kitlimits_16 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GM_Limited_Assault_MP40_K98_para",
        limit=0.15,
    ),
    plugin(limitKit, team=2, slot=1, kit="RE_SMGAssault_Limited", limit=0.15),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GM_Limited_Support_MG34_K98",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="RE_LMG_limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="GW_SMGAssault_mp717(r)_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        kit="RE_SMGAssault_pps43_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_RifleAssault_G43_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="RE_RifleAssault_SVT40_Limited",
        limit=0.2,
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO_MP40_G43", "RE_NCO_42"),
        soldiers=("gcwhsnow_nco", "re_nco_soldier_telogrieka"),
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=18, ticketLoss2=18)]

bleed_32 = [
    plugin(
        DoubleBleed,
    ),
]

pco_spawners_64 = [
    # Axis reinforcements
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_event_aa_storm_linewest_stuka",
        we_own=("CP_64_event_aa_storm_airfield " "and CP_64_event_aa_storm_linewest"),
    ),
    # Allied reinforcements
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_event_aa_storm_rusmain_kv, CP_64_event_aa_storm_rusmain_t3476_5",
        they_own=("CP_64_event_aa_storm_reinforcements"),
    ),
]

gpm_cq = {
    64: tickets_64 + kitlimits_64 + rifleNCO + pco_spawners_64 + spawns + push_64 + links_64,
    32: kitlimits_64 + rifleNCO + spawns + bleed_32 + tickets_64,
    16: kitlimits_16 + rifleNCO + spawns,
}
gpm_coop = {
    64: spawns + rifleNCO,
    32: spawns + rifleNCO,
    16: spawns + rifleNCO,
}
