# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    aiPush,
    disableSPs,
    dynamicOOB,
    limitKit,
    linkCPs,
    NCOrifleData,
    push,
    teamSPs,
    ticketLoss,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("ga_tunisia_nco_soldier", "bw_nco_soldier_alt"),
    )
]

spawns = [
    plugin(
        teamSPs,
        sps=[
            "DEgate1",
            "DEgate2",
            "DEgate3",
            "DEtown1",
            "DEtown2",
            "DEtown3",
            "DEtown4",
            "DEcannon1",
            "DEmarket2",
            "DEmarket3",
            "DEmosque1",
            "DEmosque2",
            "DEmosque3",
            "DEmosque4",
        ],
        team=1,
    ),
    plugin(
        teamSPs,
        sps=[
            "UKgate1",
            "UKgate2",
            "UKgate3",
            "UKtown1",
            "UKtown2",
            "UKtown3",
            "UKtown4",
            "UKcannon3",
            "UKmarket3",
            "UKmarket4",
            "UKmosque1",
            "UKmosque2",
            "UKmosque3",
            "UKmosque4",
        ],
        team=2,
    ),
]

linkCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_tunis_SECTOR_A_LOCKER",
        source=[
            "CP_64_tunis_old_town_entr",
            "CP_64_tunis_the_prophets_gate",
            "CP_64_tunis_harbor",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_tunis_SECTOR_B_LOCKER",
        source=[
            "CP_64_tunis_old_mosque",
            "Cannon_position",
            "CP_64_tunis_al_grabah_market",
        ],
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_tunis_SECTOR_A_LOCKER": {
                "allies": {
                    "creates": ["CombatArea_allies2"],
                    "destroys": ["CombatArea_axis1"],
                },
            },
            "CP_64_tunis_SECTOR_B_LOCKER": {
                "allies": {
                    "creates": ["CombatArea_allies3"],
                    "destroys": ["CombatArea_axis2"],
                },
            },
        },
        inactive_at_start=["CombatArea_allies2", "CombatArea_allies3"],
        delay_axis=60,
        delay_allies=0,
    )
]

kit_limits = [
    plugin(limitKit, team=1, kit="GA_ScoutK98Short_tunis", slot=0, limit=0.075),
    plugin(limitKit, team=2, kit="BA_ScoutEarly_tunis", slot=0, limit=0.075),
    plugin(limitKit, team=1, kit="GW_SMGAssault_Limited", slot=1, limit=0.12),
    plugin(limitKit, team=2, kit="BA_Assault_m1928a1_30r", slot=1, limit=0.12),
    plugin(
        limitKit,
        team=1,
        kit="IA_Limited_Support_MG34_K98",
        slot=3,
        limit=0.075,
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Support_Bren_No4",
        slot=3,
        limit=0.075,
    ),
    plugin(limitKit, team=1, kit="IA_Riflecarabine_tunis", slot=4, limit=0.1),
    plugin(limitKit, team=2, kit="BA_Riflemansmlenade_tunis", slot=4, limit=0.1),
]

push_64 = [
    plugin(
        push,
        source="CP_64_tunis_desert_rats",
        target="CP_64_tunis_old_town_entr",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_tunis_desert_rats",
        target="CP_64_tunis_the_prophets_gate",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_tunis_desert_rats",
        target="CP_64_tunis_harbor",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_tunis_old_town_entr",
        target="CP_64_tunis_SECTOR_A_LOCKER",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tunis_the_prophets_gate",
        target="CP_64_tunis_SECTOR_A_LOCKER",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tunis_harbor",
        target="CP_64_tunis_SECTOR_A_LOCKER",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tunis_SECTOR_A_LOCKER",
        target="CP_64_tunis_old_mosque",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tunis_SECTOR_A_LOCKER",
        target="Cannon_position",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tunis_SECTOR_A_LOCKER",
        target="CP_64_tunis_al_grabah_market",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tunis_old_mosque",
        target="CP_64_tunis_SECTOR_B_LOCKER",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="Cannon_position",
        target="CP_64_tunis_SECTOR_B_LOCKER",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tunis_al_grabah_market",
        target="CP_64_tunis_SECTOR_B_LOCKER",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tunis_SECTOR_B_LOCKER",
        target="CP_64_tunis_axis_HQ",
        attacker=2,
        display_arrow=False,
    ),
]
tickets_64 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=10)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=3.0 / 32.0,
        kit="GA_ScoutK98Short_tunis",
        soldier="ga_tunisia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="ga_tunisia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=6.0 / 32.0,
        kit="ga_RifleAssault_tunis",
        soldier="ga_tunisia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="IA_Limited_Support_MG34_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=8.0 / 32.0,
        kit="IA_Riflecarabine_tunis",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="IA_Riflemanonly_tunis",
        soldier="ia_light_soldier",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=3.0 / 32.0,
        kit="BA_ScoutEarly_tunis",
        soldier="bw_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="BA_Assault_m1928a1_30r",
        soldier="bw_heavy_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=8.0 / 32.0,
        kit="BA_RiflemanEarly_noNades",
        soldier="bw_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=6.0 / 32.0,
        kit="BA_Limited_Support_Bren_No4",
        soldier="bw_heavy_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=10.0 / 32.0,
        kit="BA_Riflemansmlenade_tunis",
        soldier="bw_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=0.0 / 32.0,
        kit="BA_RiflemanEarly_tunis",
        soldier="bw_heavy_soldier_alt",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    plugin(
        disableSPs,
        cp="CP_64_tunis_old_mosque",
        team=2,
        we_own="CP_64_tunis_al_grabah_market",
    ),
    plugin(
        disableSPs,
        cp="CP_64_tunis_al_grabah_market",
        team=2,
        we_own="CP_64_FinalPush_dummy",
    ),
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # Push mode
    plugin(aiPush),
    plugin(
        linkCPs,
        target="CP_64_FinalPush_dummy",
        source=("CP_64_tunis_al_grabah_market, " "Cannon_position, " "CP_64_tunis_old_mosque"),
        never_owned_by=1,
        default_zero=True,
    ),
]

gpm_cq = {
    64: tickets_64 + spawns + kit_limits + push_64 + linkCPs_64 + dynamicoob_64 + nco,
    16: tickets_16 + kit_limits + nco,
}

gpm_coop = {
    64: coop_64 + tickets_64 + nco,
}
sp3 = gpm_coop
