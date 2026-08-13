# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    NCOrifleData,
    aiPush,
    delaySpawners,
    disableSPs,
    limitKit,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    timeCP,
    DoubleBleed,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("ga_nco_soldier", "ba_nco_soldier"),
    )
]

nco_16 = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("ga_nco_soldier", "fa_dfl_legioneer_nco_soldier"),
    )
]

kit_limits = [
    plugin(limitKit, team=1, kit="GA_Limited_Assault_MP40_K98", slot=1, limit=0.25),
    plugin(limitKit, team=2, kit="BA_Limited_Assault_TommygunD_No4", slot=1, limit=0.25),
    plugin(limitKit, team=1, kit="GA_Limited_Support_MG34_K98", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.15),
    plugin(limitKit, team=1, kit="ga_ATPzB39_Limited", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="BA_ATBoys_Limited", slot=5, limit=0.1),
]

kit_limits_16 = [
    plugin(limitKit, team=1, kit="GA_Limited_Assault_MP40_K98", slot=1, limit=0.25),
    plugin(limitKit, team=2, kit="BA_Limited_Assault_TommygunD_No4", slot=1, limit=0.25),
    plugin(limitKit, team=1, kit="GA_Limited_Support_MG34_K98", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="FA_active_LMG", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="GA_RiflemanK98", slot=4, limit=0.1),
    plugin(limitKit, team=2, kit="FA_active_RiflemanGL", slot=4, limit=0.1),
    plugin(limitKit, team=1, kit="ga_ATPzB39_Limited", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="BA_ATBoys_Limited", slot=5, limit=0.1),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=12, ticketLoss2=12)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

bleed_64 = [
    plugin(
        DoubleBleed,
    ),
]
bleed_32 = [
    plugin(
        DoubleBleed,
    ),
]

coop_aipush = [plugin(aiPush)]
coop_16_kit = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GA_ScoutK98Short",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=7.0 / 32.0,
        kit="GA_Limited_Assault_MP40_K98",
        soldier="ga_masked_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=12.0 / 32.0,
        kit="GA_RiflemanK98_early",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GA_Limited_Support_MG34_K98",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GA_RiflemanK98",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=0.0 / 32.0,
        kit="ga_ATPzB39_Limited",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="FA_standard_Scout",
        soldier="fa_dfl_bm2_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=7.0 / 32.0,
        kit="BA_Limited_Assault_TommygunD_No4",
        soldier="fa_dfl_legioneer_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=12.0 / 32.0,
        kit="FA_standard_Rifleman",
        soldier="fa_dfl_legioneer_light_alt2_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="FA_active_LMG",
        soldier="fa_dfl_22cna_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="FA_active_RiflemanGL",
        soldier="fa_dfl_fm_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=0.0 / 32.0,
        kit="BA_ATBoys_Limited",
        soldier="fa_dfl_bp_heavy_soldier",
    ),
]

coop_teamsp = [plugin(teamSPs)]
coop_16_disable = [
    plugin(
        disableSPs,
        team=1,
        cp="CP_16_Gazala_GermanAdvance",
        we_own="CP_16_Gazala_BirHakeim_1",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_16_Gazala_BirHakeim_1",
        we_own="CP_16_Gazala_Trenches and CP_16_Gazala_BirHakeim_2",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_16_Gazala_BritishAdvance",
        we_own="CP_16_Gazala_BirHakeim_1",
    ),
]
coop_16_sc = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_16_Gazala_BirHakeim_2_MG",
        we_dont_own="CP_16_Gazala_BirHakeim_1",
    ),
]
coop_16_ticket = [plugin(ticketLoss, ticketLoss1=8, ticketLoss2=50)]


coop_64_kit = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GA_ScoutK98Short",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=4.0 / 32.0,
        kit="GA_Limited_Assault_MP40_K98",
        soldier="ga_masked_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GA_RiflemanK98",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GA_Limited_Support_MG34_K98",
        soldier="ga_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=6.0 / 32.0,
        kit="ga_EngineerK98Short",
        soldier="ga_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="ga_ATPzB39_Limited",
        soldier="ga_heavy_soldier",
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
        limit=4.0 / 32.0,
        kit="BA_Limited_Assault_TommygunD_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="BA_RiflemanEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=5.0 / 32.0,
        kit="BA_Limited_Support_Bren_No4",
        soldier="ba_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=6.0 / 32.0,
        kit="BA_EngineerEarly",
        soldier="ba_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=5.0 / 32.0,
        kit="BA_ATBoys_Limited",
        soldier="ba_heavy_soldier",
    ),
]
coop_64_disable = [
    plugin(disableSPs),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_Gazala_SidiMuftan",
        we_own="CP_64_Gazala_Allied_Forward_dummy",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_Gazala_150thBox",
        we_own="CP_64_Gazala_Allied_Forward_dummy",
    ),
]
coop_64_timecp = [
    plugin(timeCP, target="CP_64_Gazala_Allied_Forward_dummy", team=-1, time=120),
]

coop_64_delay = [
    plugin(
        delaySpawners,
        spawners=(
            "CP_64_Gazala_Knightsbridge_DE_GB_MediumTank2," "CP_64_Gazala_Acroma_DE_GB_LightTank_0"
        ),
    ),
]


gpm_cq = {
    64: tickets_64 + kit_limits + nco + bleed_64,
    32: tickets_32 + kit_limits + nco + bleed_32,
    16: tickets_16 + kit_limits_16 + nco_16,
}

gpm_coop = {
    64: coop_aipush
    + coop_teamsp
    + coop_64_kit
    + coop_64_disable
    + coop_64_timecp
    + coop_64_delay
    + tickets_64
    + nco,
    32: tickets_32 + nco + bleed_32,
    16: tickets_16 + nco_16,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
