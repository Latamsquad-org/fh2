# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    push,
    teamSPs,
    limitKit,
    ticketLoss,
    NCOrifleData,
    linkCPs,
    spawnerCondition,
    disableSPs,
    dynamicOOB,
    DoubleBleed,
    aiPush,
)
bleed_64 = [
    plugin(
        DoubleBleed,
    )
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_lenino_phase1_dummy": {
                "allies": {
                    "creates": ["CombatArea_allies2"],
                    "destroys": ["CombatArea_axis1"],
                },
            },
        },
        inactive_at_start=["CombatArea_allies2"],
        delay_axis=120,
        delay_allies=0,
    )
]

push = [
    plugin(
        push,
        source="CP_64_lenino_sysoevo,CP_64_lenino_moiseevo",
        target="CP_64_lenino_phase1_dummy",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_lenino_phase1_dummy",
        target="CP_64_lenino_lenino,CP_64_lenino_hill_215,CP_64_lenino_polzuhy,CP_64_lenino_trigubova",
        attacker=2,
        display_arrow=False,
    ),
]

spawns = [
    plugin(teamSPs),  # Auto-fill
]

limitkit = [
    plugin(limitKit, team=2, slot=0, kit="PE_Scout_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="PE_SMGAssault_Limited", limit=0.3),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="PE_LMG_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GW_AntitankAssault_patrone_haft", limit=0.2),
    plugin(limitKit, team=2, slot=5, kit="PE_AntitankAssault_limited", limit=0.2),
]

limitkit_16 = [
    plugin(limitKit, team=2, slot=0, kit="PE_Scout_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=1, kit="GW_SMGAssault_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=1, kit="PE_SMGAssault_Limited", limit=0.2),
    plugin(limitKit, team=1, slot=3, kit="GW_LMG_Limited", limit=0.1),
    plugin(limitKit, team=2, slot=3, kit="PE_LMG_Limited", limit=0.1),
    plugin(limitKit, team=1, slot=5, kit="GW_SMGAssault_mp717(r)_Limited", limit=0.08),
    plugin(limitKit, team=2, slot=5, kit="PE_SMGAssault_pps43_Limited", limit=0.08),
]

ticketloss = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]


rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO_G41_early", "PE_NCO_43"),
        soldiers=("GcWhFeldgrau_nco", "pe_nco_soldier"),
    )
]

linksCPs_64 = [
    plugin(
        linkCPs,
        target="CP_64_lenino_phase1_dummy",
        source="CP_64_lenino_sysoevo,CP_64_lenino_moiseevo",
    ),
]

reinforcements_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_lenino_de_reinforcement1_ferdinand",
        they_own="CP_64_lenino_phase1_dummy",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_lenino_de_reinforcement2_ferdinand",
        they_own="CP_64_lenino_phase1_dummy and CP_64_lenino_lenino and CP_64_lenino_hill_215 and CP_64_lenino_polzuhy and CP_64_lenino_trigubova",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_lenino_33_Army_plane1",
        we_own="CP_64_lenino_phase1_dummy",
    ),
]


gpm_cq = {
    64: push
    + spawns
    + limitkit
    + ticketloss
    + rifleNCO
    + linksCPs_64
    + reinforcements_64
    + dynamicoob_64,
    32: spawns + limitkit + ticketloss + rifleNCO,
    16: limitkit_16 + tickets_16 + rifleNCO,
}

kits_AI = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout_mid",
        soldier="GcWhFeldgrau_alt",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="GcWhFeldgrau_light",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault_noNadeLauncher",
        soldier="GcWhFeldgrau_alt",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GW_LMG_Limited",
        soldier="GcWhFeldgrau_light",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="GcWhFeldgrau_light",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="GW_AntitankAssault_patrone_haft",
        soldier="GcWhFeldgrau_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="PE_Scout_Limited",
        soldier="pe_light_alt_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="PE_SMGAssault_Limited",
        soldier="pe_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=10.0 / 32.0,
        kit="PE_RifleAssault",
        soldier="pe_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=5.0 / 32.0,
        kit="PE_LMG_Limited",
        soldier="pe_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="PE_Engineer",
        soldier="pe_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="PE_AntitankAssault_limited",
        soldier="pe_light_alt_soldier",
    ),
    plugin(
        NCOrifleData,
        kits=("GW_NCO_G41_early", "PE_NCO_43"),
        soldiers=("GcWhFeldgrau_nco", "pe_nco_soldier"),
    ),
]

kits_sp1 = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout_mid",
        soldier="GcWhFeldgrau_alt",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GW_SMGAssault_Limited",
        soldier="GcWhFeldgrau_light",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault_noNadeLauncher",
        soldier="GcWhFeldgrau_alt",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GW_LMG_Limited",
        soldier="GcWhFeldgrau_light",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="GcWhFeldgrau_light",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=0.08 / 32.0,
        kit="GW_SMGAssault_mp717(r)_Limited",
        soldier="GcWhFeldgrau_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="PE_Scout_Limited",
        soldier="pe_light_alt_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="PE_SMGAssault_Limited",
        soldier="pe_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=10.0 / 32.0,
        kit="PE_RifleAssault",
        soldier="pe_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=5.0 / 32.0,
        kit="PE_LMG_Limited",
        soldier="pe_heavy_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="PE_Engineer_satchel",
        soldier="pe_light_soldier",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=0.08 / 32.0,
        kit="PE_SMGAssault_pps43_Limited",
        soldier="pe_light_alt_soldier",
    ),
    plugin(
        NCOrifleData,
        kits=("GW_NCO_G41_early", "PE_NCO_43"),
        soldiers=("GcWhFeldgrau_nco", "pe_nco_soldier"),
    ),
]

disableSPs_64_AI = [
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_lenino_trigubova",
        we_own="CP_64_lenino_moiseevo or CP_64_lenino_sysoevo",
    ),
]

AI_push_64 = [
  plugin(aiPush),  # Push mode for AI
]
  
gpm_coop = {
    64: AI_push_64 + spawns + kits_AI + ticketloss + disableSPs_64_AI + reinforcements_64,
    32: spawns + ticketloss + kits_AI,
    16: tickets_16 + kits_sp1,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
