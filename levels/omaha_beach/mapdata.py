# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    teamSPs,
    push,
    linkCPs,
    ticketLoss,
    spawnerCondition,
    disableSPs,
    timeCP,
    dynamicOOB,
    NCOrifleData,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UA_NCO"),
        soldiers=("gw_heer_unteroffizier", "uw_ranger_sgt"),
    )
]

nco_32 = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_G41", "UW_NCO"),
        soldiers=("gw_heer_unteroffizier", "uw_29th_sgt"),
    )
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_Sector1",
        source="CP_64_omaha_wn72, CP_64_omaha_wn71, CP_64_omaha_wn73",
    ),
    plugin(
        linkCPs,
        target="CP_Sector2",
        source="CP_64_omaha_viervilleeast, CP_64_omaha_vierville",
    ),
    plugin(
        linkCPs, target="CP_64_omaha_secret_beach_right", source="CP_Sector1"
    ),
]

push_64 = [
    plugin(
        push,
        source="CP_64_omaha_wn72, CP_64_omaha_wn71, CP_64_omaha_wn73",
        target="CP_Sector1",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_Sector1",
        target="CP_64_omaha_vierville, CP_64_omaha_viervilleeast",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_omaha_vierville, CP_64_omaha_viervilleeast",
        target="CP_Sector2",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_Sector2",
        target="CP_64_omaha_church",
        attacker=2,
        display_arrow=False,
        delay=45,
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_omaha_beach_kampfgruppemeyer",
        target="CP_32_omaha_beach_crossroads, CP_32_omaha_beach_vierville",
        attacker=1,
        display_arrow=True,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_32_omaha_beach_crossroads, CP_32_omaha_beach_vierville",
        target="CP_32_omaha_beach_mortarposition",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_omaha_beach_mortarposition",
        target="CP_32_omaha_beach_overlook, CP_32_omaha_beach_wn71",
        attacker=1,
        display_arrow=True,
        wants_target_marker=False,
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_Sector1": {
                "allies": {
                    "creates": ["CombatArea_allies2"],
                    "destroys": ["CombatArea_axis1"],
                },
            },
            "CP_Sector2": {
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

kitlimits_64 = [
    plugin(limitKit, team=1, slot=0, kit="GW_Scout_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=0, kit="UW_Ranger_Scout_Limited", limit=0.16),
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.1),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_riflenadelauncher_limited",
        limit=0.075,
    ),
    plugin(limitKit, team=2, slot=3, kit="UW_LMG_Limited", limit=0.075),
    plugin(
        limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.09
    ),
    plugin(
        limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.1
    ),
]

kitlimits_32 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.1),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_LMG_limited",
        limit=0.1,
    ),
    plugin(limitKit, team=2, slot=3, kit="UW_LMG_Limited", limit=0.1),
    plugin(
        limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.09
    ),
    plugin(
        limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.06
    ),
]


tickets = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=15)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_omaha_church_aa, CP_64_omaha_vierville_atgun, CP_64_omaha_viervilleeast_at, CP_64_omaha_viervilleeast_DE_US_DepMG, CP_64_omaha_vierville_DE_US_DepMG, CP_64_omaha_church_DE_US_DepMG,  CP_64_omaha_church_DE_US_SupportMG42",
        we_dont_own="CP_64_omaha_wn72 and CP_64_omaha_wn71 and CP_64_omaha_wn73",
    ),
]

spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_omaha_beach_overlook_sherman1, CP_32_omaha_beach_overlook_sherman2",
        we_dont_own="CP_32_omaha_beach_mortarposition",
    ),
]


coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout_Limited",
        soldier="gw_heer_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=5.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="gw_heer_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=10.0 / 32.0,
        kit="GW_Rifleonly_ancto",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GW_riflenadelauncher_limited",
        soldier="gw_heer_gewehr",
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
        limit=4.0 / 32.0,
        kit="GW_AntitankAssault_Limited",
        soldier="gw_heer_panzerabwehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="UW_Ranger_Scout_Limited",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=5.0 / 32.0,
        kit="UW_SMGAssault_Limited",
        soldier="uw_ranger_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="UW_RifleAssault",
        soldier="uw_29th_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uw_29th_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=6.0 / 32.0,
        kit="UW_Engineer_bangalore",
        soldier="uw_29th_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=3.0 / 32.0,
        kit="UW_AntitankAssault_Limited",
        soldier="uw_29th_cpl",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_omaha_wn71",
        we_own="CP_64_Omaha_german_forward_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_omaha_wn73",
        we_own="CP_64_Omaha_german_forward_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_omaha_viervilleeast",
        we_own="CP_64_omaha_wn71 and CP_64_omaha_wn73",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_omaha_vierville",
        we_own="CP_64_omaha_wn71 or CP_64_omaha_wn73",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_omaha_beach_us_fleet",
        we_own="CP_64_omaha_beach_left or CP_64_omaha_beach_right",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_omaha_beach_left",
        we_own="CP_64_omaha_wn71 and CP_64_omaha_wn72",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_omaha_beach_right",
        we_own="CP_64_omaha_wn73 and CP_64_omaha_wn72",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_omaha_wn71",
        we_own="CP_64_omaha_viervilleeast or CP_64_omaha_vierville or CP_64_omaha_church",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_omaha_wn73",
        we_own="CP_64_omaha_viervilleeast or CP_64_omaha_vierville or CP_64_omaha_church",
    ),
    # Forward dummy
    plugin(
        timeCP, target="CP_64_Omaha_german_forward_dummy", team=-1, time=180
    ),
    # Push mode
    plugin(
        linkCPs,
        target="CP_Sector1",
        source="CP_64_omaha_wn72, CP_64_omaha_wn71, CP_64_omaha_wn73",
    ),
    plugin(
        push,
        source="CP_64_omaha_wn72, CP_64_omaha_wn71, CP_64_omaha_wn73",
        target="CP_64_omaha_vierville, CP_64_omaha_viervilleeast, CP_64_omaha_church",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_omaha_viervilleeast_mg,CP_64_omaha_viervilleeast_at50",
        they_own="CP_64_omaha_wn71 or CP_64_omaha_wn73",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_omaha_church_atgun,CP_64_omaha_church_statmg,CP_64_omaha_church_lafette,CP_64_omaha_viervilleeast_at,CP_64_omaha_vierville_atgun",
        they_own="CP_64_omaha_wn72 and CP_64_omaha_wn71 and CP_64_omaha_wn73",
    ),
]

gpm_cq = {
    64: tickets
    + spawns
    + kitlimits_64
    + push_64
    + linkCPs_64
    + spawnerConditions
    + dynamicoob_64
    + nco,
    16: tickets_16 + kitlimits_64 + nco,
    32: tickets_32 + spawns + push_32 + kitlimits_32 + nco_32 + spawnerConditions_32, 
}


disable_AI_32 = [
    plugin(
        disableSPs,
        team=2,
        cp="CP_32_omaha_beach_wn71",
        we_own="CP_32_omaha_beach_mortarposition",
    ),
]

gpm_coop = {
    64: coop_64 + tickets + spawns + nco,
    32: tickets_32 + spawns + push_32 + nco_32 + spawnerConditions_32 + disable_AI_32,
    16: tickets_16 + nco,    
}
sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop


