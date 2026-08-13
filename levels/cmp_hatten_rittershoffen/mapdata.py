
from game.plugins import plugin, limitKit, linkCPs, NCOrifleData, ticketLoss, push, dynamicOOB, teamSPs, SectorTickets, spawnerCondition, timeCP

kit_limits_64 = [
    plugin(
        limitKit, team=1, slot=1, kit="GW_StG44Assault_Limited", limit=0.25
    ),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.15),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="UW_LMG_Limited", limit=0.15),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_AntitankAssault60m_Limited",
        limit=0.12,
    ),
    plugin(
        limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.04
    ),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_hatten_sector1",
        source="CP_64_hatten_church, CP_64_hatten_west, CP_64_hatten_crossroads",
    ),
    plugin(
        linkCPs, target="CP_64_hatten_sector2", source="CP_64_hatten_railstations"
    ),
    plugin(
        linkCPs,
        target="CP_64_hatten_sector3",
        source="CP_64_hatten_rittershoffen, CP_64_hatten_rittershoffen_west, CP_64_hatten_cemetery",
    ),
]
# CombatArea_53_gpm_cq64: Axis sector1, always open
# CombatArea_95_gpm_cq64' Axis sector2 pooltable
# CombatArea_134_gpm_cq64: Axis sector3

# CombatArea_142_gpm_cq64: Allied sector3
# CombatArea_163_gpm_cq64: Allied sector2 pooltable
# CombatArea_192_gpm_cq64: Allied sector 1
dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_hatten_sector1": {
                "axis": {
                    "creates": ["CombatArea_95_gpm_cq64"],
                    "destroys": ["CombatArea_192_gpm_cq64"],
                },
            },
            "CP_64_hatten_sector2": {
                "axis": {
                    "creates": ["CombatArea_134_gpm_cq64"],
                    "destroys": ["CombatArea_163_gpm_cq64"],
                },
            },
        },
        inactive_at_start=["CombatArea_95_gpm_cq64", "CombatArea_134_gpm_cq64"],
        delay_axis=0,
        delay_allies=120,
    )
]

push_64 = [
    plugin(
        push,
        source="CP_64_hatten_kg_huss, CP_64_hatten_kg_proll",
        target="CP_64_hatten_church, CP_64_hatten_west",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_hatten_church, CP_64_hatten_west",
        target="CP_64_hatten_crossroads",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_hatten_church, CP_64_hatten_west,CP_64_hatten_crossroads",
        target="CP_64_hatten_sector1",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_hatten_sector1",
        target="CP_64_hatten_railstations",
        attacker=1,
        display_arrow=False,
        delay=60,
    ),
    plugin(
        push,
        source="CP_64_hatten_railstations",
        target="CP_64_hatten_sector2",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_hatten_sector2",
        target="CP_64_hatten_cemetery, CP_64_hatten_rittershoffen,CP_64_hatten_rittershoffen_west",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_hatten_cemetery, CP_64_hatten_rittershoffen,CP_64_hatten_rittershoffen_west",
        target="CP_64_hatten_sector3",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
]

pcospawners64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_hatten_niederbetschdorf_ShermanM4A3_2,"
            "CP_64_hatten_niederbetschdorf_chaffee,"
            "CP_64_hatten_niederbetschdorf_flamm,"
        ),
        we_dont_own="CP_64_hatten_sector1",
    )
]

spawns_64 = [
    plugin(teamSPs),  # Auto-fill
]

spawndelay_64 = [
    plugin(timeCP, team=-1, target="CP_64_hatten_sector1_allied_spawnflag", time=360),
]

Sectortickets_64 = [
    plugin(
        SectorTickets,
        sector_tickets={
            "CP_64_hatten_sector1": {"axis": '+300'},
            "CP_64_hatten_sector2": {"axis": '+300'},
        },
    )
]


rifleNCO = [
    plugin(NCOrifleData, kits = ('GS_NCO_mp40_g43', 'UW_NCO') )
]

tickets_64 = [plugin(ticketLoss, ticketLoss2=9999, ticketLoss1=15)]
tickets_16 = [plugin(ticketLoss, ticketLoss2=1000, ticketLoss1=1000)]
tickets_32 = [plugin(ticketLoss, ticketLoss2=14, ticketLoss1=7)]

gpm_cq = { 
    64:  rifleNCO + kit_limits_64 + tickets_64 + push_64 + linkCPs_64 + dynamicoob_64 + Sectortickets_64 + spawns_64 + pcospawners64 + spawndelay_64,
    32:  rifleNCO + kit_limits_64 + tickets_32,
    16:  rifleNCO + kit_limits_64 + tickets_16,
}

