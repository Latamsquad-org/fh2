# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    disableSPs,
    limitKit,
    linkCPs,
    NCOrifleData,
    push,
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
        kits=("GA_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("ga_nco_soldier", "ba_nco_soldier"),
    )
]

kit_limits = [
    plugin(
        limitKit, team=1, kit="GA_Limited_Assault_MP40_K98", slot=1, limit=0.25
    ),
    plugin(
        limitKit,
        team=2,
        kit="BA_Limited_Assault_TommygunD_No4",
        slot=1,
        limit=0.25,
    ),
    plugin(
        limitKit, team=1, kit="GA_Limited_Support_MG34_K98", slot=3, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="BA_Limited_Support_Bren_No4", slot=3, limit=0.15
    ),
    plugin(limitKit, team=1, kit="ga_ATPzB39_Limited", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="BA_ATBoys_Limited", slot=5, limit=0.1),
]

push_64 = [
    plugin(
        push,
        source="CP_64_Supercharge_British_HQ",
        target="CP_64_Supercharge_Tell_el_Eisa, CP_64_Supercharge_Tell_el_Aqqaqir, CP_64_Supercharge_Sidi_Abd_el_Rahman",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_Supercharge_Tell_el_Eisa, CP_64_Supercharge_Tell_el_Aqqaqir",
        target="CP_64_Supercharge_locker",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_Supercharge_Sidi_Abd_el_Rahman, CP_64_Supercharge_locker",
        target="CP_64_Supercharge_Ghazal",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_Supercharge_Ghazal",
        target="CP_64_Supercharge_East_El_Daba, CP_64_Supercharge_El_Daba",
        attacker=2,
        display_arrow=False,
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=18)]

tickets_32 = [plugin(ticketLoss, ticketLoss1=20, ticketLoss2=20)]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_Supercharge_locker",
        source=[
            "CP_64_Supercharge_Tell_el_Eisa",
            "CP_64_Supercharge_Tell_el_Aqqaqir",
        ],
    ),
]

spawnerConditions = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_Supercharge_El_Daba_11, CP_64_Supercharge_El_Daba_, CP_64_Supercharge_El_Daba_DE_GB_HeavyTank2_0, CP_64_Supercharge_Ghazal_DE_GB_HeavyTank, CP_64_Supercharge_Ghazal_DE_GB_HeavyTank2",
        we_dont_own="CP_64_Supercharge_locker",
    ),
]

gpm_cq = {
    64: tickets_64 + kit_limits + push_64 + links_64 + spawnerConditions + nco,
    32: kit_limits + tickets_32 + nco + bleed_32,
    16: kit_limits + nco,
}


disable_AI = [
    plugin(disableSPs),  # Auto-fill
]

team_spawns = [
    plugin(teamSPs),  # Auto-fill
]


# Push for SP
push_64_SP = [
    plugin(
        push,
        source="CP_64_SP_Supercharge_British_HQ",
        target="CP_64_SP_Supercharge_Tell_el_Eisa, CP_64_SP_Supercharge_Tell_el_Aqqaqir, CP_64_SP_Supercharge_Sidi_Abd_el_Rahman",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_SP_Supercharge_Tell_el_Eisa, CP_64_SP_Supercharge_Tell_el_Aqqaqir",
        target="CP_64_SP_Supercharge_locker",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_SP_Supercharge_Sidi_Abd_el_Rahman, CP_64_SP_Supercharge_locker",
        target="CP_64_SP_Supercharge_Ghazal",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_SP_Supercharge_Ghazal",
        target="CP_64_SP_Supercharge_East_El_Daba, CP_64_SP_Supercharge_El_Daba",
        attacker=2,
        display_arrow=False,
    ),
]


# Push for COOP
push_64_coop = [
    plugin(
        push,
        source="CP_64_coop_Supercharge_British_HQ",
        target="CP_64_coop_Supercharge_Tell_el_Eisa, CP_64_coop_Supercharge_Tell_el_Aqqaqir, CP_64_coop_Supercharge_Sidi_Abd_el_Rahman",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_coop_Supercharge_Tell_el_Eisa, CP_64_coop_Supercharge_Tell_el_Aqqaqir",
        target="CP_64_coop_Supercharge_locker",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_coop_Supercharge_Sidi_Abd_el_Rahman, CP_64_coop_Supercharge_locker",
        target="CP_64_coop_Supercharge_Ghazal",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_coop_Supercharge_Ghazal",
        target="CP_64_coop_Supercharge_East_El_Daba, CP_64_coop_Supercharge_El_Daba",
        attacker=2,
        display_arrow=False,
    ),
]


links_64_coop = [
    plugin(
        linkCPs,
        target="CP_64_coop_Supercharge_locker",
        source=[
            "CP_64_coop_Supercharge_Tell_el_Eisa",
            "CP_64_coop_Supercharge_Tell_el_Aqqaqir",
        ],
    ),
]

links_64_SP = [
    plugin(
        linkCPs,
        target="CP_64_SP_Supercharge_locker",
        source=[
            "CP_64_SP_Supercharge_Tell_el_Eisa",
            "CP_64_SP_Supercharge_Tell_el_Aqqaqir",
        ],
    ),
]


gpm_coop = {
    64: team_spawns + push_64_coop + links_64_coop + tickets_64 + nco,
    32: tickets_32 + nco + bleed_32,
    16: team_spawns + disable_AI + nco,
}


sp3 = {
    64: team_spawns + push_64_SP + links_64_SP + tickets_64 + nco,
}

sp2 = {
    32: tickets_32 + nco + bleed_32,
}

sp1 = {
    16: team_spawns + disable_AI + nco,
}
