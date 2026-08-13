# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    NCOrifleData,
    limitKit,
    linkCPs,
    spawnerCondition,
    ticketLoss,
    DoubleBleed,
)

bleed_16 = [
    plugin(DoubleBleed),
]
bleed_64 = [
    plugin(DoubleBleed),
]

NCO_32 = [
    plugin(
        NCOrifleData,
        kits=("IA_NCOBeretta38", "BA_NCOTommygunS"),
        soldiers=("ia_light_soldier", "ba_nco_soldier"),
    ),
]

NCO = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("ga_nco_soldier", "ba_nco_soldier"),
    )
]

kitlimits = [
    plugin(
        limitKit,
        team=1,
        kit="GA_Limited_Assault_MP40_K98",
        slot=1,
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Assault_TommygunD_No4",
        slot=1,
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GA_Limited_Support_MG34_K98",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Support_Bren_No4",
        slot=3,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        kit="ga_ATPzB39_Limited",
        slot=5,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_ATBoys_Limited",
        slot=5,
        limit=0.1,
    ),
]

kit_limits_32 = [
    plugin(
        limitKit,
        team=1,
        kit="IA_Limited_Assault_Beretta38_K98",
        slot=1,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Assault_TommygunD_No4",
        slot=1,
        limit=0.2,
    ),
    plugin(limitKit, team=1, kit="IA_Limited_Support_MG34_K98", slot=3, limit=0.12),
    plugin(limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.12),
    plugin(limitKit, team=1, kit="IA_AntiTank_carcano", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="BA_ATBoys_Limited", slot=5, limit=0.1),
]

tickets_64 = [
    plugin(
        ticketLoss,
        ticketLoss1=20,
        ticketLoss2=20,
    ),
]
tickets_32 = [
    plugin(
        ticketLoss,
        ticketLoss1=30,
        ticketLoss2=30,
    ),
]

spawners_64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Alamein_Alamein_h2d_fight",
        we_dont_own="CP_64_Alamein_Miteiriya",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Alamein_Alamein_DE_GB_LightbomberPlane",
        we_dont_own="CP_64_Alamein_Kidney",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Alamein_AxisHQ_fighter2",
        we_dont_own="CP_64_Alamein_Miteiriya",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Alamein_AxisHQ_DE_GB_LightbomberPlane_0",
        we_dont_own="CP_64_Alamein_Kidney",
    ),
]

links_32 = [
    plugin(
        linkCPs,
        target="Reinforcements",
        source=["cp_32_Alamein_Miteiriya", "cp_32_Alamein_trenches_south"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="Reinforcements",
        source=["cp_32_Alamein_Miteiriya", "cp_32_Alamein_roadblock_north"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="Reinforcements",
        source=[
            "cp_32_Alamein_trenches_south",
            "cp_32_Alamein_roadblock_north",
        ],
        invert=True,
    ),
]

spawnerCondition_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_32_Alamein_AxisHQ_Semo_2",
        we_own="Reinforcements",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_Alamein_AlliedHQ_Valentine",
        we_own="Reinforcements",
    ),
]

gpm_cq = {
    64: kitlimits + tickets_64 + spawners_64 + NCO + bleed_64,
    32: kit_limits_32 + tickets_32 + links_32 + spawnerCondition_32 + NCO_32,
    16: kitlimits + NCO + bleed_16,
}

gpm_coop = {
    64: tickets_64 + spawners_64 + NCO,
    32: tickets_32 + links_32 + spawnerCondition_32 + NCO_32,
    16: NCO,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
