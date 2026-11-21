# ADR-002: Human confirm before mutating AI actions

- **Status:** Accepted (synthetic example)
- **Date:** 2026-11-21

## Context

LLM output is probabilistic. Silent writes create irreversible mistakes.

## Decision

Mutating tools run in **propose → review → execute** mode. Below-threshold or unapproved proposals do not apply.

## Consequences

- Latency and operator load increase  
- Auditability improves  
- Demo “full autonomy” claims are avoided unless a separate product decision says otherwise  
