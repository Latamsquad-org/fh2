# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0209,R0902,C0116,C0115,W1514,R0205,R0903,R0911,R0912,R0915,R0914,W0703  # noqa
# vim:set ts=4 sts=4 sw=4 et syntax=python:
"""con-file parser
"""

from __future__ import print_function

import os
import glob
from string import ascii_letters

from game import is_bf2  # pylint: disable=E0401

if is_bf2:
    from game.utilities import path  # pylint: disable=E0401
else:
    from os import path


def icase(item):
    """Produce case-insensitive glob input from string"""
    if not isinstance(item, str):
        raise ValueError("input MUST be string!")
    out = ""
    for x in item:
        if x in ascii_letters:
            out += "[%s%s]" % (x.upper(), x.lower())
        else:
            out += x
    return out


def _find_file_linux(fn):
    if path.isfile(fn):  # Maybe, no further optimizations needed?
        return fn

    fn = fn.replace("\\", "/")  # escape windows path backslashes
    fn = icase(fn)
    found = glob.glob(fn)
    if found and path.isfile(found[0]):
        return found[0]
    return None


def _ci_exists_linux(fn):
    return _find_file_linux(fn) is not None


def _ci_open_linux(fn, mode):
    try:
        return open(fn, mode)
    except IOError:
        pass

    real_fn = _find_file_linux(fn)
    if real_fn is None:
        raise IOError("%s file does not exist" % fn)

    return open(real_fn, mode)


def _find_file_windows(fn):
    if path.isfile(fn):
        return fn
    return None


def _ci_exists_windows(fn):
    return path.isfile(fn)


def _ci_open_windows(fn, mode):
    return open(fn, mode)


if not is_bf2 and os.name == "nt":
    find_file = _find_file_windows
    ci_exists = _ci_exists_windows
    ci_open = _ci_open_windows
else:
    find_file = _find_file_linux
    ci_exists = _ci_exists_linux
    ci_open = _ci_open_linux


class GeometryTemplate(object):

    def __init__(self, type_, name, filepath):
        self.original_name = name
        self.type = type_.lower()
        self.name = name.lower()
        self.filepath = filepath
        if filepath:
            self.base = path.dirname(filepath)
        else:
            self.base = None
        self.properties = {}

    def __str__(self):
        return "<GeometryTemplate %s %s>" % (self.type, self.original_name)

    def __repr__(self):
        return '"%s"' % str(self)

    def verify_mesh_exists(self):
        if self.base is None:
            return

        meshpath = self.getRelativeMeshPath()
        if not ci_exists(path.join(self.base, meshpath)):
            print(
                "!!! Invalid GeometryTemplate %s in %s: can not find %s" %
                (self.original_name, self.filepath, meshpath)
            )

    def getRelativeMeshPath(self):
        ext = {
            "meshparticlemesh": "bundledmesh",
        }
        if self.type == "roadcompiled":
            return "%s_compiled.dat" % self.original_name
        return "Meshes/%s.%s" % (
            self.original_name, ext.get(self.type, self.type)
        )


class CollisionTemplate(object):

    def __init__(self, name, filepath):
        self.original_name = name
        self.name = name.lower()
        self.filepath = filepath
        if filepath:
            self.base = path.dirname(filepath)
        else:
            self.base = None

    def __str__(self):
        return "<GeometryTemplate %s>" % self.original_name

    def __repr__(self):
        return '"%s"' % str(self)

    def verify_mesh_exists(self):
        if self.base is None:
            return

        meshpath = "Meshes/%s.collisionmesh" % self.original_name
        if not ci_exists(path.join(self.base, meshpath)):
            print(
                "!!! Invalid CollisionTemplate %s in %s: can not find %s" %
                (self.original_name, self.filepath, meshpath)
            )


class Template(object):

    def __init__(self, ot_type, name, filepath):
        self.original_name = name
        self.filepath = filepath
        if filepath:
            self.base = path.dirname(filepath)
        else:
            self.base = None
        self.type = ot_type.lower()
        self.name = name.lower()
        self.properties = {}
        self.children = []
        self.children_positions = []

    def __str__(self):
        return "<ObjectTemplate %s %s>" % (self.type, self.original_name)

    def __repr__(self):
        return '"%s"' % str(self)

    def get_simple_property(self, name, default_value):
        values = self.properties.get("objecttemplate." + name.lower(), [])
        if values:
            return values[-1][0]
        return default_value


class Instance(object):

    def __init__(self, template):
        self.template = template
        self.properties = {}


class ConParser(object):

    def __init__(self, do_instances=False, ignore_warnings=False):
        self.template = None
        self.templates = []
        self.mesh = None
        self.meshes = []
        self.cols = []
        self.instance = None
        self.instances = []
        self.do_instances = do_instances
        self.ignore_warnings = ignore_warnings
        self.lines = []
        self.error_header = None
        self.constants = {}

    def load(self, filename):
        f = ci_open(filename, "r")
        self.lines.extend(f.readlines())
        f.close()

        self._go(filename, self.lines)

    def run_string(self, string):
        self.lines.extend(string.split("\n"))

        self._go(None, self.lines)

    def _go(self, filepath, lines):
        if filepath is not None:
            filepath = filepath.replace("\\", "/").lstrip("/")
        self.error_header = filepath

        ignore = False
        for line in lines:
            args = self._get_args(line)
            if not args:
                continue

            op = args[0].lower()
            if op in ("endrem", "endif"):
                ignore = False
                continue
            if ignore or op == "rem":
                continue
            if op in ("beginrem", "if"):
                ignore = True
                continue

            if op in ("run", "include"):
                assert len(args) >= 2
                assert filepath is not None, "missing base for include"

                _incfilepath = args[1].lstrip("\\/")
                basedir = path.dirname(filepath)

                p = path.join(basedir, _incfilepath)
                incpath = find_file(path.normpath(p))
                if incpath is None and basedir and not _incfilepath.startswith(
                    "."
                ):
                    incpath = find_file(
                        _incfilepath
                    )  # Maybe it's a full path (Objects/bla-bla-bla)?

                if incpath is None:
                    if (
                        basedir.lower().startswith("objects/kits/")
                        and _incfilepath.lower().endswith(".inc")
                        and ci_exists(
                            path.join(basedir, _incfilepath[:-4] + ".con")
                        )
                    ):
                        pass  # Do not report for rifle includes in NCO kits
                    else:
                        self.report("Could not find", args[1], "for", op)
                else:
                    with open(incpath, "r") as f:
                        inclines = f.readlines()

                    tmp_error_header = self.error_header
                    ignore = self._go(incpath, inclines)
                    self.error_header = tmp_error_header

                continue

            self._process_directive(filepath, op, args[1:])

        return ignore

    def _get_args(self, line):
        if '"' not in line:
            return line.split()

        out = []
        is_quoted = False
        for part in line.strip().split('"'):
            if is_quoted:
                out.append(part)
                is_quoted = False
            else:
                out += part.split()
                is_quoted = True

        if out and not is_quoted and out[0].lower() != "rem":
            self.report(
                "'%s' command either is missing a closing quote "
                "or has an excess quote" % line.strip()
            )

        return out

    def process_directive(self, filepath, command, args):
        self._process_directive(
            filepath=filepath, command=command.lower(), args=args
        )

    def _process_directive(self, filepath, command, args):
        if command.startswith("objecttemplate."):
            sub_command = command[15:]

            if sub_command == "create":
                self.template = Template(args[0], args[1], filepath)
                self.templates.append(self.template)
                return

            if sub_command == "activesafe":
                if len(args) != 2:
                    self.report(
                        "Invalid ObjectTemplate.activeSafe line:",
                        self._repr_command(command, args),
                    )
                    return
                ot_type = args[0].lower()
                name = args[1]
                name_low = name.lower()

                # Already defined?
                for x in self.templates:
                    if x.name == name_low:
                        if x.type == ot_type:
                            self.template = x
                        else:
                            self.report(
                                "activeSafe",
                                name,
                                "wrong type: wanted",
                                ot_type,
                                ", got",
                                x.type,
                            )
                            self.template = x
                        return

                # New template
                self.template = Template(ot_type, name, filepath)
                self.templates.append(self.template)
                return

            if sub_command == "active":
                name = args[0]
                name_low = name.lower()

                # Already defined?
                for x in self.templates:
                    if x.name == name_low:
                        self.template = x
                        return

                # New template
                if name_low.startswith("s_"):
                    self.template = Template("Sound", name, filepath)
                else:
                    self.report(
                        self._repr_command(command, args),
                        ": unknown template", name
                    )
                    self.template = Template("SimpleObject", name, filepath)
                self.templates.append(self.template)
                return

            cur_template = self.template
            if cur_template is None:
                self.report(
                    "Command",
                    self._repr_command(command, args),
                    "executed without activated template",
                )
                return

            if sub_command == "addtemplate":
                name = args[0].lower()
                cur_template.children.append(name)
                cur_template.children_positions.append(([0.0, 0.0,
                                                         0.0], [0.0, 0.0,
                                                                0.0]))
                return

            if sub_command in ("setposition", "setrotation"):
                if not cur_template.children:
                    self.report(
                        "Command",
                        self._repr_command(command, args),
                        "executed without ObjectTemplate.addTemplate",
                    )
                    return
                try:
                    if len(args) != 1:
                        raise ValueError("Invalid arg len!")
                    coords = args[0].split("/")
                    if len(coords) != 3:
                        raise ValueError("Invalid coord len!")
                    coords = map(float, coords)
                except Exception:
                    self.report(
                        "Invalid line:", self._repr_command(command, args)
                    )
                    return
                c_pos, c_rot = cur_template.children_positions[-1]
                if sub_command == "setposition":
                    cur_template.children_positions[-1] = (coords, c_rot)
                else:
                    cur_template.children_positions[-1] = (c_pos, coords)
                return

            self._add_args(cur_template.properties, command, args)

        elif self.do_instances and command.startswith("object."):
            if command == "object.create":
                (template, ) = args
                self.instance = Instance(template)
                self.instances.append(self.instance)
                return

            if self.instance is None:
                self.report(
                    "Command",
                    self._repr_command(command, args),
                    "executed without activated object instance",
                )
                return

            self._add_args(self.instance.properties, command, args)

        elif command == "const":
            self.constants[args[0].lower()] = args[2]

        elif command.startswith("geometrytemplate."):
            if command == "geometrytemplate.create":
                type_, name = args
                self.mesh = GeometryTemplate(type_, name, filepath)
                self.meshes.append(self.mesh)
                return

            if self.mesh is None:
                self.report(
                    "Command",
                    self._repr_command(command, args),
                    "executed without activated geometry template",
                )
                return

            self._add_args(self.mesh.properties, command, args)

        elif command == "collisionmanager.createtemplate":
            (name, ) = args
            col = CollisionTemplate(name, filepath)
            self.cols.append(col)
            return

        else:
            return

    def _add_args(self, properties_collection, command, args):
        if self.constants:
            consts = self.constants
            for i, a in enumerate(args):
                a_low = a.lower()
                if a_low.startswith("c_") and a_low in consts:
                    args[i] = consts[a_low]

        if command in properties_collection:
            properties_collection[command].append(args)
        else:
            properties_collection[command] = [args]

    @staticmethod
    def _repr_command(command, args):
        return "%s %s" % (command, " ".join(args))

    def report(self, *what):
        if self.ignore_warnings:
            return
        if self.error_header:
            print("\n%s:" % self.error_header)
            self.error_header = None
        print("    !!!", " ".join(map(str, what)))
