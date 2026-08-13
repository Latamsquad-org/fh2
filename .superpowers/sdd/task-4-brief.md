# Task 4 brief: Locate and patch the hash check

## Global Constraints (binding)

- Solo ASCII en comentarios/strings de `.py` del admin.
- Auth solo por nombre; hashes en TOML no dan admin.
- Match: quitar primer `[TAG]` al inicio; resto completo; case-insensitive.
- Tres niveles en `python/admins.toml`.
- No anadir dependencias nuevas.
- No hacer commit salvo pedido explicito del usuario.

## Already done (do not redo)

- `python/admin/nameauth.py` — helpers
- `python/admin/settings.py` — `get_admin_level(name)`, ADMINS_* as frozensets
- `python/admins.toml` — names (`Chaziz`), no hashes

## Task 4: Locate and patch the hash check

**Files:**
- Search under `C:\fh2_1` (and server Python path if different)
- Modify: the file that currently does membership against `ADMINS_HIGH` / `ADMINS_MID` / `ADMINS_LOW`

**Interfaces:**
- Consumes: `settings.get_admin_level(name)` or `get_admin_level_by_name(...)`
- Produces: admin level from `player.getName()` (or equivalent), not hash

### Step 1: Search

```bash
rg -n "ADMINS_HIGH|ADMINS_MID|ADMINS_LOW|admins_high" C:\fh2_1 --glob "!logs/**" --glob "!changelog.txt"
rg -l "ADMINS_HIGH" C:\fh2_1 -g "*.zip"
```

Also search for: `with Hash`, `getHash`, `in ADMINS`, player hash membership patterns. Check `*.pyc`, embedded packs, anything under `python/admin/` beyond settings.py.

### Step 2: If no consumer found

Stop and report BLOCKED (or DONE_WITH_CONCERNS if helpers work offline but in-game cannot be wired). Do NOT invent a fake admin command system.

### Step 3: If found — patch

Replace hash membership with `get_admin_level(player.getName())` (adapt imports/names). Preserve side effects.

### Step 4: Offline smoke

```bash
cd python/admin
python test_nameauth.py
python -c "import settings; assert settings.get_admin_level('[KKCK] Chaziz') == 'high'"
```

### Step 5: In-game smoke

Document as manual steps for the operator if you cannot run the game server. Do not claim in-game success without evidence.
