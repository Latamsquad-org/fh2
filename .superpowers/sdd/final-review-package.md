# Final whole-branch review package (uncommitted)

## Feature
Admin by player name (no CD-key hash) for FH2 server admin TOML lists.

## Spec
docs/superpowers/specs/2026-07-24-admin-by-name-design.md

## Plan
docs/superpowers/plans/2026-07-24-admin-by-name.md

## Progress ledger minors/importants to triage
- Task 1: no explicit None test for normalize_admin_name; Py2.7 not on build machine
- Task 2: (resolved by Task 3) interim hashes
- Task 4: full uncompyle6 of bf2_tools.py; no in-game smoke; Py2 print not parseable on Py3

## Files changed (working tree)
- CREATE python/admin/nameauth.py
- CREATE python/admin/test_nameauth.py
- MODIFY python/admin/settings.py (normalize lists + get_admin_level)
- MODIFY python/admins.toml (names not hashes)
- CREATE python/admin/bf2_tools.py (decompiled from .pyc + admin_level patch; module-level return removed)
- REMOVED python/admin/bf2_tools.pyc (backup: .superpowers/sdd/bf2_tools.pyc.bak)

## Key behavior
- admins.toml lists names per high/mid/low
- strip leading [TAG], case-insensitive full match on remainder
- FH2Player.admin_level -> get_admin_level(self.name)
- Offline: 13/13 nameauth tests OK; Chaziz with tag resolves high; old hash resolves None
