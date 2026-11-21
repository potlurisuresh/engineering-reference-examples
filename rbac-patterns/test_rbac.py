import unittest

from rbac import can, explain


class RbacTests(unittest.TestCase):
    def test_viewer_read_ok(self) -> None:
        self.assertTrue(can("viewer", "read", "doc"))

    def test_viewer_cannot_write(self) -> None:
        self.assertFalse(can("viewer", "write", "doc"))

    def test_editor_write_ok(self) -> None:
        self.assertTrue(can("editor", "write", "doc"))

    def test_editor_cannot_admin(self) -> None:
        self.assertFalse(can("editor", "admin", "tenant"))

    def test_unknown_role_denied(self) -> None:
        self.assertFalse(can("ghost", "read", "doc"))

    def test_explain_lists_viewer(self) -> None:
        self.assertIn("read:doc", list(explain("viewer")))


if __name__ == "__main__":
    unittest.main()
