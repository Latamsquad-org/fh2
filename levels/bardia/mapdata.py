# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    aiPush,
    balanceSPs,
    disableSPs,
    limitKit,
    linkCPs,
    NCOrifleData,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    timeCP,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("IA_NCOBeretta38", "AA_NCOTommygunS"),
        soldiers=("ia_light_soldier", "aa_nco_soldier_alt"),
    )
]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_bardia_bleeder",
        source=[
            "CP_64_bardia_City_Hospital",
            "CP_64_bardia_River_outpost",
            "CP_64_bardia_Hospital",
            "CP_64_bardia_Barracks",
        ],
    ),
]

push_64 = [
    plugin(
        push,
        source="CP_64_bardia_Hospital",
        target="CP_64_bardia_bleeder",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bardia_River_outpost",
        target="CP_64_bardia_bleeder",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bardia_City_Hospital",
        target="CP_64_bardia_bleeder",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
    plugin(
        push,
        source="CP_64_bardia_Barracks",
        target="CP_64_bardia_bleeder",
        attacker=2,
        display_arrow=False,
        wants_target_marker=False,
    ),
]

kit_limits = [
    plugin(limitKit, team=1, kit="IA_Limited_Assault_Beretta38_K98", slot=1, limit=0.2,),
    plugin(limitKit, team=2, kit="AA_Limited_Assault_TommygunD_No4", slot=1, limit=0.2,),
    plugin(limitKit, team=1, kit="IA_Limited_Support_MG34_K98", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="AA_Limited_Support_Bren_No4", slot=3, limit=0.15),
    plugin(limitKit, team=1, kit="IA_AntiTank_carcano", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="AA_ATBoys_Limited", slot=5, limit=0.1),
]
kit_limits_16 = [
    plugin(limitKit, team=1, kit="IA_Limited_Assault_Beretta38_K98", slot=1, limit=0.2,),
    plugin(limitKit, team=2, kit="AA_Limited_Assault_TommygunD_No4", slot=1, limit=0.2,),
    plugin(limitKit, team=1, kit="IA_Limited_Support_MG34_K98", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="AA_Limited_Support_Bren_No4", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="IA_AntiTank_carcano", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="BA_Grenadier_Limited", slot=5, limit=0.1),
]
tickets_64 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=20)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=12, ticketLoss2=12)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=8, ticketLoss2=8)]

gpm_cq = {
    64: push_64 + kit_limits + links_64 + tickets_64 + nco,
    32: tickets_32 + kit_limits_16 + nco,
    16: tickets_16 + kit_limits_16 + nco,
}


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
        limit=5.0 / 32.0,
        kit="IA_Limited_Assault_Beretta38_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
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
        kit="IA_EngineerK98Short",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
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
        limit=6.0 / 32.0,
        kit="AA_Limited_Assault_TommygunD_No4",
        soldier="aa_heavy_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=9.0 / 32.0,
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
        kit="AA_EngineerEarly",
        soldier="aa_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="AA_ATBoys_Limited",
        soldier="aa_heavy_soldier_alt",
    ),
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
        limit=6.0 / 32.0,
        kit="IA_Limited_Assault_Beretta38_K98",
        soldier="ia_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=16.0 / 32.0,
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
        limit=1.0 / 32.0,
        kit="IA_EngineerK98Short",
        soldier="ia_light_soldier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=0.0 / 32.0,
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
        limit=6.0 / 32.0,
        kit="AA_Limited_Assault_TommygunD_No4",
        soldier="aa_heavy_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=16.0 / 32.0,
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
        limit=1.0 / 32.0,
        kit="AA_EngineerEarly",
        soldier="aa_light_soldier_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=0.0 / 32.0,
        kit="AA_ATBoys_Limited",
        soldier="aa_heavy_soldier_alt",
    ),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    # Team locked spawn points
    plugin(teamSPs),  # Auto-fill
    # PCO spawning conditions
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_bardia_AIF_LightMortar,CP_32_bardia_AIF_DE_GB_LightMG",
        they_own="CP_32_bardia_Barracks",
    ),
    # Ticket bleed
    plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15),
]

gpm_coop = {
    16: tickets_16 + nco,
    32: coop_32 + nco,
    64: coop_64 + push_64 + links_64 + tickets_64 + nco,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
