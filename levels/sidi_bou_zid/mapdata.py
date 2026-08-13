# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    linkCPs,
    NCOrifleData,
    phaseTickets,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    timeCP,
    DoubleBleed,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GA_NCO", "UA_NCO"),
        soldiers=("ga_tunisia_nco_soldier", "uw_ranger_sgt"),
    )
]

teamspawns_64 = [
    plugin(
        teamSPs,
        sps=[
            "CP_64_SidiBouZid_KernsCrossroads_GER1",
            "CP_64_SidiBouZid_KernsCrossroads_GER2",
            "CP_64_SidiBouZid_KernsCrossroads_GER4",
            "CP_64_SidiBouZid_KernsCrossroads_GER5",
            "CP_64_SidiBouZid_KernsCrossroads_GER6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_SidiBouZid_KernsCrossroads_US1",
            "CP_64_SidiBouZid_KernsCrossroads_US2",
            "CP_64_SidiBouZid_KernsCrossroads_US3",
            "CP_64_SidiBouZid_KernsCrossroads_US4",
            "CP_64_SidiBouZid_KernsCrossroads_US5",
            "CP_64_SidiBouZid_KernsCrossroads_US6",
            "CP_64_SidiBouZid_KernsCrossroads_US7",
        ],
        team=2,
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

tickets_64 = [
    plugin(ticketLoss, ticketLoss1=28, ticketLoss2=0),
]

tickets_32 = [
    plugin(ticketLoss, ticketLoss1=999, ticketLoss2=16),
]

tickets_16 = [
    plugin(ticketLoss, ticketLoss1=16, ticketLoss2=16),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_SidiBouZid_Bleed",
        source=[
            "CP_64_SidiBouZid_SidiBouZid",
        ],
        never_owned_by=2,
        default_zero=False,
    ),
]
push_64 = [
    plugin(
        push,
        source="CP_64_SidiBouZid_PosteDeLessouda",
        target="CP_64_SidiBouZid_SidiBouZid",
        attacker=1,
        force=True,
    ),
    plugin(
        push,
        source="CP_64_SidiBouZid_Outpost",
        target="CP_64_SidiBouZid_SidiBouZid",
        attacker=1,
        force=True,
    ),
    plugin(
        push,
        source="CP_64_SidiBouZid_SidiBouZid",
        target="CP_64_SidiBouZid_KernsCrossroads",
        attacker=1,
    ),
    # Do not allow KernsCrossroads capture if whole 1st line is not capped:
    plugin(
        push,
        source="CP_64_SidiBouZid_PosteDeLessouda",
        target="CP_64_SidiBouZid_KernsCrossroads",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_SidiBouZid_Outpost",
        target="CP_64_SidiBouZid_KernsCrossroads",
        attacker=1,
        display_arrow=False,
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_bouzid_alliedmain",
        target="CP_32_bouzid_kern",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_bouzid_kern",
        target="CP_32_bouzid_sidibouzid",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_bouzid_sidibouzid",
        target="CP_32_bouzid_fallback",
        attacker=2,
    ),
]

code = """ObjectTemplate.activeSafe ControlPoint CP_64_SidiBouZid_Bleed
ObjectTemplate.areaValueTeam1 30

ObjectTemplate.activeSafe ControlPoint CP_64_SidiBouZid_PosteDeLessouda
ObjectTemplate.unableToChangeTeam 1

ObjectTemplate.activeSafe ControlPoint CP_64_SidiBouZid_Outpost
ObjectTemplate.unableToChangeTeam 1

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_KernsCrossroads_Counter_Sherman
objecttemplate.setobjecttemplate 2 m4a1_early

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_KernsCrossroads_Counter_Sherman_0
objecttemplate.setobjecttemplate 2 m4a1_early

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Stuart
objecttemplate.setobjecttemplate 2 m3a1_stuart

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Lee
objecttemplate.setobjecttemplate 2 m3_lee

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Sherman
objecttemplate.setobjecttemplate 2 m4a1_early

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Stuart_0
objecttemplate.setobjecttemplate 2 m3a1_stuart

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_KernsCrossroads_Counter_M3Halftrack
objecttemplate.setobjecttemplate 2 m3_halftrack

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_KernsCrossroads_Counter_M3Halftrack_0
objecttemplate.setobjecttemplate 2 m3_halftrack

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_P40e
objecttemplate.setobjecttemplate 2 p-40e

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_M3Halftrack
objecttemplate.setobjecttemplate 2 m3_halftrack

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Scoutcar
objecttemplate.setobjecttemplate 2 m3_scoutcar"""

# Code used to reset vaules back to defaults:

reset_code = """ObjectTemplate.activeSafe ControlPoint CP_64_SidiBouZid_Bleed
ObjectTemplate.areaValueTeam1 30

ObjectTemplate.activeSafe ControlPoint CP_64_SidiBouZid_PosteDeLessouda
ObjectTemplate.unableToChangeTeam 0

ObjectTemplate.activeSafe ControlPoint CP_64_SidiBouZid_Outpost
ObjectTemplate.unableToChangeTeam 0

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_KernsCrossroads_Counter_Sherman
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_KernsCrossroads_Counter_Sherman_0
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Stuart
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Lee
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Sherman
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Stuart_0
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_KernsCrossroads_Counter_M3Halftrack
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_KernsCrossroads_Counter_M3Halftrack_0
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_P40e
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_M3Halftrack
objecttemplate.setobjecttemplate 2 DoesNotExist

objecttemplate.activesafe objectspawner CP_64_SidiBouZid_1stArmoredDivision_Counter_Scoutcar
objecttemplate.setobjecttemplate 2 DoesNotExist"""

phase_64 = [
    plugin(
        phaseTickets,
        cps=((1, "CP_64_SidiBouZid_KernsCrossroads")),
        tickets=(500, 0),
        ticketLoss=(290, 55),
        punish_factor=(0, -3.35),
        exec_code=code,
        reset_code=reset_code,
    ),
]

spawners_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_SidiBouZid_KGrReimann_SupportTank_1,CP_64_SidiBouZid_KGrReimann_SupportTank_2",
        we_dont_own="CP_64_SidiBouZid_PosteDeLessouda",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_SidiBouZid_KGrReimann_Tiger_1,CP_64_SidiBouZid_KGrSchuette_MediumTank_1,CP_64_SidiBouZid_KGrSchuette_TacBomber_1",
        we_dont_own="CP_64_SidiBouZid_SidiBouZid",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_SidiBouZid_KGrReimann_MobileAntiAir_1,CP_64_SidiBouZid_KGrSchuette_FastTransport_1,CP_64_SidiBouZid_Outpost_MediumAromor,CP_64_SidiBouZid_PosteDeLessouda_MediumArmor,CP_64_SidiBouZid_SidiBouZid_MediumTank_0",
        we_dont_own="CP_64_SidiBouZid_KernsCrossroads",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_SidiBouZid_KGrSchuette_MediumTank_2,CP_64_SidiBouZid_KGrSchuette_MediumTank_3",
        we_dont_own="CP_64_SidiBouZid_Outpost",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_SidiBouZid_KernsCrossroads_AntiTank_1_0,CP_64_SidiBouZid_SidiBouZid_LightTank_1",
        we_dont_own="CP_64_SidiBouZid_Outpost",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_SidiBouZid_KernsCrossroads_AntiTank_1_1,CP_64_SidiBouZid_SidiBouZid_MediumTank_2",
        we_dont_own="CP_64_SidiBouZid_PosteDeLessouda",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_SidiBouZid_1stArmoredDivision_MediumTank_2,CP_64_SidiBouZid_1stArmoredDivision_MediumTank_3,CP_64_SidiBouZid_1stArmoredDivision_MediumTank_4,CP_64_SidiBouZid_1stArmoredDivision_MediumTank_5,CP_64_SidiBouZid_1stArmoredDivision_AntiAir_0",
        we_dont_own="CP_64_SidiBouZid_KernsCrossroads",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_SidiBouZid_PosteDeLessouda_MediumTank_2,"
            "CP_64_SidiBouZid_Outpost_MediumTank_2"
        ),
        we_own="CP_64_SidiBouZid_SidiBouZid",
    ),
]

kitlimits_64 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GW_SMGAssault_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UA_SMGAssault_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GA_Limited_Support_MG34_K98",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UA_LMG_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="ga_antitank_k98_haft",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UA_AT_Limited",
        limit=0.1,
    ),
]

spawndelay_64 = [
    plugin(
        timeCP,
        team=-1,
        target="CP_64_SidiBouZid_USSchuetteDummy",
        time=90,
    ),
    plugin(
        timeCP,
        team=-1,
        target="CP_64_SidiBouZid_USReimannDummy",
        time=90,
    ),
    plugin(
        timeCP,
        team=1,
        target="CP_64_SidiBouZid_DESchuetteDummy",
        time=360,
    ),
    plugin(
        timeCP,
        team=1,
        target="CP_64_SidiBouZid_DEReimannDummy",
        time=360,
    ),
]

bleed_16 = [
    plugin(
        DoubleBleed,
    ),
]

gpm_cq = {
    64: push_64
    + spawners_64
    + tickets_64
    + kitlimits_64
    + phase_64
    + spawndelay_64
    + linkCPs_64
    + teamspawns_64
    + nco,
    32: push_32 + spawns + tickets_32 + kitlimits_64 + nco,
    16: tickets_16 + kitlimits_64 + spawns + nco + bleed_16,
}


gpm_coop = {
    64: push_64 + teamspawns_64 + nco,
    32: push_32 + spawns + tickets_32 + nco,
    16: tickets_16 + spawns + nco,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
