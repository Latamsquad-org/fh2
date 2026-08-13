# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
# vim:set ts=4 sts=4 sw=4 et syntax=python:
from game.plugins import (
    plugin,
    limitKit,
    ticketLoss,
    NCOrifleData,
    teamSPs,
    spawnerCondition,
    push,
    linkCPs,
    dynamicOOB,
)

dynamicoob_64 = [
    plugin(
        dynamicOOB,
        dynamic_flags={
            "CP_64_tarawa_ThePier": {
                "allies": {
                    "creates": ["nogo_axis_pier"],
                },
            },
        },
        inactive_at_start=["nogo_axis_pier"],
        delay_axis=120,
    )
]
link_64 = [
    plugin(
        linkCPs,
        target="CP_64_tarawa_pointsflag",
        source="CP_64_tarawa_GarrisonHQ",
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=25)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=16, ticketLoss2=16)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]
kit_limits_16 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="jp_SMGAssault_early",
        limit=0.3,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UP_SMGAssault_1928a1_30rnd",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="JP_LMG_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UP_LMG_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="jp_kneemortar",
        limit=0.08,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="JP_Engineer_Turtlemine",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UP_Engineer_M1903a1_Satchel_nowrench",
        limit=0.1,
    ),
]

kit_limits_32 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="jp_SMGAssault_early",
        limit=0.3,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UP_SMGAssault_1928a1_30rnd",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="JP_LMG_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UP_LMG_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="jp_kneemortar",
        limit=0.08,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="JP_Engineer_Turtlemine",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UP_Engineer_M1903a1_Satchel_nowrench",
        limit=0.1,
    ),
]

kit_limits_64 = [
    plugin(
        limitKit,
        team=1,
        slot=1,
        kit="jp_SMGAssault_early",
        limit=0.3,
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        kit="UP_SMGAssault_1928a1_30rnd",
        limit=0.2,
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        kit="JP_LMG_Limited",
        limit=0.15,
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        kit="UP_LMG_Limited",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        kit="jp_kneemortar",
        limit=0.08,
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        kit="JP_Engineer_Turtlemine",
        limit=0.1,
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        kit="UP_Engineer_M1903a1_Satchel_nowrench",
        limit=0.1,
    ),
]


# Allied landing crafts
pco_spawners_64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner=[
            "CP_64_tarawa_2ndMarineDivision_15",
            "CP_64_tarawa_2ndMarineDivision_6",
            "CP_64_tarawa_2ndMarineDivision_3_2",
            "CP_64_tarawa_2ndMarineDivision_5",
            "CP_64_tarawa_2ndMarineDivision_4_2",
            "CP_64_tarawa_2ndMarineDivision_17",
            "CP_64_tarawa_2ndMarineDivision_18",
            "CP_64_tarawa_2ndMarineDivision_5_0",
        ],
        they_own=[
            "CP_64_tarawa_GreenBeach",
            "CP_64_tarawa_CoastalGuns",
            "CP_64_tarawa_RedBeach",
        ],
    ),
]


push_64 = [
    # PUSH BEACH - CENTER - HQ
    # ========================
    # plugin(
    #     push,
    #     source=[
    #         "CP_64_tarawa_GreenBeach",
    #         "CP_64_tarawa_CoastalGuns",
    #     ],
    #     target=[
    #         "CP_64_tarawa_ThePocket",
    #         "CP_64_tarawa_RedBeach",
    #     ],
    #     attacker=2,
    #     display_arrow=False,
    #     count=1,
    #     force=True,
    # ),
    # plugin(
    #     push,
    #     source="CP_64_tarawa_2ndMarineDivision",
    #     target=[
    #         "CP_64_tarawa_CoastalGuns",
    #         "CP_64_tarawa_GreenBeach",
    #         # "CP_64_tarawa_RedBeach",
    #         "CP_64_tarawa_ThePier",
    #         # "CP_64_tarawa_ThePocket",
    #     ],
    #     attacker=2,
    #     display_arrow=False,
    # ),
    # # Capture all to open Garrison
    # plugin(
    #     push,
    #     source=[
    #         # "CP_64_tarawa_CoastalGuns",
    #         # "CP_64_tarawa_GreenBeach",
    #         "CP_64_tarawa_RedBeach",
    #         # "CP_64_tarawa_ThePier",
    #         "CP_64_tarawa_ThePocket",
    #     ],
    #     target="CP_64_tarawa_GarrisonHQ",
    #     attacker=2,
    #     display_arrow=False,
    # ),
    # plugin(
    #     push,
    #     source="CP_64_tarawa_GarrisonHQ",
    #     target="CP_64_tarawa_pointsflag",
    #     attacker=2,
    #     display_arrow=False,
    # ),
    # ====================
    plugin(
        push,
        source="CP_64_tarawa_2ndMarineDivision",
        target=[
            "CP_64_tarawa_CoastalGuns",
            "CP_64_tarawa_GreenBeach",
            "CP_64_tarawa_ThePier",
            "CP_64_tarawa_ThePocket",
        ],
        attacker=2,
        display_arrow=False,
    ),
    # # Capture all to open Garrison
    plugin(
        push,
        source=[
            "CP_64_tarawa_CoastalGuns",
            "CP_64_tarawa_GreenBeach",
            "CP_64_tarawa_RedBeach",
            "CP_64_tarawa_ThePocket",
        ],
        target="CP_64_tarawa_GarrisonHQ",
        attacker=2,
        display_arrow=False,
    ),
    plugin(
        push,
        source="CP_64_tarawa_GarrisonHQ",
        target="CP_64_tarawa_pointsflag",
        attacker=2,
        display_arrow=False,
    ),
]


spawns_all = [plugin(teamSPs)]


rifleNCO = [
    plugin(
        NCOrifleData,
        kits=("JP_NCO", "UP_NCO_1928a1_30rnd"),
        soldiers=("jp_rilfe_khaki", "up_Sft_FrogCamo_Full"),
    )
]

gpm_cq = {
    64: (
        tickets_64
        + kit_limits_64
        + rifleNCO
        + spawns_all
        + pco_spawners_64
        + push_64
        + link_64
        + dynamicoob_64
    ),
    32: (tickets_32 + kit_limits_32 + rifleNCO + spawns_all),
    16: (tickets_16 + kit_limits_16 + rifleNCO + spawns_all),
}
