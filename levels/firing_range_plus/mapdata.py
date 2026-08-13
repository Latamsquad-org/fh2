# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401
from game.plugins import (
    plugin,
    limitKit,
    NCOrifleData,
)

kits_32 = [
    plugin(limitKit, team=2, slot=1, kit="NW_Grenadier,NW_Grenadier_Limited_alt,NW_Grenadier_Limited_alt2,NW_Grenadier_Limited_alt3", limit=1),
    plugin(limitKit, team=2, slot=4, kit="NW_Engineer,NW_Engineer_alt,NW_Engineer_alt2,NW_Engineer_alt3", limit=1),
    plugin(limitKit, team=2, slot=5, kit="NW_Antitank,NW_Antitank_Limited_alt", limit=1),
]

nco_64 = [
    plugin(
        NCOrifleData,
        kits=('GW_NCO_early', 'FA_active_NCO'),
        soldiers=("gw_heer_unteroffizier_early", "fg_nco"),
    )
]

nco_32 = [
    plugin(
        NCOrifleData,
        kits=('BG_NCO', 'NW_NCO'),
        soldiers=("BG_chasseur_sgt", "nw_sgt"),
    )
]

nco_16 = [
    plugin(
        NCOrifleData,
        kits=('ME_NCO', 'PP_NCO'),
        soldiers=("gw_heer_unteroffizier_early", "pw_nco_soldier"),
    )
]


# Run plugin settings

gpm_cq = {
  64: nco_64,
  32: nco_32 + kits_32,
  16: nco_16,
}