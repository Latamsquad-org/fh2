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
        kits=("GS_NCO", "UW_NCO"),
        soldiers=("gs_waffen_unteroffizier", "uw_ranger_sgt"),
    )
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

push_64 = [
    plugin(
        push,
        source="CP_64_Ramelle_Ruins",
        target="CP_64_ramelle_sector_a_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Ramelle_Right_Flank",
        target="CP_64_ramelle_sector_a_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Ramelle_Fountain",
        target="CP_64_ramelle_sector_a_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_ramelle_sector_a_locker",
        target="CP_64_Ramelle_Bridge",
        attacker=1,
        display_arrow=False,
        wants_source_marker=False,
        delay=15,
    ),
    plugin(
        push,
        source="CP_64_ramelle_sector_a_locker",
        target="CP_64_Ramelle_Church_Street",
        attacker=1,
        display_arrow=False,
        wants_source_marker=False,
        delay=15,
    ),
    plugin(
        push,
        source="CP_64_Ramelle_Bridge",
        target="CP_64_ramelle_sector_b_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Ramelle_Church_Street",
        target="CP_64_ramelle_sector_b_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_ramelle_sector_b_locker",
        target="CP_64_Ramelle_Alamo",
        attacker=1,
        display_arrow=False,
        wants_source_marker=False,
        delay=15,
    ),
    plugin(
        push,
        source="CP_64_Ramelle_Alamo",
        target="CP_64_Ramelle_Historical_Center,CP_64_Ramelle_Clearing",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_Ramelle_Clearing",
        target="CP_64_Ramelle_US_Reinforcements",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_Ramelle_Historical_Center",
        target="CP_64_Ramelle_CrossRoads, CP_64_Ramelle_US_Reinforcements",
        attacker=1,
        display_arrow=False,
    ),
]

push_16 = [
    plugin(
        push,
        source="CP_16_Ramelle_US_Airbourne",
        target="CP_16_Ramelle_Clearing, CP_16_Ramelle_Walled_Garden",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_16_Ramelle_Clearing, CP_16_Ramelle_Walled_Garden",
        target="CP_16_Ramelle_Coach_House",
        attacker=2,
        force=True,
        count=1,
    ),
    plugin(
        push,
        source="CP_16_Ramelle_Coach_House, CP_16_Ramelle_Walled_Garden, CP_16_Ramelle_Clearing",
        target="CP_16_Ramelle_Bridge",
        attacker=2,
        display_arrow=False,
        delay=10,
    ),
]

kitlimits_64 = [
    plugin(
        limitKit, team=1, slot=0, kit="GS_RifleAssault_G43_Limited", limit=0.05
    ),
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_MG42_Limited", limit=0.05),
    plugin(
        limitKit, team=2, slot=3, kit="UW_LMG_Limited_nobipod", limit=0.075
    ),
    plugin(
        limitKit, team=1, slot=5, kit="GS_RifleAssault_ramelle", limit=0.05
    ),
    plugin(
        limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.08
    ),
    plugin(
        limitKit, team=1, slot=4, kit="GS_Engineer_Satchel_ramelle", limit=0.05
    ),
    plugin(
        limitKit, team=2, slot=4, kit="UW_Engineer_Satchel_ramelle", limit=0.05
    ),
]

kitlimits_32 = [
    plugin(
        limitKit, team=1, slot=0, kit="GS_RifleAssault_G43_Limited", limit=0.05
    ),
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_MG42_Limited", limit=0.05),
    plugin(
        limitKit, team=2, slot=3, kit="UW_LMG_Limited_nobipod", limit=0.075
    ),
    plugin(
        limitKit, team=1, slot=5, kit="GS_RifleAssault_ramelle", limit=0.05
    ),
    plugin(
        limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.08
    ),
    plugin(
        limitKit, team=1, slot=4, kit="GS_Engineer_Satchel_ramelle", limit=0.05
    ),
    plugin(
        limitKit, team=2, slot=4, kit="UW_Engineer_Satchel_ramelle", limit=0.05
    ),
]

kitlimits_16 = [
    plugin(
        limitKit, team=1, slot=0, kit="GS_RifleAssault_G43_Limited", limit=0.05
    ),
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_MG42_Limited", limit=0.05),
    plugin(
        limitKit, team=2, slot=3, kit="UW_LMG_Limited_nobipod", limit=0.075
    ),
    plugin(
        limitKit, team=1, slot=5, kit="GS_RifleAssault_ramelle", limit=0.05
    ),
    plugin(
        limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.08
    ),
    plugin(
        limitKit, team=1, slot=4, kit="GS_Engineer_Satchel_ramelle", limit=0.05
    ),
    plugin(
        limitKit, team=2, slot=4, kit="UW_Engineer_Satchel_ramelle", limit=0.05
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_ramelle_sector_a_locker": {
                "axis": {
                    "creates": ["CombatArea_axis2"],
                    "destroys": ["CombatArea_allies1"],
                },
            },
            "CP_64_ramelle_sector_b_locker": {
                "axis": {
                    "creates": ["CombatArea_axis3"],
                    "destroys": ["CombatArea_allies2"],
                },
            },
        },
        inactive_at_start=["CombatArea_axis2", "CombatArea_axis3"],
        delay_axis=0,
        delay_allies=60,
    )
]


linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_ramelle_sector_a_locker",
        source=[
            "CP_64_Ramelle_Ruins",
            "CP_64_Ramelle_Right_Flank",
            "CP_64_Ramelle_Fountain",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_ramelle_sector_b_locker",
        source=["CP_64_Ramelle_Church_Street", "CP_64_Ramelle_Bridge"],
    ),
]

reinforcements_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Ramelle_German_Position_Tiger2, CP_64_Ramelle_German_Position_MarderB",
        they_own="CP_64_Ramelle_Right_Flank",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Ramelle_US_Reinforcements_Sherman1",
        they_own="CP_64_Ramelle_Historical_Center",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Ramelle_US_Reinforcements_sherman2",
        they_own="CP_64_Ramelle_Alamo",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Ramelle_US_Reinforcements_mgtruck",
        they_own="CP_64_Ramelle_Clearing",
    ),
]


tickets_64 = [plugin(ticketLoss, ticketLoss1=13, ticketLoss2=1000)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=7)]


coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=7.0 / 32.0,
        kit="GS_RifleAssault_G43_Limited",
        soldier="gs_waffen_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GS_SMGAssault_Limited",
        soldier="gs_waffen_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=4.0 / 32.0,
        kit="GS_Rifleonly",
        soldier="gs_waffen_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GS_LMG_MG42_Limited",
        soldier="gs_waffen_maschinengewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GS_Engineer_Satchel_ramelle",
        soldier="gs_waffen_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=7.0 / 32.0,
        kit="GS_RifleAssault_ramelle",
        soldier="gs_waffen_gewehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="UW_Scout_M1A1Carbine",
        soldier="uw101ab_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=5.0 / 32.0,
        kit="UW_SMGAssault_Limited",
        soldier="uw101ab_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="UW_Rifleonly",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=5.0 / 32.0,
        kit="UW_LMG_Limited_nobipod",
        soldier="uw_mixed",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="UW_Engineer_Satchel_ramelle",
        soldier="uw_ranger_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=5.0 / 32.0,
        kit="UW_AntitankAssault_Limited",
        soldier="uw101ab_pvt",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Ramelle_Ruins",
        we_own="CP_64_Ramelle_Fountain",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Ramelle_Alamo",
        we_own="CP_64_Ramelle_Bridge and CP_64_Ramelle_Historical_Center and (CP_64_Ramelle_Clearing or CP_64_Ramelle_CrossRoads)",
    ),
    plugin(
        balanceSPs,
        custom_weights=[
            dict(cp="CP_64_Ramelle_Right_Flank", team=1, weight=400000),
            dict(cp="CP_64_Ramelle_Church_Street", team=1, weight=500000),
            dict(cp="CP_64_Ramelle_Right_Flank", team=2, weight=300000),
            dict(cp="CP_64_Ramelle_Church_Street", team=2, weight=400000),
        ],
    ),
    # Push mode
    plugin(aiPush),
    plugin(
        linkCPs,
        target="CP_64_Sector1_dummy",
        source="CP_64_Ramelle_Ruins,CP_64_Ramelle_Right_Flank,CP_64_Ramelle_Church_Street,CP_64_Ramelle_Fountain,CP_64_Ramelle_Bridge",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Ramelle_German_Position_MarderB",
        we_dont_own="CP_64_Ramelle_Ruins",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Ramelle_German_Position_tiger2",
        they_own="CP_64_Ramelle_Right_Flank",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Ramelle_Alamo_Hanomagspawn2",
        we_dont_own="CP_64_Ramelle_Fountain or CP_64_Ramelle_Right_Flank",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Ramelle_US_Reinforcements_shermanalamo,CP_64_Ramelle_Bridge_US_Mortar",
        they_own="CP_64_Ramelle_Alamo",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Ramelle_Historical_Center_Sherman,CP_64_Ramelle_US_Reinforcements_mgtruck",
        they_own="CP_64_Ramelle_Historical_Center or CP_64_Ramelle_Clearing",
    ),
]

gpm_cq = {
    64: tickets_64
    + spawns
    + kitlimits_64
    + push_64
    + linkCPs_64
    + reinforcements_64
    + dynamicoob_64
    + nco,
    32: kitlimits_32 + nco,
    16: tickets_16 + spawns + kitlimits_16 + push_16 + nco,
}
gpm_coop = {
    64: coop_64 + tickets_64 + spawns + nco,
}
sp3 = gpm_coop
