# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302,E0401
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    push,
    linkCPs,
    teamSPs,
    spawnerCondition,
    dynamicOOB,
)

kitlimits_16 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_mp18_Limited", limit=0.04),
    plugin(limitKit, team=2, slot=1, kit="NW_Grenadier_Limited,NW_Grenadier_Limited_alt,NW_Grenadier_Limited_alt2,NW_Grenadier_Limited_alt3", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_early_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="NW_LMG_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=4, kit="GW_Engineer_early_satchel_Limited", limit=0.04),
    plugin(limitKit, team=2, slot=4, kit="NW_Engineer_dynamite,NW_Engineer_dynamite_alt,NW_Engineer_dynamite_alt2,NW_Engineer_dynamite_alt3", limit=1),
    plugin(limitKit, team=1, slot=5, kit="GW_RifleAssault_early_k98b_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="NW_Antitank_Limited,NW_Antitank_Limited_alt", limit=0.1),
]

kitlimits_32 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_mp18_Limited", limit=0.04),
    plugin(limitKit, team=2, slot=1, kit="NW_Grenadier_Limited,NW_Grenadier_Limited_alt,NW_Grenadier_Limited_alt2,NW_Grenadier_Limited_alt3", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_early_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="NW_LMG_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=4, kit="GW_Engineer_early_satchel_Limited", limit=0.04),
    plugin(limitKit, team=2, slot=4, kit="NW_Engineer,NW_Engineer_alt,NW_Engineer_alt2,NW_Engineer_alt3", limit=1),
    plugin(limitKit, team=1, slot=5, kit="GW_RifleAssault_early_k98b_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="NW_Antitank_Limited_alt3", limit=0.1),
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_mp18_Limited", limit=0.04),
    plugin(limitKit, team=2, slot=1, kit="NW_Grenadier_Limited,NW_Grenadier_Limited_alt,NW_Grenadier_Limited_alt2,NW_Grenadier_Limited_alt3", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_early_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="NW_LMG_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=4, kit="GW_Engineer_early_satchel_Limited", limit=0.04),
    plugin(limitKit, team=2, slot=4, kit="NW_Engineer,NW_Engineer_alt,NW_Engineer_alt2,NW_Engineer_alt3", limit=1),
    plugin(limitKit, team=1, slot=5, kit="GW_RifleAssault_early_k98b_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="NW_Antitank_Limited_alt2", limit=0.1),
]


tickets_64 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=25)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=250)]


linkCPs_64 = [
    plugin(
        linkCPs,
        target="cp_64_naverdalen_sectorlock1",
        source="cp_64_naverdalen_rikstad_group, cp_64_naverdalen_orkla_river, cp_64_naverdalen_gamleveien",
    ),
    plugin(
        linkCPs,
        target="cp_64_naverdalen_sectorlock2",
        source="cp_64_naverdalen_holmen, cp_64_naverdalen_naverdalen",
    ),
]


push_64 = [
    plugin(
        push,
        source="cp_64_naverdalen_gruppe_fischer",
        target="cp_64_naverdalen_rikstad_group, cp_64_naverdalen_orkla_river, cp_64_naverdalen_gamleveien",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="cp_64_naverdalen_rikstad_group, cp_64_naverdalen_orkla_river, cp_64_naverdalen_gamleveien",
        target="cp_64_naverdalen_sectorlock1",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="cp_64_naverdalen_sectorlock1",
        target="cp_64_naverdalen_holmen, cp_64_naverdalen_naverdalen",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cp_64_naverdalen_holmen, cp_64_naverdalen_naverdalen",
        target="cp_64_naverdalen_sectorlock2",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="cp_64_naverdalen_sectorlock2",
        target="cp_64_naverdalen_naverdalsbakken, cp_64_naverdalen_siksakveien, cp_64_naverdalen_tropp_sorli",
        attacker=1,
        display_arrow=False,
        delay=60
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "cp_64_naverdalen_sectorlock1": {
                "axis": {
                    "creates": ["yesgo_B_64"],
                    "destroys": ["yesgo_1_64"],
                },
            },
        },
        inactive_at_start=["yesgo_B_64"],
        delay_axis=0,
        delay_allies=60,
    ),
    plugin(
        dynamicOOB,
        dynamic_flags={
            "cp_64_naverdalen_sectorlock2": {
                "axis": {
                    "creates": ["yesgo_C_64"],
                    "destroys": ["yesgo_2_64"],
                },
            },
        },
        inactive_at_start=["yesgo_C_64"],
        delay_axis=60,
        delay_allies=60,
    ),
]

spawnerConditions_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_64_naverdalen_gruppe_fischer_pzii",
        we_dont_own="cp_64_naverdalen_sectorlock2",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_64_naverdalen_gruppe_fischer_panzeri",
        we_dont_own="cp_64_naverdalen_sectorlock2",
    ),
]

coop_32 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout_early_k98b",
        soldier="gw_heer_light_early",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=2.0 / 32.0,
        kit="GW_SMGAssault_mp18_Limited",
        soldier="gw_heer_heavy_early",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=10.0 / 32.0,
        kit="GW_RifleAssault_early",
        soldier="gw_heer_light_early",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GW_LMG_early_Limited",
        soldier="gw_heer_heavy_early",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=6.0 / 32.0,
        kit="GW_Engineer_early_Satchel_Limited",
        soldier="gw_heer_light_early",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=4.0 / 32.0,
        kit="GW_RifleAssault_early_k98b_Limited",
        soldier="gw_heer_light_early",
    ),
    # Kit limits - Allies
		
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="NW_Scout",
        soldier="nw_light",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="NW_Grenadier_Limited",
        soldier="nw_heavy",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=8.0 / 32.0,
        kit="NW_RifleAssault",
        soldier="nw_light",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=4.0 / 32.0,
        kit="NW_LMG_Limited",
        soldier="nw_light",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=6.0 / 32.0,
        kit="NW_Engineer,NW_Engineer_alt,NW_Engineer_alt2,NW_Engineer_alt3",
        soldier="nw_heavy",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="NW_Antitank_Limited_alt3",
        soldier="nw_light",
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_MP38_K98b", "NW_NCO"),
        soldiers=("gw_heer_unteroffizier_early", "nw_sgt"),
    ),
]


gpm_cq = {
    64: tickets_64
    + kitlimits_64
    + rifleNCO
    + spawns
    + linkCPs_64
    + push_64
    + spawnerConditions_64
    + dynamicoob_64,
    32: tickets_32
    + kitlimits_32
    + rifleNCO
    + spawns,
    16 : tickets_64
    + kitlimits_16
    + rifleNCO
    + spawns,
}


gpm_coop = {
    64: tickets_64
    + rifleNCO
    + spawns
    + linkCPs_64
    + push_64
    + spawnerConditions_64,
    32: coop_32
	+ tickets_32
	+ rifleNCO
	+ spawns,
    16 : tickets_64
    + rifleNCO
    + spawns,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop