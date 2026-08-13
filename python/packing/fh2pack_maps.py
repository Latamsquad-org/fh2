# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111,F0401,R0913,R1725,C0301,R0915,R0912,R0914  # noqa
# vim:set ts=4 sts=4 sw=4 et syntax=python:
"""
fh2 packing scripts, maps deriative (meant for public use)
"""

from __future__ import print_function

import os
import glob
import zipfile
import re
from fh2pack_common import (  # pylint: disable=E0001
    include,
    copy_ftimes,
    ignore_dir,
    has_ignore_file,
    normalize_path,
    icase,
    ifile_find,
)
from dependencies import dependencies as dep_dict

COM_EOF = "$fh2_eof"
COM_NOT_READ = "$fh2_donotread"
COM_READ = "$fh2_read"
COM_KITGEOMSUBFOLDER = "$fh2_kitgeomsubfolder"

ospath = os.path

ERROR_COUNTER = 0

# if os.name == 'posix':
#     zipfile = wrapSevenZip


class FileEntry:  # pylint: disable=R0903
    def __init__(self, map_path, root_path, file_name):
        self.src_path = ospath.join(root_path, file_name)
        self.zip_path = ospath.relpath(self.src_path, map_path)
        self.to_client = include(self.zip_path, None, "client")
        self.to_server = include(self.zip_path, None, "server")
        self.file_time = os.stat(self.src_path).st_mtime


def split_path(path, root_path):
    path = ospath.relpath(path, root_path).replace("\\", "/").lower()
    parts = [x for x in path.split("/") if x and x != "."]
    if parts:
        return parts
    return [""]


def con_read(path, *ops):  # pylint: disable=R0912
    try:
        with open(path, "r") as f:
            data = f.readlines()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin-1") as f:
            data = f.readlines()

    is_in_block_rem = False
    ln_no = 0
    for ln in data:
        ln_no += 1

        ln = ln.strip()
        if not ln:
            continue

        op = ln.split(None, 1)[0].lower()

        if is_in_block_rem:
            if op == "endrem":
                is_in_block_rem = False
            continue
        if op == "beginrem":
            is_in_block_rem = True
            continue
        if op not in ops:
            continue

        args_text = ln[len(op) + 1 :].lstrip()  # noqa

        if op == "rem":
            args = [args_text]
        elif '"' in args_text:
            args = []
            is_quoted = False
            for part in args_text.split('"'):
                if is_quoted:
                    args.append(part)
                    is_quoted = False
                else:
                    args += part.split()
                    is_quoted = True
            if not is_quoted:
                raise Exception(
                    "%s, line %d: missing ending quote" % (path, ln_no)
                )
        else:
            args = args_text.split()

        yield (ln_no, op, args)


def report_file_exception(filepath, line_no, e):
    global ERROR_COUNTER  # pylint: disable=W0603
    filepath = normalize_path(filepath)
    if line_no:
        print("ERROR %s, line %d:\n  %s" % (filepath, line_no, str(e)))
    else:
        print("ERROR %s:\n  %s" % (filepath, str(e)))
    ERROR_COUNTER += 1


def pack_maps(
    map_folders_path="Levels/*/",
    override_ignore=False,
):  # pylint: disable=R0915,R0912
    global ERROR_COUNTER  # pylint: disable=W0603

    map_folders = glob.glob(map_folders_path)

    from fh2pack_common import RELEASE  # pylint: disable=C0415,E0001

    compression = zipfile.ZIP_STORED
    #    if RELEASE and os.name == 'posix':
    #        compression = zipfile.ZIP_ULTRA
    #    elif RELEASE:
    if RELEASE:
        compression = zipfile.ZIP_DEFLATED

    print("building map file list...")
    for m in map_folders:
        if ".svn" in m:
            continue

        map_name = ospath.basename(m.rstrip("\\").rstrip("/"))
        if not override_ignore and ignore_dir(m):
            print("ignoring map", map_name)
            continue
        print("working on", map_name)

        ERROR_COUNTER = 0

        server_zip_path = ospath.join(m, "server.zip")
        client_zip_path = ospath.join(m, "client.zip")
        if ospath.isfile(server_zip_path) and ospath.isfile(client_zip_path):
            # if os.name == 'posix':
            #     needs_repack = False
            # else: # We still repack on Windows,
            #       # to avoid confusion in some cases.
            #     needs_repack = True
            needs_repack = False
            pack_time = min(
                os.stat(server_zip_path).st_mtime,
                os.stat(client_zip_path).st_mtime,
            )
        else:
            pack_time = 0
            needs_repack = True

        roads = read_road_list(m, map_name)
        n_added_roads = 0
        obj_lightmap_dds = read_object_lightmap_atlas_list(m, map_name)

        spawnpoints_path = ospath.join(m, "spawnpoints")
        if ospath.exists(spawnpoints_path):
            # Clean up
            for filename in os.listdir(spawnpoints_path):
                if not filename.lower().endswith(".py"):
                    continue
                filepath = ospath.join(spawnpoints_path, filename)
                if ospath.isfile(filepath):
                    os.remove(filepath)
        else:
            os.mkdir(spawnpoints_path)

        heightdata = read_heightdata(m)

        tmp_files = []
        file_entries = []
        for root, dirs, files in os.walk(m):
            root_parts = split_path(root, m)

            def skip_this_dir():
                dir_name = root_parts[-1]  # pylint: disable=W0640
                if dir_name in (".svn", "bf2_tpaint", ".git"):
                    return True
                if len(
                    root_parts  # pylint: disable=W0640  # noqa
                ) == 1 and dir_name in (
                    "info",
                    "editor",
                    "spawnpoints",
                ):
                    return True

                return not override_ignore and has_ignore_file(
                    files  # pylint: disable=W0640  # noqa
                )

            if skip_this_dir():
                # Clear the list of sub-dirs so os.walk would skip them
                del dirs[:]
                continue

            for file_name in files:
                entry = FileEntry(m, root, file_name)
                if not entry.to_client and not entry.to_server:
                    continue

                file_name_low = file_name.lower()
                if file_name_low == "resourcesatshutdown.txt":
                    continue
                elif root_parts[0] == "lightmaps":
                    if not file_name_low.endswith(
                        ".dds"
                    ) and not file_name_low.endswith(".tai"):
                        continue
                    if len(root_parts) == 2 and root_parts[1] == "objects":
                        if not file_name_low.startswith("lightmapatlas"):
                            continue
                        if (
                            file_name_low.endswith(".dds")
                            and file_name_low not in obj_lightmap_dds
                        ):
                            # print '%s: skipping unused object
                            # lightmap atlas %s' % (map_name, file_name)
                            continue
                elif (
                    root_parts[0] == "hud"
                    and len(root_parts) == 2
                    and root_parts[1] == "minimap"
                    and file_name_low != "ingamemap.dds"
                ):
                    continue
                elif file_name_low == "init.con":
                    entry.src_path = process_init(entry.src_path)
                    tmp_files.append(entry.src_path)
                elif file_name_low == "tmp.con":
                    entry.src_path = process_tmp(entry.src_path)
                    tmp_files.append(entry.src_path)
                elif file_name_low == "sky.con":
                    entry.src_path = process_sky(entry.src_path, heightdata)
                    tmp_files.append(entry.src_path)
                elif file_name_low == "gameplayobjects.con":
                    if len(root_parts) == 3 and root_parts[0] == "gamemodes":
                        entry.src_path = process_gpo(
                            entry.src_path,
                            root_parts[1],
                            root_parts[2],
                            heightdata,
                            spawnpoints_path,
                            map_name,
                        )
                        tmp_files.append(entry.src_path)
                elif (
                    file_name_low.endswith(".mesh")
                    and root_parts[0] == "roads"
                    and len(root_parts) == 1
                ):
                    if file_name_low not in roads:
                        # print '%s: skipping unused road %s' % (map_name, file_name)
                        continue
                    else:
                        n_added_roads += 1

                if not needs_repack and entry.file_time > pack_time:
                    needs_repack = True

                file_entries.append(entry)

        if ERROR_COUNTER:
            raise Exception(
                "%s: some errors have been found on the level, check the output above"
                % map_name
            )

        if not file_entries:
            continue

        if n_added_roads != len(roads):
            print(
                "%s: found only %d out of %d roads in CompiledRoads.con"
                % (map_name, n_added_roads, len(roads))
            )

        # Additional needs_repack checks
        if not needs_repack:

            def file_lists_mismatch(flag_attr, zip_path):
                new_files = [
                    x.zip_path.lower().replace("\\", "/")
                    for x in file_entries
                    if getattr(x, flag_attr)
                ]

                print("Opening zipfile %s" % zip_path)
                z = zipfile.ZipFile(zip_path, "r")
                old_files = [
                    x.lower().replace("\\", "/") for x in z.namelist()
                ]

                if set(new_files) == set(old_files):
                    return False
                return True

            if file_lists_mismatch(
                "to_client", client_zip_path
            ) or file_lists_mismatch("to_server", server_zip_path):
                needs_repack = True

        # To pack or not to pack, that is the question
        if not needs_repack:
            print(map_name, "does not need repack")
        else:
            print("packing map", map_name)
            print("opening client.zip")
            client_z = zipfile.ZipFile(client_zip_path, "w", compression)
            print("opening server.zip")
            server_z = zipfile.ZipFile(server_zip_path, "w", compression)

            for entry in file_entries:
                if entry.to_client:
                    client_z.write(entry.src_path, entry.zip_path)
                if entry.to_server:
                    server_z.write(entry.src_path, entry.zip_path)

            client_z.close()
            server_z.close()

            print("  done")

        # Delete tmp files
        for tmp in tmp_files:
            if ospath.isfile(tmp):
                os.remove(tmp)


class Set(set):
    # Set accepting only logic-1 values.
    def add(self, what):
        if what:
            set.add(self, what)


class HeightData:
    def __init__(self, size, primary_size, primary_scale):
        self.size = size

        def get_min_max(dimension, scale):
            half_dim = (float(dimension - 1) / 2.0) * scale
            return (-half_dim, half_dim)

        self.min_x, self.max_x = get_min_max(primary_size[0], primary_scale[0])
        self.min_y, self.max_y = get_min_max(primary_size[1], primary_scale[1])


def read_heightdata(mappath):
    con_path = ospath.join(mappath, "Heightdata.con")
    if not ospath.isfile(con_path):
        return None

    hd_size = None
    hd_primary_size = None
    hd_primary_scale = None
    is_primary_heightmap = False
    for ln_no, op, args in con_read(
        con_path,
        "heightmapcluster.setheightmapsize",
        "heightmapcluster.addheightmap",
        "heightmap.setsize",
        "heightmap.setscale",
    ):
        if op == "heightmapcluster.setheightmapsize":
            hd_size = int(args[0])
        elif op == "heightmapcluster.addheightmap":
            if (
                args[0].lower() == "heightmap"
                and args[1] == "0"
                and args[2] == "0"
            ):
                is_primary_heightmap = True
            else:
                is_primary_heightmap = False
        elif is_primary_heightmap:
            if op == "heightmap.setsize":
                hd_primary_size = [float(args[0]), float(args[1])]
            elif op == "heightmap.setscale":
                scales = args[0].split("/")
                hd_primary_scale = [float(scales[0]), float(scales[2])]

    if hd_size is None:
        raise Exception(
            "%s: could not find heightmapcluster.setHeightmapSize line"
            % con_path
        )
    if hd_primary_size is None:
        raise Exception(
            "%s: could not find heightmap.setSize line for the primary terrain"
            % con_path
        )
    if hd_primary_scale is None:
        raise Exception(
            "%s: could not find heightmap.setScale line for the primary terrain"
            % con_path
        )

    return HeightData(hd_size, hd_primary_size, hd_primary_scale)


def process_sky(path, heightdata):
    if heightdata is None:
        raise Exception("%s: the level has no height data" % path)

    src = open(path, "r")
    outpath = path + "_release"
    out = open(outpath, "w")
    for line in src:
        if line.lower().startswith("hemimapmanager.setbasehemimap"):
            bits = line.split()
            bits[3] = "%d.000000" % heightdata.size
            line = " ".join(bits) + "\n"
        out.write(line)
    src.close()
    out.close()
    copy_ftimes(path, outpath)
    return outpath


def process_init(path):
    short_view_dist_path = "Overgrowth/ViewDistances.con"

    lines = []
    insert_after = None
    norm_view_dist_path = normalize_path(short_view_dist_path).lower()
    with open(path, "r") as in_f:
        for ln in in_f:
            ln_strip = ln.strip()
            if ln_strip:
                words = ln_strip.lower().split()
                if words[0] == "run":
                    if (
                        len(words) >= 2
                        and normalize_path(words[1]) == norm_view_dist_path
                    ):
                        continue
                    insert_after = len(lines)
            lines.append(ln)

    if find_file(ospath.split(path)[0], short_view_dist_path):
        if insert_after is None:
            report_file_exception(
                path, None, "Could not find any 'run' to insert after"
            )
        else:
            lines.insert(insert_after + 1, "run %s\n" % short_view_dist_path)

    outpath = path + "_release"
    with open(outpath, "w") as out_f:
        for ln in lines:
            out_f.write(ln)

    copy_ftimes(path, outpath)
    return outpath


def process_tmp(path):
    subfolders = {}
    _lines = []
    with open(path, "r") as src_f:
        # Implementing most of special commands here:
        can_read = True
        for line in src_f:
            if COM_NOT_READ in line:
                can_read = False
                continue
            if COM_READ in line:
                can_read = True
                continue
            if not can_read:
                continue

            for word in line.split():
                if word.startswith(COM_KITGEOMSUBFOLDER):
                    comm, data = word.split("=")
                    for type in data.split(","):
                        kitset, subfolder = type.split(":")
                        subfolders[kitset.lower()] = subfolder + "/"

            if COM_EOF in line.split():
                break
            if "\n" not in line:
                line += "\n\n"
            _lines.append(line)

    all_map_templates = Set()
    kits = Set()
    kitsets = Set()
    mappath = ospath.split(path)[0]

    initconpath = ospath.join(mappath, "Init.con")
    collect_templates(initconpath, all_map_templates, kits, kitsets)

    for gpo_path in glob.glob(
        ospath.join(mappath, icase("GameModes/*/*/GamePlayObjects.con"))
    ):
        collect_templates(gpo_path, all_map_templates, kits, kitsets)

    outpath = path + "_release"
    with open(outpath, "w") as out:
        print("rem", COM_NOT_READ, file=out)
        print("rem *** autogenerated ***", file=out)
        print("", file=out)

        print("rem *** KIT LOADERS ***", file=out)
        for k in sorted(kits):
            print("run ../../objects/kits/%s.inc" % k, file=out)

        print("", file=out)
        print("rem *** KITSETS ***", file=out)
        for ks in kitsets:
            if len(ks) == 2:
                folder = ks
            else:
                folder = ks[:2]
            subfolder = subfolders.get(folder, "")
            print(
                "run ../../objects/kits/%s/%s%s_kits.inc"
                % (folder, subfolder, ks),
                file=out,
            )
        print("", file=out)

        # Kit spawners should go as last ones (after kits' and geoms' templates are loaded into memory)
        print("rem *** KIT SPAWNERS ***", file=out)
        for ks in kitsets:
            if len(ks) == 2:
                folder = ks
            else:
                folder = ks[:2]
            print(
                "run ../../objects/kits/%s/%s_kits_spawner.inc" % (folder, ks),
                file=out,
            )
        print("", file=out)

        dependencies = []
        extract_dependencies(all_map_templates, dependencies)
        if dependencies:
            print("rem *** CUSTOM DEPENDENCIES ***", file=out)
            for dep in dependencies:
                print("rem Pulled in by", ", ".join(dep.parents), file=out)
                print("run", dep.inc_path, file=out)
                print("", file=out)

        print("rem *** END OF AUTO_GENERATED PART ***", file=out)
        print("rem", COM_READ, file=out)
        print("", file=out)
        print("", file=out)

        for line in _lines:
            out.write(line)

    copy_ftimes(path, outpath)
    return outpath


def collect_templates(path, all_map_templates, kits, kitsets):
    assert ospath.isfile(path), "%s does not exist" % path
    for ln_no, op, args in con_read(
        path, "objecttemplate.setobjecttemplate", "gamelogic.setkit"
    ):
        if op == "objecttemplate.setobjecttemplate":
            template = args[1].lower()
            all_map_templates.add(template)

            if re.match(r"[a-z][a-z]_pickup.+", template):
                kits.add("spawnable/" + template)
        elif op == "gamelogic.setkit":
            kit = args[2].lower()
            all_map_templates.add(kit)
            kits.add("%s/%s" % (kit.split("_", 1)[0], kit))

            kitset = args[3].lower()
            all_map_templates.add(kitset)
            kitsets.add(kitset.split("_", 1)[0])


class dependency(object):
    def __init__(self, inc_path, search_path):
        self.inc_path = inc_path
        self.search_path = search_path
        self.parents = set()


def extract_dependencies(templates, out_dependencies):
    for template in templates:
        if template not in dep_dict:
            continue

        for inc_path in dep_dict[template]:
            norm_inc_path = normalize_path(inc_path)
            search_path = norm_inc_path.lower()
            for out_dep in out_dependencies:
                if out_dep.search_path == search_path:
                    out_dep.parents.add(template)
                    break
            else:
                out_dep = dependency(norm_inc_path, search_path)
                out_dep.parents.add(template)
                out_dependencies.append(out_dep)

                # TODO: add recursive check in the inc, if possible


def find_file(fixed_path_part, *path_parts):
    if fixed_path_part:
        path = fixed_path_part
        ind = 0
    else:
        path = icase(path_parts[0])
        ind = 1
    for p in path_parts[ind:]:
        path = ospath.join(path, icase(p))
    path = normalize_path(path)

    return ifile_find(path)


def read_road_list(level_path, map_name):
    con_path = find_file(level_path, "compiledroads.con")
    if con_path is None:
        # print "%s: couldn't find CompiledRoads.con" % map_name
        return []

    road_path_prefix = "levels/" + map_name.lower() + "/roads/"

    roads = []
    for ln_no, op, args in con_read(con_path, "object.geometry.loadmesh"):
        try:
            if len(args) != 1:
                raise Exception(
                    "object.geometry.loadmesh has the wrong number of args"
                )

            road_path = normalize_path(args[0]).lower()
            if not road_path.startswith(road_path_prefix):
                raise Exception("strange compiled road path - %s" % road_path)
            road_name = road_path[len(road_path_prefix) :]
            if not road_name or "/" in road_name:
                raise Exception("strange compiled road path - %s" % road_path)
            road_test_path = find_file(level_path, "Roads", road_name)
            if road_test_path is None:
                raise Exception("%s doesn't exist" % road_path)

            roads.append(road_name)
        except Exception as e:
            report_file_exception(con_path, ln_no, e)

    return roads


def read_object_lightmap_atlas_list(level_path, map_name):
    atlas_file_path = find_file(
        level_path, "Lightmaps", "Objects", "LightmapAtlas.tai"
    )
    if not atlas_file_path:
        return []

    atlas_path_prefix = "levels/" + map_name.lower() + "/lightmaps/objects/"

    proccessed_paths = []
    used_dds = []
    with open(atlas_file_path, "r") as atlas_file:
        ln_no = 0
        for ln in atlas_file:
            ln_no += 1

            try:
                words = ln.split()
                if len(words) < 2 or words[0][0] == "#":
                    continue

                if words[1] in proccessed_paths:
                    continue
                proccessed_paths.append(words[1])

                dds_path = normalize_path(words[1].rstrip(",")).lower()

                if not dds_path.startswith(atlas_path_prefix):
                    raise Exception(
                        "strange object lightmap atlas path - %s" % dds_path
                    )
                dds_name = dds_path[len(atlas_path_prefix) :]
                if not dds_name or "/" in dds_name:
                    raise Exception(
                        "strange object lightmap atlas path - %s" % dds_path
                    )
                dds_test_path = find_file(
                    level_path, "Lightmaps", "Objects", dds_name
                )
                if dds_test_path is None:
                    raise Exception("%s doesn't exist" % dds_path)

                if dds_name not in used_dds:
                    used_dds.append(dds_name)
            except Exception as e:
                report_file_exception(atlas_file_path, ln_no, e)

    return used_dds


class spawnPoint:
    def __init__(self, name):
        self.name = name
        self.cpid = None
        self.group = 0
        self.human_only = False
        self.ai_only = False


def process_gpo(
    gpo_path, gamemode, layer, heightdata, spawnpoints_path, map_name
):
    if heightdata is None:
        raise Exception("%s: the level has no height data" % gpo_path)

    # Parse GPO
    sps = []
    sps_search = {}
    cur_sp = None

    cas = []
    has_objectspawners = False
    ca_enabled = False
    ca_has_plane_cas = False
    ca_layer = "1"

    for ln_no, op, args in con_read(
        gpo_path,
        "objecttemplate.create",
        "objecttemplate.activesafe",
        "objecttemplate.active",
        "objecttemplate.setcontrolpointid",
        "objecttemplate.setonlyforhuman",
        "objecttemplate.setonlyforai",
        "objecttemplate.setgroup",
        "combatareamanager.use",
        "combatarea.create",
        "combatarea.vehicles",
        "combatarea.layer",
    ):
        try:
            # Spawnpoints
            if op in ("objecttemplate.create", "objecttemplate.activesafe"):
                cur_sp = None

                ot_type = args[0].lower()
                if ot_type == "spawnpoint":
                    name = args[1]
                    name_low = name.lower()
                    cur_sp = sps_search.get(name_low, None)
                    if cur_sp is None:
                        cur_sp = spawnPoint(name)
                        sps.append(cur_sp)
                        sps_search[name_low] = cur_sp

                elif ot_type == "objectspawner":
                    has_objectspawners = True

            elif op == "objecttemplate.active":
                cur_sp = sps_search.get(args[0].lower(), None)

            elif op == "objecttemplate.setcontrolpointid":
                if cur_sp:
                    cur_sp.cpid = int(args[0])
            elif op == "objecttemplate.setonlyforhuman":
                if cur_sp:
                    val = args[0]
                    if val == "1":
                        cur_sp.human_only = True
                    elif val == "0":
                        cur_sp.human_only = False
                    else:
                        raise Exception(
                            "invalid value of ObjectTemplate.setOnlyForHuman - %s"
                            % val
                        )
            elif op == "objecttemplate.setonlyforai":
                if cur_sp:
                    val = args[0]
                    if val == "1":
                        cur_sp.ai_only = True
                    elif val == "0":
                        cur_sp.ai_only = False
                    else:
                        raise Exception(
                            "invalid value of ObjectTemplate.setOnlyForAI - %s"
                            % val
                        )
            elif op == "objecttemplate.setgroup":
                if cur_sp:
                    cur_sp.group = int(args[0])

            # Combat areas
            elif op == "combatareamanager.use":
                val = args[0]
                if val == "1":
                    ca_enabled = True
                elif val == "0":
                    ca_enabled = False
                else:
                    raise Exception(
                        "unsupported value of CombatAreaManager.use - %s" % val
                    )

            elif op == "combatarea.create":
                cas.append(args[0].lower())

            elif op == "combatarea.vehicles":
                if cas and args[0] in ("2", "4", "5"):
                    ca_has_plane_cas = True

            elif op == "combatarea.layer":
                if cas:
                    ca_layer = args[0]

        except Exception as e:
            report_file_exception(gpo_path, ln_no, e)

    # Make spawnpoints PY
    out_path = ospath.join(spawnpoints_path, "%s_%s.py" % (gamemode, layer))
    with open(out_path, "w") as out_f:
        print(
            "# Generated by %s. Do not alter by hand." % __name__, file=out_f
        )
        print("from game.plugins.teamSPs import spawnPoint", file=out_f)
        print("spawnpoints = [", file=out_f)
        for sp in sps:
            if sp.cpid is None:
                report_file_exception(
                    gpo_path,
                    None,
                    "SpawnPoint %s is missing ObjectTemplate.setControlPointId"
                    % sp.name,
                )
                continue
            txt = '  spawnPoint("%s", %d' % (sp.name, sp.cpid)
            if sp.group:
                txt += ", group = %d" % sp.group
            if sp.human_only:
                txt += ", human_only = True"
            if sp.ai_only:
                txt += ", ai_only = True"
            txt += "),"
            print(txt, file=out_f)
        print("]", file=out_f)

    # Write new GPO
    out_path = gpo_path + "_release"
    with open(out_path, "w") as out_f:
        # AI fixes
        if gamemode in ("sp1", "sp2", "sp3", "gpm_coop"):
            out_f.write(
                "rem Auto-added FH2 AiFixes\nrun /AIFixes/aifixes.con\n\n"
            )

        try:
            with open(gpo_path, "r") as in_f:
                out_f.write(in_f.read())
        except UnicodeDecodeError:
            with open(gpo_path, "r", encoding="latin-1") as in_f:
                out_f.write(in_f.read())

        # Plane combat area
        if ca_enabled and has_objectspawners and cas and not ca_has_plane_cas:
            # Get unique name for CA
            ind = 0
            ca_name = ""
            while True:
                ca_name = "CombatArea_%s_%s_planes" % (gamemode, layer)
                if ind:
                    ca_name += "_%s" % ind
                if ca_name not in cas:
                    break
                ind += 1

            for code_ln in (
                "CombatArea.create %s" % ca_name,
                "CombatArea.min 0.000000/0.000000",
                "CombatArea.max 0.000000/0.000000",
                "CombatArea.addAreaPoint %f/%f"
                % (heightdata.max_x, heightdata.max_y),
                "CombatArea.addAreaPoint %f/%f"
                % (heightdata.max_x, heightdata.min_y),
                "CombatArea.addAreaPoint %f/%f"
                % (heightdata.min_x, heightdata.min_y),
                "CombatArea.addAreaPoint %f/%f"
                % (heightdata.min_x, heightdata.max_y),
                "CombatArea.team 0",
                "CombatArea.vehicles 2",
                "CombatArea.layer %s" % ca_layer,
                "",
            ):
                out_f.write("\n" + code_ln)

            print(
                "  %s/%s/%s: Added %s" % (map_name, gamemode, layer, ca_name)
            )

    copy_ftimes(gpo_path, out_path)
    return out_path
