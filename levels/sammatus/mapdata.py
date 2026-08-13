# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    push,
    NCOrifleData,
    teamSPs,
    spawnerCondition,
    ticketLoss,
    linkCPs,
)

kits_64 = [
    plugin(limitKit, team=1, kit="SE_SMGAssault_Limited", slot=1, limit=0.2),
    plugin(
        limitKit,
        team=1,
        kit="SE_LMG_DP28_Limited,SE_LMG_DP28_Limited_alt,SE_LMG_DP28_Limited_alt2,SE_LMG_DP28_Limited_alt3",
        slot=3,
        limit=0.15,
    ),
    plugin(limitKit, team=2, kit="RE_LMG_Limited", slot=3, limit=0.15),
    plugin(limitKit, team=1, kit="SE_Engineer,SE_Engineer_alt", slot=4, limit=1),
    plugin(limitKit, team=1, kit="SE_AntiTank_Limited", slot=5, limit=0.2),
]

push_64 = [
    plugin(
        push,
        source="conq_64_37th_Guards_Army_Corp_Mironov",
        target="conq_64_vt_line_east",
        attacker=2,
    ),
    plugin(
        push,
        source="conq_64_37th_Guards_Army_Corp_Mironov",
        target="conq_64_vt_line_center",
        attacker=2,
    ),
    plugin(
        push,
        source="conq_64_37th_Guards_Army_Corp_Mironov",
        target="conq_64_vt_line_west",
        attacker=2,
    ),
    plugin(
        push,
        source="conq_64_vt_line_east, conq_64_vt_line_center",
        target="conq_64_Sammatus_village",
        attacker=2,
    ),
    plugin(
        push,
        source="conq_64_vt_line_center ,conq_64_vt_line_west",
        target="conq_64_Lakehouse",
        attacker=2,
    ),
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("SE_NCO", "RE_NCO"),
        soldiers=("se_sgt", "re_nco_soldier"),
    ),
]

tickets_16 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=16, ticketLoss2=16)]

tickets_64 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]


spawns_64 = [
    plugin(teamSPs),  # Auto-fill
]

spawns_32 = [
    plugin(
        teamSPs,
        sps=[
            "CP_32_sammatus_east_dummy_axis_1",
            "CP_32_sammatus_east_dummy_axis_2",
            "CP_32_sammatus_east_dummy_axis_3",
            "CP_32_sammatus_east_dummy_axis_4",
            "CP_32_sammatus_middle_dummy_axis_1",
            "CP_32_sammatus_middle_dummy_axis_2",
            "CP_32_sammatus_middle_dummy_axis_3",
            "CP_32_sammatus_middle_dummy_axis_4",
            "CP_32_sammatus_west_dummy_axis_1",
            "CP_32_sammatus_west_dummy_axis_2",
            "CP_32_sammatus_west_dummy_axis_3",
            "CP_32_sammatus_west_dummy_axis_4",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_32_sammatus_east_dummy_allies_1",
            "CP_32_sammatus_east_dummy_allies_2",
            "CP_32_sammatus_east_dummy_allies_3",
            "CP_32_sammatus_east_dummy_allies_4",
            "CP_32_sammatus_middle_dummy_allies_1",
            "CP_32_sammatus_middle_dummy_allies_2",
            "CP_32_sammatus_middle_dummy_allies_3",
            "CP_32_sammatus_middle_dummy_allies_4",
            "CP_32_sammatus_west_dummy_allies_1",
            "CP_32_sammatus_west_dummy_allies_2",
            "CP_32_sammatus_west_dummy_allies_3",
            "CP_32_sammatus_west_dummy_allies_4",
        ],
        team=2,
    ),
]
spawns_16 = [
    plugin(teamSPs),  # Auto-fill
]

spawnerConditions_64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="conq_64_37th_Guards_Army_Corp_Mironov_t34, conq_64_37th_Guards_Army_Corp_Mironov_t34b",
        we_dont_own="conq_64_vt_line_east and conq_64_vt_line_center and conq_64_vt_line_west",
    ),
]

spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_sammatus_sammatus_village_t20_1, CP_32_sammatus_sammatus_village_t20_2",
        we_dont_own="CP_32_sammatus_bleed_dummy",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_sammatus_37th_guards_army_corp_mironov_t34, CP_32_sammatus_37th_guards_army_corp_mironov_su76",
        we_dont_own="CP_32_sammatus_bleed_dummy",
    ),
]

links_bleed32 = [
    plugin(
        linkCPs,
        target="CP_32_sammatus_bleed_dummy",
        source=[
            "CP_32_sammatus_ammostorage",
            "CP_32_sammatus_mainroad",
            "CP_32_sammatus_mgnest",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_32_sammatus_bleed_dummy",
        source=[
            "CP_32_sammatus_pakposition",
            "CP_32_sammatus_mainroad",
            "CP_32_sammatus_mgnest",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_32_sammatus_bleed_dummy",
        source=[
            "CP_32_sammatus_pakposition",
            "CP_32_sammatus_ammostorage",
            "CP_32_sammatus_mgnest",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_32_sammatus_bleed_dummy",
        source=[
            "CP_32_sammatus_pakposition",
            "CP_32_sammatus_ammostorage",
            "CP_32_sammatus_mainroad",
        ],
    ),
]

links_spawn32 = [
    plugin(
        linkCPs,
        target="CP_32_sammatus_west_dummy",
        source=["CP_32_sammatus_pakposition", "CP_32_sammatus_ammostorage"],
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_32_sammatus_middle_dummy",
        source=["CP_32_sammatus_ammostorage", "CP_32_sammatus_mainroad"],
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_32_sammatus_east_dummy",
        source=["CP_32_sammatus_mainroad", "CP_32_sammatus_mgnest"],
        default_zero=True,
    ),
]

gpm_cq = {
    64: kits_64 + push_64 + spawns_64 + spawnerConditions_64 + rifleNCO + tickets_64,
    32: spawns_32
    + spawnerConditions_32
    + links_bleed32
    + links_spawn32
    + kits_64
    + tickets_32
    + rifleNCO,
    16: spawns_16 + kits_64 + tickets_16 + rifleNCO,
}

gpm_coop = {
    64: push_64 + spawns_64 + spawnerConditions_64 + rifleNCO + tickets_64,
    16: spawns_16 + tickets_16 + rifleNCO,
}

sp1 = gpm_coop
sp3 = gpm_coop
