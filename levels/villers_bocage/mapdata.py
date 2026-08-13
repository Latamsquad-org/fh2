# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    teamSPs,
    disableSPs,
    timeCP,
    spawnerCondition,
    aiPush,
    balanceSPs,
    NCOrifleData,
    DoubleBleed,
)

bleed_32 = [
    plugin(
        DoubleBleed,
    )
]

nco = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO", "BW_NCO"),
        soldiers=("gs_waffen_unteroffizier", "bw_nco_soldier"),
    )
]

teamspawns = [
    plugin(teamSPs),  # Auto-fill
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_MG42_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.2),
    plugin(
        limitKit, team=1, slot=5, kit="GS_AntitankAssault_Limited", limit=0.1
    ),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.1),
]

kitlimits_32 = [
    plugin(limitKit, team=1, slot=1, kit="GS_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=1, slot=3, kit="GS_LMG_MG42_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.2),
    plugin(
        limitKit, team=1, slot=5, kit="GS_AntitankAssault_Limited", limit=0.1
    ),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.1),
]

tickets = [plugin(ticketLoss, ticketLoss1=18, ticketLoss2=14)]


coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=3.0 / 32.0,
        kit="GS_Scout",
        soldier="gs_waffen_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=5.0 / 32.0,
        kit="GS_SMGAssault_Limited",
        soldier="gs_waffen_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=7.0 / 32.0,
        kit="GS_RifleAssault",
        soldier="gs_waffen_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GS_LMG_MG42_Limited",
        soldier="gs_waffen_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=6.0 / 32.0,
        kit="GS_Engineer_Satchel",
        soldier="gs_waffen_panzerabwehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=6.0 / 32.0,
        kit="GS_AntitankAssault_Limited",
        soldier="gs_waffen_gewehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=3.0 / 32.0,
        kit="BW_Scout",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=5.0 / 32.0,
        kit="BW_SMGAssault_Limited",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=7.0 / 32.0,
        kit="BW_RifleAssault",
        soldier="bw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="BW_LMG_Limited",
        soldier="bw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=6.0 / 32.0,
        kit="BW_Engineer_Satchel",
        soldier="bw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=6.0 / 32.0,
        kit="BW_Antitank_Limited",
        soldier="bw_heavy_soldier",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=1,
        cp="Tilly_sur_Seulles",
        we_own="CP_64_Forward_German_dummy",
    ),
    plugin(
        disableSPs, team=1, cp="Crossroad", we_own="CP_64_Forward_German_dummy"
    ),
    plugin(
        balanceSPs,
        custom_weights=[
            dict(cp="Farm", weight=750000),
            dict(cp="Point_213,Villers_Bocage", team=1, weight=900000),
            dict(cp="Point_213,Villers_Bocage", team=2, weight=1400000),
            dict(cp="130th_Lehr", weight=600000),
        ],
    ),
    # Push mode
    plugin(aiPush),
    plugin(timeCP, target="CP_64_Forward_German_dummy", team=-1, time=10),
    plugin(
        spawnerCondition,
        team=1,
        spawner="Villers_Bocage_atatenterancevillerswest,Villers_Bocage_mgvillerswestenterance,Villers_Bocage_pak40",
        they_own="Crossroad or Farm or Point_213",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="130th_Lehr_opelblitzvillers2,130th_Lehr_opelblitzvillers,lighttankaxismain",
        we_dont_own="Crossroad and Tilly_sur_Seulles",
    ),
    plugin(ticketLoss, ticketLoss1=500, ticketLoss2=14),
]

gpm_cq = {
    64: kitlimits_64 + teamspawns + tickets + nco,
    32: kitlimits_32 + tickets + nco + bleed_32,
    16: kitlimits_32 + tickets + teamspawns + nco,
}
gpm_coop = {
    64: coop_64 + teamspawns + nco,
    32: tickets + nco + bleed_32,
    16: teamspawns + nco,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
