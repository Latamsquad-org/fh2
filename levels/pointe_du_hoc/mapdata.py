# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:

from game.plugins import (  # pylint: disable=E0401
    aiPush,
    destroyObjective,
    disableSPs,
    dynamicOOB,
    limitKit,
    linkCPs,
    plugin,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    timeCP,
    NCOrifleData,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO"),
        soldiers=("gw_heer_unteroffizier", "uw_ranger_sgt"),
    )
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "PDH_64_CP_SECTOR_A_DUMMY": {
                "allies": {
                    "creates": [
                        "CombatArea_64p_yesgo_allies_2",
                    ],
                    "destroys": [
                        "CombatArea_64p_yesgo_axis_1",
                    ],
                },
            },
        },
        inactive_at_start=[
            "CombatArea_64p_yesgo_allies_2",
        ],
        delay_axis=120,
        delay_allies=0,
    )
]

spawns_64 = [
    plugin(
        teamSPs,
        sps=[
            "64_SP_observationbunker_axis_1",
            "64_SP_observationbunker_axis_2",
            "64_SP_observationbunker_axis_3",
            "64_SP_observationbunker_axis_4",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_bunkers2_axis_1",
            "64_SP_bunkers2_axis_2",
            "64_SP_bunkers2_axis_3",
            "64_SP_bunkers2_axis_4",
            "64_SP_bunkers2_axis_5",
            "64_SP_bunkers2_axis_6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_bunkers1_axis_1",
            "64_SP_bunkers1_axis_2",
            "64_SP_bunkers1_axis_3",
            "64_SP_bunkers1_axis_4",
            "64_SP_bunkers1_axis_5",
            "64_SP_bunkers1_axis_6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_bunkers3_axis_1",
            "64_SP_bunkers3_axis_2",
            "64_SP_bunkers3_axis_3",
            "64_SP_bunkers3_axis_4",
            "64_SP_bunkers3_axis_5",
            "64_SP_bunkers3_axis_6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_farm1_axis_1",
            "64_SP_farm1_axis_2",
            "64_SP_farm1_axis_3",
            "64_SP_farm1_axis_4",
            "64_SP_farm1_axis_5",
            "64_SP_farm1_axis_6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_farm2_1",
            "64_SP_farm2_2",
            "64_SP_farm2_3",
            "64_SP_farm2_4",
            "64_SP_farm2_5",
            "64_SP_farm2_6",
            "64_SP_farm2_7",
            "64_SP_farm2_8",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_observationbunker_allies_1",
            "64_SP_observationbunker_allies_2",
            "64_SP_observationbunker_allies_3",
            "64_SP_observationbunker_allies_4",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_bunkers2_allies_1",
            "64_SP_bunkers2_allies_2",
            "64_SP_bunkers2_allies_3",
            "64_SP_bunkers2_allies_4",
            "64_SP_bunkers2_allies_5",
            "64_SP_bunkers2_allies_6",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_bunkers1_allies_1",
            "64_SP_bunkers1_allies_2",
            "64_SP_bunkers1_allies_3",
            "64_SP_bunkers1_allies_4",
            "64_SP_bunkers1_allies_5",
            "64_SP_bunkers1_allies_6",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_bunkers3_allies_1",
            "64_SP_bunkers3_allies_2",
            "64_SP_bunkers3_allies_3",
            "64_SP_bunkers3_allies_4",
            "64_SP_bunkers3_allies_5",
            "64_SP_bunkers3_allies_6",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "64_SP_farm1_allies_1",
            "64_SP_farm1_allies_2",
            "64_SP_farm1_allies_3",
            "64_SP_farm1_allies_4",
            "64_SP_farm1_allies_5",
            "64_SP_farm1_allies_6",
        ],
        team=2,
    ),
]

spawns_16 = [
    plugin(
        teamSPs,
        sps=[
            "16_SP_clifftop_allies1",
            "16_SP_clifftop_allies2",
            "16_SP_clifftop_allies3",
            "16_SP_clifftop_allies4",
            "16_SP_clifftop_allies5",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "16_SP_bunkers3_axis1",
            "16_SP_bunkers3_axis2",
            "16_SP_bunkers3_axis3",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "16_SP_observationbunker_axis1",
            "16_SP_observationbunker_axis2",
            "16_SP_observationbunker_axis3",
            "16_SP_observationbunker_axis4",
            "16_SP_observationbunker_axis5",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "16_SP_bunkers2_allies1",
            "16_SP_bunkers2_allies2",
            "16_SP_bunkers2_allies3",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "16_SP_bunkers1_allies1",
            "16_SP_bunkers1_allies2",
            "16_SP_bunkers1_allies3",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "16_SP_bunkers1_axis1",
            "16_SP_bunkers1_axis2",
            "16_SP_bunkers1_axis3",
        ],
        team=1,
    ),
]

push_64 = [
    plugin(
        push,
        source="64_CP_Beachbase",
        target="64_CP_observationbunker, 64_CP_bunkers2",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="64_CP_observationbunker, 64_CP_bunkers2",
        target="PDH_64_CP_SECTOR_A_DUMMY",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="PDH_64_CP_SECTOR_A_DUMMY",
        target="64_CP_bunkers1, 64_CP_bunkers3",
        attacker=2,
        display_arrow=False,
        delay=30,
    ),
    plugin(
        push,
        source="64_CP_bunkers1",
        target="64_CP_bunkers3",
        attacker=2,
        display_arrow=False,
        force=True,
    ),
    plugin(
        push,
        source="64_CP_bunkers3, 64_CP_bunkers1",
        target="64_CP_farm1",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="64_CP_farm1",
        target="64_CP_farm2",
        attacker=2,
        display_arrow=False,
    ),
]

push_32 = [
    plugin(
        push,
        source="32_CP_farm2",
        target="32_CP_farm1",
        attacker=1,
    ),
    plugin(
        push,
        source="32_CP_farm1",
        target="32_CP_bunkers3",
        attacker=1,
    ),
    plugin(
        push,
        source="32_CP_bunkers3",
        target="32_CP_bunkers1",
        attacker=1,
    ),
    plugin(
        push,
        source="32_CP_bunkers1",
        target="32_CP_bunkers2",
        attacker=1,
    ),
    plugin(
        push,
        source="32_CP_bunkers1",
        target="32_CP_observationbunker",
        attacker=1,
    ),
]

spawns_32 = [
    plugin(
        teamSPs,
        team=1,
        sps=(
            "32_SP_farm1_axis*, "
            "32_SP_bunkers1_axis*, "
            "32_SP_bunkers3_axis*"
        ),
    ),
    plugin(
        teamSPs,
        team=2,
        sps=(
            "32_SP_farm1_allies*, "
            "32_SP_bunkers1_allies*, "
            "32_SP_bunkers3_allies*"
        ),
    ),
]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_guns_dummy",
        source="64_CP_farm1",
        invert=True,
    ),
    plugin(
        linkCPs,
        target="PDH_64_CP_SECTOR_A_DUMMY",
        source=["64_CP_observationbunker", "64_CP_bunkers2"],
    ),
    plugin(
        linkCPs,
        target="cp_64_RoundEnder",
        source="CP_64_reinforcements,64_CP_farm1",
    ),
]

kit_limits = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GW_SMGAssault_mp34_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UW_SMGAssault_Limited",
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_LMG_MG26_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UW_LMG_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_AntitankAssault_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UW_AntitankSpringfieldA1_Limited",
        limit=0.1,
    ),
]

kit_limits_32 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GW_SMGAssault_mp34_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UW_SMGAssault_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_LMG_MG26_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UW_LMG_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_AntitankAssault_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UW_AntitankSpringfieldA1_Limited",
        limit=0.1,
    ),
]

kit_limits_16 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GW_SMGAssault_mp34_Limited",
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UW_SMGAssault_Limited",
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_LMG_MG26_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UW_LMG_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="GW_RifleAssault_G41_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_AntitankAssault_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UW_AntitankSpringfieldA1_Limited",
        limit=0.1,
    ),
]

time_64 = [
    plugin(
        timeCP,
        team=2,
        target="64_CP_cliff_dummy",
        time=300,
    ),
]

end_objective_64 = [
    plugin(
        destroyObjective,
        controlpoint="CP_64_reinforcements",
        refcount=4,
        template="gpf_155mm",
    ),
]
tickets_64 = [
    plugin(
        ticketLoss,
        ticketLoss1=1000,
        ticketLoss2=9,
    )
]
tickets_32 = [
    plugin(
        ticketLoss,
        ticketLoss1=10,
        ticketLoss2=10,
    )
]
tickets_16 = [
    plugin(
        ticketLoss,
        ticketLoss1=7,
        ticketLoss2=7,
    )
]


coop_32 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=3.0 / 32.0,
        kit="GW_Scout",
        soldier="gw_heer_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GW_SMGAssault_mp34_Limited",
        soldier="gw_heer_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=8.0 / 32.0,
        kit="GW_RifleAssault_noNadeLauncher",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GW_LMG_MG26_Limited",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=3.0 / 32.0,
        kit="GW_Engineer",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=7.0 / 32.0,
        kit="GW_AntitankAssault_Limited",
        soldier="gw_heer_panzerabwehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="UW_Ranger_Scout",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="UW_SMGAssault_Limited",
        soldier="uw_ranger_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="UW_RifleAssault_noNadeLauncher",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uw_ranger_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=5.0 / 32.0,
        kit="UW_Engineer_satchel",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=3.0 / 32.0,
        kit="UW_AntitankSpringfieldA1_Limited",
        soldier="uw_ranger_cpl",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
    plugin(
        spawnerCondition,
        team=1,
        spawner="32_OS_farm2_DE_US_ArmCar",
        we_dont_own="32_CP_farm1",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="32_OS_farm2_DE_US_HeavyTank",
        we_own="32_CP_farm1",
    ),
]

coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout",
        soldier="gw_heer_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GW_SMGAssault_mp34_Limited",
        soldier="gw_heer_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=11.0 / 32.0,
        kit="GW_RifleAssault_noNadeLauncher",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GW_LMG_MG26_Limited",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=5.0 / 32.0,
        kit="GW_Engineer",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=1.0 / 32.0,
        kit="GW_AntitankAssault_Limited",
        soldier="gw_heer_panzerabwehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="UW_Ranger_Scout",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="UW_SMGAssault_Limited",
        soldier="uw_ranger_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="UW_RifleAssault_noNadeLauncher",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uw_ranger_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=6.0 / 32.0,
        kit="UW_Engineer_Thermite",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=2.0 / 32.0,
        kit="UW_AntitankSpringfieldA1_Limited",
        soldier="uw_ranger_cpl",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs, team=1, cp="CP_64_reinforcements_1", we_own="64_CP_farm1"
    ),
    plugin(
        disableSPs, team=1, cp="CP_64_reinforcements_2", we_own="64_CP_farm1"
    ),
    plugin(
        disableSPs, team=2, cp="64_CP_cliff_dummy", we_own="64_CP_bunkers2"
    ),
    plugin(
        disableSPs,
        team=2,
        cp="64_US_CP_Cliffs4",
        we_own="64_CP_observationbunker or 64_CP_bunkers2",
    ),
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
    # Objectives
    plugin(
        linkCPs, target="CP_64_guns_dummy", source="64_CP_farm1", invert=True
    ),
    plugin(
        linkCPs, target="cp_64_RoundEnder", source="CP_64_reinforcements_1"
    ),
    plugin(
        linkCPs,
        target="CP_64_reinforcements_2",
        source="CP_64_reinforcements_1",
    ),
    plugin(
        destroyObjective,
        controlpoint="CP_64_reinforcements_1",
        refcount=4,
        template="gpf_155mm",
    ),
]


gpm_cq = {
    64: tickets_64
    + kit_limits
    + push_64
    + links_64
    + time_64
    + end_objective_64
    + spawns_64
    + dynamicoob_64
    + nco,
    32: tickets_32 + kit_limits_32 + push_32 + spawns_32 + nco,
    16: tickets_16 + spawns_16 + kit_limits_16 + nco,
}

gpm_coop = {
    64: coop_64 + tickets_64 + time_64 + nco,
    32: coop_32 + tickets_32 + nco,
}
sp3 = gpm_coop
sp2 = gpm_coop
