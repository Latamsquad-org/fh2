# -*- coding: utf-8 -*-
# pylint: disable=W0232,C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    neighPush,
    teamSPs,
    ticketLoss,
    NCOrifleData,
    destroyObjective,
    linkCPs,
    push,
    dynamicOOB,
    spawnerCondition
)


kitlimits_64 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GW_SMGAssault_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UW_SMGAssault_para_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_LMG_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UW_m1Carbine_para_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="GW_Engineer_Satchel_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        kit="UW_Engineer_Satchel_para_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_RifleAssault_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UW_RifleGrenadier_para_Limited",
        limit=0.1,
    ),
]

kitlimits_32 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GW_SMGAssault_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UW_SMGAssault_para_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_LMG_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UW_m1Carbine_para_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="GW_Engineer_Satchel_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        kit="UW_Engineer_Satchel_para_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_RifleAssault_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UW_RifleGrenadier_para_Limited",
        limit=0.1,
    ),
]

kitlimits_16 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="GW_SMGAssault_Limited",
        limit=0.3,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UW_SMGAssault_para_Limited",
        limit=0.3,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="GW_LMG_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UW_m1Carbine_para_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="GW_Engineer_Satchel_Limited",
        limit=0.3,
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        kit="UW_Engineer_Satchel_para_Limited",
        limit=0.3,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="GW_RifleAssault_Limited",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UW_RifleGrenadier_para_Limited",
        limit=0.1,
    ),
]

rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO_SME_para"),
        soldiers=("gw_heer_unteroffizier", "uw_airborne_sgt"),
    ),
]


# allies objectives and push 64

objectives_64 = [
    plugin(
        destroyObjective,
        controlpoint="CP_64_sme_objectives_locker",
        refcount=8,
        template=["pak40_static", "renault_ue_beute_ammo", "flakvierling38_france", "sgwr34_france", "pak35_europe_static", "hqradio1", "hqradio2"],
    ),
]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_sme_82nd_land1",
        source="CP_64_sme_objectives_locker",
        invert=False
    ),
]

push_64 = [
    plugin(
        neighPush,
        sources="CP_64_sme_82nd_land1",
        targets="CP_64_sme_to_carentan,CP_64_sme_to_utah_beach,CP_64_sme_to_azzeville",
    ),
    plugin(
        neighPush,
        sources="CP_64_sme_to_utah_beach,CP_64_sme_to_carentan",
        targets="CP_64_sme_centre_ville",
    ),
    plugin(
        neighPush,
        sources="CP_64_sme_to_utah_beach,CP_64_sme_to_azzeville",
        targets="CP_64_sme_centre_ville",
    ),
    plugin(
        neighPush,
        sources="CP_64_sme_to_azzeville,CP_64_sme_to_carentan",
        targets="CP_64_sme_centre_ville",
    ),
    plugin(
        neighPush,
        sources="CP_64_sme_to_azzeville",
        targets="CP_64_sme_to_neuville_au_plain",
    ),
    plugin(
        neighPush,
        sources="CP_64_sme_to_neuville_au_plain",
        targets="CP_64_sme_centre_ville",
    ),
    plugin(
        neighPush,
        sources="CP_64_sme_centre_ville,CP_64_sme_to_azzeville",
        targets="CP_64_sme_to_neuville_au_plain",
    ),
    plugin(
        neighPush,
        sources="CP_64_sme_to_la_fiere",
        targets="CP_64_sme_to_neuville_au_plain,CP_64_sme_centre_ville,CP_64_sme_to_carentan",
    ),
]

spawnerCondition_64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_sme_82nd_air1_c47spawn_1,CP_64_sme_82nd_air1_c47spawn_2,CP_64_sme_82nd_air1_c47spawn_3,CP_64_sme_82nd_air1_c47spawn_4,CP_64_sme_82nd_air1_c47spawn_5,"
        + "CP_64_sme_82nd_air1_c47spawn_6,CP_64_sme_82nd_air1_c47spawn_7,CP_64_sme_82nd_air1_c47spawn_8,CP_64_sme_82nd_air1_c47spawn_9",
        we_dont_own="CP_64_sme_82nd_land1",
    ),
]

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_sme_objectives_locker": {
                "allies": {
                    "creates": ["CombatArea_62_gpm_cq64"],
                    "destroys": ["CombatArea_0_Conquest_64"],
                },
            },
        },
        inactive_at_start=[
            "CombatArea_62_gpm_cq64",
        ],
        delay_axis=0,
        delay_allies=120,
    )
]

# allies push 32

npush_32 = [
    plugin(
        neighPush,
        sources="CP_32_sme_82abn",
        targets="CP_32_sme_to_carentan",
    ),
    plugin(
        neighPush,
        sources="CP_32_sme_82abn",
        targets="CP_32_sme_faubourg",
    ),
    plugin(
        neighPush,
        sources="CP_32_sme_to_carentan",
        targets="CP_32_sme_centre_ville",
    ),
    plugin(
        neighPush,
        sources="CP_32_sme_faubourg",
        targets="CP_32_sme_to_utah_beach",
    ),
    plugin(
        neighPush,
        sources="CP_32_sme_faubourg",
        targets="CP_32_sme_centre_ville",
    ),
    plugin(
        neighPush,
        sources="CP_32_sme_centre_ville",
        targets="CP_32_sme_to_utah_beach",
    ),
    plugin(
        neighPush,
        sources="CP_32_sme_centre_ville",
        targets="CP_32_sme_old_hospital",
    ),
    plugin(
        neighPush,
        sources="CP_32_sme_to_utah_beach",
        targets="CP_32_sme_old_hospital",
    ),
]
spawns = [
    plugin(teamSPs),  # Auto-fill
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=11, ticketLoss2=10)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=8, ticketLoss2=6)]

gpm_cq = {
    64: tickets_64 + kitlimits_64 + rifleNCO + spawns + spawnerCondition_64 + push_64 + 
links_64 + objectives_64 + dynamicoob_64,
    32: tickets_32 + npush_32 + kitlimits_32 + rifleNCO + spawns,
    16: kitlimits_16 + tickets_16 + rifleNCO + spawns,
}
