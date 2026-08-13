# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    push,
    linkCPs,
    ticketLoss,
    teamSPs,
    NCOrifleData,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40_early", "AA_NCOTommygunS"),
        soldiers=("ga_early_nco_soldier", "aa_nco_soldier"),
    )
]


kit_limits = [
    plugin(
        limitKit,
        team=1,
        kit="GA_Limited_Assault_MP40_K98_early",
        slot=1,
        limit=0.25,
    ),
    plugin(
        limitKit,
        team=2,
        kit="AA_Limited_Assault_TommygunD_No4",
        slot=1,
        limit=0.25,
    ),
    plugin(
        limitKit, team=1, kit="GA_Limited_Support_MG34_K98", slot=3, limit=0.1
    ),
    plugin(
        limitKit, team=2, kit="AA_Limited_Support_Bren_No4", slot=3, limit=0.15
    ),
    plugin(limitKit, team=1, kit="ga_ATPzB39_Limited", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="AA_ATBoys_Limited", slot=5, limit=0.1),
]

push_64 = [
    plugin(
        push,
        source="CP_64_Tobruk_Forte_Pilastrino",
        target="CP_64_Tobruk_Tobruk_HQ",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_Tobruk_Forte_Pilastrino",
        target="CP_64_Tobruk_Forte_Solaro",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_Tobruk_Forte_Pilastrino",
        target="CP_64_Tobruk_Bir_Baccara",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_Tobruk_Tobruk_HQ",
        target="CP_64_Tobruk_Argub_Bdawa",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_Tobruk_Tobruk_HQ",
        target="CP_64_Tobruk_Forte_Airente",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_Tobruk_Bir_Baccara",
        target="CP_64_Tobruk_Forte_Airente",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_Tobruk_Forte_Solaro",
        target="CP_64_Tobruk_Argub_Bdawa",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_Tobruk_Forte_Airente",
        target="CP_64_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_Tobruk_Argub_Bdawa",
        target="CP_64_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
    plugin(
        linkCPs,
        target="CP_64_Tobruk_dummy",
        source="CP_64_Tobruk_Argub_Bdawa",
        invert=True,
    ),
]

push_32 = [
    plugin(
        push,
        source="CP_32_Tobruk_Forte_Pilastrino",
        target="CP_32_Tobruk_Tobruk_HQ",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_32_Tobruk_Tobruk_HQ",
        target="CP_32_Tobruk_Argub_Bdawa",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_32_Tobruk_Tobruk_HQ",
        target="CP_32_Tobruk_Forte_Airente",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_32_Tobruk_Forte_Airente",
        target="CP_32_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_32_Tobruk_Argub_Bdawa",
        target="CP_32_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
]

push_16 = [
    plugin(
        push,
        source="CP_16_Tobruk_Forte_Airente",
        target="CP_16_Tobruk_Argub_Bdawa",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_16_Tobruk_Forte_Airente",
        target="CP_16_Tobruk_Outpost",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_16_Tobruk_Argub_Bdawa",
        target="CP_16_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_16_Tobruk_Outpost",
        target="CP_16_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
]
tickets_64 = [plugin(ticketLoss, ticketLoss1=18, ticketLoss2=1000)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=18, ticketLoss2=1000)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=16, ticketLoss2=16)]

coop_64_push = [
    plugin(
        push,
        source="CP_64_coop_Tobruk_Forte_Pilastrino",
        target="CP_64_coop_Tobruk_Tobruk_HQ",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_coop_Tobruk_Forte_Pilastrino",
        target="CP_64_coop_Tobruk_Forte_Solaro",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_coop_Tobruk_Forte_Pilastrino",
        target="CP_64_coop_Tobruk_Bir_Baccara",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_coop_Tobruk_Tobruk_HQ",
        target="CP_64_coop_Tobruk_Argub_Bdawa",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_coop_Tobruk_Tobruk_HQ",
        target="CP_64_coop_Tobruk_Forte_Airente",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_coop_Tobruk_Bir_Baccara",
        target="CP_64_coop_Tobruk_Forte_Airente",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_coop_Tobruk_Forte_Solaro",
        target="CP_64_coop_Tobruk_Argub_Bdawa",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_coop_Tobruk_Forte_Airente",
        target="CP_64_coop_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_coop_Tobruk_Argub_Bdawa",
        target="CP_64_coop_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
]
coop_64_linkcp = [
    plugin(
        linkCPs,
        target="CP_64_coop_Tobruk_dummy",
        source="CP_64_coop_Tobruk_Argub_Bdawa",
        invert=True,
    ),
]
coop_64_teamsp = [plugin(teamSPs)]
coop_64_tickets = [plugin(ticketLoss, ticketLoss1=18, ticketLoss2=1000)]


sp3_push = [
    plugin(
        push,
        source="CP_64_SP_Tobruk_Forte_Pilastrino",
        target="CP_64_SP_Tobruk_Tobruk_HQ",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_SP_Tobruk_Forte_Pilastrino",
        target="CP_64_SP_Tobruk_Forte_Solaro",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_SP_Tobruk_Forte_Pilastrino",
        target="CP_64_SP_Tobruk_Bir_Baccara",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_SP_Tobruk_Tobruk_HQ",
        target="CP_64_SP_Tobruk_Argub_Bdawa",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_SP_Tobruk_Tobruk_HQ",
        target="CP_64_SP_Tobruk_Forte_Airente",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_SP_Tobruk_Bir_Baccara",
        target="CP_64_SP_Tobruk_Forte_Airente",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_SP_Tobruk_Forte_Solaro",
        target="CP_64_SP_Tobruk_Argub_Bdawa",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_SP_Tobruk_Forte_Airente",
        target="CP_64_SP_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
    plugin(
        push,
        source="CP_64_SP_Tobruk_Argub_Bdawa",
        target="CP_64_SP_Tobruk_Tobruk_Outskirts",
        attacker=1,
    ),
]
sp3_cp = [
    plugin(
        linkCPs,
        target="CP_64_SP_Tobruk_dummy",
        source="CP_64_SP_Tobruk_Argub_Bdawa",
        invert=True,
    ),
]
sp3_sp = [plugin(teamSPs)]
sp3_tickets = [plugin(ticketLoss, ticketLoss1=18, ticketLoss2=1000)]

gpm_cq = {
    64: kit_limits + push_64 + tickets_64 + nco,
    32: kit_limits + push_32 + nco,
    16: kit_limits + push_16 + nco + tickets_16,
}
gpm_coop = {
    64: coop_64_push + coop_64_linkcp + coop_64_teamsp + coop_64_tickets + nco,
}

sp3 = {
    64: sp3_push + sp3_cp + sp3_sp + sp3_tickets + nco,
}
