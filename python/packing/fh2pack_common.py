# -*- coding: utf-8 -*-

import fnmatch
from os import path
import os
import calendar
import zipfile
import glob
from datetime import datetime

RELEASE = 0

DEFAULT_FILE_TIME = calendar.timegm(
    datetime(2005, 12, 15).utctimetuple()
)  # The date of the first commit to SVN

inclusions = {
    "client": (
        "*.font",
        "*.dif",
        "*.difb",
        "*.fx",
        "*.mfx",
        "*.dfx",
        "*.mesh",
        "*.fh2road",
        "*.bundledmesh",
        "*.staticmesh",
        "*.skinnedmesh",
        "*.treemesh",
        "*.mp3",
        "*.tga",
        "*.gif",
        "*.jpg",
        "*.wav",
        "*.avi",
        "*.bik",
        "*.dat",
        "*.ogg",
        "*.occ",
        "*.ani",
        "*.swf",
        "*.dds",
        "*.png",
        "*.tai",
        "*.tac",
        "*.baf",
        "terraindata.raw",
        "undergrowth.cfg",
        "undergrowth.raw",
    ),
    "server": ("*",),
}

exclusions = {
    "client": (
        "external/flashmenu/cursor/*.ani",
        "external/flashmenu/cursor/*.cur",
        "*.bak",
        "editor/*",
        "fh2editor/*",
        "info/*",
        "*.svn/*",
        ".svn/*",
        "*/.svn/*",
        "*/psd/*",
        "*.samples",
        "*.samp_01",
        "*.samp_02",
        "*.samp_03",
        "*.samp_04",
        "*.max",
        "*.baf",
        "*.psd",
        "*.xcf",
        "*.db",
        "menu/atlas/memeatlas.tai",
        "*.con_release",
        "*.md5",
        "*_lmapdummy.staticmesh",
    ),
    "server": (
        "*.font",
        "*.dif",
        "*.difb",
        "*.fx",
        "*.dfx",
        "*.mesh",
        "*.bundledmesh",
        "*.staticmesh",
        "*.skinnedmesh",
        "*.treemesh",
        "*.mp3",
        "*.dds",
        "*.tga",
        "*.gif",
        "*.jpg",
        "*.wav",
        "*.avi",
        "*.bik",
        "*.dat",
        "*.png",
        "*.ogg",
        "*.occ",
        "*.ani",
        "*.swf",
        "*.samples",
        "*.samp_01",
        "*.samp_02",
        "*.samp_03",
        "*.samp_04",
        "*.bak",
        "terraindata.raw",
        "undergrowth.cfg",
        "*/standardize-guns.cfg",
        "*.tac",
        "*.py",
        "undergrowth.raw",
        "*.db",
        "*.bik",
        "*.dat",
        "lightmaps/objects/lightmapatlas.tai",
        "overgrowth/overgrowthatlas.tai",
        "undergrowthatlas.tai",
        "*.psd",
        "*.xcf",
        "*.nfo",
        "*.zip",
        "*.rar",
        "*.7z",
        "info/*",
        "gpu_*.*",
        "*.bat",
        "*.xls",
        "*.xlsx",
        "external/flashmenu/cursor/*",
        "*.svn/*",
        ".svn/*",
        "*/.svn/*",
        "*/psd/*",
        "*.max",
        "*.con_release",
        "*.md5",
    ),
}

inclusions["client_colorblind"] = inclusions["client"]
exclusions["client_colorblind"] = exclusions["client"]

COLORBLIND_REPLACEMENTS = {
    "objective_destroy_marker.dds": "objective_destroy_marker_colorblind.dds",
    "objective_defend_marker.dds": "objective_defend_marker_colorblind.dds",
    "objective_destroyed_marker.dds": "objective_destroyed_marker_colorblind.dds",
}

# do NOT touch this line. Ignores are automagically triggered by an RC tag
ignores = [
    "ignore.txt",
    "shadersignore.txt",
]

if (
    "CI_COMMIT_TAG" in os.environ.keys()
    and "RC" in os.environ["CI_COMMIT_TAG"]
):
    ignores.append("betaignore.txt")
    ignores.extend(
        [
            "belgianignore.txt",
            "franceignore.txt",
            "hungarianignore.txt",
            "norwayignore.txt",
            "pacificignore.txt",
            "polishignore.txt",
        ],
    )
ignores = [ign.lower() for ign in ignores]


def wildcardedby(somepath, wildcards):
    pathl = somepath.lower()
    for w in wildcards:
        if fnmatch.fnmatch(pathl, w.lower()):
            return True
    return False


def include(p, what, target):
    if not wildcardedby(p, inclusions[target.lower()]):
        return False
    return not wildcardedby(p, exclusions[target.lower()])


# Copy modified time (and access time just in case) from source to dest. file to reduce false diffs in zips for distribution as torrents
def copy_ftimes(src_file_path, dst_file_path):
    stinfo = os.stat(src_file_path)
    os.utime(dst_file_path, (stinfo.st_atime, stinfo.st_mtime))
    return (stinfo.st_atime, stinfo.st_mtime)


def set_ftime(file_path, ftime=0):
    if ftime < DEFAULT_FILE_TIME:
        ftime = DEFAULT_FILE_TIME
    os.utime(file_path, (ftime, ftime))


def zip_writestr(zip, arc_path, text):
    info = zipfile.ZipInfo(arc_path, date_time=(2005, 12, 15, 0, 0, 0))
    zip.writestr(info, text, zipfile.ZIP_DEFLATED)


def ignore_dir(dir_path):
    for ignore_fname in ignores:
        if path.isfile(path.join(dir_path, ignore_fname)):
            return True
    return False


def has_ignore_file(filenames):
    for ignore_fname in ignores:
        if ignore_fname in filenames:
            return True
    return False


def walk_files(root_path, extensions=None):
    """
    Walks root_path and its sub-dirs, yielding each found file as tuple (normalized path, lowercase extension).
    Skips dirs marked with ignore files.
    Optionally, filters files by extension(s).
    """

    if extensions:
        if type(extensions) == type(""):
            extensions = [extensions.lower()]
        else:
            extensions = [x.lower() for x in extensions]

    for root, dirs, files in os.walk(root_path):
        if has_ignore_file(files):
            # Clear the list of sub-dirs so os.walk would skip them
            del dirs[:]
        else:
            for filename in files:
                fbase, ext = path.splitext(filename)
                ext = ext.lower()
                if not extensions or ext in extensions:
                    yield normalize_path(path.join(root, filename)), ext


def normalize_path(somepath):
    return somepath.replace("\\", "/")


# Case insensitive file/dir paths


def icase(text):
    # http://stackoverflow.com/a/10886685
    def either(c):
        return "[%s%s]" % (c.lower(), c.upper()) if c.isalpha() else c

    return "".join(map(either, text))


def ifile_find(ipath):
    glob_res = glob.glob(ipath)
    n_entries = len(glob_res)
    if n_entries == 1:
        if path.isfile(glob_res[0]):
            return glob_res[0]
        else:
            return None
    elif n_entries > 1:
        raise FileNotFoundError(
            "ifile_find found too many entries matching %s" % ipath
        )
    return None  # n_entries == 0


def idir_find(ipath):
    glob_res = glob.glob(ipath)
    n_entries = len(glob_res)
    if n_entries == 1:
        if path.isdir(glob_res[0]):
            return glob_res[0]
        else:
            return None
    elif n_entries > 1:
        raise FileNotFoundError(
            "idir_find found too many entries matching %s" % ipath
        )
    return None  # n_entries == 0


def ifile_exists(ipath):
    return ifile_find(ipath) is not None


def idir_exists(ipath):
    return idir_find(ipath) is not None
