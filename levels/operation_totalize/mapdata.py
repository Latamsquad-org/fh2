# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    aiPush,
    balanceSPs,
    delaySpawners,
    disableSPs,
    limitKit,
    linkCPs,
    NCOrifleData,
    # spawnerCondition,
    teamSPs,
    timeCP,
    ticketLoss,
    DoubleBleed,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO", "CW_NCO"),
        soldiers=("gs_waffen_unteroffizier", "cw_nco_soldier"),
    )
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=16, ticketLoss2=16)]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_totalize_reinforcements",
        source=["CP_64_totalize_factory"],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_totalize_reinforcements2",
        source=["CP_64_totalize_windmill"],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_totalize_reinforcements3",
        source=["CP_64_totalize_southfarm"],
        invert=True,
        default_zero=True,
    ),
]


kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=2, slot=1, kit="CW_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_MG42_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="PW_LMG_Limited", limit=0.3),
    plugin(limitKit, team=1, slot=5, kit="GS_AntitankAssault_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=5, kit="CW_Antitank_Limited", limit=0.15),
]


coop_64 = [
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_totalize_alliedmain",
        we_own="CP_64_totalize_windmill or CP_64_totalize_factory",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_totalize_factory",
        we_own="CP_64_totalize_German_forward_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_totalize_windmill",
        we_own="CP_64_totalize_German_forward_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_totalize_outpostwest",
        we_own="CP_64_totalize_factory and *",
    ),
    plugin(
        balanceSPs,
        custom_weights=[
            dict(
                cp="CP_64_totalize_factory,CP_64_totalize_windmill",
                team=1,
                weight=1250 * 1000,
            ),
            dict(
                cp="CP_64_totalize_outposteast,CP_64_totalize_outpostwest",
                team=1,
                weight=750 * 1000,
            ),
            dict(cp="CP_64_totalize_southfarm", team=1, weight=650 * 1000),
            dict(
                cp="CP_64_totalize_heavytank,CP_64_totalize_germanmain",
                team=1,
                weight=350 * 1000,
            ),
        ],
    ),
    # Team-locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
    # Forward dummy
    plugin(timeCP, target="CP_64_totalize_German_forward_dummy", team=-1, time=10),
]
bleed_32 = [
    plugin(
        DoubleBleed,
    ),
]

gpm_cq = {
    64: kitlimits_64 + links_64 + nco + tickets_64,
    32: kitlimits_64 + nco + bleed_32,
    16: kitlimits_64 + nco,
}

gpm_coop = {
    64: nco + coop_64,
    32: nco + bleed_32,
    16: nco,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
