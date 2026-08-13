# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,C0302,E0401
from game.plugins import (
    plugin,
    limitKit,
    push,
    teamSPs,
    ticketLoss,
    destroyObjective,
    linkCPs,
    disableSPs,
    aiPush,
    dynamicOOB,
    SectorTickets,
    NCOrifleData,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "BW_NCO_Sten"),
        soldiers=("gw_heer_unteroffizier", "bw_nco_soldier"),
    )
]

links_32 = [
    plugin(
        linkCPs,
        target="CP_32_Ancto_OBJ_sector_B",
        source="CP_32_Ancto_OBJ_sector_A",
        invert=True,
        never_owned_by=2,
    ),
    plugin(
        linkCPs,
        target="CP_32_Ancto_OBJ_sector_C",
        source="CP_32_Ancto_OBJ_sector_B",
        invert=True,
        never_owned_by=2,
    ),
    plugin(
        linkCPs,
        target="CP_32_Ancto_OBJ_sector_D",
        source="CP_32_Ancto_OBJ_sector_C",
        invert=True,
        never_owned_by=2,
    ),
]

sector_tickets_32 = [
    plugin(
        SectorTickets,
        sector_tickets={
            "CP_32_Ancto_OBJ_sector_A": {
                "capped_by": "allies",
                "allies": "+150",
            },
            "CP_32_Ancto_OBJ_sector_B": {
                "capped_by": "allies",
                "allies": "+150",
            },
            "CP_32_Ancto_OBJ_sector_C": {
                "capped_by": "allies",
                "allies": "+150",
            },
            "CP_32_Ancto_OBJ_sector_D": {
                "capped_by": "allies",
                "allies": "+150",
            },
        },
    )
]

dynamicoob_32 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_32_Ancto_OBJ_sector_A": {
                "allies": {
                    "creates": ["CombatArea_32_allies2"],
                    "destroys": ["CombatArea_32_axis1"],
                },
            },
            "CP_32_Ancto_OBJ_sector_B": {
                "allies": {
                    "creates": ["CombatArea_32_allies3"],
                    "destroys": ["CombatArea_32_axis2"],
                },
            },
            "CP_32_Ancto_OBJ_sector_C": {
                "allies": {
                    "creates": ["CombatArea_32_allies4"],
                    "destroys": ["CombatArea_32_axis3"],
                },
            },
        },
        inactive_at_start=[
            "CombatArea_32_allies2",
            "CombatArea_32_allies4",
            "CombatArea_32_allies3",
        ],
        delay_axis=60,
        delay_allies=30,
    )
]

objectives_32 = [
    plugin(
        destroyObjective,
        controlpoint="CP_32_Ancto_OBJ_sector_A",
        refcount=4,
        template=["Objective_belgian_gate", "flak18ns_fr"],
    ),
    plugin(
        destroyObjective,
        controlpoint="CP_32_Ancto_OBJ_sector_B",
        refcount=4,
        template=["hqradio2", "flak38_france"],
    ),
    plugin(
        destroyObjective,
        controlpoint="CP_32_Ancto_OBJ_sector_C",
        refcount=4,
        template=["hqradio1", "flakvierling38_france"],
    ),
    plugin(
        destroyObjective,
        controlpoint="CP_32_Ancto_OBJ_sector_D",
        refcount=4,
        template=["panthera_late_alt", "flak18ns_fr_two"],
    ),
]

kitlimits = [
    plugin(limitKit, team=1, slot=0, kit="GW_Scout_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=0, kit="BW_Scout_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.05),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.05),
    plugin(limitKit, team=1, slot=4, kit="GW_Engineer_Satchel_ancto", limit=0.2),
    plugin(limitKit, team=2, slot=4, kit="BW_Engineer_Satchel_ancto", limit=0.2),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BW_AssaultEngineer", limit=0.05),
]

kitlimits_16 = [
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="BW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_MG42_Limited", limit=0.05),
    plugin(limitKit, team=2, slot=3, kit="BW_LMG_Limited", limit=0.05),
    plugin(limitKit, team=1, slot=4, kit="GS_RifleAssault_ramelle", limit=0.34),
    plugin(limitKit, team=2, slot=4, kit="BW_RifleAssault_Limited", limit=0.34),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=5, kit="BW_RifleAssault_no69_Limited", limit=0.1),
]

push_64 = [
    plugin(
        push,
        source="CP_64_Anctoville_Secteur_Nord",
        target="CP_64_Anctoville_Les_Ecuries",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_Anctoville_Rue_de_la_Fontaine",
        target="CP_64_Anctoville_L_Eglise",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_Anctoville_Rue_de_la_Fontaine",
        target="CP_64_Anctoville_Mairie",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_Anctoville_L_Eglise",
        target="CP_64_Anctoville_les_Fermes_a_l_Est",
        attacker=2,
    ),
    plugin(
        push,
        source="CP_64_Anctoville_Mairie",
        target="CP_64_Anctoville_les_Fermes_a_l_Est",
        attacker=2,
    ),
]

team_spawns = [
    plugin(teamSPs),  # Auto-fill
]

tickets_cq_32 = [plugin(ticketLoss, ticketLoss1=2000, ticketLoss2=25)]
tickets_cq_64 = [plugin(ticketLoss, ticketLoss1=300, ticketLoss2=14)]
tickets_cq_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]


gpm_cq = {
    64: (kitlimits + tickets_cq_64 + push_64 + team_spawns + nco),
    32: (
        kitlimits
        + tickets_cq_32
        + objectives_32
        + links_32
        + team_spawns
        + sector_tickets_32
        + dynamicoob_32
        + nco
    ),
    16: kitlimits_16 + nco + tickets_cq_16,
}

coop_64 = [
    # Kit limits - Axis
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout_Limited",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=5.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="gw_heer_maschinenpistole",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=11.0 / 32.0,
        kit="GW_RifleAssault_noNadeLauncher",
        soldier="gw_heer_gewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GW_LMG_MG42_Limited",
        soldier="gw_heer_maschinengewehr",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer_Satchel_ancto",
        soldier="gw_heer_pionier",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=4.0 / 32.0,
        kit="GW_AntitankAssault_Limited",
        soldier="gw_heer_panzerabwehr",
    ),
    # Kit limits - Allies
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="BW_Scout_Limited",
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
        limit=10.0 / 32.0,
        kit="BW_RifleAssault",
        soldier="bw_light_soldier",
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
        limit=4.0 / 32.0,
        kit="BW_Engineer_Satchel_ancto",
        soldier="bw_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="BW_AssaultEngineer",
        soldier="bw_heavy_soldier",
    ),
    # Push mode
    plugin(aiPush),
    # AI spawn points disabler
    plugin(disableSPs),  # Auto-fill
    # Ticket bleed
    plugin(ticketLoss, ticketLoss1=14, ticketLoss2=14),
]

gpm_coop = {
    64: coop_64 + team_spawns + nco,
}
sp3 = gpm_coop
