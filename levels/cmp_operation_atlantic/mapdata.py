from game.plugins import plugin, limitKit, ticketLoss, spawnerCondition, NCOrifleData, dynamicOOB, push, linkCPs, SectorTickets, teamSPs

kit_limits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=1, kit="CW_SMGAssault", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="CW_LMG_Limited", limit=0.1),
    plugin(
        limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1
    ),
    plugin(limitKit, team=2, slot=5, kit="CW_Antitank_Limited", limit=0.1),
]

ticketloss = [
    plugin(ticketLoss, ticketLoss1 = 14, ticketLoss2 = 14)
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "cw_NCO"),
        soldiers=("gw_heer_unteroffizier", "cw_nco_soldier"),
    )
]


Sectortickets_64 = [
    plugin(
        SectorTickets,
        sector_tickets={
            "CP_64_atlantic_sector_a_locker": {"allies": '+400'}
        },
    )
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_atlantic_sector_a_locker": {
                "allies": {
                    "creates": ["CombatArea_q64_allies_2"],
                    "destroys": ["CombatArea_q64_axis_2"],
                },
            },
        },
        inactive_at_start=["CombatArea_q64_allies_2"],
        delay_axis=120,
        delay_allies=0,
    )
]

linksCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_atlantic_sector_a_locker",
        source="CP_64_atlantic_sainthonorine,cp_64_atlantic_colombelles",
    ),
]

push_64 = [
    plugin(
        push,
        source="CP_64_atlantic_sainthonorine,cp_64_atlantic_colombelles",
        target="CP_64_atlantic_sector_a_locker",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_atlantic_sector_a_locker",
        target="cp_64_atlantic_smn,CP_64_atlantic_smn_sud,CP_64_atlantic_port,CP_64_atlantic_giberville,CP_64_atlantic_herouville",
        attacker=2,
        display_arrow=False,
    ),
]

pco_spawners_64 = [
    # Axis reinforcements
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_atlantic_defender_reinforcements_heavy",
        they_own="CP_64_atlantic_sector_a_locker",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_atlantic_defender_reinforcements_arty",
        they_own="cp_64_atlantic_smn",
    ),
   
    # Allied tank spawn conditions
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_atlantic_attacker_reinforcements_heavy",
        they_own="cp_64_atlantic_smn",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_atlantic_attacker_reinforcements_arty",
        they_own="cp_64_atlantic_smn_sud",
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

gpm_cq = { 
64: kit_limits_64 + rifleNCO + ticketloss + push_64 + dynamicoob_64 + pco_spawners_64 + linksCPs_64 + Sectortickets_64,
32: kit_limits_64 + rifleNCO + ticketloss,
16: kit_limits_64 + rifleNCO + ticketloss + spawns
}
