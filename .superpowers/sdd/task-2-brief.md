# Task 2 brief: Wire settings.py to load names

Extracted from: docs/superpowers/plans/2026-07-24-admin-by-name.md

## Global Constraints (binding)

- Solo ASCII en comentarios/strings de `.py` del admin (Py2 sin coding header puede fallar con Non-ASCII).
- Auth solo por nombre; hashes en TOML no dan admin.
- Match: quitar primer `[TAG]` al inicio; resto del nombre debe coincidir completo; case-insensitive.
- Tres niveles: `admins_high` / `admins_mid` / `admins_low` en `python/admins.toml`.
- No anadir dependencias nuevas.
- No hacer commit salvo que el usuario lo pida de forma explicita.

## Task 2: Wire `settings.py` to load names

**Files:**
- Modify: `python/admin/settings.py` (admin load block ~lines 27-35)

**Interfaces:**
- Consumes: `normalize_admin_list`, `get_admin_level_by_name` from `nameauth`
- Produces: `ADMINS_HIGH` / `ADMINS_MID` / `ADMINS_LOW` as `frozenset` of normalized names; module-level `get_admin_level(name)` convenience

### Step 1-2: Confirm get_admin_level missing before edit

```bash
cd python/admin
python -c "import settings; print(hasattr(settings, 'get_admin_level'))"
```

Expected before edit: `False`

### Step 3: Update admin-load block in `settings.py`

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

Note: `nameauth.py` already exists from Task 1 at `python/admin/nameauth.py`. Import is relative same-directory style as used in BF2 (`from nameauth import ...`).

### Step 4: Verify import API

```bash
cd python/admin
python -c "import settings; print(hasattr(settings, 'get_admin_level')); print(isinstance(settings.ADMINS_HIGH, frozenset))"
```

Expected: `True` then `True`

### Step 5: Re-run unit tests

```bash
cd python/admin
python test_nameauth.py
```

Expected: `OK`

Do NOT migrate admins.toml in this task (Task 3). Do NOT commit.
