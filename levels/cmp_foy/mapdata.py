from game.plugins import plugin, limitKit, NCOrifleData, ticketLoss, dynamicOOB, push, linkCPs, SectorTickets, spawnerCondition, timeCP

# BEGIN KITLIMITS

kit_limits_64 = [
    plugin(limitKit, team=1, kit="GW_StG44Assault_Limited", slot=1, limit=0.25),
    plugin(limitKit, team=2, kit="UW_SMGAssault_Limited", slot=1, limit=0.25),
    plugin(limitKit, team=1, kit="GW_LMG_MG42_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="UW_LMG_m1919a6_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="GW_AntitankAssault60m_Limited", slot=4, limit=0.15),
    plugin(limitKit, team=2, kit="UW_AntitankAssaultM9_Limited", slot=4, limit=0.08),
]

# END KIT_LIMITS
# BEGIN RIFLENCO

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO_SME"),
        soldiers=("gcwhsnow_nco", "uc_airborne_nco"),
    )
]

# END RIFLENCO
# BEGIN TICKETLOSS

tickets_64 = [plugin(ticketLoss, ticketLoss2=15, ticketLoss1=9999)]
tickets_32 = [plugin(ticketLoss, ticketLoss2=15, ticketLoss1=15)]
tickets_16 = [plugin(ticketLoss, ticketLoss2=1000, ticketLoss1=1000)]
# END TICKETLOSS
# BEGIN LINKCPS

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_sector_A_locker",
        source=[
            "CP_64_cmp_t_foy_Foy",
            "CP_64_cmp_t_foy_Recogne",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_sector_B_locker",
        source=[
            "cp_64_cmp_t_foy_N30_Highway",
            "CP_64_cmp_t_foy_Farm",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_sector_C_locker",
        source=[
            "CP_64_cmp_t_foy_Noville",
            "CP_64_cmp_t_foy_Cobru",
        ],
    ),
]

# END LINKCPS
# BEGIN PUSH

push_64 = [
    plugin(
        push,
        source="CP_64_cmp_t_foy_Easy_Company_506th_PIR, cp_64_cmp_t_foy_GH_Company, cp_64_cmp_t_foy_11th_Armor",
        target="CP_64_cmp_t_foy_Foy, CP_64_cmp_t_foy_Recogne",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_cmp_t_foy_Foy, CP_64_cmp_t_foy_Recogne",
        target="CP_64_Sector_A_Locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Sector_A_Locker",
        target="CP_64_cmp_t_foy_Farm, CP_64_cmp_t_foy_N30_Highway",
        delay=15,
        attacker=2,
        display_arrow=False,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_cmp_t_foy_Farm, CP_64_cmp_t_foy_N30_Highway",
        target="CP_64_Sector_B_Locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Sector_B_Locker",
        target="CP_64_cmp_t_foy_Noville, CP_64_cmp_t_foy_Cobru",
        delay=15,
        attacker=2,
        display_arrow=False
    ),
    plugin(
        push,
        source="CP_64_cmp_t_foy_Noville, CP_64_cmp_t_foy_Cobru",
        target="CP_64_Sector_C_Locker",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
]

# END PUSH
# BEGIN SECTOR TICKETS

Sectortickets_64 = [
    plugin(
        SectorTickets,
        sector_tickets={
            "CP_64_Sector_A_Locker": {"allies":'+200'},
            "CP_64_Sector_B_Locker": {"allies": '+200'},
        },
    )
]

# END SECTOR TICKETS
# BEGIN DYNAMIC OOB

# ALLIED BOUNDARIES
# CombatArea_356_gpm_cq64  // ALLIES MAIN BASE
# CombatArea_104_gpm_cq_64 // ALLIES SECTOR A
# CombatArea_101_gpm_cq_64 // ALLIES SECTOR B // STARTS INACTIVE
# CombatArea_144_gpm_cq_64 // ALLIES SECTOR C // STARTS INACTIVE
#
# AXIS BOUNDARIES
# CombatArea_215_gpm_cq_64 // AXIS SECTOR A
# CombatArea_319_gpm_cq_64 SECTOR B
# CombatArea_263_gpm_cq_64 // AXIS MAIN BASE + SECTOR C
# Delay for Retreating Team (Axis) 45 seconds

dynamicOOB_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_Sector_A_Locker": {
                "allies": {
                    "destroys": ["CombatArea_215_gpm_cq_64"],
                    "creates": ["CombatArea_101_gpm_cq_64"],
                },
            },
            "CP_64_Sector_B_Locker": {
                "allies": {
                   "destroys": ["CombatArea_319_gpm_cq_64"], 
                   "creates": ["CombatArea_144_gpm_cq_64"], 
                },
            },
        },
        inactive_at_start=["CombatArea_101_gpm_cq_64", "CombatArea_144_gpm_cq_64"],
        delay_axis=120,
        delay_allies=0,
    )
]

# END COMBAT BOUNDARIES
# BEGIN SPAWNER CONDITION

spawnerConditions_64 = [
   
 plugin(spawnerCondition, team = 1, spawner = 'cp_64_cmp_t_foy_2nd_SS_Panzer_Division_Panther', we_dont_own = 'CP_64_cmp_t_foy_Recogne, CP_64_cmp_t_foy_Foy'),

 plugin(spawnerCondition, team = 1, spawner = 'cp_64_cmp_t_foy_2nd_SS_Panzer_Division_Stug', we_dont_own = 'CP_64_cmp_t_foy_Recogne, CP_64_cmp_t_foy_Foy'),

 plugin(spawnerCondition, team = 1, spawner = 'cp_64_cmp_t_foy_2nd_SS_Panzer_Division_Panzer4_01', we_dont_own = 'CP_64_cmp_t_foy_Recogne, CP_64_cmp_t_foy_Foy'),

 plugin(spawnerCondition, team = 1, spawner = 'cp_64_cmp_t_foy_2nd_SS_Panzer_Division_Panzer4_02', we_dont_own = 'CP_64_cmp_t_foy_Recogne, CP_64_cmp_t_foy_Foy'),

 plugin(spawnerCondition, team = 2, spawner = 'sherman_75mm', we_own = 'cp_64_cmp_foy_11th_dummy'),

 plugin(spawnerCondition, team = 2, spawner = 'sherman_76mm_01', we_own = 'cp_64_cmp_foy_11th_dummy'),

 plugin(spawnerCondition, team = 2, spawner = 'sherman_76mm_02', we_own = 'cp_64_cmp_foy_11th_dummy'),

 plugin(spawnerCondition, team = 2, spawner = 'hellcat_01', we_own = 'cp_64_cmp_foy_11th_dummy'),

 plugin(spawnerCondition, team = 2, spawner = 'halftrack1', we_own = 'cp_64_cmp_foy_11th_dummy'),

 plugin(spawnerCondition, team = 2, spawner = 'halftrack2', we_own = 'cp_64_cmp_foy_11th_dummy'),

]

# END SPAWNER CONDITION
# BEGIN SPAWN DELAYS

spawndelay_64 = [
    plugin(timeCP, team=2, target="cp_64_cmp_foy_11th_dummy", time=300),
]

gpm_cq = { 
    64:  rifleNCO + kit_limits_64 + tickets_64 + push_64 + linkCPs_64 + dynamicOOB_64 + Sectortickets_64 + spawnerConditions_64 + spawndelay_64,
    32:  rifleNCO + kit_limits_64 + tickets_32, 
    16:  rifleNCO + kit_limits_64 + tickets_16,
}