 # -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    NCOrifleData,
    ticketLoss,
    teamSPs,
    push,
    spawnerCondition,
    disableSPs,
)


rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("SE_NCO", "RE_NCO_tali"),
        soldiers=("se_sgt", "re_nco_soldier"),
    ),
]

rifleNCO_16 = [
    plugin(
        NCOrifleData,
        kits=("SE_NCO", "RE_NCO_ihantala"),
        soldiers=("se_sgt", "re_nco_soldier"),
    ),
]

kits_16 = [
    plugin(limitKit, team=1, kit="SE_SMGAssault_Limited", slot=1, limit=0.2),
    plugin(limitKit, team=1, kit="SE_LMG_DP28_Limited,SE_LMG_DP28_Limited_alt,SE_LMG_DP28_Limited_alt2,SE_LMG_DP28_Limited_alt3", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="RE_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="SE_Engineer,SE_Engineer_alt", slot=4, limit=1),
    plugin(limitKit, team=1, kit="SE_AntiTank_Limited", slot=5, limit=0.08),
    plugin(limitKit, team=2, kit="RE_AntitankAssault_ppsh41_RPG40_limited", slot=5, limit=0.08),
]

kits = [
    plugin(limitKit, team=2, kit="RE_Scout_AVT40_limited", slot=0, limit=0.2),
    plugin(limitKit, team=1, kit="SE_SMGAssault_Limited", slot=1, limit=0.2),
    plugin(limitKit, team=1, kit="SE_LMG_DP28_Limited,SE_LMG_DP28_Limited_alt,SE_LMG_DP28_Limited_alt2,SE_LMG_DP28_Limited_alt3", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="RE_LMG_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="SE_Engineer,SE_Engineer_alt", slot=4, limit=1),
    plugin(limitKit, team=1, kit="SE_AntiTank_Limited", slot=5, limit=0.08),
    plugin(limitKit, team=2, kit="RE_AntitankAssault_ppsh41_RPG40_limited", slot=5, limit=0.08),
]

pco_spawners_64 = [
    # Axis reinforcements
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_tali_finnish_armoured_division_lagus_kv1, CP_64_tali_finnish_armoured_division_lagus_t50, CP_64_tali_finnish_armoured_division_lagus_t34",
        they_own="CP_64_tali_portinhoikka",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_tali_JR6_Inkinen_stug_5, CP_64_tali_JR6_Inkinen_stug_6",
        they_own="CP_64_tali_portinhoikka, CP_64_tali_murokallio, CP_64_tali_hiihkallio, CP_64_tali_konkkalanvuoret, CP_64_tali_kolhi_farmstead",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_tali_finnish_armoured_division_lagus_isu, CP_64_tali_finnish_armoured_division_lagus_t3485",
        they_own="CP_64_tali_murokallio, CP_64_tali_hiihkallio, CP_64_tali_konkkalanvuoret, CP_64_tali_kolhi_farmstead",
    ),
    # Allied tank spawn conditions
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_tali_45th_Guards_Rifle_Division_Putilov_isu152_1, CP_64_tali_45th_Guards_Rifle_Division_Putilov_IS2",
        they_own="CP_64_tali_portinhoikka",
    ),
]
pco_spawners_32 = [
    # Axis reinforcements
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_tali_finnish_armoured_division_lagus_kv1, CP_32_tali_finnish_armoured_division_lagus_t3485",
        we_own="CP_32_tali_tali_village_approach",
    ),
    # Allied tank spawn conditions
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_tali_45th_Guards_Rifle_Division_Putilov_t34_1, CP_32_tali_45th_Guards_Rifle_Division_Putilov_t34_2",
        they_own="CP_32_tali_murokallio_corridor",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_tali_45th_Guards_Rifle_Division_Putilov_t34_10, CP_32_tali_45th_Guards_Rifle_Division_Putilov_t34_11",
        they_own="CP_32_tali_murokallio_corridor, CP_32_tali_open_fields",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_tali_45th_Guards_Rifle_Division_Putilov_t34_3, CP_32_tali_45th_Guards_Rifle_Division_Putilov_t34_4, CP_32_tali_45th_Guards_Rifle_Division_Putilov_t34_5, CP_32_tali_45th_Guards_Rifle_Division_Putilov_t34_6",
        they_own="CP_32_tali_highway",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_tali_45th_Guards_Rifle_Division_Putilov_t34_9",
        they_own="CP_32_tali_flank",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_tali_45th_Guards_Rifle_Division_Putilov_isu152",
        they_own="CP_32_tali_highway, CP_32_tali_flank",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_tali_45th_Guards_Rifle_Division_Putilov_is2",
        they_own="CP_32_tali_tali_village_approach",
    ),
]
pco_spawners_16 = [
    # Axis reinforcements
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_16_tali_11th_Division_Heiskanen_kv1",
        they_own="CP_16_tali_nuoralampi_stream",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_16_tali_11th_Division_Heiskanen_stug1, CP_16_tali_11th_Division_Heiskanen_stug2, CP_16_tali_11th_Division_Heiskanen_finnish_isu",
        they_own="CP_16_tali_portinhoikka",
    ),
    # Allied tank spawn conditions
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_16_tali_46th_Division_Borstsjov_isu",
        they_own="CP_16_tali_viipuri_highway",
    ),
]


push_32 = [
    plugin(
        push,
        source="CP_32_tali_finnish_armoured_division_lagus",
        target="CP_32_tali_murokallio_corridor",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_tali_murokallio_corridor",
        target="CP_32_tali_open_fields",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_tali_open_fields",
        target="CP_32_tali_highway, CP_32_tali_flank",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_tali_highway, CP_32_tali_flank",
        target="CP_32_tali_tali_village_approach",
        attacker=1,
        display_arrow=True,
    ),
]

push_16 = [
    plugin(
        push,
        source="CP_16_tali_46th_Division_Borstsjov",
        target="CP_16_tali_viipuri_highway",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_tali_viipuri_highway",
        target="CP_16_tali_nuoralampi_stream",
        attacker=2,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_16_tali_nuoralampi_stream",
        target="CP_16_tali_portinhoikka",
        attacker=2,
        display_arrow=True,
    ),
]
tickets_64 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=15)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=15)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=10)]
team_spawns = [
    plugin(teamSPs),  # Auto-fill
]

gpm_cq = {
    64: kits + tickets_64 + rifleNCO + team_spawns + pco_spawners_64,
    32: kits
    + tickets_32
    + rifleNCO
    + team_spawns
    + push_32
    + pco_spawners_32,
    16: kits_16
    + tickets_16
    + rifleNCO_16
    + team_spawns
    + push_16
    + pco_spawners_16,
}


disableSPs_16 = [
        plugin(disableSPs, team = 2, cp = 'CP_16_tali_viipuri_highway', we_own = 'CP_16_tali_nuoralampi_stream'),

]

disableSPs_32 = [
        plugin(disableSPs, team = 1, cp = 'CP_32_tali_murokallio_corridor', we_own = 'CP_32_tali_open_fields'),
        plugin(disableSPs, team = 1, cp = 'CP_32_tali_open_fields', we_own = 'CP_32_tali_highway, CP_32_tali_flank'),
        plugin(disableSPs, team = 1, cp = 'CP_32_tali_highway', we_own = 'CP_32_tali_tali_village_approach'),
        plugin(disableSPs, team = 1, cp = 'CP_32_tali_flank', we_own = 'CP_32_tali_tali_village_approach'),

        plugin(disableSPs, team = 2, cp = 'CP_32_tali_open_fields', we_own = 'CP_32_tali_murokallio_corridor'),
        plugin(disableSPs, team = 2, cp = 'CP_32_tali_highway', we_own = 'CP_32_tali_open_fields'),
        plugin(disableSPs, team = 2, cp = 'CP_32_tali_flank', we_own = 'CP_32_tali_open_fields'),
        plugin(disableSPs, team = 2, cp = 'CP_32_tali_tali_village_approach', we_own = 'CP_32_tali_highway, CP_32_tali_flank'),
]


gpm_coop = {
64: tickets_64 + rifleNCO + team_spawns + pco_spawners_64,
32: rifleNCO + tickets_32 + team_spawns + push_32 + disableSPs_32 + pco_spawners_32,
16: rifleNCO_16 + tickets_16 + team_spawns + push_16 + disableSPs_16 + pco_spawners_16,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop

