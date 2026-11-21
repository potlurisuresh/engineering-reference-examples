"""Minimal tenant-scoped store (synthetic teaching example)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Record:
    tenant_id: str
    key: str
    value: str


class TenantStore:
    def __init__(self) -> None:
        self._rows: Dict[tuple[str, str], Record] = {}

    def put(self, tenant_id: str, key: str, value: str) -> None:
        if not tenant_id:
            raise ValueError("tenant_id required")
        self._rows[(tenant_id, key)] = Record(tenant_id, key, value)

    def get(self, tenant_id: str, key: str) -> Record:
        row = self._rows.get((tenant_id, key))
        if row is None:
            raise KeyError(key)
        if row.tenant_id != tenant_id:
            # Defensive: should be unreachable with composite keys
            raise PermissionError("cross-tenant access denied")
        return row

    def list_for_tenant(self, tenant_id: str) -> List[Record]:
        return [r for (t, _), r in self._rows.items() if t == tenant_id]

    def get_unscoped(self, key: str) -> Record:
        """Intentionally unsafe helper — used only to demonstrate a negative test."""
        for (t, k), row in self._rows.items():
            if k == key:
                return row
        raise KeyError(key)
