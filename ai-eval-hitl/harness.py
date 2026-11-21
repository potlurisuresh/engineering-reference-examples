"""Synthetic propose → score → human-confirm harness."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List


@dataclass
class EvalCase:
    prompt: str
    expected_keywords: List[str]


@dataclass
class Proposal:
    text: str
    score: float
    human_approved: bool = False


def fake_model(prompt: str) -> str:
    # Deterministic stub — not an LLM
    return f"Draft answer about: {prompt}. Includes safety and review."


def score(text: str, expected_keywords: List[str]) -> float:
    if not expected_keywords:
        return 0.0
    hits = sum(1 for k in expected_keywords if k.lower() in text.lower())
    return hits / len(expected_keywords)


def run_case(case: EvalCase, require_human: bool, approve: Callable[[str], bool]) -> Proposal:
    text = fake_model(case.prompt)
    s = score(text, case.expected_keywords)
    approved = True
    if require_human:
        approved = approve(text)
    return Proposal(text=text, score=s, human_approved=approved)


def apply_if_allowed(proposal: Proposal, min_score: float = 0.5) -> str:
    if proposal.score < min_score:
        raise PermissionError("score below threshold")
    if not proposal.human_approved:
        raise PermissionError("human review required")
    return f"APPLIED: {proposal.text}"
