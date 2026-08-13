from game.plugins import ( 
plugin, 
limitKit, 
ticketLoss,
linkCPs,
push,
teamSPs, 
NCOrifleData
)

kits_64 = [
    plugin(
        limitKit, team=1, kit="GW_SMGAssault_Limited", slot=1, limit=0.2
    ),
    plugin(
        limitKit, team=2, kit="UW_SMGAssault_Limited", slot=1, limit=0.2
    ),
    plugin(
        limitKit, team=1, kit="GW_LMG_Limited", slot=3, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="UW_MG_30cal_Limited", slot=3, limit=0.1
    ),
    plugin(
        limitKit, team=1, kit="GW_Engineer_Satchel_Limited", slot=4, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="UW_Engineer_Satchel_Ramelle", slot=4, limit=0.1
    ),
    plugin(
        limitKit, team=1, kit="GW_AntitankAssault_Limited", slot=5, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="UW_AntitankAssault_Limited", slot=5, limit=0.1
    ),
]

kits_16 = [
    plugin(
        limitKit, team=1, kit="GW_SMGAssault_Limited", slot=1, limit=0.2
    ),
    plugin(
        limitKit, team=2, kit="UW_SMGAssault_Limited", slot=1, limit=0.2
    ),
    plugin(
        limitKit, team=1, kit="GW_LMG_Limited", slot=3, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="UW_MG_30cal_Limited", slot=3, limit=0.1
    ),
    plugin(
        limitKit, team=1, kit="GW_Engineer_Satchel_Limited", slot=4, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="UW_Engineer_Satchel_Ramelle", slot=4, limit=0.1
    ),
    plugin(
        limitKit, team=1, kit="GW_RifleAssault_Limited", slot=5, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="UW_Grenadier_Limited", slot=5, limit=0.1
    ),
]

linkCPs_32 = [
    plugin(
        linkCPs,
        target="CP_32_la_fiere_sector1",
        source="CP_32_la_fiere_hameauauxbrix, CP_32_la_fiere_cauquigny",
    ),
    plugin(
        linkCPs,
        target="CP_32_la_fiere_sector2",
        source="CP_32_la_fiere_causeway",
    ),
    plugin(
        linkCPs,
        target="CP_32_la_fiere_sector3",
        source="CP_32_la_fiere_la_fiere, CP_32_la_fiere_505th_PIR",
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_la_fiere_1057th_Grenadier_Regiment",
        target="CP_32_la_fiere_hameauauxbrix, CP_32_la_fiere_cauquigny",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_la_fiere_hameauauxbrix, CP_32_la_fiere_cauquigny",
        target="CP_32_la_fiere_sector1",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_32_la_fiere_sector1",
        target="CP_32_la_fiere_causeway",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_32_la_fiere_causeway",
        target="CP_32_la_fiere_sector2",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_32_la_fiere_sector2",
        target="CP_32_la_fiere_la_fiere, CP_32_la_fiere_505th_PIR",
        attacker=1,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_32_la_fiere_la_fiere, CP_32_la_fiere_505th_PIR",
        target="CP_32_la_fiere_sector3",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
]



tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=9999)]

tickets_64 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO_SME"),
        soldiers=("gw_heer_unteroffizier", "uw_airborne_sgt"),
    )
]

gpm_cq = {
16: tickets_16
  + kits_16
  + spawns
  + nco,
32: tickets_32
  + kits_64
  + spawns
  + nco
  + push_32
  + linkCPs_32,
64: tickets_64
  + kits_64
  + spawns
  + nco,
}
