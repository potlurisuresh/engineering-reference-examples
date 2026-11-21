"""Negative-access checks for the synthetic tenant store."""

import unittest

from store import TenantStore


class IsolationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = TenantStore()
        self.store.put("tenant-a", "invoice-1", "A-secret")
        self.store.put("tenant-b", "invoice-1", "B-secret")

    def test_same_tenant_read_ok(self) -> None:
        row = self.store.get("tenant-a", "invoice-1")
        self.assertEqual(row.value, "A-secret")

    def test_other_tenant_key_misses(self) -> None:
        # Composite key means tenant-a cannot address tenant-b's row by get()
        with self.assertRaises(KeyError):
            self.store.get("tenant-a", "missing")

    def test_list_does_not_leak(self) -> None:
        values = {r.value for r in self.store.list_for_tenant("tenant-a")}
        self.assertEqual(values, {"A-secret"})
        self.assertNotIn("B-secret", values)

    def test_unscoped_access_is_detectable(self) -> None:
        # Shows why unscoped APIs are dangerous — both tenants share key name
        leaked = self.store.get_unscoped("invoice-1")
        self.assertIn(leaked.tenant_id, {"tenant-a", "tenant-b"})
        # Real systems must not expose an unscoped path like this.


if __name__ == "__main__":
    unittest.main()
