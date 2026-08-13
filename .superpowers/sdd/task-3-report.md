# Task 3 Report: Migrate admins.toml to names

**Date:** 2026-07-24  
**Status:** DONE  
**Commits:** none (per instructions)

## Summary

Replaced the 32-char CD-key hash in `python/admins.toml` with the player name `Chaziz` across all three admin tiers. `settings.get_admin_level` now resolves `[KKCK] Chaziz` to `high` and rejects the legacy hash string with `None`.

## Files changed

| File | Change |
|------|--------|
| `python/admins.toml` | Replaced hash `4a64aa3317f2bc80a2c7b8cbbb5c6908` with `'Chaziz'` in `admins_high`, `admins_mid`, and `admins_low` |

**Not changed (per brief):** `python/admin/settings.py`, `python/admin/nameauth.py`, `python/admin/test_nameauth.py`, hash-check runtime code (Task 4 scope)

## Step 1: Replace hash entries with names

**Before:**

```toml
[users]
admins_high = ['4a64aa3317f2bc80a2c7b8cbbb5c6908']
admins_mid = ['4a64aa3317f2bc80a2c7b8cbbb5c6908']
admins_low = ['4a64aa3317f2bc80a2c7b8cbbb5c6908']
```

**After:**

```toml
[users]
admins_high = ['Chaziz']
admins_mid = ['Chaziz']
admins_low = ['Chaziz']
```

No 32-char hex hashes remain in the file (verified via regex scan).

## Step 2: Verify settings resolves the example name

```powershell
cd C:\fh2_1\mods\fh2\python\admin
python -c "import settings; print(settings.get_admin_level('[KKCK] Chaziz')); print(settings.get_admin_level('4a64aa3317f2bc80a2c7b8cbbb5c6908'))"
```

**Output:**

```
high
None
```

Matches expected: first line `high`, second line `None`.

## Additional verification

Loaded admin sets after TOML migration:

```powershell
python -c "import settings; print('ADMINS_HIGH:', settings.ADMINS_HIGH); print('ADMINS_MID:', settings.ADMINS_MID); print('ADMINS_LOW:', settings.ADMINS_LOW)"
```

**Output:**

```
ADMINS_HIGH: frozenset({'chaziz'})
ADMINS_MID: frozenset({'chaziz'})
ADMINS_LOW: frozenset({'chaziz'})
```

Name normalization (strip `[TAG]`, lowercase) works as designed from Task 1 wiring in Task 2.

Unit tests (unchanged, regression check):

```powershell
cd C:\fh2_1\mods\fh2\python\admin
python test_nameauth.py
```

**Output:** `Ran 13 tests in 0.000s` — **OK**

## Acceptance checklist

| Criterion | Result |
|-----------|--------|
| `admins.toml` lists contain player names, not hashes | OK |
| `get_admin_level('[KKCK] Chaziz')` returns `'high'` | OK |
| `get_admin_level('4a64aa3317f2bc80a2c7b8cbbb5c6908')` returns `None` | OK |
| No edits outside `python/admins.toml` | OK |
| No commit | OK |
| Hash-check runtime code untouched (Task 4) | OK |

## Concerns / follow-up

1. **Task 4 required:** Runtime permission checks that still compare CD-key hash against `ADMINS_*` must be patched to call `settings.get_admin_level(player_name)`. Until Task 4, in-game admin may not work even though TOML and `get_admin_level` are correct.
2. **Single admin entry:** All three tiers list the same name (`Chaziz`); `get_admin_level_by_name` priority (high > mid > low) returns `'high'` for that player. Adjust tiers independently if different levels are needed later.
3. **No git repo** at workspace root (`C:\fh2_1\mods\fh2`); change is local file edit only.

## Handoff to Task 4

- TOML is name-based; hash strings no longer grant admin via `get_admin_level`.
- Patch the live admin gate (wherever hash vs `ADMINS_*` is compared) to use `get_admin_level(player.getName())` or equivalent.
