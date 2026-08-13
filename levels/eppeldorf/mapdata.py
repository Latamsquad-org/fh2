# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    aiPush,
    disableSPs,
    limitKit,
    NCOrifleData,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    DoubleBleed,
)

bleed_32 = [
    plugin(DoubleBleed),
]

nco = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO_mp40_g43", "UW_NCO"),
        soldiers=("gcwhsnow_nco", "uc_win44_army_sgt"),
    )
]

spawns_64 = [
    plugin(
        teamSPs,
        sps=[
            "CQ_64_EPPEL_Eppeldorf_North_allied_1",
            "CQ_64_EPPEL_Eppeldorf_North_allied_2",
            "CQ_64_EPPEL_Eppeldorf_North_allied_3",
            "CQ_64_EPPEL_Eppeldorf_North_allied_4",
            "CQ_64_EPPEL_Eppeldorf_North_allied_5",
            "CQ_64_EPPEL_Eppeldorf_North_allied_6",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CQ_64_EPPEL_Eppeldorf_North_axis_1",
            "CQ_64_EPPEL_Eppeldorf_North_axis_2",
            "CQ_64_EPPEL_Eppeldorf_North_axis_3",
            "CQ_64_EPPEL_Eppeldorf_North_axis_4",
            "CQ_64_EPPEL_Eppeldorf_North_axis_5",
            "CQ_64_EPPEL_Eppeldorf_North_axis_6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CQ_64_EPPEL_East_Farm_allies_1",
            "CQ_64_EPPEL_East_Farm_allies_2",
            "CQ_64_EPPEL_East_Farm_allies_3",
            "CQ_64_EPPEL_East_Farm_allies_4",
            "CQ_64_EPPEL_East_Farm_allies_5",
            "CQ_64_EPPEL_East_Farm_allies_6",
            "CQ_64_EPPEL_East_Farm_allies_7",
            "CQ_64_EPPEL_East_Farm_allies_8",
        ],
        team=2,
    ),
    plugin(
        teamSPs,
        sps=[
            "CQ_64_EPPEL_East_Farm_axis_1",
            "CQ_64_EPPEL_East_Farm_axis_2",
            "CQ_64_EPPEL_East_Farm_axis_3",
            "CQ_64_EPPEL_East_Farm_axis_4",
            "CQ_64_EPPEL_East_Farm_axis_5",
            "CQ_64_EPPEL_East_Farm_axis_6",
            "CQ_64_EPPEL_East_Farm_axis_7",
            "CQ_64_EPPEL_East_Farm_axis_8",
        ],
        team=1,
    ),
]

spawns_32 = [
    plugin(
        teamSPs,
        sps=[
            "CQ_32_EPPEL_Eppeldorf_South_axis1",
            "CQ_32_EPPEL_Eppeldorf_South_axis2",
            "CQ_32_EPPEL_Eppeldorf_South_axis3",
            "CQ_32_EPPEL_Eppeldorf_South_axis4",
            "CQ_32_EPPEL_Eppeldorf_South_axis5",
            "CQ_32_EPPEL_Eppeldorf_South_axis6",
            "CQ_32_EPPEL_Eppeldorf_South_axis7",
            "CQ_32_EPPEL_Eppeldorf_South_axis8",
            "CQ_32_EPPEL_Eppeldorf_South_axis9",
            "CQ_32_EPPEL_Eppeldorf_North_axis_1",
            "CQ_32_EPPEL_Eppeldorf_North_axis_2",
            "CQ_32_EPPEL_Eppeldorf_North_axis_3",
            "CQ_32_EPPEL_Eppeldorf_North_axis_4",
            "CQ_32_EPPEL_Eppeldorf_North_axis_5",
            "CQ_32_EPPEL_Eppeldorf_North_axis_6",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "CQ_32_EPPEL_Eppeldorf_South_allied1",
            "CQ_32_EPPEL_Eppeldorf_South_allied2",
            "CQ_32_EPPEL_Eppeldorf_South_allied3",
            "CQ_32_EPPEL_Eppeldorf_North_allied_1",
            "CQ_32_EPPEL_Eppeldorf_North_allied_2",
            "CQ_32_EPPEL_Eppeldorf_North_allied_3",
            "CQ_32_EPPEL_Eppeldorf_North_allied_4",
            "CQ_32_EPPEL_Eppeldorf_North_allied_5",
            "CQ_32_EPPEL_Eppeldorf_North_allied_5",
        ],
        team=2,
    ),
]

kit_limits = [
    plugin(
        limitKit, team=1, kit="GW_StG44Assault_Limited", slot=1, limit=0.15
    ),
    plugin(limitKit, team=2, kit="UW_SMGAssault_Limited", slot=1, limit=0.15),
    plugin(limitKit, team=1, kit="GW_LMG_MG42_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="UW_LMG_Limited", slot=3, limit=0.1),
    plugin(
        limitKit,
        team=1,
        kit="GW_AntitankAssault60m_Limited",
        slot=5,
        limit=0.04,
    ),
    plugin(
        limitKit, team=2, kit="UW_AntitankAssault_Limited", slot=5, limit=0.1
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=40)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]


spawns_AI = [
    plugin(teamSPs),  # Auto-fill
]

kits_AI = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout",
        soldier="gcwhsnow_sumpf",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GW_StG44Assault_Limited",
        soldier="gcwhsnow_white",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault_G43",
        soldier="gcwhsnow_sumpf",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=4.0 / 32.0,
        kit="GW_LMG_MG42_Limited",
        soldier="gcwhsnow_white",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="gcwhsnow_splitter",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=6.0 / 32.0,
        kit="GW_AntitankAssault60m_Limited",
        soldier="gcwhsnow_splitter",
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
        limit=8.0 / 32.0,
        kit="UW_RifleAssault_noNadeLauncher",
        soldier="uc_win44_army_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=5.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uc_win44_army_cpl_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="UW_Engineer_Satchel",
        soldier="uc_win44_army_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=6.0 / 32.0,
        kit="UW_AntitankAssault_Limited",
        soldier="uc_win44_army_cpl",
    ),
]

coop_32 = [
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    # Allies
    plugin(
        disableSPs,
        team=2,
        cp="CQ_32_EPPEL_Allied_main",
        we_own="CQ_32_EPPEL_Eppeldorf_South",
    ),
    # Push mode
    plugin(aiPush),
]
coop_64 = [
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=1,
        cp="CQ_64_EPPEL_Axis_main",
        we_own="CQ_64_EPPEL_East_Farm",
    ),
    # Push mode
    plugin(aiPush),
    # For Allies spawn the APCs and main base's Willys only when they loose any flag
    plugin(
        spawnerCondition,
        team=2,
        spawner="CQ_64_EPPEL_Allied_main_apc,CQ_64_EPPEL_Allied_main_apc2,CQ_64_EPPEL_Allied_main_willy,CQ_64_EPPEL_South_Farm_halftrack",
        we_dont_own="CQ_64_EPPEL_Hill or CQ_64_EPPEL_East_Farm or CQ_64_EPPEL_Eppeldorf_South or CQ_64_EPPEL_Eppeldorf_North or CQ_64_EPPEL_South_Farm",
    ),
]

gpm_cq = {
    64: spawns_64 + kit_limits + tickets_64 + nco,
    32: kit_limits + spawns_32 + nco + bleed_32,
    16: kit_limits + tickets_16 + nco,
}
gpm_coop = {
    64: coop_64 + tickets_64 + spawns_AI + kits_AI + nco,
    32: coop_32 + spawns_AI + kits_AI + nco,
}
sp2 = gpm_coop
sp3 = gpm_coop
