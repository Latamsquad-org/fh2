# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302,E0401
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    push,
    teamSPs,
    spawnerCondition,
    timeCP,
)


kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GM_Limited_Assault_MP40_K98_para", limit=0.2),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="BW_SMGAssault_stenmkiistrut_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit, team=1, slot=3, kit="GA_Limited_Support_MG34_K98", limit=0.05
    ),
    plugin(limitKit, team=2, slot=3, kit="FA_colonial_LMG", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_ggp40_haft", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BW_LMG_Colt_Limited", limit=0.05),
]

kitlimits_32 = [
    plugin(limitKit, team=1, slot=1, kit="GM_Limited_Assault_MP40_K98_para", limit=0.2),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="BA_Assault_m1928a1_30r",
        limit=0.08,
    ),
    plugin(
        limitKit, team=1, slot=3, kit="GA_Limited_Support_MG34_K98", limit=0.05
    ),
    plugin(limitKit, team=2, slot=3, kit="BA_Limited_Support_Bren_No4", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_ggp40_haft", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BA_TankHunter_hawkin_rifle", limit=0.1),
]

kitlimits_16 = [
    plugin(limitKit, team=1, slot=1, kit="GM_Limited_Assault_MP40_K98_para", limit=0.2),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_stenmkiistrut_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GA_Limited_Support_MG34_K98", limit=0.05),
    plugin(limitKit, team=2, slot=3, kit="FA_colonial_LMG", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GW_Riflenadelauncher_ggp40_limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BW_LMG_Colt_Limited", limit=0.05),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=9999, ticketLoss2=15)]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_mid", "FA_standard_NCO"),
        soldiers=("gb_nco_grunmeliert_trop", "fa_nco"),
    ),
]

rifleNCO_32 = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_mid", "BA_NCOTommygunS"),
        soldiers=("gb_nco_grunmeliert_trop", "bw_nco_soldier_alt"),
    ),
]

push_64 = [
    plugin(
        push,
        source="CP_64_meb_axismain1",
        target="CP_64_meb_church, CP_64_meb_entrance, CP_64_meb_cemetery, CP_64_meb_mosque, CP_64_meb_eastbank",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_meb_church, CP_64_meb_entrance, CP_64_meb_cemetery, CP_64_meb_mosque, CP_64_meb_eastbank",
        target="CP_64_meb_westbank",
        attacker=1,
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_meb_alliedmain",
        target="CP_32_meb_westbank",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_meb_westbank",
        target="CP_32_meb_eastbank",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_meb_eastbank",
        target="CP_32_meb_mosque",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_meb_mosque",
        target="CP_32_meb_cemetery",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_32_meb_cemetery",
        target="CP_32_meb_entrance",
        attacker=2,
    ),
]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "CP_32_meb_entrance_axistank, "
        ),
        we_dont_own="CP_32_meb_eastbank",
    ),
]

spawnerConditions_64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_meb_westbank_tank, "
        ),
        we_dont_own="CP_64_meb_church and CP_64_meb_entrance",
    ),
]

spawndelay_64 = [
    plugin(
        timeCP,
        team=-1,
        target="CP_64_meb_entrancedummy",
        time=90,
    ),
    plugin(
        timeCP,
        team=-1,
        target="CP_64_meb_churchdummy",
        time=90,
    ),
]

gpm_cq = {
    64: tickets_64 + kitlimits_64 + rifleNCO + spawns + push_64 + spawndelay_64 + spawnerConditions_64,
    32: tickets_32 + kitlimits_32 + rifleNCO_32 + spawns + push_32 + spawnerConditions,
    16: kitlimits_16 + rifleNCO + spawns,
}

gpm_coop = {
    64: tickets_64 + rifleNCO + spawns + push_64 + spawndelay_64 + spawnerConditions_64,
    32: tickets_32 + rifleNCO_32 + spawns + push_32 + spawnerConditions,
}

sp2 = gpm_coop
sp3 = gpm_coop

