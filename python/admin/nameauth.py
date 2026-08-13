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
