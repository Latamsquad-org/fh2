# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302,E0401
from game.plugins import (
    plugin,
    teamSPs,
    limitKit,
    ticketLoss,
    spawnerCondition,
    push,
    # delaySpawners,
    timeCP,
    NCOrifleData,
    linkCPs,
    dynamicOOB,
    disableSPs,
)

#

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_STG44", "FW_NCO"),
        soldiers=("GcWhCamo_nco", "fw_late1944_1rtm_nco"),
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

kitlimits_64 = [
    plugin(limitKit, team=1, kit="GW_SMGAssault_mp738(i)_Limited", slot=1, limit=0.13),
    plugin(limitKit, team=2, kit="FW_SMGAssault_Limited", slot=1, limit=0.13),
    plugin(limitKit, team=1, kit="GW_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="FW_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="GW_AntitankAssault60m_Limited", slot=5, limit=0.05),
    plugin(limitKit, team=1, kit="GW_Engineer_Satchel_limited_alt", slot=4, limit=0.07),
    plugin(limitKit, team=2, kit="FW_AntitankAssault_Limited", slot=5, limit=0.05),
]

kitlimits_16 = [
    plugin(limitKit, team=1, kit="GW_SMGAssault_mp738(i)_Limited", slot=1, limit=0.13),
    plugin(limitKit, team=2, kit="FW_SMGAssault_Limited", slot=1, limit=0.13),
    plugin(limitKit, team=1, kit="GW_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="FW_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="GW_RifleAssault_G41_Limited", slot=4, limit=0.1),
    plugin(limitKit, team=2, kit="FW_CarbineAssault_Limited", slot=4, limit=0.1),
    plugin(limitKit, team=1, kit="GW_AntitankAssault60m_Limited", slot=5, limit=0.05),
    plugin(limitKit, team=2, kit="FW_Grenadier_Limited", slot=5, limit=0.05),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=30)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=15)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

tickets_8 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]

spawndelay_64 = [
    plugin(
        timeCP,
        team=-1,
        target="cp_64_la_hardt_french_forwardspawns",
        time=45,
    ),
]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="cp_64_la_hardt_pont_du_bouc_M10_2",
        we_dont_own="cp_64_la_hardt_point_232",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="cp_64_la_hardt_pont_du_bouc_M10_3",
        we_dont_own="cp_64_la_hardt_mulhouse_canal",
    ),

]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="cp_64_la_hardt_sectorlock1dummy",
        source="cp_64_la_hardt_point_232, cp_64_la_hardt_grunhutte, cp_64_la_hardt_mulhouse_canal",
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "cp_64_la_hardt_sectorlock1dummy": {
                "axis": {
                    "creates": ["yesgoB_cq_64"],
                    "destroys": ["yesgo1_cq_64"],
                },
            },
        },
        inactive_at_start=["yesgoB_cq_64"],
        delay_allies=45,
        delay_axis=0,
    )
]

push_64 = [
    plugin(
        push,
        source="cp_64_la_hardt_19_armee",
        target="cp_64_la_hardt_point_232, cp_64_la_hardt_grunhutte, cp_64_la_hardt_mulhouse_canal",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="cp_64_la_hardt_point_232, cp_64_la_hardt_grunhutte, cp_64_la_hardt_mulhouse_canal",
        target="cp_64_la_hardt_sectorlock1dummy",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="cp_64_la_hardt_sectorlock1dummy",
        target="cp_64_la_hardt_allee_centrale, cp_64_la_hardt_allee_de_la_fontaine, cp_64_la_hardt_zimmerplan",
        attacker=1,
        display_arrow=False,
    ),
]

push_32 = [
    plugin(
        push,
        source="cp_32_la_hardt_ottmarsheim_road",
        target="cp_32_la_hardt_pont_du_bouc, cp_32_la_hardt_zimmerplan",
        attacker=1,
        display_arrow=False,
    ),
]

spawndelay_32 = [
    plugin(
        timeCP,
        team=-1,
        target="cp_32_la_hardt_forward_spawnpoints",
        time=45,
    ),
]

links_32 = [
    plugin(
        linkCPs,
        target="cp_la_hardt_32_reinforcements_dummy",
        source=[
            "cp_32_la_hardt_pont_du_bouc", "cp_32_la_hardt_zimmerplan", "cp_32_la_hardt_ottmarsheim_road",
        ],
        invert=True,
    ),]

gpm_cq = {
    64: tickets_64
    + kitlimits_64
    + rifleNCO
    + spawns
    + spawndelay_64
    + linkCPs_64
    + push_64
    + spawnerConditions
    + dynamicoob_64,
    32: tickets_32 + kitlimits_64 + spawns + spawndelay_32 + push_32 + rifleNCO + links_32,
    16: tickets_16 + kitlimits_16 + rifleNCO,
    128 : kitlimits_16 + tickets_8 + rifleNCO,
}


disable_AI = [
    plugin(disableSPs),  # Auto-fill
]

spawndelay_64 = [
    plugin(
        timeCP,
        team=-1,
        target="cp_64_la_hardt_forward_spawnpoints",
        time=45,
    ),
]


push_32 = [
    plugin(
        push,
        source="cp_32_la_hardt_ottmarsheim_road",
        target="cp_32_la_hardt_pont_du_bouc, cp_32_la_hardt_zimmerplan",
        attacker=1,
        display_arrow=False,
    ),
]


push_64_coop = [
    plugin(
        push,
        source="cp_64_la_hardt_19_armee",
        target="cp_64_la_hardt_point_232",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="cp_64_la_hardt_point_232",
        target="cp_64_la_hardt_allee_de_la_fontaine",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="cp_64_la_hardt_allee_de_la_fontaine",
        target="cp_64_la_hardt_zimmerplan",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="cp_64_la_hardt_zimmerplan",
        target="cp_64_la_hardt_pont_du_bouc",
        attacker=1,
        display_arrow=True,
    ),
]

tickets_64_coop = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=15)]


spawnerCondition_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="cp_32_la_hardt_xix_armee_pz4_2",
        they_own="cp_32_la_hardt_zimmerplan",
    ),]

gpm_coop = {
    32: tickets_32 + spawns + push_32 + rifleNCO + spawndelay_32 + spawnerCondition_32 + links_32,
    64: tickets_64_coop + spawns + push_64_coop + rifleNCO,
}

sp2 = gpm_coop
sp3 = gpm_coop
