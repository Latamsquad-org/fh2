from game.plugins import plugin, NCOrifleData
kit_limits_64 = []
nco_kits_64 = [plugin(NCOrifleData, kits = ('jp_NCO_early_sig1920jp', 'BE_NCOTommygunS')),]
nco_kits_32 = [plugin(NCOrifleData, kits = ('GW_NCO_STG44', 'UP_NCO_resing_spring')),]

# Run plugin settings

gpm_cq = {
  64: nco_kits_64,
  32: nco_kits_32
}
