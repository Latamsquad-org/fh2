# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    aiPush,
    delaySpawners,
    disableSPs,
    limitKit,
    NCOrifleData,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    timeCP,
    DoubleBleed,
    neighPush,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO"),
        soldiers=("GcWhCamo_nco", "uc_fall44_28th_sgt"),
    )
]

kits_64 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_SMGAssault_Limited",
        slot=1,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_Limited",
        slot=1,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_MG42_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault60m_Limited",
        slot=5,
        limit=0.05,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankAssault_Limited",
        slot=5,
        limit=0.05,
    ),
]

kits_32 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_SMGAssault_Limited",
        slot=1,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_Limited",
        slot=1,
        limit=0.13,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_MG42_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited",
        slot=3,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault60m_Limited",
        slot=5,
        limit=0.05,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankAssault_Limited",
        slot=5,
        limit=0.05,
    ),
]

kits_16 = [
    plugin(
        limitKit,
        team=1,
        kit="GW_SMGAssault_Limited",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_SMGAssault_Limited",
        slot=1,
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_LMG_MG42_Limited",
        slot=3,
        limit=0.05,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_LMG_Limited_nobipod",
        slot=3,
        limit=0.05,
    ),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault60m_Limited",
        slot=5,
        limit=0.05,
    ),
    plugin(
        limitKit,
        team=2,
        kit="UW_AntitankAssault_Limited",
        slot=5,
        limit=0.05,
    ),
]

push_32 = [
    plugin(
        neighPush,
        sources="CP_32_vo_germeter",
        targets="CP_32_vo_church,CP_32_vo_kalltrail",
    ),
    plugin(
        neighPush,
        sources="CP_32_vo_church,CP_32_vo_kalltrail",
        targets="CP_32_vo_unterdorf",
    ),
]

extra_64 = [
    plugin(teamSPs),
    plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20),
]
extra_32 = [
    plugin(teamSPs),
    plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15),
    plugin(DoubleBleed),
]
extra_16 = [
    plugin(teamSPs),
    plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000),
]


kits_64_bots = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=5.0 / 32.0,
        kit="GW_Scout_G43",
        soldier="GcWhCamo_splitter",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=5.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="GcWhCamo_splitter",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=6.0 / 32.0,
        kit="GW_RifleAssault",
        soldier="GcWhCamo_sumpf",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GW_LMG_MG42_Limited",
        soldier="GcWhCamo_sumpf",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=5.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="GcWhCamo_splitter",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=6.0 / 32.0,
        kit="GW_AntitankAssault60m_Limited",
        soldier="GcWhCamo_sumpf_splitter",
    ),
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="UW_Scout",
        soldier="uc_fall44_army_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=5.0 / 32.0,
        kit="UW_SMGAssault_Limited",
        soldier="uc_fall44_army_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=7.0 / 32.0,
        kit="UW_RifleAssault",
        soldier="uc_fall44_army_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uc_fall44_army_cpl_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=5.0 / 32.0,
        kit="UW_Engineer_Satchel",
        soldier="uc_fall44_28th_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=6.0 / 32.0,
        kit="UW_AntitankAssault_Limited",
        soldier="uc_fall44_28th_cpl",
    ),
]

coop_16 = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout",
        soldier="GcWhCamo_splitter",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=7.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="GcWhCamo_splitter",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=10.0 / 32.0,
        kit="GW_RifleAssault_G43",
        soldier="GcWhCamo_sumpf",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GW_LMG_MG42_Limited",
        soldier="GcWhCamo_sumpf",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="GcWhCamo_splitter",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=2.0 / 32.0,
        kit="GW_AntitankAssault60m_Limited",
        soldier="GcWhCamo_sumpf_splitter",
    ),
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="UW_Scout",
        soldier="uc_fall44_army_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=7.0 / 32.0,
        kit="UW_SMGAssault_Limited",
        soldier="uc_fall44_army_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=10.0 / 32.0,
        kit="UW_RifleAssault_noNadeLauncher",
        soldier="uc_fall44_army_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="UW_LMG_Limited_nobipod",
        soldier="uc_fall44_army_cpl_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="UW_Engineer_Satchel",
        soldier="uc_fall44_28th_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=2.0 / 32.0,
        kit="UW_AntitankAssault_Limited",
        soldier="uc_fall44_28th_cpl",
    ),
    plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20),
    plugin(
        disableSPs,
        team=1,
        cp="CP_16_vo_south",
        we_own="CP_16_vo_axis_dummy",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_16_vo_north",
        we_own="CP_16_vo_allied_dummy",
    ),
    plugin(timeCP, team=-1, target="CP_16_vo_axis_dummy", time=60),
    plugin(timeCP, team=-1, target="CP_16_vo_allied_dummy", time=60),
]

coop_32 = []
coop_64 = [
    plugin(teamSPs),
    plugin(disableSPs),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_vo_germeter",
        we_own="CP_64_vo_hof or CP_64_vo_oberdorf",
    ),
    plugin(aiPush),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_vo_unterdorf_mg1",
        they_own="CP_64_vo_church",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_vo_kreuzheck_wurfgerat1",
        they_own="CP_64_vo_unterdorf or CP_64_vo_church",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_vo_church_stug",
        we_own="CP_64_vo_hof or CP_64_vo_oberdorf",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "CP_64_vo_kreuzheck_panzer41,CP_64_vo_kreuzheck_stug,"
            "CP_64_vo_kreuzheck_kuebelwagen,CP_64_vo_kreuzheck_apc3"
        ),
        we_dont_own=(
            "CP_64_vo_unterdorf or CP_64_vo_kalltrail" " or CP_64_vo_church"
        ),
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=("CP_64_vo_germeter_howitzer1,CP_64_vo_germeter_howitzer2"),
        they_own="CP_64_vo_hof or CP_64_vo_oberdorf",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_vo_hof_6pdr,CP_64_vo_oberdorf_atgun",
        they_own="CP_64_vo_church",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_vo_church_m10",
        we_own="CP_64_vo_unterdorf or CP_64_vo_kalltrail",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "CP_64_vo_germeter_tank,CP_64_vo_germeter_tank3,"
            "CP_64_vo_germeter_apc3"
        ),
        we_dont_own=("CP_64_vo_hof or CP_64_vo_oberdorf or CP_64_vo_church"),
    ),
    plugin(
        delaySpawners,
        spawners=(
            "CP_64_vo_germeter_tank1,CP_64_vo_germeter_sherman76,"
            "CP_64_vo_germeter_tank3,CP_64_vo_germeter_m3a1,"
            "CP_64_vo_kreuzheck_panzer41,CP_64_vo_kreuzheck_kt1,"
            "CP_64_vo_kreuzheck_wespe_0,"
            "CP_64_vo_kreuzheck_kuebelwagen,"
            "CP_64_vo_kreuzheck_apc3"
        ),
    ),
]

gpm_cq = {
    64: kits_64 + extra_64 + nco,
    32: kits_32 + push_32 + extra_32 + nco,
    16: kits_16 + extra_16 + nco,
}
gpm_coop = {
    64: kits_64_bots + coop_64 + nco,
    16: coop_16 + nco,
}

sp3 = gpm_coop
sp1 = gpm_coop
