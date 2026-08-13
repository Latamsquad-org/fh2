# Common plugins
from game.plugins import (
    plugin, 
    limitKit, 
    teamSPs, 
    linkCPs,
    ticketLoss, 
    NCOrifleData,
    push
)

# -------------------------------------------------- #
#   Common plugins
# -------------------------------------------------- #

# Officer kit
rifleNCO = [
  plugin(NCOrifleData, kits = ('GS_NCO_mp40_g43', 'UW_NCO_late'))
]

# Team Spawns
spawns = [
  plugin(teamSPs), # Auto-fill
]

# Kit limits for the 64p layer
kit_limits_64 = [
  plugin(
    limitKit,
    team = 1,
    slot = 1,
    kit = 'GW_StG44Assault_Limited',
    limit = 0.2
  ),
  plugin(
    limitKit,
    team = 2,
    slot = 1,
    kit = 'UW_SMGAssault_Limited',
    limit = 0.2
  ),
  plugin(
    limitKit,
    team = 1,
    slot = 3,
    kit = 'GW_LMG_MG42_Limited',
    limit = 0.1
  ),
  plugin(
    limitKit,
    team = 2,
    slot = 3,
    kit = 'UW_LMG_m1919a6_Limited',
    limit = 0.1
  ),
  plugin(
    limitKit,
    team = 1,
    slot = 5,
    kit = 'GW_AntitankAssault60m_Limited',
    limit = 0.1
  ),
  plugin(
    limitKit,
    team = 2,
    slot = 5,
    kit = 'UW_AntitankAssaultM9_Limited',
    limit = 0.1
  ),
]

# Ticket loss per minute
tickets_64 = [
  plugin(ticketLoss, ticketLoss1 = 20, ticketLoss2 = 15)
]

links_64 = [
    plugin(
        linkCPs,
        target="CP_64_event_la_gleize_axis_reinforcements_1",
        source=["CP_64_event_la_gleize_hotel"],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_event_la_gleize_axis_reinforcements_2",
        source=["CP_64_event_la_gleize_town_hall"],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_event_la_gleize_axis_reinforcements_3",
        source=["CP_64_event_la_gleize_werimont"],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_event_la_gleize_axis_reinforcements_4",
        source=["CP_64_event_la_gleize_crossroads"],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_event_la_gleize_allied_reinforcements_1",
        source=["CP_64_event_la_gleize_chapelle"],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_64_event_la_gleize_allied_reinforcements_2",
        source=["CP_64_event_la_gleize_crossroads"],
        invert=True,
        default_zero=True,
    ),
]

links_32 = [
    plugin(
        linkCPs,
        target="CP_32_event_la_gleize_axis_reinforcements",
        source=["CP_32_event_la_gleize_hotel", "CP_32_event_la_gleize_crossroads", "CP_32_event_la_gleize_town_hall"],
        invert=True,
        default_zero=True,
    ),
    plugin(
        linkCPs,
        target="CP_32_event_la_gleize_allied_reinforcements",
        source=["CP_32_event_la_gleize_hotel", "CP_32_event_la_gleize_crossroads", "CP_32_event_la_gleize_town_hall"],
        invert=True,
        default_zero=True,
    )
]

links_16 = [
    plugin(
        push,
        source="CP_16_event_la_gleize_allied_main",
        target="CP_16_event_la_gleize_hotel",
        attacker=2,
        display_arrow=False
    ),
    plugin(
        push,
        source="CP_16_event_la_gleize_hotel",
        target="CP_16_event_la_gleize_center",
        attacker=2,
        display_arrow=False
    ),
    plugin(
        push,
        source="CP_16_event_la_gleize_center",
        target=["CP_16_event_la_gleize_crossroads", "CP_16_event_la_gleize_cafe"],
        attacker=2,
        display_arrow=False
    ),
    plugin(
        push,
        source=["CP_16_event_la_gleize_crossroads", "CP_16_event_la_gleize_cafe"],
        target="CP_16_event_la_gleize_town_hall",
        attacker=2,
        display_arrow=False
    ),
    # Spawns available when controlling both CPs
    plugin(
        linkCPs,
        target="CP_16_event_la_gleize_dummy",
        source=["CP_16_event_la_gleize_crossroads", "CP_16_event_la_gleize_cafe"],
        invert=False,
        default_zero=True,
    )
]

tickets_32 = [plugin(ticketLoss, ticketLoss1=15, ticketLoss2=15)]

tickets_16 = [plugin(ticketLoss, ticketLoss1=10, ticketLoss2=10)]


gpm_cq = {
  64: rifleNCO + spawns + kit_limits_64 + tickets_64 + links_64,
  32: rifleNCO + spawns + kit_limits_64 + tickets_32 + links_32,
  16: rifleNCO + spawns + kit_limits_64 + tickets_16 + links_16
}
