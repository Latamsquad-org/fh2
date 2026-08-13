# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    aiPush,
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

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_m34", "UW_NCO_SME"),
        soldiers=("gb_nco_splittermuster", "uw_airborne_sgt"),
    ),
]
spawns_32 = [plugin(teamSPs)]

spawns_64 = [
    plugin(
        teamSPs,
        sps=[
            "bridgeno3_axis1",
            "bridgeno3_axis2",
            "bridgeno3_axis3",
            "bridgeno3_axis4",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "bridgeno3_allies1",
            "bridgeno3_allies2",
            "bridgeno3_allies3",
            "bridgeno3_allies4",
            "bridgeno3_allies5",
            "bridgeno3_allies6",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "causeway_axis_1",
            "causeway_axis_2",
            "causeway_axis_3",
            "causeway_axis_4",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "causeway_allies_1",
            "causeway_allies_2",
            "causeway_allies_3_0",
            "causeway_allies_4_0",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "bridgeno4_axis1",
            "bridgeno4_axis2",
            "bridgeno4_axis3",
            "bridgeno4_axis4",
            "bridgeno4_axis5",
            "bridgeno4_axis6",
            "bridgeno4_axis7",
            "bridgeno4_axis8",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "bridgeno4_allies1",
            "bridgeno4_allies2",
            "bridgeno4_allies3",
            "bridgeno4_allies4",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "crossroad_axis1",
            "crossroad_axis2",
            "crossroad_axis3",
            "crossroad_axis4",
            "crossroad_axis5",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "crossroad_allies1",
            "crossroad_allies2",
            "crossroad_allies3",
            "crossroad_allies4",
            "crossroad_allies5",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "ingouf_farm_axis1",
            "ingouf_farm_axis2",
            "ingouf_farm_axis3",
            "ingouf_farm_axis4",
            "ingouf_farm_axis5",
            "ingouf_farm_axis6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "ingouf_farm_allies1",
            "ingouf_farm_allies2",
            "ingouf_farm_allies3",
            "ingouf_farm_allies4",
            "ingouf_farm_allies5",
            "ingouf_farm_allies6",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "orchard_axis1",
            "orchard_axis2",
            "orchard_axis3",
            "orchard_axis4",
            "orchard_axis5",
            "orchard_axis6",
            "orchard_axis7",
            "orchard_axis8",
            "orchard_axis9",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "orchard_allies_1",
            "orchard_allies_2",
            "orchard_allies_3",
            "orchard_allies_4",
        ],
        team=2,
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_phl_locker_1st": {
                "allies": {
                    "creates": ["CombatArea_allies2"],
                    "destroys": ["CombatArea_axis1"],
                },
            },
            "CP_64_phl_locker_2nd": {
                "allies": {
                    "creates": ["CombatArea_allies3"],
                    "destroys": ["CombatArea_axis2"],
                },
            },
        },
        inactive_at_start=["CombatArea_allies2", "CombatArea_allies3"],
        delay_axis=180,
        delay_allies=0,
    )
]

dynamicoob_32 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_32_phl_locker_2nd": {
                "allies": {
                    "creates": ["yesgo_32_allies3"],
                    "destroys": ["yesgo_32_axis2"],
                },
            },
        },
        inactive_at_start=["yesgo_32_allies3"],
        delay_axis=180,
        delay_allies=0,
    )
]

push_64 = [
    plugin(
        push,
        source="502_main",
        target="bridge_no_3",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="502_main",
        target="causeway",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="502_main",
        target="bridge_no_4",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="bridge_no_3, causeway, bridge_no_4",
        target="CP_64_phl_locker_1st",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_phl_locker_1st",
        target="fjr_defense_position, ingouf_farm",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="ingouf_farm, fjr_defense_position",
        target="CP_64_phl_locker_2nd",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_phl_locker_2nd",
        target="crossroad, orchard",
        attacker=2,
        display_arrow=False,
        delay=30,
    ),
]
push_32 = [
    plugin(
        push,
        source="CP_32_PHL_bridge_no_4",
        target="CP_32_PHL_fjr_defense_position, CP_32_PHL_ingouf_farm",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_32_PHL_ingouf_farm, CP_32_PHL_fjr_defense_position",
        target="CP_32_phl_locker_2nd",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_32_phl_locker_2nd",
        target="CP_32_PHL_crossroad, CP_32_PHL_orchard",
        attacker=2,
        display_arrow=False,
        delay=30,
    ),
]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_phl_locker_2nd",
        source=["fjr_defense_position", "ingouf_farm"],
    ),
    plugin(
        linkCPs,
        target="CP_64_phl_locker_1st",
        source=["bridge_no_3", "causeway", "bridge_no_4"],
    ),
]

links_32 = [
    plugin(
        linkCPs,
        target="CP_32_PHL_locker_2nd",
        source=["CP_32_PHL_fjr_defense_position", "CP_32_PHL_ingouf_farm"],
    ),
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_FG42_Limited", limit=0.08),
    plugin(limitKit, team=2, slot=3, kit="UW_MG_30cal_Limited", limit=0.12),
    plugin(limitKit, team=1, slot=5, kit="GS_RifleAssault_G41_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="UW_RifleGrenadierM1_Limited", limit=0.2),
]

kitlimits_32 = [
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_FG42_Limited", limit=0.08),
    plugin(limitKit, team=2, slot=3, kit="UW_MG_30cal_Limited", limit=0.12),
    plugin(limitKit, team=1, slot=5, kit="GS_RifleAssault_G41_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="UW_RifleGrenadierM1_Limited", limit=0.2),
]


kitlimits_16 = [
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_FG42_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="UW_MG_30cal_Limited", limit=0.15),
    plugin(limitKit, team=1, slot=5, kit="GS_RifleAssault_G41_Limited", limit=0.3),
    plugin(limitKit, team=2, slot=5, kit="UW_RifleGrenadierM1_Limited", limit=0.3),
]
tickets_64 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=12)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=12)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

gpm_cq = {
    64: (rifleNCO + dynamicoob_64 + kitlimits_64 + links_64 + push_64 + spawns_64 + tickets_64),
    32: (rifleNCO + dynamicoob_32 + kitlimits_32 + links_32 + push_32 + spawns_32 + tickets_32),
    16: rifleNCO + kitlimits_16 + tickets_16,
}

coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GS_Scout",
        soldier="gb_light_splittermuster",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GS_SMGAssault_Limited",
        soldier="gb_light_sumpfmuster",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=10.0 / 32.0,
        kit="GW_RifleAssault_noNadeLauncher",
        soldier="gb_light_splittermuster",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GS_LMG_FG42_Limited",
        soldier="gb_heavy_splittermuster",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=3.0 / 32.0,
        kit="GS_Engineer_Satchel",
        soldier="gb_light_splittermuster",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="GS_RifleAssault_G41_Limited",
        soldier="gb_heavy_grunmeliert",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=2.0 / 32.0,
        kit="UW_Scout",
        soldier="uw_airborne_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="UW_SMGAssault_Limited",
        soldier="uw_airborne_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=11.0 / 32.0,
        kit="UW_RifleAssault_noNadeLauncher",
        soldier="uw_airborne_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=8.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uw_airborne_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="UW_Engineer_Satchel_m1a1",
        soldier="uw_airborne_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=2.0 / 32.0,
        kit="UW_RifleGrenadierM1_Limited",
        soldier="uw_airborne_pvt",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
    plugin(ticketLoss, ticketLoss1=40, ticketLoss2=10),
    plugin(
        spawnerCondition,
        team=1,
        spawner="farm_lafette_mg42",
        they_own="bridge_no_4",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="ingouf_farm_axis_mg,ingouf_farm_mg34",
        they_own="bridge_no_4 and fjr_defense_position",
    ),
]


gpm_coop = {
    64: coop_64 + rifleNCO,
    32: rifleNCO,
    16: rifleNCO,
}

sp3 = gpm_coop
