# Synthetic AI evaluation + human-in-the-loop review

**Goal:** show a tiny eval loop: model **proposes** → score against expectations → optional **human confirm** before “apply”.

## Limits

- No real LLM calls — proposals are fake strings.
- Scoring is keyword overlap — not a research benchmark.
- HITL is a boolean flag in-process — not a workflow product.

## Run

```bash
python3 -m unittest test_eval.py -v
```
