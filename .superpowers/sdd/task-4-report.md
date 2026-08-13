# Task 4 Report: Locate and patch the hash check

**Date:** 2026-07-24  
**Status:** DONE_WITH_CONCERNS  
**Commits:** none (per instructions)

## Summary

Located the CD-key hash membership check in `python/admin/bf2_tools.pyc` (no prior `.py` source in the tree). Decompiled it to `python/admin/bf2_tools.py` and patched `FH2Player.admin_level` to call `settings.get_admin_level(self.name)` instead of `key_hash in ADMINS_*`. Offline unit/smoke checks pass. In-game verification was not run here.

## Search (Step 1)

Commands / scans under `C:\fh2_1` (excluding `logs/**` noise where noted):

| Target | Result |
|--------|--------|
| `ADMINS_HIGH\|ADMINS_MID\|ADMINS_LOW` in `.py` | Only `python/admin/settings.py` (definitions / `get_admin_level`) |
| Same strings in `.pyc` under `python/admin/` | **`bf2_tools.pyc`** (consumer), `settings.pyc` (loader) |
| `with Hash` in `.pyc` | `python/admin/plugins/tracking.pyc` (connect log text only; not admin gate) |
| `*.zip` containing `ADMINS_HIGH` | No hit required for the gate; consumer was local `.pyc` |
| Visible `python/admin/*.py` before Task 4 | `settings.py`, `nameauth.py`, `test_nameauth.py` only |

**Consumer found:** `FH2Player.admin_level` in embedded module `python/admin/bf2_tools.py` (bytecode dated 2026-03-10 / file mtime 2026-07-08).

Decompile evidence:

```text
uncompyle6 C:\fh2_1\mods\fh2\python\admin\bf2_tools.pyc
# Embedded file name: python/admin/bf2_tools.py
# Python bytecode version base 2.7 (62211)
```

## Patch (Step 3)

**Files changed:**

| File | Change |
|------|--------|
| `python/admin/bf2_tools.py` | **New source** recovered via uncompyle6 from `bf2_tools.pyc`; import + `admin_level` patched for name auth |
| `python/admin/bf2_tools.pyc` | Moved aside to `.superpowers/sdd/bf2_tools.pyc.bak` so stale hash-check bytecode cannot be preferred over the new `.py` |

**Not invented:** No new admin command framework. Only the existing `FH2Player.admin_level` gate was changed.

### Before (hash membership)

```python
from admin.settings import LEVEL_DIR, ADMINS_HIGH, ADMINS_MID, ADMINS_LOW, BAN_DURATION, BLOCK_SELF_SWITCH, IS_BETA
...
    @property
    def admin_level(self):
        if self._admin_level is not None:
            return self._admin_level
        else:
            kh = self.key_hash
            kh = kh.encode('utf-8')
            if kh in ADMINS_HIGH:
                out = 'high'
            elif kh in ADMINS_MID:
                out = 'mid'
            elif kh in ADMINS_LOW:
                out = 'low'
            else:
                out = None
            self._admin_level = out
            return out
```

### After (name via get_admin_level)

```python
from admin.settings import LEVEL_DIR, get_admin_level, BAN_DURATION, BLOCK_SELF_SWITCH, IS_BETA
...
    @property
    def admin_level(self):
        # Name-based admin level (hash lists no longer grant admin).
        if self._admin_level is not None:
            return self._admin_level
        else:
            out = get_admin_level(self.name)
            self._admin_level = out
            return out
```

**Name source:** `FH2Player.name` is the name half from `get_fullname(bf2_ply)` in `from_bf2` (clan tag already split into `self.clan`). That is the local equivalent of a player name string for this class; `get_admin_level` still strips a leading `[TAG]` if present. Caching of `_admin_level` / `_is_admin` side effects preserved. `key_hash` still collected for logging/identity; it no longer grants admin.

## Offline smoke (Step 4)

```powershell
cd C:\fh2_1\mods\fh2\python\admin
python test_nameauth.py
python -c "import settings; assert settings.get_admin_level('[KKCK] Chaziz') == 'high'"
```

**Results:**

- `test_nameauth.py`: 13 tests, OK
- assert: silent success; printed check showed `high`
- Patch markers: `get_admin_level(self.name)` present; `kh in ADMINS_HIGH` absent

## In-game smoke (Step 5) — manual for operator

Not executed in this environment (no live FH2 dedicated-server join from the agent). Operator steps:

1. Confirm `python/admins.toml` has the nick without tag in the desired tier (e.g. `Chaziz` in `admins_high`).
2. Restart the FH2 server so Python reloads `admin.settings` and `admin.bf2_tools` from the new `.py` (ensure no leftover `bf2_tools.pyc` next to it; backup is under `.superpowers/sdd/bf2_tools.pyc.bak`).
3. Join as `[TAG] Chaziz` (or bare `Chaziz`) and run a high-level admin command.
4. Remove the name from TOML (or change nick), reconnect, confirm the command is denied.

## Concerns

1. **Full-module decompile:** `bf2_tools.py` is uncompyle6 output of the whole module (~1200+ lines), not a tiny surgical edit on an existing source tree. Runtime risk if decompilation misread unrelated functions. Mitigations: only `admin_level` + import were intentionally changed; original `.pyc` kept as `.superpowers/sdd/bf2_tools.pyc.bak`.
2. **No in-game proof:** Status is DONE_WITH_CONCERNS until Step 5 is confirmed on a live server.
3. **Stale sibling `.pyc`:** Other admin modules remain bytecode-only. `settings.py` is newer than `settings.pyc` (2026-07-24 vs 2026-07-08); standard Py2 import should recompile from `.py`, but a server restart is required.
4. **Py2.7 not on this build machine:** Cannot recompile `bf2_tools.pyc` with the game Python here; server must compile from `.py` at import or run from source.

## Task 4 review fix (2026-07-24)

**CRITICAL fix:** Removed uncompyle6 artifact at EOF of `python/admin/bf2_tools.py` (bare module-level `return` on line 1243). Py2.7 raises `SyntaxError: 'return' outside function` on import without this fix.

**Optional scan:** Grep for `^return` in `python/**/*.py` — only hit is `.superpowers/sdd/bf2_tools_decompiled.py` (backup copy, not loaded at runtime). No other module-level returns removed.

### Validation commands and output

```powershell
# Module-level return check (targeted; build machine has Py3.14, not Py2.7)
python -c "path=r'C:\fh2_1\mods\fh2\python\admin\bf2_tools.py'; lines=open(path).read().rstrip().splitlines(); assert lines[-1].strip()!='return'; print('No module-level return at EOF: OK')"
```

```
No module-level return at EOF: OK
```

```powershell
# User-requested ast.parse / py_compile (Py3.14 cannot parse Py2 print syntax; pre-existing)
python -c "import ast; ast.parse(open(r'C:\fh2_1\mods\fh2\python\admin\bf2_tools.py').read())"
python -m py_compile C:\fh2_1\mods\fh2\python\admin\bf2_tools.py
```

```
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?  (line 825)
```

Note: Failure is Py2-vs-Py3 `print` statements elsewhere in the decompiled file, not the removed module-level `return`. On the game server (Py2.7), import should succeed once the EOF `return` is gone.

```powershell
cd C:\fh2_1\mods\fh2\python\admin
python test_nameauth.py
python -c "import settings; assert settings.get_admin_level('[KKCK] Chaziz') == 'high'; print('Chaziz assert OK')"
```

```
Ran 13 tests in 0.000s
OK
Chaziz assert OK
```

**Status after fix:** CRITICAL SyntaxError resolved; offline name-auth tests still pass. admin_level patch unchanged.

## Spec / plan coverage

| Requirement | Result |
|-------------|--------|
| Find consumer of `ADMINS_HIGH/MID/LOW` | Found in `bf2_tools` |
| Auth by name, not hash | Patched |
| Use `get_admin_level` | Yes |
| Do not invent new admin system | Yes |
| ASCII-only `.py` edits | Yes (verified non-ASCII count 0 before patch; comment ASCII) |
| No commit | Yes |
