# Review package Task 4 (uncommitted)

## Commit list
(none)

## Stat
 python/admin/bf2_tools.py | NEW ~1244 lines (decompiled + patch)
 python/admin/bf2_tools.pyc | REMOVED (backed up to .superpowers/sdd/bf2_tools.pyc.bak)

## Critical patch hunk (admin_level)

Before: key_hash membership in ADMINS_HIGH/MID/LOW
After:
  from admin.settings import ..., get_admin_level, ...
  @property
  def admin_level(self):
      if self._admin_level is not None:
          return self._admin_level
      else:
          out = get_admin_level(self.name)
          self._admin_level = out
          return out

Note: FH2Player.name is already split from clan via get_fullname(); get_admin_level still strips [TAG] if present.

## Risk
Full-module uncompyle6 recovery of Py2.7 bytecode via Py3.14 uncompyle6 — not a surgical .pyc edit.

Full files: C:\fh2_1\mods\fh2\python\admin\bf2_tools.py
Report: C:\fh2_1\mods\fh2\.superpowers\sdd\task-4-report.md
