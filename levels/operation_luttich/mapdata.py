# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0301,R1735
from game.plugins import (
    plugin,
    balanceSPs,
    delaySpawners,
    disableSPs,
    DoubleBleed,
    limitKit,
    NCOrifleData,
    teamSPs,
    ticketLoss,
    timeCP,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GS_NCO", "UW_NCO"),
        soldiers=("gs_waffen_unteroffizier", "uw_ranger_sgt"),
    )
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

bleed_16 = [
    plugin(DoubleBleed),
]

kit_limits = [
    plugin(limitKit, team=1, kit="GW_Scout_G41_limited", slot=0, limit=0.2),
    plugin(limitKit, team=1, kit="GS_SMGAssault_Limited", slot=1, limit=0.25),
    plugin(limitKit, team=2, kit="UW_SMGAssault_Limited_GGun", slot=1, limit=0.25),
    plugin(limitKit, team=1, kit="GS_LMG_MG42_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="UW_LMG_Limited", slot=3, limit=0.15),
    plugin(limitKit, team=1, kit="GW_AntitankAssault_haft", slot=5, limit=0.15),
    plugin(limitKit, team=2, kit="UW_AntitankAssault_Limited", slot=5, limit=0.15),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=8, ticketLoss2=8)]


kits_AI = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=6.0 / 32.0,
        kit="GW_Scout_G41_limited",
        soldier="gs_waffen_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GS_SMGAssault_Limited",
        soldier="gs_waffen_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=7.0 / 32.0,
        kit="GW_RifleAssault",
        soldier="gs_waffen_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="GS_LMG_MG42_Limited",
        soldier="gs_waffen_maschinengewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=5.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="gs_waffen_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=3.0 / 32.0,
        kit="GW_AntitankAssault_haft",
        soldier="gs_waffen_panzerabwehr",
    ),
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=5.0 / 32.0,
        kit="UW_Scout",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="UW_SMGAssault_Limited_GGun",
        soldier="uw_ranger_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=7.0 / 32.0,
        kit="UW_RifleAssault",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="UW_LMG_Limited",
        soldier="uw_ranger_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=5.0 / 32.0,
        kit="UW_Engineer_Satchel",
        soldier="uw_ranger_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="UW_AntitankAssault_Limited",
        soldier="uw_ranger_cpl",
    ),
]

coop_64 = [
    # AI spawn points disabler
    # Axis
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Luttich_Axismain_Center",
        we_own="CP_64_luttich_eastmortain or CP_64_luttich_westmortain",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Luttich_Axismain_East",
        we_own="CP_64_luttich_eastmortain or CP_64_luttich_westmortain or CP_64_luttich_farm",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_Luttich_Axismain_West",
        we_own="CP_64_luttich_eastmortain or CP_64_luttich_westmortain or CP_64_luttich_abbayeblanche",
    ),
    # Allies
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_luttich_eastmortain",
        we_own="CP_64_Luttich_Allied_Forward_Dummy",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_luttich_westmortain",
        we_own="CP_64_Luttich_Allied_Forward_Dummy",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_luttich_abbayeblanche",
        we_own="CP_64_Luttich_Allied_Forward_Dummy",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_luttich_farm",
        we_own="CP_64_Luttich_Allied_Forward_Dummy",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_Luttich_Alliedmain_Center",
        we_own="CP_64_luttich_eastmortain or CP_64_luttich_westmortain",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_Luttich_Alliedmain_East",
        we_own="CP_64_luttich_eastmortain or CP_64_luttich_westmortain or CP_64_luttich_farm",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_Luttich_Alliedmain_West",
        we_own="CP_64_luttich_eastmortain or CP_64_luttich_westmortain or CP_64_luttich_abbayeblanche",
    ),
    plugin(
        balanceSPs,
        custom_weights=[
            dict(
                cp="CP_64_luttich_abbayeblanche, CP_64_luttich_farm",
                weight=750000,
            ),
            dict(
                cp="CP_64_luttich_eastmortain, CP_64_luttich_westmortain",
                weight=1000000,
            ),
        ],
    ),
    plugin(
        delaySpawners,
        spawners="CP_64_luttich_alliedmain_ArmouredCar_0,CP_64_luttich_alliedmain_MediumTank_0,CP_64_luttich_alliedmain_Car,\
                                        CP_64_luttich_alliedmain_TankDestroyer_0,CP_64_luttich_alliedmain_Truck,CP_64_luttich_alliedmain_Truck_0,\
                                        CP_64_luttich_alliedmain_apc,CP_64_luttich_alliedmain_apc2",
    ),
    plugin(timeCP, target="CP_64_Luttich_Allied_Forward_Dummy", team=-1, time=10),
]
gpm_cq = {
    64: (nco + spawns + kit_limits + tickets_64),
    32: (nco + spawns + kit_limits + tickets_32),
    16: (nco + spawns + kit_limits + tickets_64 + bleed_16),
}

gpm_coop = {
    64: coop_64 + tickets_64 + spawns + kits_AI + nco,
    16: tickets_64 + kits_AI + nco,
}
sp1 = gpm_coop
sp3 = gpm_coop
