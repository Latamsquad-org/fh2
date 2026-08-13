from game.plugins import plugin, limitKit, ticketLoss, NCOrifleData, teamSPs

kit_limits_64 = [
  
plugin(limitKit, team = 1, slot = 1, kit = 'GW_SMGAssault_Limited', limit = 0.25),
  
plugin(limitKit, team = 2, slot = 1, kit = 'BW_SMGAssault_Limited', limit = 0.25),
  
plugin(limitKit, team = 1, slot = 3, kit = 'GW_LMG_Limited', limit = 0.15),
  
plugin(limitKit, team = 2, slot = 3, kit = 'BW_LMG_Limited', limit = 0.3),
  
plugin(limitKit, team = 1, slot = 5, kit = 'GW_AntitankAssault_Limited', limit = 0.15),

plugin(limitKit, team = 2, slot = 5, kit = 'BW_Antitank_Limited', limit = 0.15),

]

kit_limits_16 = [
  
plugin(limitKit, team = 1, slot = 1, kit = 'GW_SMGAssault_Limited', limit = 0.2),
  
plugin(limitKit, team = 2, slot = 1, kit = 'BW_SMGAssault_Limited', limit = 0.2),
  
plugin(limitKit, team = 1, slot = 3, kit = 'GW_LMG_Limited', limit = 0.2),
  
plugin(limitKit, team = 2, slot = 3, kit = 'BW_LMG_Limited', limit = 0.2),

plugin(limitKit, team = 1, slot = 4, kit = 'GW_RifleAssault_G41_Limited', limit = 0.2),

plugin(limitKit, team = 2, slot = 4, kit = 'BW_CarbineAssault_Limited', limit = 0.2),
  
plugin(limitKit, team = 1, slot = 5, kit = 'GW_RifleAssault_G43_Limited', limit = 0.15),

plugin(limitKit, team = 2, slot = 5, kit = 'BW_SMGAssault_m1928a1_Limited', limit = 0.15),

]

tickets_64 = [plugin(ticketLoss, ticketLoss1=25, ticketLoss2=25)]

rifleNCO = [
    plugin(NCOrifleData, kits = ('GW_NCO', 'BW_NCO')),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

gpm_cq = {
64: kit_limits_64 + tickets_64 + rifleNCO + spawns,
32: kit_limits_64 + tickets_64 + rifleNCO + spawns,
16: kit_limits_16 + tickets_64 + rifleNCO + spawns,
} 

