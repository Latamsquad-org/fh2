# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    teamSPs,
    push,
    limitKit,
    disableSPs,
    timeCP,
    spawnerCondition,
    linkCPs,
    aiPush,
    dynamicOOB,
    ticketLoss,
    timeCP,
    SectorTickets,
    NCOrifleData,
)

spawns = [
    plugin(teamSPs),
]
nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_OST", "BW_NCO"),
        soldiers=("gw_osttruppen_unteroffizier", "bw_nco_soldier"),
    )
]

nco_8 = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_G41", "BW_NCO_StenMk5"),
        soldiers=("gw_heer_unteroffizier", "bj_airborne_sgt_night"),
    )
]

push_64 = [
    plugin(
        push,
        source="cq_64_gold_hable_de_heurlot",
        target="cq_64_gold_beach_head",
        attacker=2,
        force=True,
    ),
    plugin(
        push,
        source="cq_64_gold_swamps",
        target="cq_64_gold_beach_head",
        attacker=2,
        force=True,
    ),
    plugin(
        push,
        source=[
            "cq_64_gold_beach_head",
            "cq_64_gold_hable_de_heurlot",
            "cq_64_gold_swamps",
        ],
        target="cq_64_gold_cross_road",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source=[
            "cq_64_gold_beach_head",
            "cq_64_gold_hable_de_heurlot",
            "cq_64_gold_swamps",
        ],
        target="cq_64_gold_artillery_observation_post",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cq_64_gold_cross_road",
        target="cq_64_gold_mont_fleury",
        attacker=2,
        force=True,
    ),
    plugin(
        push,
        source="cq_64_gold_artillery_observation_post",
        target="cq_64_gold_mont_fleury",
        attacker=2,
        force=True,
    ),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="cq_64_gold_german_spawns",
        source="cq_64_gold_secret_3",
    ),
]

push_32 = [
    plugin(
        push,
        source="cq_32_gold_british_base",
        target="cq_32_gold_hable_de_heurlot, cq_32_gold_beach_head",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cq_32_gold_hable_de_heurlot, cq_32_gold_beach_head",
        target="CP_32_gold_sector1",
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_32_gold_sector1",
        target="cq_32_gold_artillery_observation_post, cq_32_gold_cross_road",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
        delay=45
    ),
    plugin(
        push,
        source="cq_32_gold_artillery_observation_post, cq_32_gold_cross_road",
        target="CP_32_gold_sector2",
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_32_gold_sector2",
        target="cq_32_gold_mont_fleury",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
        delay=45
    ),
]

linkCPs_32 = [
    plugin(linkCPs, target="CP_32_gold_sector1", source="cq_32_gold_hable_de_heurlot, cq_32_gold_beach_head"),
    plugin(linkCPs, target="CP_32_gold_sector2", source="cq_32_gold_artillery_observation_post, cq_32_gold_cross_road"),
    plugin(linkCPs, target="CP_32_gold_german_spawns", source="cq_32_gold_secret_3",
    ),
]

dynamicoob_32 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_32_gold_sector1": {
                "allies": {
                    "creates": ["CombatArea_conq_32_allies_sector_2"],
                    "destroys": ["CombatArea_conq_32_axis_sector_1"],
                },
            },
            "CP_32_gold_sector2": {
                "allies": {
                    "creates": ["CombatArea_conq_32_allies_sector_3"],
                    "destroys": ["CombatArea_conq_32_axis_sector_2"],
                },
            },
        },
        inactive_at_start=["CombatArea_conq_32_allies_sector_2", "CombatArea_conq_32_allies_sector_3"],
        delay_axis=60,
        delay_allies=45,
    )
]

push_16 = [
    plugin(
        push,
        source="cq_16_gold_british_base",
        target="cq_16_gold_swamps",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cq_16_gold_swamps",
        target="CP_16_gold_sector1",
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_16_gold_sector1",
        target="cq_16_gold_artillery_observation_post",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="cq_16_gold_artillery_observation_post",
        target="CP_16_gold_sector2",
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_16_gold_sector2",
        target="cq_16_gold_mont_fleury",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
]

linkCPs_16 = [
    plugin(linkCPs, target="CP_16_gold_sector1", source="cq_16_gold_swamps"),
    plugin(
        linkCPs,
        target="CP_16_gold_sector2",
        source="cq_16_gold_artillery_observation_post",
    ),
]

dynamicoob_16 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_16_gold_sector1": {
                "allies": {
                    "creates": ["CombatArea_16_allies2"],
                    "destroys": ["CombatArea_16_axis1"],
                },
            },
            "CP_16_gold_sector2": {
                "allies": {
                    "creates": ["CombatArea_16_allies3"],
                    "destroys": ["CombatArea_16_axis2"],
                },
            },
        },
        inactive_at_start=["CombatArea_16_allies2", "CombatArea_16_allies3"],
        delay_axis=60,
        delay_allies=0,
    )
]

time_8 = [
    plugin(
        timeCP,
        team=1,
        target="cq_8_gold_axis_secret",
        time=90,
    ),
    plugin(
        timeCP,
        team=2,
        target="cq_8_gold_allied_secret",
        time=90,
    ),
    plugin(
        timeCP,
        team=0,
        target="cq_8_gold_allied_start",
        time=90,
    ),
]

kitlimits = [
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG120(r)_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.15),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Mosin_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.1),
]

kitlimits_8 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_mk5", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG26_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Colt_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=4, kit="GS_RifleAssault_ramelle", limit=0.1),
    plugin(limitKit, team=2, slot=4, kit="BW_CarbineAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BW_RifleAssault_no69_Limited", limit=0.1),
]

spawnerConditions_64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="cq_64_gold_british_base_bedford, cq_64_gold_british_base_bedford_ammo, cq_64_gold_british_base_avre, cq_64_gold_british_base_tanker7, cq_64_gold_british_base_tanker8, cq_64_gold_british_base_pickup_mortar",
        we_own="cq_64_gold_swamps, cq_64_gold_beach_head, cq_64_gold_hable_de_heurlot",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="cq_64_gold_british_base_crocodile, cq_64_gold_british_base_centuar",
        we_dont_own="cq_64_gold_cross_road, cq_64_gold_artillery_observation_post",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="cq_64_gold_mont_fleury_marder, cq_64_gold_mont_fleury_tanker, cq_64_gold_mont_fleury_mortar",
        we_dont_own="cq_64_gold_swamps, cq_64_gold_beach_head, cq_64_gold_hable_de_heurlot",
    ),

    plugin(
        spawnerCondition,
        team=1,
        spawner="cq_64_gold_cross_road_marder, cq_64_gold_cross_road_tanker",
        we_dont_own="cq_64_gold_swamps, cq_64_gold_hable_de_heurlot",
    ),
]

spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="cq_32_gold_mont_fleury_marder, cq_32_gold_mont_fleury_tanker, cq_32_gold_mont_fleury_mortar",
        we_dont_own="CP_32_gold_sector1",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="cq_32_gold_british_base_uc_bren",
        we_dont_own="CP_32_gold_sector1",
    ),
]

tickets_32 = [plugin(ticketLoss, ticketLoss1=160, ticketLoss2=15)]

spawnerConditions_16 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_16_gold_german_spawns_marder, CP_16_gold_german_spawns_tanker",
        they_own="CP_16_gold_sector1",
        we_own="CP_16_gold_sector2",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="cq_16_gold_mont_fleury_arty, cq_16_gold_mont_fleury_ammo",
        we_dont_own="CP_16_gold_sector1",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="cq_16_gold_swamps_avre",
        we_dont_own="CP_16_gold_sector2",
    ),
]

tickets_16 = [plugin(ticketLoss, ticketLoss1=160, ticketLoss2=10)]

tickets_8 = [plugin(ticketLoss, ticketLoss1=18, ticketLoss2=18)]

Sectortickets_16 = [
    plugin(
        SectorTickets,
        sector_tickets={
            "CP_16_gold_sector1": {"allies": 150},
            "CP_16_gold_sector2": {"allies": 150},
        },
    )
]

coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout_mid",
        soldier="gw_heer_unteroffizier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=8.0 / 32.0,
        kit="GW_RifleAssault_noNadeLauncher",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault_Mosin",
        soldier="gw_osttruppen_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=4.0 / 32.0,
        kit="GW_LMG_MG120(r)_Limited",
        soldier="gw_osttruppen_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="gw_heer_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=4.0 / 32.0,
        kit="GW_AntitankAssault_Mosin_Limited",
        soldier="gw_osttruppen_panzerabwehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="BW_Scout",
        soldier="bw_light_marines",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="BW_SMGAssault_Limited",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="BW_RifleAssault",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="BW_LMG_Limited",
        soldier="bw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="BW_Engineer_Satchel",
        soldier="bw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="BW_Antitank_Limited",
        soldier="bw_heavy_marines",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=2,
        cp="cq_64_gold_british_base",
        we_own="cq_64_gold_swamps and cq_64_gold_beach_head",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="cq_64_gold_cross_road",
        we_own="cq_64_gold_beach_head",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="cq_64_gold_mont_fleury",
        we_own="cq_64_gold_beach_head",
    ),
     plugin(
        disableSPs,
        team=1,
        cp="cq_64_gold_artillery_observation_post",
        we_own="cq_64_gold_beach_head",
    ),   
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
]


disable_AI_32 = [
    # AI spawn points disabling - Axis and Allies
    plugin(
        disableSPs,
        team=1,
        cp="cq_32_gold_cross_road",
        we_own="cq_32_gold_beach_head",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="cq_32_gold_mont_fleury",
        we_own="cq_32_gold_beach_head",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="cq_32_gold_artillery_observation_post",
        we_own="cq_32_gold_beach_head",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="cq_32_gold_british_base",
        we_own="cq_32_gold_hable_de_heurlot and cq_32_gold_beach_head",
    ),
]


gpm_cq = {
    128: spawns + time_8 + kitlimits_8 + tickets_8 + nco_8,
    64: spawns + push_64 + linkCPs_64 + kitlimits + spawnerConditions_64  + nco,
    32: spawns + push_32 + linkCPs_32 + dynamicoob_32 + kitlimits + spawnerConditions_32 + tickets_32 + nco,
    16: spawns + push_16 + linkCPs_16 + dynamicoob_16 + kitlimits + spawnerConditions_16 + tickets_16 + Sectortickets_16 + nco,
}

gpm_coop = {
    64: coop_64 + push_64 + linkCPs_64 + spawnerConditions_64 + nco,
    32: spawns + disable_AI_32 + push_32 + linkCPs_32 + spawnerConditions_32 + tickets_32 + nco,
    16: spawns + push_16 + linkCPs_16 + spawnerConditions_16 + tickets_16 + Sectortickets_16 + nco,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
