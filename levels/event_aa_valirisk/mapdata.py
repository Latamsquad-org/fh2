from game.plugins import plugin, teamSPs, limitKit, ticketLoss, NCOrifleData

kitlimits_64 = [

	plugin(limitKit, team = 1, slot = 1, kit = 'GW_SMGAssault_Limited', limit = 0.15),
	plugin(limitKit, team = 2, slot = 1, kit = 'RE_SMGAssault_Limited', limit = 0.15),
	plugin(limitKit, team = 1, slot = 3, kit = 'GA_Limited_Support_MG34_K98', limit = 0.1),
	plugin(limitKit, team = 2, slot = 3, kit = 'RE_LMG_Limited', limit = 0.1),
	plugin(limitKit, team = 1, slot = 5, kit = 'ga_antitank_k98_haft', limit = 0.2),
	plugin(limitKit, team = 2, slot = 5, kit = 'RE_AntitankAssault_Limited', limit = 0.2),
]

kitlimits_16 = [

	plugin(limitKit, team = 1, slot = 1, kit = 'GW_SMGAssault_Limited', limit = 0.15),
	plugin(limitKit, team = 2, slot = 1, kit = 'RE_SMGAssault_Limited', limit = 0.15),
	plugin(limitKit, team = 1, slot = 3, kit = 'GA_Limited_Support_MG34_K98', limit = 0.1),
	plugin(limitKit, team = 2, slot = 3, kit = 'RE_LMG_Limited', limit = 0.1),
        plugin(limitKit, team = 1, slot = 4, kit = 'GW_RifleAssault_G41_Limited', limit = 0.15),
	plugin(limitKit, team = 2, slot = 4, kit = 'RE_RifleAssault_SVT40_Limited', limit = 0.15),
	plugin(limitKit, team = 1, slot = 5, kit = 'GW_SMGAssault_mp38_Limited', limit = 0.15),
	plugin(limitKit, team = 2, slot = 5, kit = 'RE_SMGAssault_pps43_Limited', limit = 0.15),
]

tickets_64 = [
	plugin(ticketLoss, ticketLoss1 = 12, ticketLoss2 = 12)

]

rifleNCO = [
    plugin(NCOrifleData, kits = ('GA_NCOMP40', 'RE_NCO')),
]

spawns_64 = [
    plugin(teamSPs, sps = ['CP_64_event_aa_valirisk_redarmyhouse_DE1', 'CP_64_event_aa_valirisk_redarmyhouse_DE2', 'CP_64_event_aa_valirisk_redarmyhouse_DE3', 'CP_64_event_aa_valirisk_redarmyhouse_DE4', 'CP_64_event_aa_valirisk_oldtowncenter_DE1', 'CP_64_event_aa_valirisk_oldtowncenter_DE2', 'CP_64_event_aa_valirisk_oldtowncenter_DE3', 'CP_64_event_aa_valirisk_oldtowncenter_DE4', 'CP_64_event_aa_valirisk_redoctoberraffinery_DE1', 'CP_64_event_aa_valirisk_redoctoberraffinery_DE2', 'CP_64_event_aa_valirisk_redoctoberraffinery_DE3', 'CP_64_event_aa_valirisk_redoctoberraffinery_DE4', 'CP_64_event_aa_valirisk_kholkoze_DE1', 'CP_64_event_aa_valirisk_kholkoze_DE2', 'CP_64_event_aa_valirisk_kholkoze_DE3', 'CP_64_event_aa_valirisk_kholkoze_DE4', 'CP_64_event_aa_valirisk_sawmill_DE1', 'CP_64_event_aa_valirisk_sawmill_DE2', 'CP_64_event_aa_valirisk_sawmill_DE3', 'CP_64_event_aa_valirisk_sawmill_DE4', 'CP_64_event_aa_valirisk_coalmine_DE1', 'CP_64_event_aa_valirisk_coalmine_DE2', 'CP_64_event_aa_valirisk_coalmine_DE3', 'CP_64_event_aa_valirisk_coalmine_DE4'], team = 1),
    plugin(teamSPs, sps = ['CP_64_event_aa_valirisk_redarmyhouse_RU1', 'CP_64_event_aa_valirisk_redarmyhouse_RU2', 'CP_64_event_aa_valirisk_redarmyhouse_RU3', 'CP_64_event_aa_valirisk_redarmyhouse_RU4', 'CP_64_event_aa_valirisk_oldtowncenter_RU1', 'CP_64_event_aa_valirisk_oldtowncenter_RU2', 'CP_64_event_aa_valirisk_oldtowncenter_RU3', 'CP_64_event_aa_valirisk_oldtowncenter_RU4', 'CP_64_event_aa_valirisk_redoctoberraffinery_RU1', 'CP_64_event_aa_valirisk_redoctoberraffinery_RU2', 'CP_64_event_aa_valirisk_redoctoberraffinery_RU3', 'CP_64_event_aa_valirisk_redoctoberraffinery_RU4', 'CP_64_event_aa_valirisk_kholkoze_RU1', 'CP_64_event_aa_valirisk_kholkoze_RU2', 'CP_64_event_aa_valirisk_kholkoze_RU3', 'CP_64_event_aa_valirisk_kholkoze_RU4', 'CP_64_event_aa_valirisk_sawmill_RU1', 'CP_64_event_aa_valirisk_sawmill_RU2', 'CP_64_event_aa_valirisk_sawmill_RU3', 'CP_64_event_aa_valirisk_sawmill_RU4', 'CP_64_event_aa_valirisk_coalmine_RU1', 'CP_64_event_aa_valirisk_coalmine_RU2', 'CP_64_event_aa_valirisk_coalmine_RU3', 'CP_64_event_aa_valirisk_coalmine_RU4'], team = 2),
]

gpm_cq = {
  64: tickets_64 + spawns_64 + kitlimits_64 + rifleNCO,
  32: tickets_64 + kitlimits_64 + rifleNCO,
  16: tickets_64 + kitlimits_16 + rifleNCO,
}
