# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    teamSPs,
    limitKit,
    spawnerCondition,
    disableSPs,
    delaySpawners,
    NCOrifleData,
)

nco = [
    plugin(
        NCOrifleData,
        kits=("GW_NCO", "UW_NCO"),
        soldiers=("GcSsSnow_nco", "uc_win44_army_sgt"),
    )
]

pco_spawns_64 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_meuseriver_axismain_pz4",
        they_own="CP_64_meuseriver_farm",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_meuseriver_axismain_hetzer",
        they_own="CP_64_meuseriver_outskirtwest",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_meuseriver_axismain_fw190, CP_64_meuseriver_axismain_DE_US_Pilot, CP_64_meuseriver_axismain_kingtiger2_0",
        they_own="CP_64_meuseriver_outskirtwest and CP_64_meuseriver_farm and CP_64_meuseriver_townwest and CP_64_meuseriver_northeast",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_meuseriver_alliedmain_m10",
        they_own="CP_64_meuseriver_farm",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_meuseriver_alliedmain_sherman2",
        they_own="CP_64_meuseriver_outskirtwest",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_meuseriver_alliedmain_p47, CP_64_meuseriver_alliedmain_DE_US_Pilot, CP_64_meuseriver_alliedmain_m362",
        they_own="CP_64_meuseriver_outskirtwest and CP_64_meuseriver_farm and CP_64_meuseriver_townwest and CP_64_meuseriver_northeast",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_meuseriver_axismain_commando",
        they_own="CP_64_meuseriver_outskirtwest and CP_64_meuseriver_farm",
    ),
]

pco_spawns_32 = [
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_32_meuseriver_axismain_fw190, CP_32_meuseriver_axismain_DE_US_Pilot",
        they_own="CP_32_meuseriver_farm and CP_32_meuseriver_townwest and CP_32_meuseriver_northeast",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_32_meuseriver_alliedmain_p47, CP_32_meuseriver_alliedmain_DE_US_Pilot",
        they_own="CP_32_meuseriver_farm and CP_32_meuseriver_townwest and CP_32_meuseriver_northeast",
    ),
]

spawns_64 = [
    plugin(teamSPs),  # Auto-fill
]

spawns_32 = [
    plugin(teamSPs),  # Auto-fill
]

spawns_16 = [
    plugin(teamSPs),  # Auto-fill
]

kit_limits = [
    plugin(limitKit, team=1, kit="GW_StG44Assault_Limited", slot=1, limit=0.25),
    plugin(limitKit, team=2, kit="UW_SMGAssault_Limited_GGun", slot=1, limit=0.25),
    plugin(limitKit, team=1, kit="GW_LMG_MG42_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=2, kit="UW_LMG_m1919a6_Limited", slot=3, limit=0.1),
    plugin(limitKit, team=1, kit="GW_AntitankAssault60m_Limited", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="UW_AntitankAssaultM9_Limited", slot=5, limit=0.1),
]

kit_limits_16 = [
    plugin(limitKit, team=1, kit="GW_StG44Assault_Limited", slot=1, limit=0.2),
    plugin(limitKit, team=2, kit="UW_SMGAssault_Limited_GGun", slot=1, limit=0.3),
    plugin(limitKit, team=1, kit="GW_LMG_MG42_Limited", slot=3, limit=0.08),
    plugin(limitKit, team=2, kit="UW_LMG_m1919a6_Limited", slot=3, limit=0.08),
    plugin(limitKit, team=1, kit="GW_AntitankAssault60m_Limited", slot=5, limit=0.1),
    plugin(limitKit, team=2, kit="UW_AntitankAssaultM9_Limited", slot=5, limit=0.05),
]

kits_AI = [
    plugin(
        limitKit,
        team=1,
        slot=0,
        limit=4.0 / 32.0,
        kit="GW_Scout",
        soldier="GcSsSnow_eichen_green",
    ),
    plugin(
        limitKit,
        team=1,
        slot=1,
        limit=6.0 / 32.0,
        kit="GW_StG44Assault_Limited",
        soldier="GcSsSnow_white_platane",
    ),
    plugin(
        limitKit,
        team=1,
        slot=2,
        limit=9.0 / 32.0,
        kit="GW_RifleAssault_G43",
        soldier="GcSsSnow_eichen_brown",
    ),
    plugin(
        limitKit,
        team=1,
        slot=3,
        limit=5.0 / 32.0,
        kit="GW_LMG_MG42_Limited",
        soldier="GcSsSnow_white_platane",
    ),
    plugin(
        limitKit,
        team=1,
        slot=4,
        limit=4.0 / 32.0,
        kit="GW_Engineer_Satchel",
        soldier="GcSsSnow_eichen_brown",
    ),
    plugin(
        limitKit,
        team=1,
        slot=5,
        limit=5.0 / 32.0,
        kit="GW_AntitankAssault60m_Limited",
        soldier="GcSsSnow_white_eichen",
    ),
    plugin(
        limitKit,
        team=2,
        slot=0,
        limit=4.0 / 32.0,
        kit="UW_Scout",
        soldier="uc_win44_army_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=1,
        limit=6.0 / 32.0,
        kit="UW_SMGAssault_Limited_GGun",
        soldier="uc_win44_army_cpl",
    ),
    plugin(
        limitKit,
        team=2,
        slot=2,
        limit=10.0 / 32.0,
        kit="UW_RifleAssault",
        soldier="uc_win44_army_pvt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=3,
        limit=5.0 / 32.0,
        kit="UW_LMG_m1919a6_Limited",
        soldier="uc_win44_army_cpl_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=4,
        limit=4.0 / 32.0,
        kit="UW_Engineer_Satchel",
        soldier="uc_win44_army_pvt_alt",
    ),
    plugin(
        limitKit,
        team=2,
        slot=5,
        limit=4.0 / 32.0,
        kit="UW_AntitankAssaultM9_Limited",
        soldier="uc_win44_army_cpl",
    ),
]

disableSPs_64_AI = [
    plugin(
        disableSPs,
        team=1,
        cp="CP_64_meuseriver_axismain",
        we_own="CP_64_meuseriver_townwest or CP_64_meuseriver_northeast",
    ),
    plugin(
        disableSPs,
        team=2,
        cp="CP_64_meuseriver_alliedmain",
        we_own="CP_64_meuseriver_townwest or CP_64_meuseriver_northeast",
    ),
]

delaySpawners_64_AI = [
    plugin(
        delaySpawners,
        spawners="CP_64_meuseriver_axismain_sdkz4,CP_64_meuseriver_axismain_kubel,CP_64_meuseriver_alliedmain_apc2,CP_64_meuseriver_alliedmain_willys2",
    ),
]

pco_spawns_64_AI = [
    # Stuff from CQ
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_meuseriver_axismain_pz4",
        they_own="CP_64_meuseriver_farm",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_meuseriver_axismain_hetzer",
        they_own="CP_64_meuseriver_outskirtwest",
    ),
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_meuseriver_axismain_fw190, CP_64_meuseriver_axismain_DE_US_Pilot, CP_64_meuseriver_axismain_kingtiger2_0",
        they_own="CP_64_meuseriver_outskirtwest and CP_64_meuseriver_farm and CP_64_meuseriver_townwest and CP_64_meuseriver_northeast",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_meuseriver_alliedmain_m10",
        they_own="CP_64_meuseriver_farm",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_meuseriver_alliedmain_sherman2",
        they_own="CP_64_meuseriver_outskirtwest",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_meuseriver_alliedmain_p47, CP_64_meuseriver_alliedmain_DE_US_Pilot, CP_64_meuseriver_alliedmain_m362",
        they_own="CP_64_meuseriver_outskirtwest and CP_64_meuseriver_farm and CP_64_meuseriver_townwest and CP_64_meuseriver_northeast",
    ),
    # AI-specific stuff
    plugin(
        spawnerCondition,
        team=1,
        spawner="CP_64_meuseriver_axismain_vierling,CP_64_meuseriver_axismain_vierling2,CP_64_meuseriver_farm_vierling,CP_64_meuseriver_outskirtwest_vierling",
        we_own="CP_64_meuseriver_outskirtwest and CP_64_meuseriver_farm and CP_64_meuseriver_townwest and CP_64_meuseriver_northeast",
    ),
    plugin(
        spawnerCondition,
        team=2,
        spawner="CP_64_meuseriver_alliedmain_m51_0,CP_64_meuseriver_alliedmain_m51nr2,CP_64_meuseriver_outskirtwest_m51,CP_64_meuseriver_farm_m51",
        we_own="CP_64_meuseriver_outskirtwest and CP_64_meuseriver_farm and CP_64_meuseriver_townwest and CP_64_meuseriver_northeast",
    ),
]

gpm_cq = {
    64: spawns_64 + pco_spawns_64 + kit_limits + nco,
    32: spawns_32 + pco_spawns_32 + kit_limits + nco,
    16: spawns_16 + kit_limits_16 + nco,
}
gpm_coop = {
    64: spawns_64
    + pco_spawns_64_AI
    + kits_AI
    + disableSPs_64_AI
    + delaySpawners_64_AI
    + nco
}
sp3 = gpm_coop
