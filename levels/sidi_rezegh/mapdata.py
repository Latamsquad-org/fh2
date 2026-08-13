# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    limitKit,
    linkCPs,
    NCOrifleData,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    DoubleBleed,
    disableSPs,
    dynamicOOB,
)

links_32 = [
    plugin(
        linkCPs,
        target="CP_32_SR_Reinforcements",
        source=[
            "CP_32_SR_19FlakRegimentHKL",
            "CP_32_SR_19FlakRegimentGefechtsstand",
        ],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_32_SR_Reinforcements",
        source=[
            "CP_32_SR_19FlakRegimentGefechtsstand",
            "CP_32_SR_19FlakRegimentDepot",
        ],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_32_SR_Reinforcements",
        source=[
            "CP_32_SR_19FlakRegimentDepot",
            "CP_32_SR_19FlakRegimentHKL",
        ],
        invert=True,
    ),
]

spawnerCondition_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "CP_32_SR_SidiRezeghMosque_ax_bleed_tank_a," "CP_32_SR_SidiRezeghMosque_ax_bleed_tank_b"
        ),
        we_own="CP_32_SR_Reinforcements",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_32_SR_18thBattalionOutpost_al_bleed_tank_a,"
            "CP_32_SR_18thBattalionOutpost_al_bleed_tank_b"
        ),
        we_own="CP_32_SR_Reinforcements",
    ),
]

nco = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40_early", "BA_NCOTommygunS"),
        soldiers=("ga_early_nco_soldier", "ba_nco_soldier"),
    )
]

tickets_64 = [
    plugin(ticketLoss, ticketLoss1=25, ticketLoss2=25),
]

tickets_32 = [
    plugin(ticketLoss, ticketLoss1=25, ticketLoss2=25),
]

tickets_16 = [
    plugin(ticketLoss, ticketLoss1=100, ticketLoss2=10),
]

tickets_8 = [
    plugin(ticketLoss, ticketLoss1=18, ticketLoss2=18),
]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_SR_AlliedAttack1_dummy",
        source="CP_64_SR_19FlakRegimentHKL",
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_SR_AlliedAttack2_dummy",
        source="CP_64_SR_19FlakRegimentGefechtsstand",
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_SR_AlliedAttack3_dummy",
        source="CP_64_SR_19FlakRegimentDepot",
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_SR_AlliedDefense",
        source=[
            "CP_64_SR_19FlakRegimentGefechtsstand",
            "CP_64_SR_19FlakRegimentDepot",
            "CP_64_SR_19FlakRegimentHKL",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_SR_AxisReinforcements_dummy",
        source=[
            "CP_64_SR_19FlakRegimentGefechtsstand",
            "CP_64_SR_19FlakRegimentHKL",
            "CP_64_SR_19FlakRegimentDepot",
        ],
        invert=True,
    ),
]

push_16 = [
    plugin(
        push,
        source="CP_16_SR_Gatehouse",
        target="CP_16_SR_FieldKitchen",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_16_SR_FieldKitchen",
        target="CP_16_SR_PaKPosition, CP_16_SR_Barracks",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_16_SR_Barracks, CP_16_SR_PaKPosition",
        target="CP_16_SR_Headquarters",
        attacker=2,
        delay=30,
    ),
]


spawns = [
    plugin(teamSPs),  # Auto-fill
]

cond_16_cq = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_16_SR_Headquarters_pzjgrI",
        we_dont_own="CP_16_SR_Barracks, CP_16_SR_PaKPosition",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_16_SR_Gatehouse_Stuart",
        we_dont_own="CP_16_SR_Barracks, CP_16_SR_PaKPosition",
    ),
]
cond_16_coop = [
    # plugin(
    #     spawnerCondition,
    #     team=1,
    #     spawner="CP_16_SR_Headquarters_pzjgrI",
    #     we_dont_own="CP_16_SR_Barracks, CP_16_SR_PaKPosition",
    # ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_16_SR_Gatehouse_Stuart",
        we_dont_own="CP_16_SR_Barracks, CP_16_SR_PaKPosition",
    ),
]

dynamicoob_16 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_16_SR_FieldKitchen": {
                "allies": {
                    "destroys": ["CombatArea_Axis_16_1st"],
                },
            },
        },
        delay_axis=0,
        delay_allies=0,
    )
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="IA_Limited_Assault_Beretta38_K98", limit=0.2),
    plugin(limitKit, team=2, slot=1, kit="BA_Limited_Assault_TommygunD_No4", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="IA_Limited_Support_MG34_K98", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="BA_Limited_Support_Bren_No4", limit=0.15),
    plugin(limitKit, team=1, slot=5, kit="GA_ATPzB39_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BA_ATBoys_Limited", limit=0.1),
]

kitlimits_16 = [
    plugin(limitKit, team=1, slot=1, kit="IA_Limited_Assault_Beretta38_K98", limit=0.2),
    plugin(limitKit, team=2, slot=1, kit="BA_Limited_Assault_TommygunD_No4", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="IA_Limited_Support_MG34_K98", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="BA_Limited_Support_Bren_No4", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GA_ATPzB39_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BA_ATBoys_Limited", limit=0.1),
]

kitlimits_8 = [
    plugin(limitKit, team=1, slot=1, kit="IA_Limited_Assault_Beretta38_K98", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="BA_Limited_Assault_TommygunD_No4", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GA_Limited_Support_MG34_K98", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="BA_Limited_Support_Bren_No4", limit=0.1),
    plugin(limitKit, team=2, slot=4, kit="BA_Grenadier_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="IA_Riflecarabine_Smoke_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BA_RiflemanEarly_Smoke_Limited", limit=0.1),
]

double_32 = [plugin(DoubleBleed)]

gpm_cq = {
    64: kitlimits_64 + links_64 + tickets_64 + spawns + nco,
    32: tickets_32 + spawns + nco + double_32,
    16: kitlimits_16 + tickets_16 + spawns + push_16 + cond_16_cq + nco + dynamicoob_16,
    128: kitlimits_8 + tickets_8 + spawns + nco,
}

disable_AI = [
    plugin(disableSPs),  # Auto-fill
]

gpm_coop = {
    64: links_64 + tickets_64 + spawns + nco,
    32: spawns + nco + double_32,
    16: tickets_16 + spawns + push_16 + cond_16_coop + nco + dynamicoob_16,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
