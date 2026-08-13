# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    disableSPs,
    FastBleed,
    limitKit,
    NCOrifleData,
    # neighPush,
    push,
    spawnerCondition,
    teamSPs,
    ticketLoss,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO_SME"),
        soldiers=("gcwhsnow_nco", "uc_late44_airborne_sgt"),
    )
]

fastbleed_64 = [
    plugin(
        FastBleed,
        affected_team="allies",
        target_flags=[
            "conq_64_bastogne_trainstation",
            "conq_64_bastogne_outskirts_0",
        ],
    ),
]

# This push section intends to unlock the flags in the following pattern:
#
# To unlock the Trainstation, either:
#   a) hold Bizory + Mageret + Mont
#   b) hold Bizory + Mageret + Wardin
#   c) hold Outskirts
#
# To unlock Outskirts, either:
#   a) hold Mageret + Wardin + Marvie
#   b) hold Wardin + Mont + Marvie
#   c) hold Trainstation
#
# Mont is unlocked by either Wardin or Mageret.
# Bizory is unlocked by Mageret.
# Marvie is unlocked by Wardin.
push_64 = [
    plugin(push, source="conq_64_mageret", target="conq_64_bizory", attacker=1),
    plugin(push, source="conq_64_mageret", target="conq_64_mont", attacker=1),
    plugin(push, source="conq_64_wardin", target="conq_64_mont", attacker=1),
    plugin(push, source="conq_64_wardin", target="conq_64_marvie", attacker=1),
    plugin(
        push,
        source=[
            "conq_64_wardin",
            "conq_64_mageret",
        ],
        target="conq_64_mont",
        attacker=1,
        force=True,
        count=1,
    ),
    plugin(
        push,
        source=[
            "conq_64_bizory",
            "conq_64_mageret",
            "conq_64_mont",
            "conq_64_wardin",
        ],
        target="conq_64_bastogne_trainstation",
        attacker=1,
        force=True,
        count=3,
        display_arrow=False,
    ),
    plugin(
        push,
        source=[
            "conq_64_mageret",
            "conq_64_mont",
            "conq_64_wardin",
            "conq_64_marvie",
        ],
        target="conq_64_bastogne_outskirts_0",
        attacker=1,
        force=True,
        count=3,
        display_arrow=False,
    ),
    # capture *other* town flag once one goes down. unfortunately, once they are both captured,
    # they will both lock. Ideally a `neighborPush` would be used here, but this does not play
    # nice with the `push`: if you use that, the "Outskirts" flag is unlocked due to the
    # plugins bugging out, because they are not designed to be used at the same time!
    plugin(
        push,
        source="conq_64_bastogne_trainstation",
        target="conq_64_bastogne_outskirts_0",
        attacker=1,
    ),
    plugin(
        push,
        source="conq_64_bastogne_outskirts_0",
        target="conq_64_bastogne_trainstation",
        attacker=1,
    ),
]

push_32 = [
    plugin(
        push,
        source="conq_32_Outskirts",
        target="conq_32_Bastogne",
        attacker=1,
        force=True,
    ),
    plugin(
        push,
        source="conq_32_Church",
        target="conq_32_Bastogne",
        attacker=1,
        force=True,
    ),
]

pco_spawners_64 = [
    # Allied flyovers
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            [
                "conq_64_allied_airsupport_flyover",
                "conq_64_allied_airsupport_0",
                "conq_64_allied_airsupport_1",
                "conq_64_allied_airsupport_2",
                "conq_64_allied_airsupport_4",
                "conq_64_allied_airsupport_5",
                "conq_64_allied_airsupport_0_0",
                "conq_64_allied_airsupport_0_1",
                "conq_64_allied_airsupport_0_2",
            ]
        ),
        we_own="conq_64_mageret and conq_64_wardin",
    ),
    # Axis reinforcements
    plugin(
        spawnerCondition,
        team=1,
        spawner=(
            "conq_64_axis_reinforcements_hanomag, "
            "conq_64_axis_reinforcements_kingtiger, "
            "conq_64_axis_reinforcements_jagdpanzer"
        ),
        we_own="conq_64_mageret or conq_64_wardin",
        they_own="conq_64_mont",
    ),
    # Allied reinforcements
    plugin(
        spawnerCondition,
        team=2,
        spawner=(
            "conq_64_allied_airsupport_alt",
            "conq_64_allied_airsupport_piper",
            "conq_64_allied_airsupport_6",
            "conq_64_allied_airsupport_8",
            "conq_64_allied_airsupport_0_3",
            "conq_64_allied_airsupport_Medic",
            "conq_64_4th_armored_0_gmcammo",
            "conq_64_4th_armored_0_chaffee",
            "conq_64_4th_armored_0_jumbo76",
            "conq_64_4th_armored_0_jumbo",
            "conq_64_4th_armored_0_m4a3",
            "conq_64_4th_armored_0_ammo",
            "conq_64_4th_armored_0_m18",
            "conq_64_bastogne_outskirts_0_chaf",
            "conq_64_bastogne_trainstation_m4a3",
        ),
        they_own="conq_64_bizory or conq_64_marvie or conq_64_mont",
    ),
]


kits_64 = [
    plugin(limitKit, team=1, kit="GW_StG44Assault_Limited", slot=1, limit=0.1),
    plugin(limitKit, team=2, kit="UW_SMGAssault_Limited_GGun", slot=1, limit=0.1),
    plugin(limitKit, team=1, kit="GW_LMG_MG42_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="UW_LMG_m1919a6_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="GW_AntitankAssault60m_Limited", slot=5, limit=0.15),
    plugin(limitKit, team=2, kit="UW_AntitankAssaultM9_Limited", slot=5, limit=0.08),
]

team_spawns = [
    plugin(teamSPs),  # Auto-fill
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=14, ticketLoss2=64)]

gpm_cq = {
    16: kits_64 + nco,
    32: push_32 + kits_64 + team_spawns + nco,
    64: push_64 + kits_64 + team_spawns + tickets_64 + pco_spawners_64 + nco + fastbleed_64,
}


disable_AI = [
    plugin(disableSPs),  # Auto-fill
]

gpm_coop = {
    16: nco,
    32: push_32 + team_spawns + nco,
    64: push_64 + team_spawns + tickets_64 + pco_spawners_64 + disable_AI + nco,
}

sp1 = gpm_coop
sp2 = gpm_coop
sp3 = gpm_coop
