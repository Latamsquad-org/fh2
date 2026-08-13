# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    limitKit,
    NCOrifleData,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    push,
    DoubleBleed,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO_MP40_G43", "UW_NCO"),
        soldiers=("GcWhCamo_nco", "uc_win44_84th_sgt"),
    )
]


bleed_64 = [
    plugin(DoubleBleed),
]

kits_64 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_SMGAssault_Limited",
        slot=1,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_Limited",
        slot=1,
        limit=0.05,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_MG42_Limited",
        slot=3,
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited",
        slot=3,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault60m_Limited",
        slot=5,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankAssault_Limited",
        slot=5,
        limit=0.05,
    ),
]

kits_16 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_SMGAssault_Limited",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_Limited",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_MG42_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited_nobipod",
        slot=3,
        limit=0.1,
    ),
	    plugin(
        limitKit,
        team=1,
        kit="GW_RifleAssault_G43_Limited",
        slot=4,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_CarbineAssault_Limited",
        slot=4,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault60m_Limited",
        slot=5,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankSpringfieldA3_Limited",
        slot=5,
        limit=0.1,
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

spawnerConditions_64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_verdenne_alliedmain1_sherman3A, CP_64_verdenne_alliedmain1_sherman4A, CP_64_verdenne_alliedmain2_planeA",
        they_own="CP_64_verdenne_verdenne and CP_64_verdenne_observationpost and CP_64_verdenne_chateau",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_verdenne_axismain1_mpbileaa",
        we_own="CP_64_verdenne_verdenne and CP_64_verdenne_observationpost and CP_64_verdenne_chateau",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_verdenne_alliedmain1_sherman5B, CP_64_verdenne_alliedmain1_Sherman6B, CP_64_verdenne_alliedmain1_Sherman7B, CP_64_verdenne_alliedmain2_planeB",
        they_own="(CP_64_verdenne_crossroads and CP_64_verdenne_bourdon) or (CP_64_verdenne_fueldump and CP_64_verdenne_bourdon)",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_verdenne_axismain2_mobileAA",
        we_own="(CP_64_verdenne_crossroads and CP_64_verdenne_bourdon) or (CP_64_verdenne_fueldump and CP_64_verdenne_bourdon)",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_verdenne_axismain2_v1a",
        we_own="(CP_64_verdenne_crossroads and CP_64_verdenne_fueldump)",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_verdenne_axismain2_v1b",
        we_own="(CP_64_verdenne_bourdon and CP_64_verdenne_verdenne)",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_verdenne_axismain2_tankhunter, CP_64_verdenne_axismain2_scoutcar",
        they_own="CP_64_verdenne_verdenne and CP_64_verdenne_observationpost and CP_64_verdenne_chateau",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_verdenne_axismain1_panther2, CP_64_verdenne_axismain1_Panther1",
        they_own="(CP_64_verdenne_crossroads and CP_64_verdenne_bourdon) or (CP_64_verdenne_fueldump and CP_64_verdenne_bourdon)",
    ),
]

spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_verdenne_observationpost_panzeriv, CP_32_verdenne_observationpost_panther",
        they_own="CP_32_verdenne_crossroad",
    ),
]

ticketloss_64 = [
    plugin(teamSPs),
    plugin(ticketLoss, ticketLoss1=16, ticketLoss2=16),
]

ticketloss_32 = [
    plugin(teamSPs),
    plugin(ticketLoss, ticketLoss1=999, ticketLoss2=20),
]

ticketloss_16 = [
    plugin(teamSPs),
    plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000),
]


push_32 = [
    plugin(
        push,
        source="CP_32_verdenne_bourdon",
        target="CP_32_verdenne_crossroad",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_verdenne_crossroad",
        target="CP_32_verdenne_chateau",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_verdenne_chateau",
        target="CP_32_verdenne_verdenne",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_verdenne_verdenne",
        target="CP_32_verdenne_observationpost",
        attacker=2,
    ),
]

# fmt: off
gpm_cq = {
    64: kits_64 + ticketloss_64 + nco + spawns + spawnerConditions_64 + bleed_64,
    32: kits_64 + ticketloss_32 + nco + spawns + spawnerConditions_32 + push_32,
    16: kits_16 + ticketloss_16 + nco + spawns,
}
# fmt: on


gpm_coop = {
    64: ticketloss_64 + nco + spawns + spawnerConditions_64,
    32: ticketloss_32 + nco + spawns + spawnerConditions_32 + push_32,
    16: ticketloss_16 + nco + spawns,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
