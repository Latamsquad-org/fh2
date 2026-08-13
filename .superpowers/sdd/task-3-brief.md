# Task 3 brief: Migrate admins.toml to names

## Global Constraints (binding)

- Solo ASCII en comentarios/strings de `.py` del admin.
- Auth solo por nombre; hashes en TOML no dan admin.
- Match: quitar primer `[TAG]` al inicio; resto completo; case-insensitive.
- Tres niveles: `admins_high` / `admins_mid` / `admins_low` en `python/admins.toml`.
- No anadir dependencias nuevas.
- No hacer commit salvo pedido explicito del usuario.

## Task 3: Migrate `admins.toml` to names

**Files:**
- Modify: `python/admins.toml`

**Interfaces:**
- Produces: TOML lists of player names without required clan tag

### Step 1: Replace hash entries with names

Set contents to (example from design/logs — Chaziz was the previous hash owner):

```toml
[users]
admins_high = ['Chaziz']
admins_mid = ['Chaziz']
admins_low = ['Chaziz']
```

Do not leave 32-char hex hashes in these lists.

### Step 2: Verify settings resolves the example name

```bash
cd python/admin
python -c "import settings; print(settings.get_admin_level('[KKCK] Chaziz')); print(settings.get_admin_level('4a64aa3317f2bc80a2c7b8cbbb5c6908'))"
```

Expected first line: `high`
Expected second line: `None`

Do NOT commit. Do NOT patch hash check (Task 4).
