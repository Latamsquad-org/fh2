# Admin por nombre (sin hash) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Dar admin high/mid/low solo por nombre de jugador (sin tag de clan), usando `admins.toml`, sin hashes.

**Architecture:** Helpers puros en `python/admin/nameauth.py` (strip tag, normalizar, resolver nivel). `settings.py` carga y normaliza las listas del TOML. El punto que hoy compara hash contra `ADMINS_*` se cambia para usar `get_admin_level_by_name(player_name)`. Si ese chequeo no esta en `.py` visible, la Task 4 lo localiza en el arbol del servidor y lo parchea.

**Tech Stack:** Python 2.7 (BF2/FH2), `toml`, `unittest` (sin depender de `host`/`bf2` para tests unitarios).

## Global Constraints

- Solo ASCII en comentarios/strings de `.py` del admin (Py2 sin coding header puede fallar con Non-ASCII).
- Auth solo por nombre; hashes en TOML no dan admin.
- Match: quitar primer `[TAG]` al inicio; resto del nombre debe coincidir completo; case-insensitive.
- Tres niveles: `admins_high` / `admins_mid` / `admins_low` en `python/admins.toml`.
- No anadir dependencias nuevas.
- No hacer commit salvo que el usuario lo pida de forma explicita.

## File map

| File | Responsibility |
|------|----------------|
| `python/admin/nameauth.py` | strip tag, normalize, resolve level from name lists |
| `python/admin/test_nameauth.py` | unit tests (stdlib unittest) |
| `python/admin/settings.py` | load TOML, normalize lists into frozensets, re-export resolver |
| `python/admins.toml` | name lists per level |
| (localizado en Task 4) | replace hash membership check with name resolver |

---

### Task 1: Helpers `nameauth.py` + tests

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

- [ ] **Step 1: Write the failing tests**

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

- [ ] **Step 2: Run tests to verify they fail**

Run from `python/admin`:

```bash
python test_nameauth.py
```

Expected: FAIL / ImportError: `No module named nameauth` (or similar).

- [ ] **Step 3: Implement `nameauth.py`**

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

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd python/admin
python test_nameauth.py
```

Expected: `OK` (all tests pass).

---

### Task 2: Wire `settings.py` to load names

**Files:**
- Modify: `python/admin/settings.py` (admin load block ~lines 27-35)

**Interfaces:**
- Consumes: `normalize_admin_list`, `get_admin_level_by_name` from `nameauth`
- Produces: `ADMINS_HIGH` / `ADMINS_MID` / `ADMINS_LOW` as `frozenset` of normalized names; module-level `get_admin_level(name)` convenience

- [ ] **Step 1: Write a small failing load test**

Create `python/admin/test_settings_names.py` (uses a temp TOML path by testing helpers already covered; this file only checks import + API shape after settings change). Prefer extending Task 1 coverage instead if import of `settings` pulls `toml`/paths awkwardly.

Add to `test_nameauth.py` (already enough for pure logic). For settings, run a one-off check after edit:

```bash
python -c "import settings; print(type(settings.ADMINS_HIGH)); print(hasattr(settings, 'get_admin_level'))"
```

Run from `python/admin` after Step 3; before Step 3 expect AttributeError for `get_admin_level`.

- [ ] **Step 2: Confirm `get_admin_level` missing**

```bash
cd python/admin
python -c "import settings; print(hasattr(settings, 'get_admin_level'))"
```

Expected: `False`

- [ ] **Step 3: Update admin-load block in `settings.py`**

Near the top with other imports, add:

```python
from nameauth import normalize_admin_list, get_admin_level_by_name
```

Replace the try/except that sets `ADMINS_*` with:

```python
try:
    adm_conf = toml.load(ADMINS_FILE)
    ADMINS_HIGH = normalize_admin_list(adm_conf['users']['admins_high'])
    ADMINS_MID = normalize_admin_list(adm_conf['users']['admins_mid'])
    ADMINS_LOW = normalize_admin_list(adm_conf['users']['admins_low'])
except (IOError, KeyError, TypeError):
    ADMINS_LOW = frozenset()
    ADMINS_MID = frozenset()
    ADMINS_HIGH = frozenset()


def get_admin_level(name):
    """Resolve admin level for a raw player name (with or without [TAG])."""
    return get_admin_level_by_name(name, ADMINS_HIGH, ADMINS_MID, ADMINS_LOW)
```

Keep the rest of `settings.py` unchanged.

- [ ] **Step 4: Verify import API**

```bash
cd python/admin
python -c "import settings; print(hasattr(settings, 'get_admin_level')); print(isinstance(settings.ADMINS_HIGH, frozenset))"
```

Expected: `True` then `True`

- [ ] **Step 5: Re-run unit tests**

```bash
cd python/admin
python test_nameauth.py
```

Expected: `OK`

---

### Task 3: Migrate `admins.toml` to names

**Files:**
- Modify: `python/admins.toml`

**Interfaces:**
- Consumes: none
- Produces: TOML lists of player names without required clan tag

- [ ] **Step 1: Replace hash entries with names**

Set contents to (adjust names to the real admins of this server; example from design/logs):

```toml
[users]
admins_high = ['Chaziz']
admins_mid = ['Chaziz']
admins_low = ['Chaziz']
```

Do not leave 32-char hex hashes in these lists; they will not grant admin under name matching.

- [ ] **Step 2: Verify settings resolves the example name**

```bash
cd python/admin
python -c "import settings; print(settings.get_admin_level('[KKCK] Chaziz')); print(settings.get_admin_level('4a64aa3317f2bc80a2c7b8cbbb5c6908'))"
```

Expected first line: `high`  
Expected second line: `None`

---

### Task 4: Locate and patch the hash check

**Files:**
- Search under `C:\fh2_1` (and server Python path if different)
- Modify: the file that currently does membership against `ADMINS_HIGH` / `ADMINS_MID` / `ADMINS_LOW` (path unknown until search)

**Interfaces:**
- Consumes: `settings.get_admin_level(name)` or `get_admin_level_by_name(...)`
- Produces: admin level assignment based on `player.getName()` (or equivalent name string), not hash

- [ ] **Step 1: Search for consumers of `ADMINS_`**

Run (PowerShell or ripgrep):

```bash
rg -n "ADMINS_HIGH|ADMINS_MID|ADMINS_LOW|admins_high" C:\fh2_1 --glob "!logs/**" --glob "!changelog.txt"
```

Also search zip/archives if present:

```bash
rg -l "ADMINS_HIGH" C:\fh2_1 -g "*.zip"
```

Record the file(s) that compare a player hash to those lists.

- [ ] **Step 2: If no `.py` consumer is found**

Check runtime-only packs (common FH2 patterns): look for embedded admin beside `settings.py` comment `Embedded file name`, any `*.pyc` under mod python, or docs from the install that "bump admin".  
If still missing: stop and report blocker — helpers + TOML are ready, but in-game admin will not change until the hash check site is patched. Do not invent a fake admin command system.

- [ ] **Step 3: Patch the check (when file is found)**

Replace patterns like:

```python
if player_hash in ADMINS_HIGH:
    level = 'high'
elif player_hash in ADMINS_MID:
    level = 'mid'
elif player_hash in ADMINS_LOW:
    level = 'low'
```

with:

```python
from admin.settings import get_admin_level
# or relative import matching that package style
level = get_admin_level(player.getName())
```

Adapt to the local variable names (`player`, `p`, etc.). Preserve existing side effects (logging, permission object creation). Prefer calling `get_admin_level` once per check.

If the old code only received a hash string and not a player object, change the call site to pass the player name string available in that scope (connect handler usually has both).

- [ ] **Step 4: Smoke check offline**

```bash
cd python/admin
python test_nameauth.py
python -c "import settings; assert settings.get_admin_level('[KKCK] Chaziz') == 'high'"
```

Expected: tests OK; assert silent.

- [ ] **Step 5: In-game smoke (manual)**

1. Ensure your nick without tag is in `admins_high` in `python/admins.toml`.
2. Restart / reload server so `settings.py` reloads.
3. Join with `[TAG] YourName` and run a high-level admin command.
4. Remove the name from TOML (or change nick), reconnect, confirm command denied.

---

## Spec coverage (self-review)

| Spec requirement | Task |
|------------------|------|
| Solo nombre, sin hash | 3, 4 |
| Tres niveles high/mid/low | 1-3 |
| Reutilizar `admins.toml` | 3 |
| Strip `[TAG]`, match completo, case-insensitive | 1 |
| Normalizar entradas TOML (tag accidental) | 1 (`normalize_admin_list`) |
| TOML invalido -> listas vacias | 2 |
| Prioridad high > mid > low | 1 |
| Smoke test | 4 Step 5 |
| Riesgo paquete admin incompleto | 4 Steps 1-2 |

## Placeholder scan

None intentional. Task 4 path is discovery-bound by design (consumer not in tree today).

## Type consistency

- Lists after load: `frozenset` of `str` (normalized).
- Levels: `'high' | 'mid' | 'low' | None` as plain strings.
- Public API: `settings.get_admin_level(name)` wraps `get_admin_level_by_name`.
