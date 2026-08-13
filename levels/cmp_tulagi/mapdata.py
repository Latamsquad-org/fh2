# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    limitKit,
    NCOrifleData,
    ticketLoss,
    spawnerCondition,
    linkCPs,
)

kit_limits_32 = [
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UP_SMGAssault_resing",
        limit=0.3,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="JP_LMG_Limited_scoped",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UP_LMG_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="JP_Antitank_type93",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        kit="UP_Engineer_shotgun",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UP_Engineer_M1903a1_Satchel_nowrench",
        limit=0.1,
    ),
]
kit_limits_64 = [
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UP_SMGAssault_resing",
        limit=0.3,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="JP_LMG_Limited_scoped",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UP_LMG_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="JP_Antitank_type93",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        kit="UP_Engineer_shotgun",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UP_Engineer_M1903a1_Satchel_nowrench",
        limit=0.1,
    ),
]

links_64 = [
    plugin(
        linkCPs,
        target="cp_64_dummylooseflag",
        source=["Sasapi", "Blue_Beach", "Vanita", "Hill_208", "Japanese_HQ"],
        invert=False,
    ),
]

spawnerCondition_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="3rd_Kure_SNLF_japdestroyer",
        they_own="Sasapi and Blue_Beach and Hill_208",
    ),
    # tanks should spawn as soon as US take one island flag
    plugin(
        spawnerCondition,
        team=1,
        spawner="Hill_208_hago",
        they_own="Sasapi or Blue_Beach or Hill_208 or Japanese_HQ or Vanita",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="Japanese_HQ_hago",
        they_own="Sasapi or Blue_Beach or Hill_208 or Japanese_HQ or Vanita",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="Vanita_hago",
        they_own="Sasapi or Blue_Beach or Hill_208 or Japanese_HQ or Vanita",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="Vanita_MediumTank",
        they_own="Sasapi or Blue_Beach or Hill_208 or Japanese_HQ or Vanita",
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=25, ticketLoss2=25)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=16, ticketLoss2=16)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("JP_NCO_early", "UP_NCO_resing_spring"),
        soldiers=("jp_rilfe_sgt", "up_earlyusmc_olive"),
    ),
]

gpm_cq = {
    16: kit_limits_64 + rifleNCO + tickets_16,
    32: kit_limits_32 + rifleNCO + tickets_32,
    64: kit_limits_64 + rifleNCO + spawnerCondition_64 + links_64 + tickets_64,
}
