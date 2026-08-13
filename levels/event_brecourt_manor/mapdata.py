# -*- coding: utf-8 -*-
# pylint: disable=W0232,C0103,C0111,F0401
from game.plugins import (
    plugin,
    destroyObjective,
    push,
    teamSPs,
    limitKit,
    ticketLoss,
    NCOrifleData,
    spawnerCondition,
    linkCPs,
    dynamicOOB,
    SectorTickets,
)

push_64 = [
    plugin(
        push,
        source="CP_64_bm_506th_PIR",
        target="CP_64_bm_Le_Grand_Chemin",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_bm_506th_PIR",
        target="CP_64_bm_crossroads",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_bm_Company_D",
        target="CP_64_bm_Le_Grand_Chemin",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_bm_Company_D",
        target="CP_64_bm_crossroads",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_bm_Le_Grand_Chemin",
        target="CP_sector_a_locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bm_Crossroads",
        target="CP_sector_a_locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_sector_a_locker",
        target="CP_64_bm_gun_battery",
        attacker=2,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_sector_a_locker",
        target="CP_64_bm_radar_bunker",
        attacker=2,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bm_Gun_Battery",
        target="CP_sector_b_locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bm_radar_bunker",
        target="CP_sector_b_locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_sector_b_locker",
        target="CP_64_bm_Brecourt_Manor",
        attacker=2,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_sector_b_locker",
        target="CP_64_bm_Franqueville",
        attacker=2,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bm_Brecourt_Manor",
        target="CP_sector_c_locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bm_Franqueville",
        target="CP_sector_c_locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_sector_c_locker",
        target="CP_64_bm_Farm",
        attacker=2,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_sector_c_locker",
        target="CP_64_bm_Germain",
        attacker=2,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bm_Farm",
        target="cp_sector_d_locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bm_Germain",
        target="cp_sector_d_locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
]


linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_sector_a_locker",
        source=["CP_64_bm_Le_Grand_Chemin", "CP_64_bm_crossroads"],
    ),
    plugin(
        linkCPs,
        target="CP_sector_b_locker",
        source=["CP_64_bm_gun_battery", "CP_64_bm_radar_bunker"],
    ),
    plugin(
        linkCPs,
        target="CP_sector_c_locker",
        source=["CP_64_bm_Brecourt_Manor", "CP_64_bm_Franqueville"],
    ),
    plugin(
        linkCPs,
        target="cp_sector_d_locker",
        source=["CP_64_bm_Farm", "CP_64_bm_Germain"],
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_sector_a_locker": {
                "allies": {
                    "creates": ["CombatArea_385_Default"],
                    "destroys": ["CombatArea_363_Default"],
                },
            },
            "CP_sector_b_locker": {
                "allies": {
                    "creates": ["CombatArea_273_Default"],
                    "destroys": ["CombatArea_403_Default"],
                },
            },
            "CP_sector_c_locker": {
                "allies": {
                    "creates": ["CombatArea_316_Default"],
                    "destroys": ["CombatArea_296_Default"],
                },
            },
        },
        inactive_at_start=[
            "CombatArea_385_Default",
            "CombatArea_273_Default",
            "CombatArea_316_Default",
        ],
        delay_axis=120,
        delay_allies=0,
    )
]

Sectortickets_64 = [
    plugin(
        SectorTickets,
        sector_tickets={
            "CP_sector_a_locker": {"allies": "+300"},
            "CP_sector_b_locker": {"allies": "+300"},
            "CP_sector_c_locker": {"allies": "+300"},
            "CP_sector_d_locker": {"allies": "+300"},
        },
    )
]

objective_64 = [
    plugin(
        destroyObjective,
        controlpoint="CP_64_bm_Gun_Battery",
        refcount=4,
        template="lefh18_france",
    ),
]


spawners_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "CP_64_bm_Farm_apc,CP_64_bm_Franqueville_Marder,"
            "CP_64_bm_Germain_Stug"
        ),
        we_dont_own="CP_64_bm_Le_Grand_Chemin and CP_64_bm_Crossroads",
    ),
]
spawns = [
    plugin(teamSPs),  # Auto-fill
]

limitkit_64 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GW_SMGAssault_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_LMG_Limited",
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
        slot=1,
        kit="UW_SMGAssault_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UW_MG_30cal_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UW_AntitankAssault_Limited",
        limit=0.1,
    ),
]

ticketloss = [plugin(ticketLoss, ticketLoss1=5, ticketLoss2=5)]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO_SME"),
        soldiers=("gb_nco_splittermuster", "uw_airborne_sgt"),
    )
]

gpm_cq = {
    64: (
        push_64
        + linkCPs_64
        + spawns
        + spawners_64
        + limitkit_64
        + ticketloss
        + rifleNCO
        + dynamicoob_64
        + Sectortickets_64
    ),
    32: limitkit_64 + ticketloss + rifleNCO + spawns,
    16: limitkit_64 + ticketloss + rifleNCO + spawns,
}
