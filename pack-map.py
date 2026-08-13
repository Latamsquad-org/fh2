#!/usr/bin/env python
# pylint: disable=C0103,C0111,F0401,C0415,C0209
"""Pack a map. Called from a 'pack_mymap.bat' file
"""

from __future__ import print_function

import os
import sys
from python.packing.fh2pack_maps import pack_maps


# Fix Python 2.x.: `raw_input` renamed to `input` in python3
try:
    # py2
    INPUT = raw_input
except NameError:
    # py3
    INPUT = input

COMMAND_LINE_HELP = "Usage: pack-map.py mapname [--release]"


if __name__ == "__main__":
    mapname = None
    is_release = False

    n_args = len(sys.argv)
    if n_args == 1:
        print(COMMAND_LINE_HELP)
        print("Warning! This can potentialy break your game. Use only on custom maps!")
        print("Type 'exit', 'quit' or 'bye' to exit.")
        while True:
            mapname = INPUT("Name of the map to pack? ").strip()
            if mapname == "":
                continue
            if mapname.lower() in ("exit", "quit", "bye"):
                sys.exit(1)
            mappath = os.path.join("Levels", mapname)
            if not os.path.exists(mappath):
                print("Couldn't find map %s. Try again." % mapname)
                continue
            break
    else:
        if n_args > 2:
            if n_args == 3 and sys.argv[2] == "--release":
                is_release = True
            else:
                print(COMMAND_LINE_HELP)
                INPUT("Press any key to exit...")
                sys.exit(1)

        mapname = sys.argv[1]
        mappath = os.path.join("Levels", mapname)
        if not os.path.exists(mappath):
            print(mapname, "map doesn't exist.")
            INPUT("Press any key to exit...")
            sys.exit(1)

    if is_release:
        import python.packing.fh2pack_common

        python.packing.fh2pack_common.RELEASE = 1

    pack_maps("Levels/%s/" % mapname)
