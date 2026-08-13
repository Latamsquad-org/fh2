# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    limitKit,
    push,
    teamSPs,
    linkCPs,
    timeCP,
    ticketLoss,
    spawnerCondition,
    aiPush,
    disableSPs,
    balanceSPs,
    dynamicOOB,
    NCOrifleData,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO"),
        soldiers=("GcWhCamo_nco", "uc_fall44_9th_sgt"),
    )
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_hurtgen_forest_katzenhardt": {
                "allies": {
                    "creates": ["CombatArea_allies2"],
                    "destroys": ["CombatArea_axis1"],
                },
            },
        },
        inactive_at_start=["CombatArea_allies2"],
        delay_axis=180,
        delay_allies=60,
    )
]

push_64 = [
    plugin(
        push,
        source="CP_64_hurtgen_forest_lookout",
        target="CP_64_hurtgen_forest_bunker",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_hurtgen_forest_north",
        target="CP_64_hurtgen_forest_northerntrail",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_hurtgen_forest_bridge",
        target="CP_64_hurtgen_forest_crossroads",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_hurtgen_forest_crossroads, CP_64_hurtgen_forest_northerntrail, CP_64_hurtgen_forest_bunker",
        target="CP_64_hurtgen_forest_katzenhardt",
        attacker=2,
        force=True,
        count=2,
    ),
    plugin(
        push,
        source="CP_64_hurtgen_forest_katzenhardt",
        target="CP_64_hurtgen_forest_germeter",
        attacker=2,
        delay=60,
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_hurtgen_alliedmain",
        target="CP_32_hurtgen_katzenhardt",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_hurtgen_katzenhardt",
        target="CP_32_hurtgen_hof",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_hurtgen_hof",
        target="CP_32_hurtgen_germeternorth",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_hurtgen_germeternorth",
        target="CP_32_hurtgen_germetersouth",
        attacker=2,
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

kits_64 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_StG44Assault_hurtgen_Limited",
        slot=1,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_Limited",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_MG42_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited",
        slot=3,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_RifleAssault_G43_hurtgen_Limited",
        slot=4,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault_Limited",
        slot=5,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankAssault_Limited",
        slot=5,
        limit=0.1,
    ),
]

kits_32 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_StG44Assault_hurtgen_Limited",
        slot=1,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_Limited",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_MG42_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited",
        slot=3,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_RifleAssault_G43_hurtgen_Limited",
        slot=4,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault_patrone_grenades",
        slot=5,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankAssault_Limited",
        slot=5,
        limit=0.1,
    ),
]

kits_16 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_StG44Assault_hurtgen_Limited",
        slot=1,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_Limited",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_MG42_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited",
        slot=3,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_RifleAssault_G43_hurtgen_Limited",
        slot=4,
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault_Limited",
        slot=5,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankAssault_Limited",
        slot=5,
        limit=0.1,
    ),
]

spawnerCondition_64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_hurtgen_forest_sermannorth_dummy_sherman",
        we_own="CP_64_hurtgen_forest_north and CP_64_hurtgen_forest_lookout",
        we_dont_own="CP_64_hurtgen_forest_northerntrail and CP_64_hurtgen_forest_katzenhardt",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_hurtgen_forest_sherman_dummy_sherman",
        we_own="CP_64_hurtgen_forest_lookout and CP_64_hurtgen_forest_bridge",
        we_dont_own="CP_64_hurtgen_forest_crossroads and CP_64_hurtgen_forest_katzenhardt",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="germeter_stugIV_1,germeter_stugIV_2,germeter_flak,germeter_pak40_1,germeter_pak40_2,germeter_stuka_zu_fuss,"
        + "germeter_PU_G43sc,germeter_PU_Gr34_1,germeter_PU_Gr34_2,germeter_PU_k98zf41_1,germeter_PU_k98zf41_2,germeter_PU_MG42_Lafette,germeter_PU_Schreck",
        they_own="CP_64_hurtgen_forest_katzenhardt",
    ),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_hurtgen_forest_north_axis_dummy",
        source="CP_64_hurtgen_forest_katzenhardt, CP_64_hurtgen_forest_north",
        never_owned_by=2,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_hurtgen_forest_lookout_axis_dummy",
        source="CP_64_hurtgen_forest_katzenhardt, CP_64_hurtgen_forest_lookout",
        never_owned_by=2,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_hurtgen_forest_bridge_axis_dummy",
        source="CP_64_hurtgen_forest_katzenhardt, CP_64_hurtgen_forest_bridge",
        never_owned_by=2,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_hurtgen_forest_northerntrail_dummy",
        source="CP_64_hurtgen_forest_northerntrail, CP_64_hurtgen_forest_bunker",
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_hurtgen_forest_crossroads_dummy",
        source="CP_64_hurtgen_forest_crossroads, CP_64_hurtgen_forest_bunker",
        default_zero=True,
    ),
]

spawndelay_64 = [
    plugin(
        timeCP, team=-1, target="CP_64_hurtgen_forest_axisspawn_dummy", time=60
    ),
    plugin(
        timeCP, team=2, target="CP_64_hurtgen_forest_usspawn_dummy", time=360
    ),
]

bleed_64 = [plugin(ticketLoss, ticketLoss1=300, ticketLoss2=15)]

bleed_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]


coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout_hurtgen",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=4.0 / 32.0,
        kit="GW_StG44Assault_hurtgen_Limited",
        soldier="GcWhCamo_splitter",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault_hurtgen",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GW_LMG_MG42_Limited",
        soldier="gw_heer_maschinengewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=5.0 / 32.0,
        kit="GW_RifleAssault_G43_hurtgen_Limited",
        soldier="gw_heer_maschinengewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="GW_AntitankAssault_Limited",
        soldier="GcWhCamo_sumpf",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="UW_Scout_hurtgen",
        soldier="uc_late44_ranger_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="UW_SMGAssault_Limited",
        soldier="uc_fall44_army_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="UW_RifleAssault_hurtgen",
        soldier="uc_fall44_army_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uc_fall44_army_cpl_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="UW_Engineer_Satchel",
        soldier="uc_fall44_9th_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="UW_AntitankAssault_Limited",
        soldier="uc_late44_ranger_cpl",
    ),
    # Push mode
    plugin(aiPush),
    plugin(
        linkCPs,
        target="CP_64_northentrail_bunker_dummy",
        source="CP_64_hurtgen_forest_northerntrail, CP_64_hurtgen_forest_bunker",
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_crossroads_bunker_dummy",
        source="CP_64_hurtgen_forest_crossroads, CP_64_hurtgen_forest_bunker",
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_northerntrail_crossroads_dummy",
        source="CP_64_hurtgen_forest_northerntrail, CP_64_hurtgen_forest_crossroads",
        default_zero=True,
    ),
    # AI spawn points disabling - Axis
    plugin(
        linkCPs,
        target="CP_64_hurtgen_forest_north_axis_dummy",
        source="CP_64_hurtgen_forest_katzenhardt, CP_64_hurtgen_forest_north",
        never_owned_by=2,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_hurtgen_forest_lookout_axis_dummy",
        source="CP_64_hurtgen_forest_katzenhardt, CP_64_hurtgen_forest_lookout",
        never_owned_by=2,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_hurtgen_forest_bridge_axis_dummy",
        source="CP_64_hurtgen_forest_katzenhardt, CP_64_hurtgen_forest_bridge",
        never_owned_by=2,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_northentrail_spawn_dummy",
        source="CP_64_hurtgen_forest_northerntrail, CP_64_hurtgen_forest_bunker",
        never_owned_by=2,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_crossroads_spawn_dummy",
        source="CP_64_hurtgen_forest_crossroads, CP_64_hurtgen_forest_bunker",
        never_owned_by=2,
        default_zero=True,
    ),
    plugin(timeCP, team=-1, target="CP_64_axis_forward_dummy", time=60),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_hurtgen_forest_north_axis_dummy",
        we_own="CP_64_axis_forward_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_hurtgen_forest_lookout_axis_dummy",
        we_own="CP_64_axis_forward_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_hurtgen_forest_bridge_axis_dummy",
        we_own="CP_64_axis_forward_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_northentrail_spawn_dummy",
        we_own="CP_64_hurtgen_forest_north",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_crossroads_spawn_dummy",
        we_own="CP_64_hurtgen_forest_bridge and CP_64_hurtgen_forest_lookout",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_hurtgen_forest_katzenhardt",
        we_own="CP_64_hurtgen_forest_germeter and (CP_64_northentrail_spawn_dummy or CP_64_crossroads_spawn_dummy)",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_hurtgen_forest_germeter",
        we_own="CP_64_hurtgen_forest_katzenhardt and (CP_64_northentrail_spawn_dummy or CP_64_crossroads_spawn_dummy)",
    ),
    # AI spawn point disabling - Allies
    plugin(timeCP, team=2, target="CP_64_us_forward_dummy_north", time=300),
    plugin(timeCP, team=2, target="CP_64_us_forward_dummy_center", time=300),
    plugin(timeCP, team=2, target="CP_64_us_forward_dummy_south", time=300),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_hurtgen_forest_us",
        we_own="CP_64_us_forward_dummy_north",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_us_forward_dummy_north",
        we_own="CP_64_hurtgen_forest_north or (CP_64_hurtgen_forest_lookout and CP_64_hurtgen_forest_bridge) or CP_64_hurtgen_forest_northerntrail or CP_64_hurtgen_forest_bunker or CP_64_hurtgen_forest_crossroads",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_us_forward_dummy_center",
        we_own="CP_64_hurtgen_forest_lookout or (CP_64_hurtgen_forest_north and CP_64_hurtgen_forest_bridge) or CP_64_hurtgen_forest_northerntrail or CP_64_hurtgen_forest_bunker or CP_64_hurtgen_forest_crossroads",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_us_forward_dummy_south",
        we_own="CP_64_hurtgen_forest_bridge or (CP_64_hurtgen_forest_north and CP_64_hurtgen_forest_lookout) or CP_64_hurtgen_forest_northerntrail or CP_64_hurtgen_forest_bunker or CP_64_hurtgen_forest_crossroads",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_hurtgen_forest_north",
        we_own="CP_64_hurtgen_forest_northerntrail and CP_64_hurtgen_forest_lookout",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_hurtgen_forest_lookout",
        we_own="CP_64_hurtgen_forest_bunker and CP_64_hurtgen_forest_north and CP_64_hurtgen_forest_bridge",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_hurtgen_forest_bridge",
        we_own="CP_64_hurtgen_forest_crossroads and CP_64_hurtgen_forest_lookout",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_hurtgen_forest_northerntrail",
        we_own="CP_64_hurtgen_forest_katzenhardt and CP_64_hurtgen_forest_north",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_hurtgen_forest_bunker",
        we_own="CP_64_hurtgen_forest_katzenhardt and CP_64_hurtgen_forest_lookout",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_hurtgen_forest_crossroads",
        we_own="CP_64_hurtgen_forest_germeter",
    ),
    plugin(
        balanceSPs,
        custom_weights=[
            dict(
                cp="CP_64_hurtgen_forest_us,CP_64_us_forward_dummy_north,CP_64_us_forward_dummy_center,CP_64_us_forward_dummy_south",
                weight=250000,
            ),
            dict(
                cp="CP_64_hurtgen_forest_north_axis_dummy,CP_64_hurtgen_forest_lookout_axis_dummy,CP_64_hurtgen_forest_bridge_axis_dummy",
                weight=1000000,
            ),
            dict(
                cp="CP_64_northentrail_spawn_dummy,CP_64_crossroads_spawn_dummy",
                weight=1000000,
            ),
            dict(cp="CP_64_hurtgen_forest_germeter", team=1, weight=100000),
        ],
    ),
    # PCO spawning conditions
    plugin(
        spawnerCondition,
        team=2,
        spawner="us_sherman_north",
        we_own="CP_64_hurtgen_forest_north and CP_64_hurtgen_forest_lookout",
        we_dont_own="CP_64_hurtgen_forest_northerntrail",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="us_sherman_south",
        we_own="CP_64_hurtgen_forest_bridge and CP_64_hurtgen_forest_lookout",
        we_dont_own="CP_64_hurtgen_forest_crossroads",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_hurtgen_forest_secsherman_dummy_sherman",
        we_own="CP_64_hurtgen_forest_crossroads",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="germeter_stugIV_1, germeter_stugIV_2, germeter_mg42tri_2, germeter_stuka_zu_fuss",
        they_own="CP_64_hurtgen_forest_katzenhardt",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="germeter_pak40, germeter_mg42tri_1, germeter_mg42",
        they_own="CP_64_hurtgen_forest_crossroads or CP_64_hurtgen_forest_katzenhardt",
    ),
    # Ticket bleed
    plugin(ticketLoss, ticketLoss1=300, ticketLoss2=10),
]

gpm_cq = {
    64: push_64
    + spawns
    + kits_64
    + linkCPs_64
    + spawndelay_64
    + bleed_64
    + spawnerCondition_64
    + dynamicoob_64
    + nco,
    32: push_32 + spawns + kits_32 + bleed_64 + nco,
    16: kits_16 + bleed_16 + nco,
}
gpm_coop = {
    64: coop_64 + spawns + nco,
}
sp3 = gpm_coop
