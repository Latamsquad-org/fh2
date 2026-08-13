# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    linkCPs,
    NCOrifleData,
    DoubleBleed,
)


bleed_32 = [
    plugin(
        DoubleBleed,
    )
]
nco = [
    plugin(
        NCOrifleData,
        kits=("GA_NCOMP40", "BA_NCOTommygunS"),
        soldiers=("ga_nco_soldier", "ba_nco_soldier"),
    )
]
links_64 = [
    plugin(
        linkCPs,
        target="CP_64_MM_StukaDummy",
        source=["CP_64_MM_Station", "CP_64_MM_West_Matruh", "CP_64_MM_Matruh"],
        invert=True,
    ),
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
]

gpm_cq = {
    64: kit_limits + links_64 + nco,
    32: kit_limits + nco + bleed_32,
    16: kit_limits + nco + bleed_32,
}

gpm_coop = {
    64: links_64 + nco,
    32: nco + bleed_32,
    16: nco + bleed_32,
}

sp3 = gpm_coop
sp2 = gpm_coop
sp1 = gpm_coop
