from game.plugins import plugin, limitKit, NCOrifleData, ticketLoss, teamSPs


kit_limits_64 = [
    plugin(
        limitKit, team=1, kit="GW_SMGAssault_mp738(i)_Limited", slot=1, limit=0.15
    ),
    plugin(limitKit, team=2, kit="UW_SMGAssault_Limited", slot=1, limit=0.15),
    plugin(limitKit, team=1, kit="GW_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="UW_LMG_Limited", slot=3, limit=0.1),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault60m_Limited",
        slot=5,
        limit=0.04,
    ),
    plugin(
        limitKit, team=2, kit="UW_AntitankAssault_Limited", slot=5, limit=0.1
    ),
    plugin(limitKit, team=1, kit="GW_Engineer_Satchel_limited_alt", slot=4, limit=0.07),
    plugin(limitKit, team=2, kit="UW_Engineer_Satchel", slot=4, limit=0.07),
]
rifleNCO = [
    plugin(NCOrifleData, kits = ('GW_NCO_STG44', 'UW_NCO') )
]

ticketloss = [
    plugin(ticketLoss, ticketLoss1 = 13, ticketLoss2 = 13)
]



spawns = [
    plugin(teamSPs),  # Auto-fill
]

gpm_cq = {
  64: kit_limits_64 + rifleNCO  + ticketloss + spawns,
  32: kit_limits_64 + rifleNCO  + ticketloss + spawns,
  16: kit_limits_64 + rifleNCO  + ticketloss,
}





