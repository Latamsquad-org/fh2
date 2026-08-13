# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    disableSPs,
    dynamicOOB,
    limitKit,
    linkCPs,
    NCOrifleData,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    MiniObjective,
    aiPush,
)

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="RE_LMG_limited", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_heavy", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="RE_AntiTankAssault_PPS43_Limited", limit=0.2),
]

kitlimits_8 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="RE_SMGAssault_Late_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="RE_LMG_limited", limit=0.1),
    plugin(limitKit, team=1, slot=4, kit="GW_RifleAssault_Smoke_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=4, kit="RE_CarbineAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GW_SMGAssault_mp717(r)_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="RE_SMGAssault_pps43_Limited", limit=0.1),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_ogledow_sectorlock1dummy",
        source="CP_64_ogledow_barn, CP_64_ogledow_observationpost",
    ),
    plugin(
        linkCPs,
        target="CP_64_ogledow_sectorlock2dummy",
        source="CP_64_ogledow_defenseline, CP_64_ogledow_manor",
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_ogledow_sectorlock1dummy": {
                "axis": {
                    "creates": ["CombatArea_yesgo_axis_center_cq_64"],
                    "destroys": ["CombatArea_yesgo_allies_west_cq_64"],
                },
            },
            "CP_64_ogledow_sectorlock2dummy": {
                "axis": {
                    "creates": ["CombatArea_yesgo_axis_east_cq_64"],
                    "destroys": ["CombatArea_yesgo_allies_center_cq_64"],
                },
            },
        },
        inactive_at_start=[
            "CombatArea_yesgo_axis_center_cq_64",
            "CombatArea_yesgo_axis_east_cq_64",
        ],
        delay_axis=0,
        delay_allies=120,
    )
]

push_64 = [
    plugin(
        push,
        source="CP_64_ogledow_barn, CP_64_ogledow_observationpost",
        target="CP_64_ogledow_sectorlock1dummy",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_ogledow_sectorlock1dummy",
        target="CP_64_ogledow_defenseline, CP_64_ogledow_manor",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_ogledow_defenseline, CP_64_ogledow_manor",
        target="CP_64_ogledow_sectorlock2dummy",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_ogledow_sectorlock2dummy",
        target="CP_64_ogledow_staszowindustrialarea",
        attacker=1,
        display_arrow=False,
        delay=60,
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_ogledow_legat",
        target="CP_32_ogledow_exit",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_ogledow_exit",
        target="CP_32_ogledow_guardstankcorps",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_ogledow_guardstankcorps",
        target="CP_32_ogledow_staszow",
        attacker=1,
        display_arrow=True,
    ),
]


ktpunish32 = [
    plugin(
        MiniObjective,
        vehicle_worth={
            'kingtiger_standard': 100,
        },
        team_to_punish='axis',
    ),
]


push_16 = [
    plugin(
        push,
        source="CP_16_ogledow_axismain",
        target="CP_16_ogledow_farm, CP_16_ogledow_construction_yard",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_ogledow_farm, CP_16_ogledow_construction_yard",
        target="CP_16_ogledow_observation_post",
        attacker=1,
        display_arrow=True,
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=12, ticketLoss2=9999)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=9999)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=12, ticketLoss2=9999)]

tickets_8 = [plugin(ticketLoss, ticketLoss1=18, ticketLoss2=18)]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO_MP40_G43", "RE_NCO"),
        soldiers=("gw_heer_unteroffizier", "re_nco_soldier"),
    ),
]

spawnerConditions32 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_ogledow_guardstankcorps_t34a, CP_32_ogledow_guardstankcorps_t34b, CP_32_ogledow_guardstankcorps_t34c",
        we_dont_own="CP_32_ogledow_exit",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_ogledow_staszow_is2a, CP_32_ogledow_staszow_is2b, CP_32_ogledow_staszow_is2c",
        we_dont_own="CP_32_ogledow_guardstankcorps",
    ),

]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_ogledow_sectorlock2dummy_t34_1, CP_64_ogledow_sectorlock2dummy_t34_2, CP_64_ogledow_sectorlock2dummy_su152, CP_64_ogledow_sectorlock2dummy_t34_3, CP_64_ogledow_sectorlock2dummy_t34_4, CP_64_ogledow_sectorlock2dummy_t34_5",
        we_dont_own="CP_64_ogledow_sectorlock1dummy",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_ogledow_staszowindustrialarea_t3485_1, CP_64_ogledow_staszowindustrialarea_t3485_2, CP_64_ogledow_staszowindustrialarea_is2_1, CP_64_ogledow_staszowindustrialarea_is2_2, CP_64_ogledow_staszowindustrialarea_su152",
        we_dont_own="CP_64_ogledow_sectorlock2dummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_ogledow_axismain_kt1, CP_64_ogledow_axismain_kt2, CP_64_ogledow_axismain_panzeriv1, CP_64_ogledow_axismain_panzeriv2, CP_64_ogledow_axismain_pziv3, CP_64_ogledow_axismain_panzeriv4",
        we_dont_own="CP_64_ogledow_sectorlock1dummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_ogledow_sectorlock1dummy_kt1, CP_64_ogledow_sectorlock1dummy_kt2, CP_64_ogledow_sectorlock1dummy_pziv1, CP_64_ogledow_sectorlock1dummy_pziv2, CP_64_ogledow_sectorlock1dummy_panther1, CP_64_ogledow_sectorlock1dummy_panther2",
        we_dont_own="CP_64_ogledow_sectorlock2dummy",
    ),
]

gpm_cq = {

    128: tickets_8 + kitlimits_8 + rifleNCO + spawns,
    64: tickets_64 + kitlimits_64 + rifleNCO + spawnerConditions + spawns + push_64 + linkCPs_64 + dynamicoob_64,
    32: tickets_32 + ktpunish32 + push_32 + kitlimits_64 + rifleNCO + spawnerConditions32 + spawns,
    16: tickets_16 + kitlimits_64 + rifleNCO + spawns + push_16,
}


disable_AI = [
    # AI spawn points disabling - Axis
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_ogledow_axismain",
        we_own="CP_64_ogledow_observationpost and CP_64_ogledow_barn",
    ),
    # AI spawn points disabling - Allies
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_ogledow_manor",
        we_own="CP_64_ogledow_observationpost or CP_64_ogledow_barn",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_ogledow_defenseline",
        we_own="CP_64_ogledow_observationpost or CP_64_ogledow_barn",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_ogledow_staszowindustrialarea",
        we_own="CP_64_ogledow_manor or CP_64_ogledow_defenseline",
    ),
]


disable_AI = [
  plugin(disableSPs),  # Auto-fill
]

Push_AI_64 = [
  plugin(aiPush),  # Push mode
]

gpm_coop = {
    64: tickets_64 + rifleNCO + spawnerConditions + spawns + push_64 + disable_AI + Push_AI_64 + linkCPs_64,
    32: tickets_32 + ktpunish32 + push_32 + rifleNCO + spawnerConditions32 + spawns + disable_AI,
    16: tickets_16 + rifleNCO + spawns + push_16 + disable_AI,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop

