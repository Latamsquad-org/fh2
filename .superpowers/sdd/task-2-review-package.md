# Review package Task 2 (uncommitted)

## Commit list
(none)

## Stat
 python/admin/settings.py | modified admin-load block + get_admin_level

## Diff excerpt (settings.py admin section)

Import added:
 from nameauth import normalize_admin_list, get_admin_level_by_name

Replaced ADMINS_* load with normalize_admin_list(...); empty fallback frozenset().
Added:
 def get_admin_level(name):
     return get_admin_level_by_name(name, ADMINS_HIGH, ADMINS_MID, ADMINS_LOW)

Rest of settings.py unchanged.
Read full file: C:\fh2_1\mods\fh2\python\admin\settings.py
