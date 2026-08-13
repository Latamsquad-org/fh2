# FH2 latamstats Implementation Plan

> **For agentic workers:** implement task-by-task.

**Goal:** Port PR latamstats to FH2 with separate DB and upload endpoint.

**Architecture:** Adapt PR module: FH2 CD-key hash, bf2.playerManager, host PM/handlers; keep SQLite/upload/GeoIP helpers.

**Tech Stack:** Python 2.7 (BF2), sqlite3, urllib2/curl, host/bf2 bindings.

## Global Constraints
- ASCII-safe comments/strings where possible; `# -*- coding: utf-8 -*-` if needed
- No new third-party deps
- Paths under `C:/fh2_db`
- Upload only to `/fh2.php`

### Task 1: Create latamstats.py
- Create: `C:/fh2_1/mods/fh2/python/latamstats.py`
- Adapt player ID, getPlayers, PM, config paths/URL
- [ ] Implement module
- [ ] Smoke-test offline helpers (schema, payload, geoip)

### Task 2: Wire import
- Modify: `game/__init__.py`
- [ ] `import latamstats` when `is_bf2`
- [ ] Verify syntax
