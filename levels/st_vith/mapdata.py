# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    aiPush,
    disableSPs,
    dynamicOOB,
    limitKit,
    linkCPs,
    NCOrifleData,
    neighPush,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO_mp40_g43", "UW_NCO"),
        soldiers=("gcwhsnow_nco", "uc_win44_7thAD_sgt"),
    )
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_Stvith_sector_a_locker": {
                "axis": {
                    "creates": ["yesgo_64p_axis_2"],
                    "destroys": ["yesgo_64p_allies_1"],
                },
            },
            "CP_64_Stvith_sector_b_locker": {
                "axis": {
                    "creates": ["yesgo_64p_axis_3"],
                    "destroys": ["yesgo_64p_allies_2"],
                },
            },
            "CP_64_Stvith_sector_c_locker": {
                "axis": {
                    "creates": ["yesgo_64p_axis_4"],
                    "destroys": ["yesgo_64p_allies_3"],
                },
            },
            "CP_64_Stvith_Wiesenbach": {
                "axis": {
                    "destroys": ["yesgo_64p_allies_wiesen"],
                },
            },
        },
        inactive_at_start=[
            "yesgo_64p_axis_2",
            "yesgo_64p_axis_3",
            "yesgo_64p_axis_4",
        ],
        delay_axis=0,
        delay_allies=120,
    )
]

spawns = [
    plugin(
        teamSPs,
        sps=[
            "CP_64_Stvith_Rosenhuegels_Farms_1",
            "CP_64_Stvith_Rosenhuegels_Farms_3",
            "CP_64_Stvith_Rosenhuegels_Farms_5",
            "CP_64_Stvith_Rosenhuegels_Farms_7",
            "CP_64_Stvith_Walleroder_Wood_1",
            "CP_64_Stvith_Walleroder_Wood_3",
            "CP_64_Stvith_Walleroder_Wood_5",
            "CP_64_Stvith_Walleroder_Wood_7",
            "CP_64_Stvith_Friedensstrasse_Bridge_1",
            "CP_64_Stvith_Friedensstrasse_Bridge_3",
            "CP_64_Stvith_Friedensstrasse_Bridge_5",
            "CP_64_Stvith_Friedensstrasse_Bridge_7",
            "CP_64_Stvith_Trainstation_1",
            "CP_64_Stvith_Trainstation_3",
            "CP_64_Stvith_Trainstation_5",
            "CP_64_Stvith_Trainstation_7",
            "CP_64_Stvith_Wiesenbach_1",
            "CP_64_Stvith_Wiesenbach_3",
            "CP_64_Stvith_Wiesenbach_5",
            "CP_64_Stvith_Wiesenbach_7",
            "CP_64_Stvith_Crossroads_1",
            "CP_64_Stvith_Crossroads_3",
            "CP_64_Stvith_Crossroads_5",
            "CP_64_Stvith_Crossroads_7",
            "CP_64_Stvith_Buchler_Turm_1",
            "CP_64_Stvith_Buchler_Turm_3",
            "CP_64_Stvith_Buchler_Turm_5",
            "CP_64_Stvith_Buchler_Turm_7",
            "CP_64_Stvith_St_Joseph_Kloster_1",
            "CP_64_Stvith_St_Joseph_Kloster_3",
            "CP_64_Stvith_St_Joseph_Kloster_5",
            "CP_64_Stvith_St_Joseph_Kloster_7",
            "CP_64_Stvith_Road_to_Malmedy_1",
            "CP_64_Stvith_Road_to_Malmedy_3",
            "CP_64_Stvith_Road_to_Malmedy_5",
            "CP_64_Stvith_Road_to_Malmedy_7",
            "CP_64_Stvith_Ober_Emmels_1",
            "CP_64_Stvith_Ober_Emmels_3",
            "CP_64_Stvith_Ober_Emmels_5",
            "CP_64_Stvith_Ober_Emmels_7",
            "CP_64_Stvith_Aachener_path_1",
            "CP_64_Stvith_Aachener_path_3",
            "CP_64_Stvith_Aachener_path_5",
            "CP_64_Stvith_Aachener_path_7",
            "CP_64_Stvith_Nieder_Emmels_1",
            "CP_64_Stvith_Nieder_Emmels_3",
            "CP_64_Stvith_Nieder_Emmels_5",
            "CP_64_Stvith_Nieder_Emmels_7",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CP_64_Stvith_Rosenhuegels_Farms_2",
            "CP_64_Stvith_Rosenhuegels_Farms_4",
            "CP_64_Stvith_Rosenhuegels_Farms_6",
            "CP_64_Stvith_Rosenhuegels_Farms_8",
            "CP_64_Stvith_Walleroder_Wood_2",
            "CP_64_Stvith_Walleroder_Wood_4",
            "CP_64_Stvith_Walleroder_Wood_6",
            "CP_64_Stvith_Walleroder_Wood_8",
            "CP_64_Stvith_Walleroder_Wood_10",
            "CP_64_Stvith_Walleroder_Wood_12",
            "CP_64_Stvith_Walleroder_Wood_14",
            "CP_64_Stvith_Friedensstrasse_Bridge_2",
            "CP_64_Stvith_Friedensstrasse_Bridge_4",
            "CP_64_Stvith_Friedensstrasse_Bridge_6",
            "CP_64_Stvith_Friedensstrasse_Bridge_8",
            "CP_64_Stvith_Trainstation_2",
            "CP_64_Stvith_Trainstation_4",
            "CP_64_Stvith_Trainstation_6",
            "CP_64_Stvith_Trainstation_8",
            "CP_64_Stvith_Wiesenbach_2",
            "CP_64_Stvith_Wiesenbach_4",
            "CP_64_Stvith_Wiesenbach_6",
            "CP_64_Stvith_Wiesenbach_8",
            "CP_64_Stvith_Crossroads_2",
            "CP_64_Stvith_Crossroads_4",
            "CP_64_Stvith_Crossroads_6",
            "CP_64_Stvith_Crossroads_8",
            "CP_64_Stvith_Buchler_Turm_2",
            "CP_64_Stvith_Buchler_Turm_4",
            "CP_64_Stvith_Buchler_Turm_6",
            "CP_64_Stvith_Buchler_Turm_8",
            "CP_64_Stvith_St_Joseph_Kloster_2",
            "CP_64_Stvith_St_Joseph_Kloster_4",
            "CP_64_Stvith_St_Joseph_Kloster_6",
            "CP_64_Stvith_St_Joseph_Kloster_8",
            "CP_64_Stvith_Road_to_Malmedy_2",
            "CP_64_Stvith_Road_to_Malmedy_4",
            "CP_64_Stvith_Road_to_Malmedy_6",
            "CP_64_Stvith_Road_to_Malmedy_8",
            "CP_64_Stvith_Ober_Emmels_2",
            "CP_64_Stvith_Ober_Emmels_4",
            "CP_64_Stvith_Ober_Emmels_6",
            "CP_64_Stvith_Ober_Emmels_8",
            "CP_64_Stvith_Aachener_path_2",
            "CP_64_Stvith_Aachener_path_4",
            "CP_64_Stvith_Aachener_path_6",
            "CP_64_Stvith_Aachener_path_8",
            "CP_64_Stvith_Nieder_Emmels_2",
            "CP_64_Stvith_Nieder_Emmels_4",
            "CP_64_Stvith_Nieder_Emmels_6",
            "CP_64_Stvith_Nieder_Emmels_8",
        ],
        team=2,
    ),
]

spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_stvith_roadtomalmedy_m36, CP_32_stvith_roadtomalmedy_sherman3",
        they_own="CP_32_stvith_crossroads",
    ),
]

spawns_small = [
    plugin(teamSPs),  # Auto-fill
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_Stvith_sector_a_locker",
        source=["CP_64_Stvith_Aachener_path", "CP_64_Stvith_Walleroder_Wood"],
    ),
    plugin(
        linkCPs,
        target="CP_64_Stvith_sector_b_locker",
        source=[
            "CP_64_Stvith_Friedensstrasse_Bridge",
            "CP_64_Stvith_Trainstation",
            "CP_64_Stvith_Rosenhuegels_Farms",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_Stvith_sector_c_locker",
        source=[
            "CP_64_Stvith_St_Joseph_Kloster",
            "CP_64_Stvith_Buchler_Turm",
            "CP_64_Stvith_Crossroads",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_Stvith_sector_d_locker",
        source=[
            "CP_64_Stvith_Ober_Emmels",
            "CP_64_Stvith_Nieder_Emmels",
            "CP_64_Stvith_Road_to_Malmedy",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_Stvith_sector_viesen_locker",
        source="CP_64_Stvith_Wiesenbach",
    ),
    plugin(
        linkCPs,
        target="CP_64_Stvith_allies_tank_dummy1",
        source="CP_64_Stvith_sector_a_locker",
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_Stvith_allies_tank_dummy2",
        source="CP_64_Stvith_sector_b_locker",
        invert=True,
    ),
]

push_64 = [
    plugin(
        push,
        source="CP_64_Stvith_German_Positions",
        target="CP_64_Stvith_Walleroder_Wood",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_Stvith_German_Positions",
        target="CP_64_Stvith_Aachener_path",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Aachener_path",
        target="CP_64_Stvith_sector_a_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Walleroder_Wood",
        target="CP_64_Stvith_sector_a_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_a_locker",
        target="CP_64_Stvith_Friedensstrasse_Bridge",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_a_locker",
        target="CP_64_Stvith_Trainstation",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_a_locker",
        target="CP_64_Stvith_Rosenhuegels_Farms",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Friedensstrasse_Bridge",
        target="CP_64_Stvith_sector_b_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Trainstation",
        target="CP_64_Stvith_sector_b_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Rosenhuegels_Farms",
        target="CP_64_Stvith_sector_b_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_b_locker",
        target="CP_64_Stvith_Wiesenbach",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_b_locker",
        target="CP_64_Stvith_St_Joseph_Kloster",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_b_locker",
        target="CP_64_Stvith_Buchler_Turm",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_b_locker",
        target="CP_64_Stvith_Crossroads",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Wiesenbach",
        target="CP_64_Stvith_sector_viesen_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_St_Joseph_Kloster",
        target="CP_64_Stvith_sector_c_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Buchler_Turm",
        target="CP_64_Stvith_sector_c_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Crossroads",
        target="CP_64_Stvith_sector_c_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_c_locker",
        target="CP_64_Stvith_Ober_Emmels",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_c_locker",
        target="CP_64_Stvith_Nieder_Emmels",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_sector_c_locker",
        target="CP_64_Stvith_Road_to_Malmedy",
        attacker=1,
        display_arrow=True,
        wants_source_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Ober_Emmels",
        target="CP_64_Stvith_sector_d_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Nieder_Emmels",
        target="CP_64_Stvith_sector_d_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_Stvith_Road_to_Malmedy",
        target="CP_64_Stvith_sector_d_locker",
        attacker=1,
        display_arrow=False,
        wants_target_marker=False,
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_stvith_wiesenbach",
        target="CP_32_stvith_crossroads",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_stvith_crossroads",
        target="CP_32_stvith_stjosephkloster",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_stvith_crossroads",
        target="CP_32_stvith_buchlerturm",
        attacker=1,
        display_arrow=True,
    ),
    plugin(
        push,
        source="CP_32_stvith_buchlerturm, CP_32_stvith_stjosephkloster",
        target="CP_32_stvith_roadtomalmedy",
        attacker=1,
        display_arrow=True,
    ),
]

push_16 = [
    plugin(
        neighPush,
        sources="CP_16_stvith_rosenhuegel",
        targets="CP_16_stvith_crossroads",
    ),
    plugin(
        neighPush,
        sources="CP_16_stvith_crossroads",
        targets="CP_16_stvith_stjosephkloster",
    ),
    plugin(
        neighPush,
        sources="CP_16_stvith_stjosephkloster",
        targets="CP_16_stvith_buchlerturm",
    ),
]

kitlimits_64 = [
    plugin(
        limitKit, team=1, slot=1, kit="GW_StG44Assault_Limited", limit=0.15
    ),
    plugin(limitKit, team=2, slot=1, kit="UW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.075),
    plugin(limitKit, team=2, slot=3, kit="UW_LMG_Limited", limit=0.1),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_AntitankAssault60m_Limited",
        limit=0.09,
    ),
    plugin(
        limitKit, team=2, slot=5, kit="UW_AntitankAssault_Limited", limit=0.06
    ),
]

tickets = [plugin(ticketLoss, ticketLoss1=11, ticketLoss2=1000)]


coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=5.0 / 32.0,
        kit="GW_Scout",
        soldier="GcWhSnow_splitter",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=5.0 / 32.0,
        kit="GW_StG44Assault_Limited",
        soldier="GcWhSnow_splitter_white",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault",
        soldier="gcwhsnow_sumpf",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GW_LMG_MG42_Limited",
        soldier="GcWhSnow_white",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer_satchel",
        soldier="GcWhSnow_splitter_white",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=4.0 / 32.0,
        kit="GW_AntitankAssault60m_Limited",
        soldier="GcWhSnow_white",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="UW_Scout",
        soldier="uc_win44_army_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="UW_SMGAssault_Limited",
        soldier="uc_win44_army_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
        kit="UW_RifleAssault",
        soldier="uc_win44_army_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=4.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uc_win44_army_cpl_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=5.0 / 32.0,
        kit="UW_Engineer_Satchel",
        soldier="uc_win44_7thAD_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=5.0 / 32.0,
        kit="UW_AntitankAssault_Limited",
        soldier="uc_win44_7thAD_cpl",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_Stvith_Road_to_Malmedy",
        we_own="CP_64_Stvith_St_Joseph_Kloster or CP_64_Stvith_Crossroads",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Stvith_Buchler_Turm",
        we_own="CP_64_Stvith_St_Joseph_Kloster and CP_64_Stvith_Crossroads and (CP_64_Stvith_Ober_Emmels or CP_64_Stvith_Nieder_Emmels or CP_64_Stvith_Road_to_Malmedy)",
    ),
    # Team-locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
    plugin(
        linkCPs,
        target="CP_64_Stvith_Last_Sector_dummy",
        source="CP_64_Stvith_Ober_Emmels,CP_64_Stvith_Nieder_Emmels,CP_64_Stvith_Road_to_Malmedy",
        default_zero=True,
    ),
    # Allied reinforcements
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Stvith_allies_tank_dummy1_M4,CP_64_Stvith_Buchler_Turm_sherman",
        they_own="CP_64_Stvith_Aachener_path and CP_64_Stvith_Walleroder_Wood",
        we_own="CP_64_Stvith_Buchler_Turm",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Stvith_Watermill_DE_GB_sherman1,CP_64_Stvith_allies_tank_dummy1_M476",
        they_own="CP_64_Stvith_Friedensstrasse_Bridge and CP_64_Stvith_Trainstation and CP_64_Stvith_Rosenhuegels_Farms",
        we_own="CP_64_Stvith_St_Joseph_Kloster and CP_64_Stvith_Crossroads",
    ),
    #
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Stvith_German_Positions_hanomag_aachener",
        we_dont_own="CP_64_Stvith_Aachener_path or CP_64_Stvith_Walleroder_Wood",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Stvith_German_Positions_sdkfz,CP_64_Stvith_German_Positions_Hanomag",
        we_dont_own="CP_64_Stvith_Trainstation",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Stvith_Wiesenbach_ATgun,CP_64_Stvith_Wiesenbach_mg,CP_64_Stvith_Wiesenbach_mg_0",
        they_own="CP_64_Stvith_Rosenhuegels_Farms or CP_64_Stvith_Trainstation or CP_64_Stvith_Crossroads",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Stvith_Road_to_Malmedy_M1atgun",
        they_own="CP_64_Stvith_Friedensstrasse_Bridge or CP_64_Stvith_St_Joseph_Kloster or CP_64_Stvith_Buchler_Turm",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_Stvith_Ober_Emmels_USMG,CP_64_Stvith_Ober_Emmels_MG,CP_64_Stvith_Ober_Emmels_Us_stionnary57,CP_64_Stvith_Nieder_Emmels_stionnary76b",
        they_own="CP_64_Stvith_St_Joseph_Kloster or CP_64_Stvith_Buchler_Turm",
    ),
]

gpm_cq = {
    64: tickets
    + spawns
    + kitlimits_64
    + push_64
    + linkCPs_64
    + dynamicoob_64
    + nco,
    32: tickets
    + spawns_small
    + kitlimits_64
    + push_32
    + spawnerConditions_32
    + nco,
    16: tickets + spawns_small + kitlimits_64 + push_16 + nco,
}
gpm_coop = {
    64: coop_64 + tickets + nco,
    32: tickets
    + spawns_small
    + push_32
    + spawnerConditions_32
    + nco,
    16: tickets + spawns_small + push_16 + nco,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
