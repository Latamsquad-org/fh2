# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    push,
    teamSPs,
    spawnerCondition,
    ticketLoss,
    disableSPs,
    aiPush,
    NCOrifleData,
    DoubleBleed,
)

bleed_16 = [
    plugin(DoubleBleed),
]

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "BW_NCO_colt"),
        soldiers=("gw_heer_unteroffizier", "bw_nco_marines"),
    )
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.25),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="BW_SMGAssault_m1928a1_Limited",
        limit=0.25,
    ),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Colt_Limited", limit=0.15),
    plugin(
        limitKit, team=1, slot=5, kit="GW_RifleAssault_G41_Limited", limit=0.04
    ),
    plugin(limitKit, team=2, slot=5, kit="BW_CommandoStenMK2S", limit=0.1),
]

kitlimits_32 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.25),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="BW_SMGAssault_m1928a1_Limited",
        limit=0.25,
    ),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Colt_Limited", limit=0.15),
    plugin(
        limitKit, team=1, slot=5, kit="GW_RifleAssault_G41_Limited", limit=0.04
    ),
    plugin(limitKit, team=2, slot=5, kit="BW_CommandoStenMK2S", limit=0.1),
]

push_64 = [
    plugin(
        push,
        source="cq64_roadtocommes",
        target="cq64_shipyard",
        attacker=2,
    ),
    plugin(
        push,
        source="cq64_roadtoescures",
        target="cq64_church",
        attacker=2,
    ),
    plugin(
        push,
        source="cq64_shipyard",
        target="cq64_wn56",
        attacker=2,
    ),
    plugin(
        push,
        source=["cq64_church", "cq64_shipyard", "cq64_wn56"],
        target="cq64_outskirts",
        attacker=2,
        force=True,
        count=2,
    ),
    plugin(
        push,
        source=["cq64_outskirts", "cq64_wn56"],
        target="cq64_portenbessin",
        attacker=2,
    ),
    plugin(
        push,
        source=["cq64_outskirts", "cq64_portenbessin"],
        target="cq64_wn57",
        attacker=2,
    ),
]
push_32 = [
    plugin(
        push,
        source="CP_32_peb_roadtoescures",
        target="CP_32_peb_church",
        attacker=2,
    ),
    plugin(
        push,
        source=["CP_32_peb_church"],
        target="CP_32_peb_outskirts",
        attacker=2,
    ),
    plugin(
        push,
        source=["CP_32_peb_outskirts"],
        target="CP_32_peb_portenbessin",
        attacker=2,
    ),
    plugin(
        push,
        source=["CP_32_peb_outskirts", "CP_32_peb_portenbessin"],
        target="CP_32_peb_wn57",
        attacker=2,
    ),
]


spawner_cond_64 = [
    plugin(
        spawnerCondition,
        spawner="cq64_wn57_stug",
        team=1,
        they_own="cq64_church and cq64_shipyard",
    ),
]
spawner_cond_32 = [
    plugin(
        spawnerCondition,
        spawner="CP_32_peb_wn57_stug",
        team=1,
        they_own="CP_32_peb_church and CP_32_peb_outskirts",
    ),
]


tickets_64 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=8)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=8)]


gpm_cq = {
    64: nco + spawns + tickets_64 + kitlimits_64 + push_64 + spawner_cond_64,
    32: nco + spawns + tickets_32 + kitlimits_32 + push_32 + spawner_cond_32,
    16: nco + spawns + kitlimits_64 + bleed_16,
}

coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout",
        soldier="gw_heer_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=5.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="gw_heer_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault_noNadeLauncher",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GW_LMG_Limited",
        soldier="gw_heer_maschinengewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=5.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="GW_RifleAssault_G41_Limited",
        soldier="gw_heer_panzerabwehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="BW_Scout",
        soldier="bw_light_marines",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=5.0 / 32.0,
        kit="BW_SMGAssault_m1928a1_Limited",
        soldier="bw_light_marines",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="BW_RifleAssault",
        soldier="bw_light_marines",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="BW_LMG_Colt_Limited",
        soldier="bw_heavy_marines",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="BW_Engineer_Satchel",
        soldier="bw_heavy_marines",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=5.0 / 32.0,
        kit="BW_CommandoStenMK2S",
        soldier="bw_light_marines",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=2,
        cp="cq64_wn57",
        we_own="cq64_outskirts and cq64_portenbessin",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="cq64_outskirts",
        we_own="cq64_church and cq64_shipyard and cq64_portenbessin and cq64_wn56 and cq64_wn57",
    ),
    # Push mode
    plugin(aiPush),
    # PCO spawning conditions - Axis
    plugin(
        spawnerCondition,
        spawner="cq64_church_mg34",
        team=1,
        we_dont_own="cq64_outskirts",
    ),
    plugin(
        spawnerCondition,
        spawner="cq64_wn56_mg34_0",
        team=1,
        we_dont_own="cq64_portenbessin",
    ),
    plugin(
        spawnerCondition,
        spawner="cq64_wn57_stug",
        team=1,
        they_own="cq64_church and cq64_shipyard",
        they_dont_own="cq64_portenbessin",
    ),
    # plugin(spawnerCondition, spawner = 'cq64_roadtocommes_sherman', team = 2, we_dont_own = 'cq64_church or cq64_shipyard'),
    # Ticket bleed
    plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=10),
]

gpm_coop = {
    64: coop_64 + spawns + nco,
}
sp3 = gpm_coop
