# ADR-001: Require tenant id on every data access path

- **Status:** Accepted (synthetic example)
- **Date:** 2026-11-21

## Context

Multi-tenant systems fail when a shared “get by id” path forgets tenancy.

## Decision

Every read/write API takes an explicit `tenant_id`. Composite keys include tenant. Unscoped helpers are forbidden in production code paths.

## Consequences

- Slightly more verbose call sites  
- Negative tests become straightforward  
- Accidental cross-tenant reads surface as missing keys or hard errors  
