# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    teamSPs,
    spawnerCondition,
)


kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GM_Limited_Assault_MP40_K98", limit=0.2),
    plugin(limitKit, team=2, slot=1, kit="RE_SMGAssault_ppd34_Limited", limit=0.05),
    plugin(limitKit, team=1, slot=3, kit="GM_Limited_Support_MG34_K98", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="RE_LMG_limited", limit=0.05),
    plugin(limitKit, team=1, slot=5, kit="GW_RifleAssault_SVT40_Limited", limit=0.1),
]


tickets_64 = [plugin(ticketLoss, ticketLoss1=25, ticketLoss2=25)]


spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GM_NCOMP40", "RE_NCO_42"),
        soldiers=("GcWhFeldgrau_nco", "re_nco_soldier_telogrieka"),
    ),
]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_motovskiybay_alliedmain_testprototype",
        we_dont_own="CP_64_motovskiy_reinforcementaxis",
    ),
]

gpm_cq = {
    64: tickets_64 + kitlimits_64 + rifleNCO + spawns + spawnerConditions,
    32: tickets_64 + kitlimits_64 + rifleNCO + spawns,
    16: tickets_64 + kitlimits_64 + rifleNCO + spawns,
}

kits_AI = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GM_ScoutK98Short",
        soldier="GcWhFeldgrau_alt",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GM_Limited_Assault_MP40_K98",
        soldier="GcWhFeldgrau_light",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GM_RiflemanK98",
        soldier="GcWhFeldgrau_alt",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GM_Limited_Support_MG34_K98",
        soldier="GcWhFeldgrau_light",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GM_EngineerG3340",
        soldier="GcWhFeldgrau_light",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=7.0 / 32.0,
        kit="GW_RifleAssault_SVT40_Limited",
        soldier="GcWhFeldgrau_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=7.0 / 32.0,
        kit="RE_Scout_SVT40",
        soldier="re_light_soldier_telogrieka",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=1.0 / 32.0,
        kit="RE_SMGAssault_ppd34_Limited",
        soldier="re_heavy_soldier_telogrieka",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=12.0 / 32.0,
        kit="RE_RifleAssault_SVT40",
        soldier="re_light_soldier_telogrieka",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=1.0 / 32.0,
        kit="RE_LMG_limited",
        soldier="re_heavy_soldier_telogrieka_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="RE_Engineer_Satchel",
        soldier="re_light_soldier_telogrieka",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=7.0 / 32.0,
        kit="RE_RifleAssault_Early",
        soldier="re_heavy_soldier_telogrieka",
    ),
    plugin(
        NCOrifleData,
        kits=("GM_NCOMP40", "RE_NCO_42"),
        soldiers=("GcWhFeldgrau_nco", "re_nco_soldier_telogrieka"),
    ),
]

gpm_coop = {
    64: tickets_64 + kits_AI + spawns + spawnerConditions,
    32: tickets_64 + kits_AI + spawns,
    16: tickets_64 + kits_AI + spawns,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
