# Synthetic multi-tenant isolation

**Goal:** show a tiny in-memory store where records are tagged by `tenant_id`, plus **negative-access** tests (tenant A must not read tenant B).

## Limits (read first)

- In-memory only — not a database product.
- No networking, auth server, or crypto.
- Passes unit tests locally; that is **not** production isolation proof.

## Run

```bash
python3 -m unittest test_isolation.py -v
```

## Idea

Every read/write path requires an explicit `tenant_id`. Cross-tenant reads raise `PermissionError`.
