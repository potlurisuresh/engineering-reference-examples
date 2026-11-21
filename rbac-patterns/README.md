# RBAC / permission patterns (synthetic)

**Goal:** tiny role → permission map and a `can(role, action, resource)` check.

## Limits

- Static roles only (`viewer`, `editor`, `admin`).
- No groups, ABAC, SSO, or audit log.
- Resource matching is string equality / simple prefix — not a security product.

## Run

```bash
python3 -m unittest test_rbac.py -v
```
