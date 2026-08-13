# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    push,
    limitKit,
    NCOrifleData,
    spawnerCondition,
    ticketLoss,
    teamSPs,
    neighPush,
    linkCPs,
    disableSPs,
)

push_64 = [
    plugin(
        neighPush,
        sources="CP_64_Ihantala_63rdGuardRifleDiv",
        targets="CP_64_Ihantala_Lakeside,CP_64_Ihantala_Pekarinoja_Bridge,CP_64_Ihantala_Pekarila",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_Pekarinoja_Bridge",
        targets="CP_64_Ihantala_highway",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_Lakeside",
        targets="CP_64_Ihantala_highway",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_Pekarinoja_Bridge",
        targets="CP_64_Ihantala_Lakeside",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_Pekarila",
        targets="CP_64_Ihantala_Pyorakangas",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_Pyorakangas",
        targets="CP_64_Ihantala_Old_Cemetery",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_highway",
        targets="CP_64_Ihantala_Crossroad",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_highway",
        targets="CP_64_Ihantala_Old_Cemetery",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_Old_Cemetery",
        targets="CP_64_Ihantala_Crossroad",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_6thDivVihma",
        targets="CP_64_Ihantala_Old_Cemetery",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_Ammavuori",
        targets="CP_64_Ihantala_Crossroad",
    ),
    plugin(
        neighPush,
        sources="CP_64_Ihantala_JR12_Hanste",
        targets="CP_64_Ihantala_Pyorakangas",
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_Ihantala_268th_Division_Voitulevits",
        target="CP_32_Ihantala_Ruunakorpi",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_Ihantala_Ruunakorpi",
        target="CP_32_Ihantala_Rauhamaki",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_Ihantala_Rauhamaki",
        target="CP_32_Ihantala_Kokkomaki",
        attacker=2,
        display_arrow=True,
    ),
]

push_16 = [
    plugin(
        push,
        source="CP_16_Ihantala_RussianMain",
        target="CP_16_Ihantala_Crossroads",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_Ihantala_Crossroads",
        target="CP_16_Ihantala_Swamps",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_Ihantala_Swamps",
        target="CP_16_Ihantala_Farm",
        attacker=2,
        display_arrow=True,
    ),
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("SE_NCO", "RE_NCO_ihantala"),
        soldiers=("se_sgt", "re_nco_soldier"),
    ),
]

kits_64 = [
    plugin(limitKit, team=1, kit="SE_SMGAssault_Limited", slot=1, limit=0.2),
    plugin(limitKit, team=1, kit="SE_LMG_DP28_Limited,SE_LMG_DP28_Limited_alt,SE_LMG_DP28_Limited_alt2,SE_LMG_DP28_Limited_alt3", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="RE_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="SE_Engineer,SE_Engineer_alt", slot=4, limit=1),
    plugin(limitKit, team=1, kit="SE_AntiTank_Limited", slot=5, limit=0.15),
    plugin(limitKit, team=2, kit="RE_AntitankAssault_pps42_RPG40_limited", slot = 5, limit = 0.08),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=30, ticketLoss2=15)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=12, ticketLoss2=18)]

pco_spawners_64 = [
    # Axis reinforcements
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Ihantala_StuGReinforcemence02_StuG01, CP_64_Ihantala_StuGReinforcemence02_StuG02",
        they_own="CP_64_Ihantala_Pyorakangas",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Ihantala_StuGReinforcemence03_StuH, CP_64_Ihantala_StuGReinforcemence03_StuG01",
        they_own="CP_64_Ihantala_Crossroad",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Ihantala_StuGReinforcemence01_StuG01, CP_64_Ihantala_StuGReinforcemence01_StuG02",
        they_own="CP_64_Ihantala_highway",
    ),
    # Allied tank spawn conditions
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Ihantala_63rdGuardRifleDiv_t34_76_1, CP_64_Ihantala_63rdGuardRifleDiv_t34_76_2, CP_64_Ihantala_63rdGuardRifleDiv_IL2, CP_64_Ihantala_63rdGuardRifleDiv_IS2, CP_64_Ihantala_63rdGuardRifleDiv_ISU152",
        we_dont_own="CP_64_Ihantala_Pekarila, CP_64_Ihantala_Pekarinoja_Bridge, CP_64_Ihantala_Lakeside, CP_64_Ihantala_highway",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Ihantala_Pekarila_t34_76_m43_1, CP_64_Ihantala_Pekarila_t34_76_m43_2",
        we_own="CP_64_Ihantala_Pekarila, CP_64_Ihantala_Pekarinoja_Bridge",
    ),
]

pco_spawners_32 = [
    # Axis reinforcements
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_Ihantala_Rauhamaki_stug1, CP_32_Ihantala_Rauhamaki_stug2",
        we_own="CP_32_Ihantala_Ruunakorpi",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_Ihantala_Detachment_Bjorkman_stug1, CP_32_Ihantala_Detachment_Bjorkman_stug2",
        they_own="CP_32_Ihantala_Ruunakorpi, CP_32_Ihantala_Rauhamaki",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_Ihantala_Detachment_Bjorkman_stuh",
        they_own="CP_32_Ihantala_Ruunakorpi, CP_32_Ihantala_Rauhamaki, CP_32_Ihantala_Kokkomaki, CP_32_Ihantala_268th_Division_Voitulevits",
    ),
    # Allied reinforcements
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_Ihantala_268th_Division_Voitulevits_isu152",
        they_own="CP_32_Ihantala_Ruunakorpi, CP_32_Ihantala_Rauhamaki, CP_32_Ihantala_Kokkomaki",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_Ihantala_268th_Division_Voitulevits_t3485",
        they_own="CP_32_Ihantala_Kokkomaki, CP_32_Ihantala_Rauhamaki",
    ),
]

pco_spawners_16 = [
    # Allied reinforcements
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_16_Ihantala_RussianMain_t34_76",
        they_own="CP_16_Ihantala_Farm, CP_16_Ihantala_Crossroads",
    ),
]

team_spawns = [
    plugin(teamSPs),  # Auto-fill
]


gpm_cq = {
    64: push_64
    + kits_64
    + tickets_64
    + rifleNCO
    + pco_spawners_64
    + team_spawns,
    32: push_32
    + kits_64
    + tickets_32
    + rifleNCO
    + pco_spawners_32
    + team_spawns,
    16: push_16
    + kits_64
    + tickets_16
    + rifleNCO
    + pco_spawners_16
    + team_spawns,
}



disableSPs_32 = [
        plugin(disableSPs, team = 1, cp = 'CP_32_Ihantala_Detachment_Bjorkman', we_own = 'CP_32_Ihantala_Rauhamaki'),
        plugin(disableSPs, team = 1, cp = 'CP_32_Ihantala_Kokkomaki', we_own = 'CP_32_Ihantala_Rauhamaki'),

        plugin(disableSPs, team = 2, cp = 'CP_32_Ihantala_Ruunakorpi', we_own = 'CP_32_Ihantala_Rauhamaki'),
        plugin(disableSPs, team = 2, cp = 'CP_32_Ihantala_Rauhamaki', we_own = 'CP_32_Ihantala_Kokkomaki'),
]

disableSPs_16 = [
        plugin(disableSPs, team = 1, cp = 'CP_16_Ihantala_Swamps', we_own = 'CP_16_Ihantala_Crossroads'),
        plugin(disableSPs, team = 1, cp = 'CP_16_Ihantala_Farm', we_own = 'CP_16_Ihantala_Swamps'),
        plugin(disableSPs, team = 1, cp = 'CP_16_Ihantala_FinnishMain', we_own = 'CP_16_Ihantala_Farm'),


        plugin(disableSPs, team = 2, cp = 'CP_16_Ihantala_RussianMain', we_own = 'CP_16_Ihantala_Crossroads'),
        plugin(disableSPs, team = 2, cp = 'CP_16_Ihantala_Crossroads', we_own = 'CP_16_Ihantala_Swamps'),
        plugin(disableSPs, team = 2, cp = 'CP_16_Ihantala_Swamps', we_own = 'CP_16_Ihantala_Farm'),

]


gpm_coop = {
	64: push_64 + tickets_64 + rifleNCO + pco_spawners_64 + team_spawns,
	32: push_32 + rifleNCO + tickets_32 + pco_spawners_32 + disableSPs_32 + team_spawns,  
	16: push_16 + rifleNCO + tickets_16 + pco_spawners_16 + disableSPs_16 + team_spawns,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
