# Task 1 brief: Helpers nameauth.py + tests

Extracted from: docs/superpowers/plans/2026-07-24-admin-by-name.md

## Global Constraints (binding)

- Solo ASCII en comentarios/strings de `.py` del admin (Py2 sin coding header puede fallar con Non-ASCII).
- Auth solo por nombre; hashes en TOML no dan admin.
- Match: quitar primer `[TAG]` al inicio; resto del nombre debe coincidir completo; case-insensitive.
- Tres niveles: `admins_high` / `admins_mid` / `admins_low` en `python/admins.toml`.
- No anadir dependencias nuevas.
- No hacer commit salvo que el usuario lo pida de forma explicita.

## Task 1: Helpers `nameauth.py` + tests

**Files:**
- Create: `python/admin/nameauth.py`
- Create: `python/admin/test_nameauth.py`

**Interfaces:**
- Consumes: nothing (pure functions)
- Produces:
  - `strip_clan_tag(name)` -> `str`
  - `normalize_admin_name(name)` -> `str` (strip tag + trim + lower); empty input -> `''`
  - `normalize_admin_list(entries)` -> `frozenset` of normalized non-empty names
  - `get_admin_level_by_name(name, high, mid, low)` -> `'high'|'mid'|'low'|None` (priority high > mid > low)

### Step 1: Write the failing tests

Create `python/admin/test_nameauth.py`:

```python
# Unit tests for admin name matching (Python 2.7 / unittest)
import unittest

from nameauth import (
    strip_clan_tag,
    normalize_admin_name,
    normalize_admin_list,
    get_admin_level_by_name,
)


class TestStripClanTag(unittest.TestCase):

    def test_strips_bracket_tag(self):
        self.assertEqual(strip_clan_tag('[KKCK] Chaziz'), 'Chaziz')

    def test_strips_tag_with_symbols(self):
        self.assertEqual(strip_clan_tag('[LP!] MarceloGallardo'), 'MarceloGallardo')

    def test_no_tag_unchanged(self):
        self.assertEqual(strip_clan_tag('axelpro'), 'axelpro')

    def test_unclosed_bracket_unchanged(self):
        self.assertEqual(strip_clan_tag('[broken Chaziz'), '[broken Chaziz')

    def test_empty(self):
        self.assertEqual(strip_clan_tag(''), '')


class TestNormalize(unittest.TestCase):

    def test_case_and_tag(self):
        self.assertEqual(normalize_admin_name('  [KKCK] Chaziz  '), 'chaziz')

    def test_toml_entry_with_accidental_tag(self):
        self.assertEqual(normalize_admin_name('[KKCK] Chaziz'), 'chaziz')


class TestNormalizeList(unittest.TestCase):

    def test_drops_empty_and_normalizes(self):
        result = normalize_admin_list(['Chaziz', '', '  ', '[X] Bob'])
        self.assertEqual(result, frozenset(['chaziz', 'bob']))


class TestGetLevel(unittest.TestCase):

    def setUp(self):
        self.high = frozenset(['chaziz'])
        self.mid = frozenset(['bob'])
        self.low = frozenset(['carl'])

    def test_high_wins(self):
        high = frozenset(['shared'])
        mid = frozenset(['shared'])
        self.assertEqual(
            get_admin_level_by_name('[T] Shared', high, mid, self.low),
            'high',
        )

    def test_mid(self):
        self.assertEqual(
            get_admin_level_by_name('Bob', self.high, self.mid, self.low),
            'mid',
        )

    def test_low(self):
        self.assertEqual(
            get_admin_level_by_name('carl', self.high, self.mid, self.low),
            'low',
        )

    def test_none(self):
        self.assertIsNone(
            get_admin_level_by_name('nobody', self.high, self.mid, self.low)
        )

    def test_hash_like_string_does_not_match_name_list(self):
        # Old hash values must not grant admin when lists hold names
        self.assertIsNone(
            get_admin_level_by_name(
                '4a64aa3317f2bc80a2c7b8cbbb5c6908',
                self.high,
                self.mid,
                self.low,
            )
        )


if __name__ == '__main__':
    unittest.main()
```

### Step 2: Run tests to verify they fail

Run from `python/admin`:

```bash
python test_nameauth.py
```

Expected: FAIL / ImportError: `No module named nameauth` (or similar).

### Step 3: Implement `nameauth.py`

Create `python/admin/nameauth.py`:

```python
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
    return strip_clan_tag(str(name)).strip().lower()


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
```

### Step 4: Run tests to verify they pass

```bash
cd python/admin
python test_nameauth.py
```

Expected: `OK` (all tests pass).
