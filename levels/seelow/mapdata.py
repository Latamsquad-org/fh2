from game.plugins import plugin, limitKit, push, ticketLoss, linkCPs, NCOrifleData, teamSPs, spawnerCondition, dynamicOOB, aiPush, disableSPs

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            'sector_locker_a': {
                'allies': {
                    'creates': ['CombatArea_64_allies2'],
                    'destroys': ['CombatArea_64_axis1'],
                },
            },
            'sector_locker_b': {
                'allies': {
                    'creates': ['CombatArea_64_allies3'],
                    'destroys': ['CombatArea_64_axis2'],
                },
            },
        },
        inactive_at_start=['CombatArea_64_allies2', 'CombatArea_64_allies3'],
        delay_axis=120,
        delay_allies=0,
    )
]

kit_limits = [
    plugin(limitKit, team=1, slot=3, kit='GW_LMG_MG42_Limited', limit=0.15),
    plugin(limitKit, team=2, slot=3, kit='RE_LMG_Limited', limit=0.15),
    plugin(limitKit, team=1, slot=5, kit='GW_AntitankAssault60m_Limited', limit=0.2),
    plugin(limitKit, team=2, slot=5, kit='RE_AntitankAssault_faustnik_Limited', limit=0.2),
]

kit_limits_8 = [
    plugin(limitKit, team=1, slot=1, kit='GW_StG44Assault_Limited', limit=0.2),
    plugin(limitKit, team=1, slot=3, kit='GW_LMG_MG42_Limited', limit=0.1),
    plugin(limitKit, team=2, slot=3, kit='RE_LMG_Limited', limit=0.1),
    plugin(limitKit, team=1, slot=4, kit='GW_VG45Assault_Limited', limit=0.1),
    plugin(limitKit, team=2, slot=4, kit='RE_SMGAssault_pps43_Limited', limit=0.1),
    plugin(limitKit, team=1, slot=5, kit='GW_SMGAssault_mp717(r)_Limited', limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="RE_SMGAssault_Late_Limited", limit=0.1),
]

# Links

links_64 = [
    plugin(linkCPs,
           target='Sector_Locker_A',
           source='conq_64_seelow_trainstation, conq_64_road'),
    plugin(linkCPs,
           target='Sector_Locker_B',
           source='conq_64_bridge, conq_64_south_defenses'),
    plugin(linkCPs,
           target='sector_locker_c',
           source='conq_64_seelow, CP_64_seelow_apartments'),
]

# Allies Sector Push

push_64 = [
    plugin(push,
           source='conq_64_seelow_trainstation, conq_64_road',
           target='sector_locker_a',
           attacker=2,
           display_arrow=False,
           wants_target_marker=False),
    plugin(push,
           source='sector_locker_a',
           target='conq_64_bridge, conq_64_south_defenses',
           attacker=2,
           display_arrow=False,
           wants_source_marker=False),
    plugin(push,
           source='conq_64_bridge, conq_64_south_defenses',
           target='sector_locker_b',
           attacker=2,
           display_arrow=False,
           wants_target_marker=False),
    plugin(push,
           source='sector_locker_b',
           target='conq_64_seelow, CP_64_seelow_apartments',
           attacker=2,
           display_arrow=False,
           wants_source_marker=False),
     plugin(push,
           source='conq_64_seelow, CP_64_seelow_apartments',
           target='sector_locker_c',
           attacker=2,
           display_arrow=False,
           wants_source_marker=False),   
]

push_16 = [
    plugin(push,
           source='CP_16_seelow_russianmain',
           target='CP_16_seelow_heights',
           attacker=2,
           display_arrow=False),
    plugin(push,
           source='CP_16_seelow_heights',
           target='CP_16_seelow_apartments',
           attacker=2,
           display_arrow=False),
    plugin(push,
           source='CP_16_seelow_apartments',
           target='CP_16_seelow_church',
           attacker=2,
           display_arrow=False),
    plugin(push,
           source='CP_16_seelow_church',
           target='CP_16_seelow_block',
           attacker=2,
           display_arrow=False),
    plugin(push,
           source='CP_16_seelow_block',
           target='CP_16_seelow_germanmain',
           attacker=2,
           display_arrow=False),
]

# Ticketloss
tickets_cq_64 = [plugin(ticketLoss, ticketLoss1=500, ticketLoss2=15)]

tickets_cq_32 = [plugin(ticketLoss, ticketLoss1=30, ticketLoss2=30)]

tickets_cq_16 = [plugin(ticketLoss, ticketLoss1=500, ticketLoss2=20)]

tickets_cq_8 = [plugin(ticketLoss, ticketLoss1=18, ticketLoss2=18)]

nco_kits = [
    plugin(NCOrifleData,
           kits=('GW_NCO_STG44', 'RE_NCO_45'),
           soldiers=('Gcwhcamo_nco', 're_nco_soldier_telogrieka')),
]

spawns = [
    plugin(teamSPs),    # Auto-fill
]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=1,
        spawner=
        'conq_64_9th_army_kingtiger, conq_64_seelow_stug, conq_64_9th_army_panther, conq_64_9th_army_jagdpanther, conq_64_9th_army_apc, conq_64_9th_army_jgdpz38t,  conq_64_9th_army_stug, conq_64_9th_army_fighter',
        we_dont_own='sector_locker_a'),
    plugin(
        spawnerCondition,
        team=2,
        spawner=
        'conq_64_1st_Belorussian_Front_t34, conq_64_1st_Belorussian_Front_is2, conq_64_1st_Belorussian_Front_su152, conq_64_1st_Belorussian_Front_t34b, conq_64_1st_Belorussian_Front_t34c, conq_64_1st_Belorussian_Front_t34d',
        we_dont_own='sector_locker_b'),
]

# Run plugin settings

gpm_cq = {
    128:
    kit_limits_8 + tickets_cq_8 + nco_kits + spawns,
    64:
    kit_limits + push_64 + tickets_cq_64 + links_64 + nco_kits + spawns +
    spawnerConditions + dynamicoob_64,
    32:
    kit_limits + tickets_cq_32 + nco_kits,
    16:
    kit_limits + nco_kits + tickets_cq_16 + spawns + push_16,
}



disable_AI = [
  plugin(disableSPs),  # Auto-fill
]

Push_AI= [
  plugin(aiPush),  # Push mode
]

spawnerConditions_AI = [
    plugin(
        spawnerCondition,
        team=1,
        spawner=
        'conq_64_9th_army_kingtiger, conq_64_seelow_stug, conq_64_9th_army_panther, conq_64_9th_army_jagdpanther, conq_64_9th_army_apc, conq_64_9th_army_jgdpz38t,  conq_64_9th_army_stug, conq_64_9th_army_fighter',
        we_dont_own='sector_locker_a'),
    plugin(
        spawnerCondition,
        team=2,
        spawner=
        'conq_64_1st_Belorussian_Front_t34, conq_64_1st_Belorussian_Front_is2, conq_64_1st_Belorussian_Front_su152, conq_64_1st_Belorussian_Front_t34b, conq_64_1st_Belorussian_Front_t34c, conq_64_1st_Belorussian_Front_t34d',
        we_dont_own='sector_locker_b'),
]

links_64_AI = [
    plugin(linkCPs,
           target='Sector_Locker_A',
           source='conq_64_seelow_trainstation, conq_64_road'),
    plugin(linkCPs,
           target='Sector_Locker_B',
           source='conq_64_bridge, conq_64_south_defenses'),
    plugin(linkCPs,
           target='sector_locker_c',
           source='conq_64_seelow'),
]


gpm_coop = {
  64: Push_AI + tickets_cq_64 + links_64_AI + spawns + spawnerConditions_AI + nco_kits,
  32: tickets_cq_32 + nco_kits ,
  16: tickets_cq_16 + spawns + Push_AI + nco_kits + disable_AI ,
}


sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
