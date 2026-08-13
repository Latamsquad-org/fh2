# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    # aiPush,
    disableSPs,
    limitKit,
    linkCPs,
    NCOrifleData,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    # timeCP,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "BW_NCO"),
        soldiers=("gw_heer_unteroffizier", "bw_nco_soldier"),
    )
]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_lebisey_dummy2",
        source="CP_64_lebisey_3coy_cp",
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_lebisey_dummy",
        source="CP_64_lebisey_hq",
        invert=True,
    ),
    plugin(
        push,
        source="CP_64_lebisey_staff_yeomanry",
        target="CP_64_lebisey_east_at",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_lebisey_staff_yeomanry",
        target="CP_64_lebisey_centre_at",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_lebisey_staff_yeomanry",
        target="CP_64_lebisey_west_at",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_lebisey_east_at",
        target="CP_64_lebisey_hq",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_lebisey_centre_at",
        target="CP_64_lebisey_hq",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_lebisey_west_at",
        target="CP_64_lebisey_3coy_cp",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_lebisey_centre_at",
        target="CP_64_lebisey_3coy_cp",
        attacker=2,
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]
spawnercond_16 = [
    # spawn stug on bleed
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_16_lebisey_hq_stug",
        they_own="CP_16_lebisey_garage",
    ),
]

kitlimits_64 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG26_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.15),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.1),
]

kitlimits_32 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.25),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG26_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.15),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.1),
]


kitlimits_16 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG26_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.15),
    plugin(limitKit, team=2, slot=5, kit="BW_Antitank_Limited", limit=0.1),
]

spawnerConditions_32 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_lebisey_staff_yeomanry_sherman1",
        we_dont_own="CP_32_lebisey_centre_at",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_lebisey_staff_yeomanry_sherman2",
        we_dont_own="CP_32_lebisey_west_at",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_lebisey_staff_yeomanry_sherman3",
        we_dont_own="CP_32_lebisey_3coy_cp",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_lebisey_caen_pz4",
        we_dont_own="CP_32_lebisey_centre_at",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_lebisey_caen_stug",
        we_dont_own="CP_32_lebisey_west_at",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_lebisey_caen_pz3",
        we_dont_own="CP_32_lebisey_3coy_cp",
    ),
]

links_16 = [
    plugin(
        linkCPs,
        target="CP_16_lebisey_dummy",
        source="CP_16_lebisey_garage",
        invert=True,
    ),
    plugin(
        push,
        source="CP_16_lebisey_west_lebisey",
        target="CP_16_lebisey_main_street",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_16_lebisey_main_street",
        target="CP_16_lebisey_cafe_dasson",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_16_lebisey_cafe_dasson",
        target="CP_16_lebisey_garage",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_16_lebisey_garage",
        target="CP_16_lebisey_hq",
        attacker=2,
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]


coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout",
        soldier="gw_heer_spaher",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="gw_heer_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=8.0 / 32.0,
        kit="GW_RifleAssault",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GW_LMG_MG26_Limited",
        soldier="gw_heer_maschinengewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=5.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="GW_AntitankAssault_Limited",
        soldier="gw_heer_panzerabwehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="BW_Scout",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="BW_SMGAssault_Limited",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=8.0 / 32.0,
        kit="BW_RifleAssault",
        soldier="bw_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=5.0 / 32.0,
        kit="BW_LMG_Limited",
        soldier="bw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=5.0 / 32.0,
        kit="BW_Engineer_Satchel",
        soldier="bw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=5.0 / 32.0,
        kit="BW_Antitank_Limited",
        soldier="bw_heavy_soldier",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_lebisey_caen",
        we_own="CP_64_lebisey_3coy_cp",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_lebisey_staff_yeomanry",
        we_own="CP_64_lebisey_west_at or CP_64_lebisey_centre_at or CP_64_lebisey_east_at",
    ),
]

disable_AI = [
    plugin(disableSPs),  # Auto-fill
]

gpm_cq = {
    64: tickets_64 + kitlimits_64 + links_64 + spawns + nco,
    32: tickets_32 + kitlimits_32 + spawnerConditions_32 + spawns + nco,
    16: tickets_16 + links_16 + spawnercond_16 + kitlimits_16 + spawns + nco,
}
gpm_coop = {
    64: coop_64 + links_64 + spawns + tickets_64 + nco,
    32: tickets_32 + spawnerConditions_32 + spawns + nco,
    16: tickets_16 + links_16 + spawnercond_16 + spawns + nco + disable_AI,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
