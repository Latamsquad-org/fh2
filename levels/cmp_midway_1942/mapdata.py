# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,R0913
from game.plugins import (
    plugin,
    destroyObjective,
    limitKit,
    linkCPs,
    # NamedObjective,
    NCOrifleData,
    spawnerCondition,
    teamSPs,
    ticketLoss,
    cmp_ABC,
)


# bullshit config, but the cmp map checker demands this
kit_limits_64 = [plugin(limitKit, team=1, slot=2, kit="JP_Pilot", limit=1.0)]
kit_limits_32 = [plugin(limitKit, team=1, slot=2, kit="JP_Pilot", limit=1.0)]
kit_limits_16 = [plugin(limitKit, team=1, slot=2, kit="JP_Pilot", limit=1.0)]

abc_16 = [
    plugin(
        cmp_ABC,
        name="allied_main",
        sw=(1200.0, 550.0),
        nw=(1200.0, 2048.0),
        se=(2048.0, 550.0),
    ),
    plugin(
        cmp_ABC,
        name="axis_main",
        se=(-1200.0, 550.0),
        ne=(-1200.0, 2048.0),
        sw=(-2048.0, 550.0),
    ),
]
abc_64 = [
    plugin(
        cmp_ABC,
        name="allied_main",
        sw=(550.0, 550.0),
        nw=(550.0, 2048.0),
        se=(2048.0, 550.0),
    ),
    plugin(
        cmp_ABC,
        name="axis_main",
        se=(-550.0, 550.0),
        ne=(-550.0, 2048.0),
        sw=(-2048.0, 550.0),
    ),
]

NCO_all = [
    plugin(
        NCOrifleData,
        kits=("jp_NCO_early", "UP_NCO_Early_1928_30rnd"),
        soldiers=("jp_rilfe_white_sgt", "up_earlyusmc_khaki_nco"),
    ),
]

spawns_all = [plugin(teamSPs)]

reinforcements_64 = [
    plugin(
        spawnerCondition,
        team=2,
        spawner=[
            "CP_64_midway_American_Carrier_North_carrier",
            "CP_64_midway_American_Carrier_North_divebomber_0",
            "CP_64_midway_American_Carrier_North_divebomber_1",
            "CP_64_midway_American_Carrier_North_fighter_0",
            "CP_64_midway_American_Carrier_North_fighter_1",
            "CP_64_midway_American_Carrier_South_carrier",
            "CP_64_midway_American_Carrier_South_divebomber_0",
            "CP_64_midway_American_Carrier_South_divebomber_1",
            "CP_64_midway_American_Carrier_South_fighter_0",
            "CP_64_midway_American_Carrier_South_fighter_1",
        ],
        they_own=["CP_64_midway_Henderson_Field"],
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=[
            "CP_64_midway_American_Carrier_North_carrier",
            "CP_64_midway_American_Carrier_North_divebomber_0",
            "CP_64_midway_American_Carrier_North_divebomber_1",
            "CP_64_midway_American_Carrier_North_fighter_0",
            "CP_64_midway_American_Carrier_North_fighter_1",
            "CP_64_midway_American_Carrier_South_carrier",
            "CP_64_midway_American_Carrier_South_divebomber_0",
            "CP_64_midway_American_Carrier_South_divebomber_1",
            "CP_64_midway_American_Carrier_South_fighter_0",
            "CP_64_midway_American_Carrier_South_fighter_1",
        ],
        they_own=["CP_64_midway_Objective_Hangar"],
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner=[
            "CP_64_midway_American_Carrier_North_carrier",
            "CP_64_midway_American_Carrier_North_divebomber_0",
            "CP_64_midway_American_Carrier_North_divebomber_1",
            "CP_64_midway_American_Carrier_North_fighter_0",
            "CP_64_midway_American_Carrier_North_fighter_1",
            "CP_64_midway_American_Carrier_South_carrier",
            "CP_64_midway_American_Carrier_South_divebomber_0",
            "CP_64_midway_American_Carrier_South_divebomber_1",
            "CP_64_midway_American_Carrier_South_fighter_0",
            "CP_64_midway_American_Carrier_South_fighter_1",
        ],
        they_own=["CP_64_midway_Objective_Fuel"],
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner=[
            "CP_64_midway_Japanese_Destroyers_destroyer_1",
            "CP_64_midway_Japanese_Destroyers_destroyer_2",
            "CP_64_midway_Japanese_Cruisers_heavycruiser",
            "CP_64_midway_Japanese_Torpedoboats_boat_1",
            "CP_64_midway_Japanese_Torpedoboats_boat_2",
        ],
        they_own=[
            "CP_64_midway_Japanese_Carrier_South",
            "CP_64_midway_Japanese_Carrier_West",
            "CP_64_midway_Japanese_Carrier_East",
        ],
    ),
]
links_32 = [
    plugin(
        linkCPs,
        target="CP_32_midway_Japanese_Pointsflag",
        source=[
            "CP_32_midway_Japanese_Carrier_North",
            "CP_32_midway_Japanese_Carrier_South",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_32_midway_American_Pointsflag",
        source=[
            "CP_32_midway_American_Carrier_South",
            "CP_32_midway_American_Carrier_North",
        ],
    ),
]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_midway_American_Carrier_South",
        source=["CP_64_midway_Objective_Hangar"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_American_Carrier_North",
        source=["CP_64_midway_Objective_Fuel"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_Japanese_Carrier_North",
        source=["CP_64_midway_Japanese_Carrier_East"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_Japanese_Carrier_West",
        source=["CP_64_midway_Japanese_Carrier_South"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_Japanese_Cruisers",
        source=[
            "CP_64_midway_Japanese_Carrier_East",
            "CP_64_midway_Japanese_Carrier_West",
            "CP_64_midway_Japanese_Carrier_South",
        ],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_Japanese_Destroyers",
        source=[
            "CP_64_midway_Japanese_Carrier_East",
            "CP_64_midway_Japanese_Carrier_West",
            "CP_64_midway_Japanese_Carrier_South",
        ],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_Japanese_Torpedoboats",
        source=[
            "CP_64_midway_Japanese_Carrier_East",
            "CP_64_midway_Japanese_Carrier_West",
            "CP_64_midway_Japanese_Carrier_South",
        ],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_American_Ships",
        source=["CP_64_midway_Japanese_Torpedoboats"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_Japanese_Pointsflag",
        source=[
            "CP_64_midway_Japanese_Carrier_East",
            "CP_64_midway_Japanese_Carrier_West",
            "CP_64_midway_Japanese_Carrier_North",
            "CP_64_midway_Japanese_Carrier_South",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_American_Pointsflag",
        source=[
            "CP_64_midway_American_Carrier_South",
            "CP_64_midway_American_Carrier_North",
            "CP_64_midway_Objective_Fuel",
            "CP_64_midway_Objective_Hangar",
            "CP_64_midway_Henderson_Field",
            "CP_64_midway_Objective_Guns",
        ],
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_American_Ships",
        source=["CP_64_midway_Henderson_Field"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_American_Carrier_South",
        source=["CP_64_midway_Henderson_Field"],
        invert=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_midway_American_Carrier_North",
        source=["CP_64_midway_Henderson_Field"],
        invert=True,
    ),
]

tickets_64 = [plugin(ticketLoss, ticketLoss1=2000, ticketLoss2=2000)]
tickets_32 = [plugin(ticketLoss, ticketLoss1=2000, ticketLoss2=2000)]
tickets_16 = [plugin(ticketLoss, ticketLoss1=1000, ticketLoss2=1000)]

objective_32 = [
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_32_midway_Japanese_Carrier_South",
        template="fh1_shokaku_dest",
    ),
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_32_midway_Japanese_Carrier_North",
        template="fh1_shokaku_dest_1",
    ),
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_32_midway_American_Carrier_North",
        template="fh1_enterprise_dest_1",
    ),
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_32_midway_American_Carrier_South",
        template="fh1_enterprise_dest",
    ),
]


objective_64 = [
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_64_midway_Japanese_Carrier_South",
        template="fh1_shokaku_dest",
    ),
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_64_midway_Japanese_Carrier_North",
        template="fh1_shokaku_dest_1",
    ),
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_64_midway_Japanese_Carrier_West",
        template="fh1_shokaku_dest_2",
    ),
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_64_midway_Japanese_Carrier_East",
        template="fh1_shokaku_dest_3",
    ),
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_64_midway_American_Carrier_North",
        template="fh1_enterprise_dest",
    ),
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_64_midway_American_Carrier_South",
        template="fh1_enterprise_dest_1",
    ),
    plugin(
        destroyObjective,
        refcount=11,
        controlpoint="CP_64_midway_Objective_Fuel",
        template="krupp_silo_dest",
    ),
    plugin(
        destroyObjective,
        refcount=1,
        controlpoint="CP_64_midway_Objective_Hangar",
        template="midway_hangar",
    ),
    plugin(
        destroyObjective,
        refcount=4,
        controlpoint="CP_64_midway_Objective_Guns",
        template="m1_90mm_aa_radar",
    ),
    plugin(
        destroyObjective,
        refcount=5,
        controlpoint="CP_64_midway_Henderson_Field",
        template="krupp_silo_dest_1",
    ),
]

# obj_nam_64 = [
#     plugin(
#         NamedObjective,
#         flagname="CP_64_midway_Objective_Hangar",
#         spawners={"CP_64_midway_Objective_Hangar_building": "midway_hangar"},
#     ),
# ]

gpm_cq = {
    64: (
        NCO_all
        + objective_64
        + tickets_64
        + links_64
        + spawns_all
        + reinforcements_64
        # + obj_nam_64
        + abc_64
    ),
    32: (
        NCO_all
        + spawns_all
        + tickets_32
        + objective_32
        #
        + links_32
    ),
    16: (
        NCO_all
        + spawns_all
        + tickets_16
        #
        + abc_16
    ),
}
