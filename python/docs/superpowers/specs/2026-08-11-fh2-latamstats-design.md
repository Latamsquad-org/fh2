# FH2 latamstats - diseno

## Objetivo
Subir estadisticas de Forgotten Hope 2 a `https://stats.latamsquad.org/fh2.php` sin mezclarlas con Project Reality.

## Decisiones
- Archivo: `mods/fh2/python/latamstats.py`
- Arranque: `import latamstats` en `game/__init__.py` (solo en servidor BF2)
- SQLite: `C:/fh2_db/stats.sqlite3` (tablas stats1..stats4, schema igual a PR)
- server_id: `latamsquad-1` -> tabla `stats1`
- Upload URL: `https://stats.latamsquad.org/fh2.php`
- API: mismo JSON y misma X-API-Key que PR
- GeoIP/log: `C:/fh2_db/geo_ip.bin`, `C:/fh2_db/latamstats_upload.log`
- ID jugador: CD-key hash (32 hex) via `admin.listplayers`
- Comando chat: `!stats` con cooldown
- Sin dependencias de reality*, latamtreasures ni latamassetban (fallback seguro)

## Flujo
1. Snapshot en memoria en disconnect
2. En EndGame: merge con jugadores conectados, upsert SQLite, POST a fh2.php
3. `!stats` lee SQLite local y responde por PM
