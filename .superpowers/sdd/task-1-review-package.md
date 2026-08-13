# Review package for Task 1 (uncommitted — no commits per plan constraint)

## Commit list
(none — working tree only)

## Stat summary
 python/admin/nameauth.py      | new file, 56 lines
 python/admin/test_nameauth.py | new file, 91 lines

## Full diff (new files)

=== CREATE python/admin/nameauth.py ===
# Name-based admin matching helpers (ASCII only for Py2 safety)
"""
nameauth
--------
Match admin levels by player name (no CD-key hash).
Strips a leading [CLAN] tag, then case-insensitive full match.
"""


def strip_clan_tag(name):
    """Remove a leading [TAG] block and following spaces; else return name as-is."""
    if not name:
        return ''
    s = name
    if s.startswith('['):
        end = s.find(']')
        if end != -1:
            s = s[end + 1:].lstrip()
    return s


def normalize_admin_name(name):
    """Strip clan tag, trim, lowercase. Empty -> ''."""
    if name is None:
        return ''
    return strip_clan_tag(str(name).strip()).strip().lower()


def normalize_admin_list(entries):
    """Build frozenset of normalized names; skip empties."""
    out = []
    if not entries:
        return frozenset()
    for item in entries:
        n = normalize_admin_name(item)
        if n:
            out.append(n)
    return frozenset(out)


def get_admin_level_by_name(name, high, mid, low):
    """
    Return 'high', 'mid', 'low', or None.
    Priority: high > mid > low.
    high/mid/low must be frozensets of normalize_admin_name results.
    """
    key = normalize_admin_name(name)
    if not key:
        return None
    if key in high:
        return 'high'
    if key in mid:
        return 'mid'
    if key in low:
        return 'low'
    return None

=== CREATE python/admin/test_nameauth.py ===
(full file matches brief tests; 13 unittest cases)
See C:\fh2_1\mods\fh2\python\admin\test_nameauth.py for complete contents.
Key coverage: strip tag, normalize, list normalize, get level high/mid/low/none/hash-no-match.
