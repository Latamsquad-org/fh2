# Design: Admin por nombre de jugador (sin hash)

Fecha: 2026-07-24  
Estado: aprobado; plan en docs/superpowers/plans/2026-07-24-admin-by-name.md

## Objetivo

Reemplazar la autenticacion de admin por hash de CD key en `admins.toml` por autenticacion **solo por nombre de jugador**, manteniendo archivos TOML y los tres niveles existentes (`high` / `mid` / `low`).

## Contexto actual (verificado en el workspace)

- `python/admins.toml` define `admins_high`, `admins_mid`, `admins_low` como listas de hashes.
- `python/admin/settings.py` carga esas listas en `ADMINS_HIGH` / `ADMINS_MID` / `ADMINS_LOW`.
- En este arbol, el codigo que compara el hash del jugador al conectar no aparece como `.py` fuera de `settings.py` (el resto del paquete admin no esta visible aqui).
- Los logs de chat registran conectes del estilo: `Player [KKCK] Chaziz with Hash <hash>`.

## Decisiones acordadas

| Tema | Decision |
|------|----------|
| Criterio de auth | Solo nombre (los hashes dejan de dar admin) |
| Niveles | Se mantienen `high` / `mid` / `low` |
| Archivo | Se reutiliza `admins.toml` (enfoque 1) |
| Match | Quitar tag de clan `[TAG]` al inicio; el resto del nombre debe coincidir completo con la entrada del TOML |
| Case | Comparacion case-insensitive |
| Seguridad | Spoofing de nick aceptado a proposito |

## Formato TOML

```toml
[users]
admins_high = ['Chaziz']
admins_mid = ['Chaziz']
admins_low = ['OtroJugador']
```

- Cada entrada es el nombre **sin** tag de clan.
- Ejemplo: jugador `[KKCK] Chaziz` -> se compara contra `Chaziz`.

## Arquitectura

### Componentes

1. **`admins.toml`** - Fuente de verdad de nombres por nivel.
2. **`settings.py`** - Carga y normaliza listas al arrancar el mod/admin.
3. **Helper de match** (nuevo o en modulo admin existente) - Funciones:
   - `strip_clan_tag(name) -> str`
   - `normalize_admin_name(name) -> str` (strip tag + trim + lower)
   - `get_admin_level_by_name(name) -> 'high'|'mid'|'low'|None`
4. **Punto de chequeo** - El mismo lugar que hoy valida hash contra `ADMINS_*`. Si ese codigo no esta en fuente visible, enganche minimo en connect que use el helper.

### Flujo

```
Connect / check admin
  -> nombre del jugador
  -> normalize_admin_name()
  -> buscar en ADMINS_HIGH, luego MID, luego LOW (prioridad high > mid > low)
  -> asignar nivel o None
```

### Normalizacion de tag

- Si el nombre empieza con `[` y hay un `]` posterior, se elimina solo el primer bloque `[...]` al inicio y los espacios siguientes.
- Si no hay un `[...]` valido al inicio, se usa el nombre entero (tras trim).
- Cada entrada del TOML se normaliza con la misma funcion (strip tag + trim + lower), por si alguien pega el nick con tag por error.

## Casos borde

| Caso | Comportamiento |
|------|----------------|
| TOML ausente o invalido | Listas vacias; nadie admin por TOML |
| Entrada vacia / solo espacios | Ignorar al cargar |
| Sin tag | Comparar nombre completo normalizado |
| Con tag | Quitar tag; comparar resto |
| Nombre en high y mid | Gana high |
| Hash antiguo en el TOML | No da admin; limpiar al migrar |
| Cambio de nick mid-round | Se reevalua cuando el sistema ya chequea admin |

## Fuera de alcance

- Auth por IP, password o segundo factor.
- Watcher continuo de renombres (salvo que el admin actual ya lo haga).
- Mantener compatibilidad dual hash+nombre.

## Prueba smoke

1. Poner el nick sin tag en `admins_high`.
2. Entrar al servidor y ejecutar un comando de nivel high.
3. Quitar el nombre del TOML (o cambiar nick) y verificar que el comando deja de funcionar.

## Riesgos

- **Spoofing de nombre:** cualquier jugador puede adoptar el nick listado.
- **Paquete admin incompleto en el workspace:** puede hacer falta localizar o recrear el punto de chequeo que hoy usa el hash.

## Criterio de exito

Un jugador cuyo nombre (sin tag de clan) figura en `admins_high` / `mid` / `low` obtiene ese nivel de admin sin necesidad de hash en el TOML.
