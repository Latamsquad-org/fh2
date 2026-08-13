from game.plugins import plugin, limitKit, NCOrifleData, vehicleMetadata, spawnerCondition

kit_limits_64 = [

    plugin(limitKit, team = 1, slot = 0, kit = 'JP_Scout', limit = 0.19),
    plugin(limitKit, team = 1, slot = 3, kit = 'JP_LMG_Limited', limit = 0.19),
    plugin(limitKit, team = 1, slot = 4, kit = 'JP_Engineer_type93_early_nowrench', limit = 0.19),
    plugin(limitKit, team = 1, slot = 5, kit = 'JP_Antitank_arisaka_turtlemine', limit = 0.19),
    plugin(limitKit, team = 2, slot = 0, kit = 'UP_Scout_spring', limit = 0.19),
    plugin(limitKit, team = 2, slot = 1, kit = 'UP_SMGAssault_1928_30rnd', limit = 0.19),
    plugin(limitKit, team = 2, slot = 3, kit = 'UP_LMG_Limited', limit = 0.19),
    plugin(limitKit, team = 2, slot = 4, kit = 'UP_Engineer_m1903', limit = 0.19),
    plugin(limitKit, team = 2, slot = 5, kit = 'UP_TankHunter_Spring_Satchel_nowrench', limit = 0.19),

  ]

rifleNCO = [plugin(NCOrifleData, kits = ('JP_NCO', 'UP_NCO_Early_1928_30rnd')),]


spawnerConditions_64 = [
    plugin(spawnerCondition, team = 1, spawner = 'Carrier_Fighter_01', we_dont_own = 'cp_64_cmp_wake_island_airfield'),
    plugin(spawnerCondition, team = 1, spawner = 'Carrier_Fighter_02', we_dont_own = 'cp_64_cmp_wake_island_airfield'),
    plugin(spawnerCondition, team = 1, spawner = 'Carrier_FighterBomber_01', we_dont_own = 'cp_64_cmp_wake_island_airfield'),
    plugin(spawnerCondition, team = 1, spawner = 'IJN_Destroyer', we_dont_own = 'cp_64_cmp_wake_island_airfield, cp_64_cmp_wake_island_Wilkes_Island, cp_64_cmp_wake_island_peale_Island, cp_64_cmp_wake_island_heel_point, cp_64_cmp_wake_island_marines_camp'),
    plugin(spawnerCondition, team = 1, spawner = 'Rufe_SeaPlane', we_dont_own = 'cp_64_cmp_wake_island_airfield, cp_64_cmp_wake_island_Wilkes_Island, cp_64_cmp_wake_island_peale_Island, cp_64_cmp_wake_island_heel_point, cp_64_cmp_wake_island_marines_camp'),
    plugin(spawnerCondition, team = 2, spawner = 'cp_64_cmp_wake_island_Airfield_Fighter2', we_dont_own = 'cp_64_cmp_wake_island_Wilkes_Island, cp_64_cmp_wake_island_peale_Island, cp_64_cmp_wake_island_heel_point, cp_64_cmp_wake_island_marines_camp'),
]

gpm_cq = {
  64: kit_limits_64 + rifleNCO + spawnerConditions_64,
  32: kit_limits_64 + rifleNCO,
  16: kit_limits_64 + rifleNCO,
}
