# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    push,
    teamSPs,
    ticketLoss,
    neighPush,
    NCOrifleData,
    DoubleBleed,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO"),
        soldiers=("gw_heer_unteroffizier", "uw_29th_sgt"),
    )
]

double_bleed_32 = [plugin(DoubleBleed)]

spawns_64 = [
    plugin(
        teamSPs,
        sps=[
            "Villiers_Fossard_Axis_1",
            "Villiers_Fossard_Axis_2",
            "Villiers_Fossard_Axis_3",
            "Les_Foulons_Axis_1",
            "Les_Foulons_Axis_2",
            "Les_Foulons_Axis_3",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "Villiers_Fossard_1",
            "Villiers_Fossard_2",
            "Villiers_Fossard_3",
            "Villiers_Fossard_4",
            "Villiers_Fossard_5",
            "Les_Foulons_1",
            "Les_Foulons_2",
            "Les_Foulons_3",
            "Les_Foulons_4",
            "Les_Foulons_5",
        ],
        team=2,
    ),
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GS_StG44Assault_Limited", limit=0.1875),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited_GGun", limit=0.1875),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_FG42_Limited", limit=0.125),
    plugin(limitKit, team=2, slot=3, kit="UW_LMG_Limited", limit=0.1875),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1875),
    plugin(limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.1875),
]

kitlimits_32 = [
    plugin(limitKit, team=1, slot=1, kit="GS_StG44Assault_Limited", limit=0.1875),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited_GGun", limit=0.1875),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_FG42_Limited", limit=0.125),
    plugin(limitKit, team=2, slot=3, kit="UW_LMG_Limited", limit=0.1875),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1875),
    plugin(limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.1875),
]

kitlimits_16 = [
    plugin(limitKit, team=1, slot=1, kit="GS_StG44Assault_Limited", limit=0.1875),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited_GGun", limit=0.1875),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_FG42_Limited", limit=0.125),
    plugin(limitKit, team=2, slot=3, kit="UW_LMG_Limited", limit=0.1875),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1875),
    plugin(limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.1875),
]

push_64 = [
    plugin(
        neighPush,
        sources="cp_64_stlo_29th_Division",
        targets="cp_64_stlo_Villiers_Fossard,cp_64_stlo_Les_Foulons, cp_64_stlo_Hill_108",
    ),
    plugin(neighPush, sources="cp_64_stlo_Hill_108", targets="cp_64_stlo_Chateau"),
    plugin(
        neighPush,
        sources="cp_64_stlo_Villiers_Fossard",
        targets="cp_64_stlo_Chateau, cp_64_stlo_Church, ,cp_64_stlo_Les_Foulons",
    ),
    plugin(
        neighPush,
        sources="cp_64_stlo_Les_Foulons",
        targets="cp_64_stlo_Church, cp_64_stlo_Windmill, cp_64_stlo_Villiers_Fossard",
    ),
    plugin(neighPush, sources="cp_64_stlo_Chateau", targets="cp_64_stlo_Church"),
    plugin(
        neighPush,
        sources="cp_64_stlo_Church",
        targets="cp_64_stlo_Chateau,cp_64_stlo_Windmill",
    ),
    plugin(neighPush, sources="cp_64_stlo_Windmill", targets="cp_64_stlo_Church"),
    plugin(
        neighPush,
        sources="cp_64_stlo_352_Headquarters",
        targets="cp_64_stlo_Church, cp_64_stlo_Windmill, cp_64_stlo_Chateau",
    ),
]
push_32 = [
    plugin(
        push,
        source="cp_32_stlo_29th_Division",
        target="cp_32_stlo_Villiers_Fossard",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cp_32_stlo_29th_Division",
        target="cp_32_stlo_Les_Foulons",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cp_32_stlo_29th_Division",
        target="cp_32_stlo_Church",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cp_32_stlo_29th_Division",
        target="cp_32_stlo_Chateau",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cp_32_stlo_Church",
        target="cp_32_stlo_352_Headquarters",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cp_32_stlo_Chateau",
        target="cp_32_stlo_352_Headquarters",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cp_32_stlo_Villiers_Fossard",
        target="cp_32_stlo_352_Headquarters",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="cp_32_stlo_Les_Foulons",
        target="cp_32_stlo_352_Headquarters",
        attacker=2,
        display_arrow=False,
    ),
]

tickets = [plugin(ticketLoss, ticketLoss1=8, ticketLoss2=8)]


gpm_cq = {
    64: nco + tickets + kitlimits_64 + push_64 + spawns_64,
    32: nco + tickets + kitlimits_32 + push_32 + double_bleed_32,
    16: nco + tickets + kitlimits_16,
}
gpm_coop = {
    64: nco + push_64 + spawns_64 + tickets,
    32: nco + push_32 + tickets,
    16: nco,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
