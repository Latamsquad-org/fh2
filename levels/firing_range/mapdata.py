from game.plugins import plugin, NCOrifleData


nco_kits_64 = [
    plugin(NCOrifleData, kits = ('SE_NCO', 'RE_NCO_42')),
]

nco_kits_32 = [
    plugin(NCOrifleData, kits = ('GW_NCO', 'UW_NCO')),
]

nco_kits_16 = [
    plugin(NCOrifleData, kits = ('GA_NCOMP40', 'BA_NCOTommygunS')),
]

# Run plugin settings

gpm_cq = {
  64: nco_kits_64,
  32: nco_kits_32,
  16: nco_kits_16
}
