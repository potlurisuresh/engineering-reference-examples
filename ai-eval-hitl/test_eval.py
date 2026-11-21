import unittest

from harness import EvalCase, apply_if_allowed, run_case


class EvalTests(unittest.TestCase):
    def test_scores_and_applies_with_human_ok(self) -> None:
        case = EvalCase(prompt="tenant isolation", expected_keywords=["safety", "review"])
        proposal = run_case(case, require_human=True, approve=lambda _t: True)
        self.assertGreaterEqual(proposal.score, 0.5)
        out = apply_if_allowed(proposal)
        self.assertTrue(out.startswith("APPLIED:"))

    def test_blocks_without_human(self) -> None:
        case = EvalCase(prompt="rbac", expected_keywords=["safety"])
        proposal = run_case(case, require_human=True, approve=lambda _t: False)
        with self.assertRaises(PermissionError):
            apply_if_allowed(proposal)


if __name__ == "__main__":
    unittest.main()
