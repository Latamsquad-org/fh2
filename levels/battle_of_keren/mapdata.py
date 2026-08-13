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
    timeCP,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("IA_NCOBeretta38", "BA_NCOTommygunS"),
        soldiers=("ia_light_soldier", "ba_nco_soldier"),
    )
]


kit_limits = [
    plugin(limitKit, team=1, kit="IA_Limited_Assault_Beretta38_K98", slot=1, limit=0.2),
    plugin(limitKit, team=2, kit="BA_Limited_Assault_TommygunD_No4", slot=1, limit=0.2),
    plugin(limitKit, team=1, kit="IA_Limited_Support_MG34_K98", slot=3, limit=0.12),
    plugin(limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.12),
    plugin(limitKit, team=1, kit="IA_AntiTank_carcano", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="BA_ATBoys_Limited", slot=5, limit=0.1),
]

kit_limits_32 = [
    plugin(limitKit, team=1, kit="IA_Limited_Assault_Beretta38_K98", slot=1, limit=0.2),
    plugin(limitKit, team=2, kit="BA_Limited_Assault_TommygunD_No4", slot=1, limit=0.2),
    plugin(limitKit, team=1, kit="IA_Limited_Support_MG34_K98", slot=3, limit=0.12),
    plugin(limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.12),
    plugin(limitKit, team=2, kit="BA_Grenadier_Limited", slot=4, limit=0.2),
    plugin(limitKit, team=1, kit="IA_AntiTank_carcano", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="BA_ATBoys_Limited", slot=5, limit=0.1),
]

kit_limits_16  = [
    plugin(limitKit, team=1, kit="IA_Limited_Assault_Beretta38_K98", slot=1, limit=0.1),
    plugin(limitKit, team=2, kit="BA_Limited_Assault_TommygunD_No4", slot=1, limit=0.1),
    plugin(limitKit, team=1, kit="IA_Limited_Support_MG34_K98", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="IA_Engineer_Satchel_Limited", slot=4, limit=0.1),
    plugin(limitKit, team=2, kit="AA_Engineer_Satchel_Limited", slot=4, limit=0.1),
    plugin(limitKit, team=1, kit="IA_AntiTank_carcano", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="AA_ATNo73Grenade_Limited", slot=5, limit=0.1),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

push_64 = [
    plugin(
        linkCPs,
        target="sector1_dummy",
        source="conq_64_agordat, conq_64_agordat_trainstation",
    ),
    plugin(
        push,
        source="conq_64_agordat, conq_64_agordat_trainstation",
        target="sector1_dummy",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="sector1_dummy",
        target="conq_64_ascidera_valley, conq_64_sanchil, conq_64_sammana",
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="conq_64_ascidera_valley",
        target="conq_64_Fort_Dologorodoc",
        attacker=2,
    ),
    plugin(
        push,
        source="conq_64_Fort_Dologorodoc",
        target="conq_64_keren, conq_64_trainstation",
        attacker=2,
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "sector1_dummy": {
                "allies": {
                    "creates": ["CombatArea_allies2"],
                    "destroys": ["CombatArea_axis1"],
                },
            },
        },
        inactive_at_start=["CombatArea_allies2"],
        delay_axis=120,
        delay_allies=0,
    )
]

ticket_loss = [
    plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15),
]


pcospawners64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "conq_64_british_mainbase_0_17,"
            " conq_64_british_mainbase_1_1,conq_64_british_mainbase_tank,"
            " conq_64_british_mainbase_tank_0,"
            " conq_64_british_mainbase_tank_1"
        ),
        we_dont_own="sector1_dummy",
    ),

    plugin(
        spawnerCondition,
        team=1,
        spawner=
            "conq_64_keren_at"
        ,
        they_own="sector1_dummy",
    ),
]

pcospawners32 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "conq_32_ascidera_mortar"
        ),
        we_dont_own="conq_32_camaron or conq_32_sanchil",
    ),
]

gpm_cq = {
    16: kit_limits_16 + nco,
    32: kit_limits + pcospawners32 + spawns + nco,
    64: kit_limits
    + push_64
    + ticket_loss
    + dynamicoob_64
    + pcospawners64
    + nco,
}

coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=3.0 / 32.0,
        kit="IA_ScoutK98Short",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="IA_Limited_Assault_Beretta38_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="IA_RiflemanK98",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="IA_Limited_Support_MG34_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="IA_EngineerK98Short",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="IA_AntiTank_carcano",
        soldier="ia_heavy_soldier",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="BA_ScoutEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="BA_Limited_Assault_TommygunD_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=11.0 / 32.0,
        kit="BA_RiflemanEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="BA_Limited_Support_Bren_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="BA_EngineerEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=2.0 / 32.0,
        kit="BA_ATBoys_Limited",
        soldier="ba_heavy_soldier",
    ),
    plugin(disableSPs),
    plugin(
        disableSPs,
        team=1,
        cp="conq_64_agordat",
        we_own="axis_forward_spawn_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="conq_64_agordat_trainstation",
        we_own="axis_forward_spawn_dummy",
    ),
    plugin(timeCP, target="axis_forward_spawn_dummy", team=-1, time=30),
    plugin(
        disableSPs,
        team=1,
        cp="conq_64_keren",
        we_own="conq_64_trainstation and (conq_64_sanchil or conq_64_sammana)",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="conq_64_trainstation",
        we_own=(
            "conq_64_trainstation and "
            "conq_64_Fort_Dologorodoc and "
            "(conq_64_sanchil or conq_64_sammana)"
        ),
    ),
    plugin(
        disableSPs,
        team=2,
        cp="conq_64_british_mainbase",
        we_own="conq_64_agordat or conq_64_agordat_trainstation",
    ),
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
    plugin(
        linkCPs,
        target="sector1_dummy",
        source="conq_64_agordat,conq_64_agordat_trainstation",
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="sector2_dummy",
        source=(
            "conq_64_camaron,"
            "conq_64_sammana,"
            "conq_64_sanchil,"
            "conq_64_ascidera_valley,"
            "conq_64_Fort_Dologorodoc"
        ),
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="sector3_dummy",
        source="conq_64_keren,conq_64_trainstation",
        default_zero=True,
    ),
    # PCO spawning conditions - Allies
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "conq_64_british_mainbase_car,"
            "conq_64_british_mainbase_truck,"
            "conq_64_british_mainbase_apc,"
            "conq_64_british_mainbase_1_0,"
            "conq_64_british_mainbase_2_0,"
            "conq_64_british_mainbase_1_2"
        ),
        we_dont_own="conq_64_agordat or conq_64_agordat_trainstation",
    ),
    plugin(ticketLoss, ticketLoss1=500, ticketLoss2=10),
]


coop_32 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="IA_ScoutK98Short",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="IA_Limited_Assault_Beretta38_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=12.0 / 32.0,
        kit="IA_RiflemanK98",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="IA_Limited_Support_MG34_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="IA_Engineer_Satchel",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=1.0 / 32.0,
        kit="IA_AntiTank_carcano",
        soldier="ia_heavy_soldier",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="BA_ScoutEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=7.0 / 32.0,
        kit="BA_Limited_Assault_TommygunD_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=14.0 / 32.0,
        kit="BA_Rifleman_noNadeLauncher",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="BA_Limited_Support_Bren_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=2.0 / 32.0,
        kit="BA_Grenadier_Limited",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=0.0 / 32.0,
        kit="BA_ATBoys_Limited",
        soldier="ba_heavy_soldier",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=2,
        cp="conq_32_ascidera",
        we_own="conq_32_sammana or conq_32_sanchil or conq_32_camaron",
    ),
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
]
gpm_coop = {
    16: nco,
    32: coop_32 + spawns + nco,
    64: coop_64 + nco,    
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
