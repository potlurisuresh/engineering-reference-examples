# CI / release quality gates (example)

**Goal:** document a minimal gate set and show a sample GitHub Actions workflow.

## Suggested gates

1. **Lint / format** — style consistency  
2. **Unit tests** — must pass on every PR  
3. **Secrets scan** — block known key patterns (tooling choice is yours)  
4. **Tagged release** — publish only from `main` + tag  
5. **Rollback note** — previous tag remains deployable

## Limits

- Workflow file is a **template**, not your production pipeline.
- No deployment credentials included.
- Rollback is procedural (redeploy previous artifact), not automated here.

See [`.github/workflows/reference-ci.yml`](../.github/workflows/reference-ci.yml).
