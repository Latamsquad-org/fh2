from game.plugins import plugin, limitKit, spawnerCondition, NCOrifleData, ticketLoss, teamSPs, timeCP

kit_limits_64 = [
    plugin(limitKit, team = 2, slot = 1, kit = 'UW_SMGAssault_Limited', limit = 0.1),
    plugin(limitKit, team = 1, slot = 1, kit = 'GW_SMGAssault_Limited', limit = 0.1),
    plugin(limitKit, team = 1, slot = 3, kit = 'GW_LMG_Limited', limit = 0.1),
    plugin(limitKit, team = 2, slot = 3, kit = 'UW_MG_30cal_Limited', limit = 0.1),
    plugin(limitKit, team = 1, slot = 5, kit = 'GW_AntitankAssault_patrone_haft', limit = 0.1),
    plugin(limitKit, team = 2, slot = 5, kit = 'UW_AntitankAssault_Limited', limit = 0.1),
]

rifleNCO = [
    plugin(NCOrifleData, kits = ('GW_NCO_G41', 'UW_NCO_SME'))
]

spawner_conditions_64 = [
    plugin(spawnerCondition,\
        team = 2,\
        spawner = 'CP_64_stmarie_alliedmain_stuart1, CP_64_stmarie_alliedmain_stuart1_0',\
        they_own = 'CP_64_stmarie_rue_du_joly or CP_64_stmarie_MP_checkpoint or CP_64_stmarie_chateau'),
    
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_stmarie_alliedmain_shermanA, CP_64_stmarie_alliedmain_shermanB, CP_64_stmarie_alliedmain_shermanC",
        they_own="CP_64_stmarie_church or CP_64_stmarie_chateau",
    ),
]

spawner_conditions_32 = [
    plugin(spawnerCondition,
        team = 2,
        spawner = 'CP_32_stmarie_alliedmain_ShermanA',
        they_own = 'CP_32_stmarie_bunker'
    ),
      plugin(spawnerCondition,
        team = 2,
        spawner = 'CP_32_stmarie_alliedmain_ShermanB',
        they_own = 'CP_32_stmarie_rue_galie'
    ),
    plugin(spawnerCondition,
        team = 2,
        spawner = 'CP_32_stmarie_alliedmain_StuartA',
        they_own = 'CP_32_stmarie_rue_carentan'
    ),
    plugin(spawnerCondition,
        team = 2,
        spawner = 'CP_32_stmarie_alliedmain_StuartB',
        they_own = 'CP_32_stmarie_chateau'
    ),
  
    plugin(spawnerCondition,
        team = 1,
        spawner = 'CP_32_stmarie_germanmain_Stug',
        they_own = 'CP_32_stmarie_bunker'
    ),
      plugin(spawnerCondition,
        team = 1,
        spawner = 'CP_32_stmarie_germanmain_PzIII',
        they_own = 'CP_32_stmarie_rue_galie'
    ),
    plugin(spawnerCondition,
        team = 1,
        spawner = 'CP_32_stmarie_germanmain_pz738',
        they_own = 'CP_32_stmarie_rue_carentan'
    ),
    plugin(spawnerCondition,
        team = 1,
        spawner = 'CP_32_stmarie_germanmain_pz735B',
        they_own = 'CP_32_stmarie_chateau'
    ),
]

spawner_conditions_16 = [
    plugin(spawnerCondition,
        team = 2,
        spawner = 'CP_16_stmarie_rue_thouays_bleedtank',
        they_own = 'CP_16_stmarie_church'),
    
    plugin(
        spawnerCondition,
        team=1,
        spawner='CP_16_stmarie_rue_joly_bleedtank',
        they_own="CP_16_stmarie_church",
    ),
]
spawns_64 = [
    plugin(teamSPs),  # Auto-fill
]

spawndelay_64 = [
    plugin(
        timeCP,
        team=-1,
        target="cp_64_stmarie_USforward",
        time=45,
    ),
]

spawns_32 = [
    plugin(
        teamSPs,
        sps=[
            "CP_32_stmarie_alliedmain_Us1",
            "CP_32_stmarie_alliedmain_Us2",
            "CP_32_stmarie_alliedmain_Us3",
            "CP_32_stmarie_alliedmain_Us4",
            "CP_32_stmarie_alliedmain_Us5",
            "CP_32_stmarie_alliedmain_Us6",
            "CP_32_stmarie_alliedmain_Us7",
            "CP_32_stmarie_alliedmain_Us8",
            "CP_32_stmarie_rue_galie_Us1",
            "CP_32_stmarie_rue_galie_Us2",
            "CP_32_stmarie_rue_galie_Us3",
            "CP_32_stmarie_rue_galie_Us4",
            "CP_32_stmarie_rue_galie_Us5",
            "CP_32_stmarie_rue_galie_Us6",
            "CP_32_stmarie_rue_galie_Us7",
            "CP_32_stmarie_rue_galie_Us8",
            "CP_32_stmarie_spawns_dummy_Us1",
            "CP_32_stmarie_spawns_dummy_Us2",
            "CP_32_stmarie_spawns_dummy_Us3",
            "CP_32_stmarie_spawns_dummy_Us4",
            "CP_32_stmarie_spawns_dummy_Us5",
            "CP_32_stmarie_spawns_dummy_Us6",
            "CP_32_stmarie_spawns_dummy_Us7",
            "CP_32_stmarie_spawns_dummy_Us8",
            "CP_32_stmarie_spawns_dummy_Us9",
            "CP_32_stmarie_spawns_dummy_Us10",
            "CP_32_stmarie_spawns_dummy_Us11",
            "CP_32_stmarie_spawns_dummy_Us12",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_32_stmarie_germanmain_Ger1",
            "CP_32_stmarie_germanmain_Ger2",
            "CP_32_stmarie_germanmain_Ger3",
            "CP_32_stmarie_germanmain_Ger4",
            "CP_32_stmarie_germanmain_Ger5",
            "CP_32_stmarie_germanmain_Ger6",
            "CP_32_stmarie_germanmain_Ger7",
            "CP_32_stmarie_germanmain_Ger8",
            "CP_32_stmarie_rue_carentan_Ger1",
            "CP_32_stmarie_rue_carentan_Ger2",
            "CP_32_stmarie_rue_carentan_Ger3",
            "CP_32_stmarie_rue_carentan_Ger4",
            "CP_32_stmarie_rue_carentan_Ger5",
            "CP_32_stmarie_rue_carentan_Ger6",
            "CP_32_stmarie_rue_carentan_Ger7",
            "CP_32_stmarie_rue_carentan_Ger8",
        ],
        team=1,
    ),
]

spawns_16 = [
    plugin(
        teamSPs,
        sps=[
            "CP_16_stmarie_rue_thouays_Us1",
            "CP_16_stmarie_rue_thouays_Us2",
            "CP_16_stmarie_rue_thouays_Us3",
            "CP_16_stmarie_rue_thouays_Us4",
            "CP_16_stmarie_rue_thouays_Us5",
            "CP_16_stmarie_rue_thouays_Us6",
            "CP_16_stmarie_rue_thouays_Us7",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_16_stmarie_rue_joly_Ger1",
            "CP_16_stmarie_rue_joly_Ger2",
            "CP_16_stmarie_rue_joly_Ger3",
            "CP_16_stmarie_rue_joly_Ger4",
            "CP_16_stmarie_rue_joly_Ger5",
            "CP_16_stmarie_rue_joly_Ger6",
            "CP_16_stmarie_rue_joly_Ger7",
        ],
        team=1,
    ),
]

ticketloss_64 = [
    plugin(ticketLoss, ticketLoss1 = 12, ticketLoss2 = 12)
]

ticketloss_32 = [
    plugin(ticketLoss, ticketLoss1 = 10, ticketLoss2 = 12)
]

ticketloss_16 = [
    plugin(ticketLoss, ticketLoss1 = 1000, ticketLoss2 = 1000)
]

earlyspawns_32 = [
    plugin(timeCP, team=-1, target="CP_32_stmarie_spawns_dummy", time=150),
]


gpm_cq = { 
    64:  rifleNCO + kit_limits_64 + ticketloss_64 + spawner_conditions_64 + spawns_64 + spawndelay_64,
    32:  rifleNCO + kit_limits_64 + ticketloss_32 + spawner_conditions_32 + earlyspawns_32 + spawns_32,
    16:  rifleNCO + kit_limits_64 + ticketloss_16 + spawner_conditions_16 + spawns_16,
}
