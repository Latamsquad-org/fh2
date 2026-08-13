# -*- coding: utf-8 -*-
"""master dictionary for map-dynamic template dependencies loading
"""

from os import environ

try:
    execfile
except NameError:

    def execfile(fname, globals_=None, locals_=None):
        with open(fname) as f:
            code = compile(f.read(), fname, "exec")
        exec(code, globals_, locals_)


_dependencies = {
    # 'template': 'path to inc file',
    # OR
    # 'template': ('path to inc file 1', 'path to inc file 1', ... 'path to inc file N'),
    "audacity": "/Objects/Vehicles/Sea/GB/Audacity/audacity_spawners.inc",
    "agassiz": "/Objects/Vehicles/Sea/GB/FlowerClass/Agassiz/agassiz_ObjectSpawner_lifeboat.inc",
    "lct_mk5_gb_normandy": "/Objects/Vehicles/Sea/GB/LCT_MK5/lct_mk5_gb_normandy_TankSpawner1.inc",
    "lct_mk5_stat_gb_normandy": "/Objects/Vehicles/Sea/GB/LCT_MK5_stat_GB_Normandy/lct_mk5_stat_gb_normandy_TankSpawner1.inc",
    "libertyship": "/Objects/Vehicles/Sea/GB/Liberty/libertyship/libertyship_PlaneSpawner.inc",
    "dd_gleaversclass_Measure21_Arty": "/Objects/Vehicles/Sea/US/DD_GleaversClass/dd_gleaversclass_Arty_spawner.inc",
    "lct_mk5_us_normandy": "/Objects/Vehicles/Sea/US/LCT_MK5/LCT_MK5_US_Normandy_TankSpawner1.inc",
}

# lower case keys:
# ===========================================
dependencies = {}

metadata = {}
try:
    execfile("python/game/plugins/vehicleMetadata.py", metadata)
except IOError:
    # e.g. pozzo trying to run this at home
    fh2pydir = environ["FH2PYDIR"]
    execfile(fh2pydir + "/game/plugins/vehicleMetadata.py", metadata)
for truck_name, info in metadata["portee_info"].items():
    dependencies[truck_name.lower()] = [info["inc_path"]]

for template, files in _dependencies.items():
    if type(files) == type(""):
        _files = [files]
    else:
        _files = files
    dependencies[template.lower()] = _files
# ===========================================
