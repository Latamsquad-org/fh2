# -*- coding: utf-8 -*-
# pylint: disable=W0232,C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    aiPush,
    balanceSPs,
    destroyObjective,
    disableSPs,
    limitKit,
    NCOrifleData,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    timeCP,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("IA_NCOBeretta38_early", "BA_NCOTommygunS"),
        soldiers=("ia_light_soldier", "ba_nco_soldier"),
    )
]


kit_limits = [
    plugin(
        limitKit,
        team=1,
        kit="IA_Limited_Assault_Beretta38_early",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Assault_TommygunS",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit, team=1, kit="IA_Limited_Support_MG34_K98", slot=3, limit=0.1
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Support_lewishandheld",
        slot=3,
        limit=0.1,
    ),
    plugin(limitKit, team=1, kit="IA_Riflecarabine_tunis", slot=5, limit=0.25),
    plugin(limitKit, team=2, kit="BA_SapperNo1NightST", slot=5, limit=0.1),
]

objectives_64 = [
    plugin(
        destroyObjective,
        controlpoint="CP_64_Hyacinth_Airfield",
        refcount=6,
        template="mc202_objective",
    ),
    plugin(
        destroyObjective,
        controlpoint="CP_64_Hyacinth_Station",
        refcount=4,
        template="carrom13_40",
    ),
    plugin(
        destroyObjective,
        controlpoint="CP_64_Hyacinth_Barce",
        refcount=4,
        template="hqradio1, hqradio2",
    ),
]

spawn_cond_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "CP_64_Hyacinth_Barce_RadioObj1,"
            "CP_64_Hyacinth_Barce_RadioObj2,"
            "CP_64_Hyacinth_Barce_RadioObj3,"
            "CP_64_Hyacinth_Barce_RadioObj4"
        ),
        they_own="CP_64_Hyacinth_Station",
    ),
]

tickets_64 = [
    plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=30),
]

dummy_64 = [
    plugin(
        timeCP,
        target="CP_64_Hyacinth_Forward_Italian_dummy",
        team=-1,
        time=90,
    ),
    plugin(teamSPs),
]

gpm_cq = {
    64: kit_limits
    + objectives_64
    + spawn_cond_64
    + tickets_64
    + dummy_64
    + nco,
    32: kit_limits + nco,
    16: kit_limits + nco,
}

kit_limits_bots = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=6.0 / 32.0,
        kit="IA_ScoutK98Short",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="IA_Limited_Assault_Beretta38_early",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=7.0 / 32.0,
        kit="IA_Riflemanonly_tunis",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="IA_Limited_Support_MG34_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=8.0 / 32.0,
        kit="IA_Beretta38_Police",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=4.0 / 32.0,
        kit="IA_Riflecarabine_tunis",
        soldier="ia_light_soldier",
    ),
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
        limit=8.0 / 32.0,
        kit="BA_Limited_Assault_TommygunS",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=12.0 / 32.0,
        kit="BA_Rifleman_noNadeLauncher",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=5.0 / 32.0,
        kit="BA_Limited_Support_lewishandheld",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=2.0 / 32.0,
        kit="BA_SapperNo1NightSB",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=2.0 / 32.0,
        kit="BA_SapperNo1NightST",
        soldier="ba_heavy_soldier",
    ),
]

disable_spawn_bots = [
    plugin(disableSPs),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Hyacinth_Station",
        we_own="CP_64_Hyacinth_Forward_Italian_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Hyacinth_Airfield",
        we_own="CP_64_Hyacinth_Forward_Italian_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Hyacinth_Barce",
        we_own="CP_64_Hyacinth_Airfield and *",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Hyacinth_Base",
        we_own="(CP_64_Hyacinth_Station or CP_64_Hyacinth_Airfield) and *",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_Hyacinth_LRDG",
        we_own="CP_64_Hyacinth_Station or CP_64_Hyacinth_Airfield",
    ),
    plugin(
        balanceSPs,
        custom_weights=[
            dict(cp="CP_64_Hyacinth_Airfield", team=1, weight=800000),
            dict(cp="CP_64_Hyacinth_Base", team=1, weight=2000000),
        ],
    ),
]

coop_64 = [
    plugin(teamSPs),
    plugin(aiPush),
    plugin(
        timeCP, target="CP_64_Hyacinth_Forward_Italian_dummy", team=-1, time=10
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_Hy_LRDGBase_DE_GB_Truck2_1,"
            "CP_64_Hy_LRDGBase_DE_GB_Truck2_0,"
            "CP_64_Hy_LRDGBase_DE_GB_Truck2,"
            "CP_64_Hyacinth_LRDG_DE_GB_Truck2,"
            "CP_64_Hyacinth_LRDG_DE_GB_Truck2_2"
        ),
        we_dont_own=("CP_64_Hyacinth_Station and CP_64_Hyacinth_Airfield"),
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_Hyacinth_LRDG_DE_GB_CommTruck,"
            "CP_64_Hy_LRDGBase_Chevy,"
            "CP_64_Hyacinth_LRDG_DE_GB_TruckAA,"
            "CP_64_Hyacinth_LRDG_DE_GB_TruckAA_1,"
            "CP_64_Hyacinth_LRDG_DE_GB_TruckAA_4,"
            "CP_64_Hy_LRDGBase_Transport,"
            "CP_64_Hyacinth_LRDG_DE_GB_Scout,"
            "CP_64_Hyacinth_LRDG_DE_GB_Scout_0"
        ),
        we_dont_own=("CP_64_Hyacinth_Station or " "CP_64_Hyacinth_Airfield"),
    ),
]

gpm_coop = {
    16: nco,
    64: kit_limits_bots + disable_spawn_bots + coop_64 + nco,

}

sp1 = gpm_coop
sp3 = gpm_coop
