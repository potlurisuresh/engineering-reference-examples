"""Minimal RBAC helper (synthetic)."""

from __future__ import annotations

from typing import Dict, FrozenSet, Iterable

# role -> permissions (action:resource). "*" resource means any of that action.
ROLE_PERMISSIONS: Dict[str, FrozenSet[str]] = {
    "viewer": frozenset({"read:doc", "list:doc"}),
    "editor": frozenset({"read:doc", "list:doc", "write:doc"}),
    "admin": frozenset({"read:doc", "list:doc", "write:doc", "admin:tenant"}),
}


def can(role: str, action: str, resource: str) -> bool:
    perms = ROLE_PERMISSIONS.get(role, frozenset())
    exact = f"{action}:{resource}"
    any_res = f"{action}:*"
    return exact in perms or any_res in perms


def explain(role: str) -> Iterable[str]:
    return sorted(ROLE_PERMISSIONS.get(role, frozenset()))
