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
    neighPush,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    timeCP,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO", "cw_NCO"),
        soldiers=("gs_waffen_unteroffizier", "cw_nco_soldier"),
    )
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_A_sector_dummy": {
                "axis": {
                    "creates": ["CombatArea_axis2"],
                    "destroys": ["CombatArea_allies1"],
                },
            },
        },
        inactive_at_start=["CombatArea_axis2"],
        delay_axis=0,
        delay_allies=120,
    )
]

spawndelay_32 = [
    plugin(
        timeCP,
        team=-1,
        target="CP_32_lamb_st_lambert_south_forwardspawn",
        time=60,
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

kitlimits = [
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=1, kit="CW_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_MG42_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="CW_LMG_Limited", limit=0.1),
    plugin(
        limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1
    ),
    plugin(limitKit, team=2, slot=5, kit="CW_Antitank_Limited", limit=0.1),
]

reinforcements_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_st_lambert_kampfgruppe_fuchs_0_p4_0",
        we_dont_own="CP_64_st_lambert_st_lambert_south and CP_64_falaise_pocket_stlambert and CP_64_st_lambert_st_lambert_north",
    ),
]

reinforcements_32_allies = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_lamb_canadians_wasp",
        we_dont_own="CP_32_lamb_st_lambert_south and CP_32_lamb_stlambert and CP_32_lamb_st_lambert_north",
    ),
]

reinforcements_32_axis = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_lamb_st_lambert_church_hano2",
        we_dont_own="CP_32_lamb_st_lambert_south and CP_32_lamb_stlambert and CP_32_lamb_st_lambert_north",
    ),
]

push_64 = [
    plugin(
        neighPush,
        sources="CP_64_st_lambert_kampfgruppe_fuchs_0",
        targets="CP_64_st_lambert_destroyed_battery,CP_64_st_lambert_st_lambert_church",
    ),
    plugin(
        neighPush,
        sources="CP_64_st_lambert_destroyed_battery",
        targets="CP_64_st_lambert_st_lambert_church",
    ),
    plugin(
        linkCPs,
        target="CP_64_A_sector_dummy",
        source="CP_64_st_lambert_destroyed_battery, CP_64_st_lambert_st_lambert_church",
    ),
    plugin(
        neighPush,
        sources="CP_64_A_sector_dummy",
        targets="CP_64_st_lambert_destroyed_battery,CP_64_st_lambert_st_lambert_church,CP_64_st_lambert_st_lambert_south, CP_64_falaise_pocket_stlambert, CP_64_st_lambert_st_lambert_north",
    ),
    plugin(
        neighPush,
        sources="CP_64_st_lambert_st_lambert_south",
        targets="CP_64_falaise_pocket_stlambert",
    ),
    plugin(
        neighPush,
        sources="CP_64_falaise_pocket_stlambert",
        targets="CP_64_st_lambert_st_lambert_north, CP_64_st_lambert_mortar_battery",
    ),
    plugin(
        neighPush,
        sources="CP_64_st_lambert_st_lambert_north",
        targets="CP_64_st_lambert_mortar_battery",
    ),
]

push_16 = [
    plugin(
        push,
        source="CP_16_st_lambert_allies",
        target="CP_16_st_lambert_north",
        attacker=2,
    ),
    plugin(push, source="CP_16_st_lambert_north", target="CP_16_st_lambert"),
    plugin(push, source="CP_16_st_lambert", target="CP_16_st_lambert_south"),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=100)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=300, ticketLoss2=20)]

coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout",
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
        limit=10.0 / 32.0,
        kit="GW_RifleAssault_noNadeLauncher",
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
        limit=3.0 / 32.0,
        kit="GW_Engineer_Satchel",
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
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="cw_Scout",
        soldier="cw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="cw_SMGAssault_Limited",
        soldier="cw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="cw_RifleAssault",
        soldier="cw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="cw_LMG_Limited",
        soldier="cw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=3.0 / 32.0,
        kit="cw_Engineer_Satchel",
        soldier="cw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=5.0 / 32.0,
        kit="cw_Antitank_Limited",
        soldier="cw_heavy_soldier",
    ),
    # Push mode
    plugin(aiPush),
    plugin(
        linkCPs,
        target="CP_64_A_sector_dummy",
        source="CP_64_st_lambert_destroyed_battery, CP_64_st_lambert_st_lambert_church",
        default_zero=True,
    ),
    plugin(ticketLoss, ticketLoss1=12, ticketLoss2=100),
    # Vehicle spawning conditions
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_st_lambert_kampfgruppe_fuchs_0_sd_0",
        they_own="CP_64_st_lambert_destroyed_battery or CP_64_st_lambert_st_lambert_church",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_st_lambert_mortar_battery_mortar",
        we_dont_own="CP_64_falaise_pocket_stlambert or CP_64_st_lambert_st_lambert_north",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_German_forward_dummy_South",
        we_own="CP_64_st_lambert_destroyed_battery",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_German_forward_dummy_North",
        we_own="CP_64_st_lambert_st_lambert_church",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_st_lambert_kampfgruppe_fuchs_0",
        we_own="CP_64_st_lambert_st_lambert_church or CP_64_st_lambert_destroyed_battery",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_A_sector_dummy",
        we_own="CP_64_st_lambert_st_lambert_south",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_st_lambert_st_lambert_north",
        we_own="CP_64_st_lambert_st_lambert_south and *",
    ),
    plugin(
        balanceSPs,
        custom_weights=[
            dict(
                cp="CP_64_st_lambert_kampfgruppe_fuchs_0, CP_64_German_forward_dummy_South, CP_64_German_forward_dummy_North",
                weight=500000,
            ),
            dict(cp="CP_64_A_sector_dummy", weight=1000000),
        ],
    ),
]


disable_AI = [
    plugin(disableSPs),  # Auto-fill
]

gpm_cq = {
    64: (
        nco
        + spawns
        + tickets_64
        + kitlimits
        + push_64
        + reinforcements_64
        + dynamicoob_64
    ),
    32: (nco + spawns + kitlimits + tickets_32 + reinforcements_32_allies + reinforcements_32_axis + spawndelay_32),
    16: tickets_16 + kitlimits + push_16 + spawns + nco,
}


gpm_coop = {
    64: coop_64 + spawns + nco,
    32: nco + spawns + tickets_32,
    16: tickets_16 + push_16 + spawns + nco + disable_AI,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
