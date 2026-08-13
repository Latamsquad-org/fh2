from game.plugins import plugin, limitKit, NCOrifleData, ticketLoss, timeCP, teamSPs

kit_limits_64 = [
 plugin(limitKit, team = 1, slot = 3, kit = 'JP_LMG_Limited', limit = 0.2),
 plugin(limitKit, team = 2, slot = 3, kit = 'UP_LMG_Limited', limit = 0.2),
 plugin(limitKit, team = 1, slot = 5, kit = 'JP_Kneemortar', limit = 0.2),
 plugin(limitKit, team = 2, slot = 5, kit = 'UP_AntitankAssault_Limited', limit = 0.2),
 ]


ticketloss = [
    plugin(ticketLoss, ticketLoss1 = 10, ticketLoss2 = 10)
]



spawns_64 = [
    
plugin(teamSPs, sps = ['Cabu_Bridge_1','Cabu_Bridge_2','Cabu_Bridge_3','Cabu_Bridge_4'], team = 1),
    
plugin(teamSPs, sps = ['Cabu_Bridge_5','Cabu_Bridge_6','Cabu_Bridge_7','Cabu_Bridge_8'], team = 2),    
]


spawns_16 = [
    
plugin(teamSPs, sps = ['Bathhouse_1','Bathhouse_2','Bathhouse_3','Bathhouse_4'], team = 1),
    
plugin(teamSPs, sps = ['Officers_Dining_1','Officers_Dining_2','Officers_Dining_3','Officers_Dining_4'], team = 2),    
]



rifleNCO = [plugin(NCOrifleData, kits = ('JP_NCO', 'UP_NCO')),]

timeCPAssault = [

    plugin(timeCP, target = 'Forward_Positions', time = 180, team = 0),

    plugin(timeCP, target = 'Guard_Posts', time = 120, team = 0)

]




gpm_cq = {
	16: kit_limits_64 + rifleNCO + spawns_16,
	32: kit_limits_64 + rifleNCO,
	64: kit_limits_64 + rifleNCO + spawns_64 + timeCPAssault,
}





