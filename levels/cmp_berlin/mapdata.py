from game.plugins import plugin, limitKit, timeCP, linkCPs, NCOrifleData, ticketLoss, spawnerCondition, push, teamSPs

kit_limits_64 = [
  plugin(limitKit, team = 1, slot = 1, kit = 'GW_StG44Assault_Limited', limit = 0.15),
  plugin(limitKit, team = 1, slot = 3, kit = 'GW_LMG_MG42_Limited', limit = 0.05),
  plugin(limitKit, team = 2, slot = 3, kit = 'RE_LMG_Limited', limit = 0.15),
  plugin(limitKit, team = 1, slot = 4, kit = 'GW_HJ_Limited', limit = 0.05),
  plugin(limitKit, team = 1, slot = 5, kit = 'GW_VS_Limited', limit = 0.05),
  plugin(limitKit, team = 2, slot = 5, kit = 'RE_AntitankAssault_faustnik_Limited', limit = 0.15),
]

kit_limits_32 = [
  plugin(limitKit, team = 1, slot = 3, kit = 'GW_LMG_MG42_Limited', limit = 0.1),
  plugin(limitKit, team = 2, slot = 3, kit = 'RE_LMG_Limited', limit = 0.15),
  plugin(limitKit, team = 1, slot = 4, kit = 'GW_HJ32_Limited', limit = 0.05),
  plugin(limitKit, team = 1, slot = 5, kit = 'GW_VS32_Limited', limit = 0.05),
  plugin(limitKit, team = 2, slot = 5, kit = 'RE_SMGAssault_Limited', limit = 0.15),
]

nco_kits = [
    plugin(NCOrifleData, kits = ('GW_NCO_STG44_K98', 'RE_NCO_45'), soldiers = ('gs_waffen_unteroffizier', 're_nco_soldier_telogrieka')),
]

links_64 = [
    plugin(linkCPs, target = 'sector_locker_a', source = 'Yard, Apotheke'),
    plugin(linkCPs, target = 'sector_locker_new', source = 'Park, Appartments'),
    plugin(linkCPs, target = 'sector_locker_b', source = 'Supplies, Store'),
    plugin(linkCPs, target = 'sector_locker_c', source = 'Square, Altona'),
    plugin(linkCPs, target = 'GMain', source = 'Hotel_Pension, Schneiderei'),
]

push_64 = [
	plugin(push, source = 'Yard, Apotheke', target = 'sector_locker_a', attacker = 2, display_arrow = False, wants_target_marker = False),

	plugin(push, source = 'sector_locker_a', target = 'Park, Appartments', delay = 30, attacker = 2, display_arrow = False, wants_source_marker = False),

	plugin(push, source = 'Park, Appartments', target = 'sector_locker_new', attacker = 2, display_arrow = False, wants_target_marker = False),

	plugin(push, source = 'sector_locker_new', target = 'Supplies, Store', delay = 30, attacker = 2, display_arrow = False, wants_source_marker = False),

	plugin(push, source = 'Supplies, Store', target = 'sector_locker_b', attacker = 2, display_arrow = False, wants_target_marker = False),

	plugin(push, source = 'sector_locker_b', target = 'Boulevard', delay = 50, attacker = 2, display_arrow = False, wants_source_marker = False),

	plugin(push, source = 'Square, Altona', target = 'sector_locker_c', attacker = 2, display_arrow = False, wants_target_marker = False),

	plugin(push, source = 'Boulevard', target = 'Square, Altona', delay = 70, attacker = 2, display_arrow = False, wants_source_marker = False),

	plugin(push, source = 'sector_locker_c', target = 'Schneiderei, Hotel_Pension', delay = 40, attacker = 2, display_arrow = False, wants_source_marker = False),

]

tickets_cq_64 = [
	plugin(ticketLoss, ticketLoss1 = 500, ticketLoss2 = 15)
]

tickets_cq_16 = [
	plugin(ticketLoss, ticketLoss1 = 1000, ticketLoss2 = 1000)

]

spawnerConditions = [
    plugin(spawnerCondition, team = 1, spawner = 'Tiger2, Panther2', we_dont_own = 'boulevard'),
    plugin(spawnerCondition, team = 1, spawner = 'FG1', we_dont_own = 'sector_locker_a'),

    plugin(spawnerCondition, team = 2, spawner = 'T3475, RU_Mainbase_T34, RU_Mainbase_T342, RU_Mainbase_IS2, RU_Mainbase_newtank', we_dont_own = 'Boulevard'),
]

spawndelay_64 = [

  plugin(timeCP, team = -1, target = 'Dummy_0', time = 65),

]


spawns = [
    plugin(teamSPs, sps = ['Yard_0_3', 'Ruins_1_2', 'Ruins_0_1', 'Ruins_1_3', 'Ruins_3_0', 'Yard_1_1', 'Yard_0_4', 'Yard_1_2', 'Yard_0_5', 'Ruins_0_2', 'Ruins_0_3', 'Ruins_4_0', 'Yard_2', 'Yard_7', 'Square_8', 'BG1', 'BG2', 'BG3', 'BG4', 'BG5', 'BG6', 'Hospital_3_0', 'Hospital_4_0', 'Hospital_5_0', 'Hospital_8_0', 'Altona_0', 'Altona_2_0', 'Altona_1_1', 'Altona_9', 'Altona_10', 'Schneiderei_1_3', 'Schneiderei_1_2_0', 'Schneiderei_1_4', 'H1', 'H2', 'H3', 'Supplies_7', 'Supplies_8', 'Park_8', 'Park_9_0', 'Park_10', 'Park_11', 'Park_12', 'Hospital_1_0', 'Hospital_2_0', 'H4', 'bou_1', 'bou_2', 'Appartments_1', 'Appartments_2', 'Appartments_3', 'Appartments_4'], team = 1),
    plugin(teamSPs, sps = ['Park_1', 'Park_2', 'Park_3', 'Park_4', 'Park_5', 'Park_6', 'Park_7', 'Ruins_R1', 'HotelR_1', 'HotelR_2', 'HotelR_3', 'HotelR_4', 'Ruins_R2', 'Ruins_R3', 'Ruins_R4', 'Ruins_R5', 'Ruins_R6', 'Yard_R1', 'Yard_R2', 'Yard_R3', 'Yard_R4', 'Yard_R5', 'Yard_R6', 'Yard_R7','SP2', 'SP3', 'Square_10', 'Square_2', 'Square_3', 'rus1', 'rus2', 'Altona_4_0', 'Altona_5_0', 'Altona_6_0', 'BR1', 'BR2', 'BR3', 'BR4', 'BR5', 'BR6', 'Hospital_6_0', 'Hospital_7_0', 'Hospital_9', 'Hospital_11_0', 'Hospital_11_1', 'Hospital_12', 'SchR_1', 'SchR_2', 'SchR_3', 'SchR_4', 'bow_1', 'bow_2', 'bow_3', 'bow_4', 'bow_5', 'bow_6', 'bow_7', 'bow_8'], team = 2),    
]


gpm_cq = {
  64: kit_limits_64 + push_64 + tickets_cq_64 + links_64 + nco_kits + spawnerConditions + spawndelay_64 + spawns,
  32: kit_limits_32 + nco_kits,
  16: kit_limits_32 + nco_kits + tickets_cq_16,
}