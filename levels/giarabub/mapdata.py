# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    aiPush,
    disableSPs,
    limitKit,
    push,
    neighPush,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    timeCP,
    NCOrifleData,
    DoubleBleed,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("IA_NCOBeretta38", "AA_NCOTommygunS"),
        soldiers=("ia_light_soldier", "aa_nco_soldier_alt"),
    )
]

nco_test = [
    plugin(
        NCOrifleData,
        kits=("test_miscellaneous_1", "test_miscellaneous_2"),
        soldiers=("ia_light_soldier", "aa_nco_soldier_alt"),
    )
]

kit_limits = [
    plugin(
        limitKit,
        team=1,
        kit="IA_Limited_Assault_Beretta38_K98",
        slot=1,
        limit=0.08,
    ),
    plugin(
        limitKit,
        team=2,
        kit="AA_Limited_Assault_TommygunD_No4",
        slot=1,
        limit=0.08,
    ),
    plugin(
        limitKit,
        team=1,
        kit="IA_Limited_Support_MG34_K98",
        slot=3,
        limit=0.1
    ),
    plugin(
        limitKit,
        team=2,
        kit="AA_Limited_Support_Bren_No4",
        slot=3,
        limit=0.15
    ),
    plugin(
        limitKit,
        team=1,
        kit="IA_Engineer_Satchel_Limited",
        slot=4,
        limit=0.15
    ),
    plugin(
        limitKit,
        team=2,
        kit="AA_Engineer_Satchel_Limited",
        slot=4,
        limit=0.1
    ),
    plugin(
        limitKit,
        team=1,
        kit="IA_AntiTank_carcano",
        slot=5,
        limit=0.08
    ),
    plugin(
        limitKit,
        team=2,
        kit="AA_ATNo73Grenade_Limited",
        slot=5,
        limit=0.08
    ),
]

kit_limits_16 = [
    plugin(
        limitKit,
        team=1,
        kit="IA_Limited_Assault_Beretta38_K98",
        slot=1,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        kit="AA_Limited_Assault_TommygunD_No4",
        slot=1,
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        kit="IA_Limited_Support_MG34_K98",
        slot=3,
        limit=0.15
    ),
    plugin(
        limitKit,
        team=2,
        kit="AA_Limited_Support_Bren_No4",
        slot=3,
        limit=0.15
    ),
    plugin(
        limitKit,
        team=1,
        kit="IA_Engineer_Satchel_Limited",
        slot=4,
        limit=0.1
    ),
    plugin(
        limitKit,
        team=2,
        kit="AA_Engineer_Satchel_Limited",
        slot=4,
        limit=0.1
    ),
    plugin(
        limitKit,
		team=1,
        kit="IA_AntiTank_carcano",
        slot=5,
        limit=0.1
    ),
    plugin(
        limitKit,
        team=2,
        kit="AA_ATNo73Grenade_Limited",
        slot=5,
        limit=0.1
    ),
]


push_32 = [
    plugin(
        push,
        source="CP_32_giarabub_AlliedHQ",
        target="CP_32_giarabub_oasis",
        attacker=2,
    ),
    plugin(
        neighPush,
        sources="CP_32_giarabub_oasis",
        targets="CP_32_giarabub_mosque,CP_32_giarabub_barracks",
    ),
    plugin(
        neighPush,
        sources="CP_32_giarabub_mosque",
        targets="CP_32_giarabub_village,CP_32_giarabub_east",
    ),
    plugin(
        neighPush,
        sources="CP_32_giarabub_barracks",
        targets="CP_32_giarabub_village,CP_32_giarabub_east",
    ),
]
tickets_64 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=15)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=45, ticketLoss2=15)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]

timecp_32 = [
    plugin(
        timeCP,
        team=2,
        target="CP_32_giarabub_forward_dummy",
        time="32",
    ),
]

teamsp_32 = [
    plugin(
        teamSPs,
    ),
]


coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="IA_ScoutK98Short",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=4.0 / 32.0,
        kit="IA_Limited_Assault_Beretta38_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=12.0 / 32.0,
        kit="IA_RiflemanK98",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="IA_Limited_Support_MG34_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="IA_Engineer_Satchel_Limited",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=2.0 / 32.0,
        kit="IA_AntiTank_carcano",
        soldier="ia_heavy_soldier",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="AA_ScoutEarly",
        soldier="aa_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=4.0 / 32.0,
        kit="AA_Limited_Assault_TommygunD_No4",
        soldier="aa_heavy_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=12.0 / 32.0,
        kit="AA_RiflemanEarly",
        soldier="aa_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="AA_Limited_Support_Bren_No4",
        soldier="aa_heavy_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="AA_Engineer_Satchel_Limited",
        soldier="aa_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=2.0 / 32.0,
        kit="AA_ATNo73Grenade_Limited",
        soldier="aa_heavy_soldier_alt",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_giarabub_AlliedDummy2",
        we_own="CP_64_giarabub_barracks or CP_64_giarabub_mosque",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_giarabub_east",
        we_own="CP_64_giarabub_AlliedHQ",
    ),  # Never
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_giarabub_barracks",
        we_own="CP_64_giarabub_barracks_dummy",
    ),
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_giarabub_village",
        we_own="CP_64_giarabub_village_dummy",
    ),
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Timed CP switching
    plugin(timeCP, target="CP_64_giarabub_barracks_dummy", time=30, team=-1),
    plugin(timeCP, target="CP_64_giarabub_village_dummy", time=30, team=-1),
    # PCO spawning conditions - Allies
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_giarabub_AlliedHQ_DE_GB_HeavyTruck",
        we_dont_own="CP_64_giarabub_village or CP_64_giarabub_barracks",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_giarabub_AlliedHQ_DE_GB_PersonelCarrier_0",
        we_dont_own="CP_64_giarabub_village and CP_64_giarabub_barracks",
    ),
    # Ticket bleed
    plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=16),
]
coop_32 = [
# Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="IA_ScoutK98Short",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=4.0 / 32.0,
        kit="IA_Limited_Assault_Beretta38_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=12.0 / 32.0,
        kit="IA_RiflemanK98",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=6.0 / 32.0,
        kit="IA_Limited_Support_MG34_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="IA_Engineer_Satchel_Limited",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=2.0 / 32.0,
        kit="IA_AntiTank_carcano",
        soldier="ia_heavy_soldier",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="AA_ScoutEarly",
        soldier="aa_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=4.0 / 32.0,
        kit="AA_Limited_Assault_TommygunD_No4",
        soldier="aa_heavy_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=12.0 / 32.0,
        kit="AA_RiflemanEarly",
        soldier="aa_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="AA_Limited_Support_Bren_No4",
        soldier="aa_heavy_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="AA_Engineer_Satchel_Limited",
        soldier="aa_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=2.0 / 32.0,
        kit="AA_ATNo73Grenade_Limited",
        soldier="aa_heavy_soldier_alt",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
]

bleed_16 = [
    plugin(
        DoubleBleed,
    ),
]

gpm_cq = {
    64: kit_limits + tickets_64 + nco,
    32: kit_limits + tickets_32 + push_32 + timecp_32 + teamsp_32 + nco,
    16: kit_limits_16 + tickets_16 + nco + bleed_16,
}

gpm_coop = {
    16: tickets_16 + nco + bleed_16,
    32: coop_32 + tickets_32 + nco,
    64: coop_64 + nco,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
