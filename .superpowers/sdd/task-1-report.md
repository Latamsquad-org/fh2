# Task 1 Report: Helpers nameauth.py + tests

## What was implemented

Created pure helper functions for name-based admin matching under `python/admin/`:

| Function | Purpose |
|---|---|
| `strip_clan_tag(name)` | Removes leading `[TAG]` block and following spaces; returns name unchanged if no valid tag |
| `normalize_admin_name(name)` | Strips clan tag, trims whitespace, lowercases; `None`/empty -> `''` |
| `normalize_admin_list(entries)` | Returns `frozenset` of normalized non-empty names from a list |
| `get_admin_level_by_name(name, high, mid, low)` | Returns `'high'`, `'mid'`, `'low'`, or `None` (priority: high > mid > low) |

All comments and docstrings are ASCII-only for Python 2 safety.

### Deviation from brief Step 3

The brief's sample `normalize_admin_name` used `strip_clan_tag(str(name)).strip().lower()`, which fails `test_case_and_tag` for input `'  [KKCK] Chaziz  '` (leading spaces prevent tag detection). Fixed by stripping before tag removal:

```python
return strip_clan_tag(str(name).strip()).strip().lower()
```

This matches the test intent (normalize = strip tag + trim + lower) and is required for Step 4 "Expected: OK".

## What was tested and results

13 unit tests in `python/admin/test_nameauth.py` covering:

- Clan tag stripping (normal, symbols, no tag, unclosed bracket, empty)
- Name normalization (case + tag, accidental tag in TOML entry)
- List normalization (drop empties, normalize all)
- Level lookup (high priority, mid, low, none, hash-like string no match)

**Final result:** 13/13 passed on Python 3.14.6.

## TDD Evidence

### RED (tests before implementation)

```
Command: cd C:\fh2_1\mods\fh2\python\admin && python test_nameauth.py

Traceback (most recent call last):
  File "C:\fh2_1\mods\fh2\python\admin\test_nameauth.py", line 4, in <module>
    from nameauth import (
    ...<4 lines>...
    )
ModuleNotFoundError: No module named 'nameauth'
```

Exit code: 1

### GREEN (after implementation + normalize fix)

```
Command: cd C:\fh2_1\mods\fh2\python\admin && python test_nameauth.py -v

test_hash_like_string_does_not_match_name_list ... ok
test_high_wins ... ok
test_low ... ok
test_mid ... ok
test_none ... ok
test_case_and_tag ... ok
test_toml_entry_with_accidental_tag ... ok
test_drops_empty_and_normalizes ... ok
test_empty ... ok
test_no_tag_unchanged ... ok
test_strips_bracket_tag ... ok
test_strips_tag_with_symbols ... ok
test_unclosed_bracket_unchanged ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.000s

OK
```

Exit code: 0

## Files changed

| File | Action |
|---|---|
| `python/admin/nameauth.py` | Created |
| `python/admin/test_nameauth.py` | Created |

No other files modified. No commits made.

## Self-review findings

1. **Correctness:** All four public functions match the brief interfaces. Priority order in `get_admin_level_by_name` is high > mid > low. Hash-like strings do not match name lists (by design).
2. **ASCII compliance:** All `.py` strings and comments verified ASCII-only.
3. **No new dependencies:** Uses only stdlib (`frozenset`, `str` methods).
4. **Py2 compatibility (static):** Code uses Py2-safe patterns (`str(name)`, no f-strings, no Py3-only syntax). `frozenset` and `unittest` are available in Py2.7.
5. **Edge cases handled:** `None` input, empty strings, whitespace-only entries, unclosed brackets, tags with special chars (`[LP!]`).
6. **Scope:** Task 1 only; no wiring to `settings.toml` or hash check (deferred to later tasks).

## Issues / concerns

1. **Python 2.7 not available on build machine:** Tests ran on Python 3.14.6 only. `py -2` not found. Code is written for Py2.7 per project convention; recommend running tests on the BF2/Py2 runtime before deploy.
2. **Brief Step 3 typo:** Sample `normalize_admin_name` missing pre-strip would fail one test; fix applied as noted above.
3. **`strip_clan_tag` vs `normalize_admin_name` trim order:** Only `normalize_admin_name` trims leading whitespace before tag detection; raw `strip_clan_tag('  [X] Bob')` leaves spaces/tag intact. This is intentional per tests (strip_clan_tag is lower-level).
