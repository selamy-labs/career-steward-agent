from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from career_steward.policy import ApprovalRequest, exact_text_approved, privacy_errors, validate_external_action
from career_steward.validator import load_yaml


class PolicyEngineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = load_yaml(ROOT / "policies" / "approval-gates.yaml")

    def test_exact_text_approval_required(self) -> None:
        req = ApprovalRequest(
            channel="linkedin",
            recipient="Jordan",
            exact_text="Hi Jordan, thanks.",
            approval_text="Approved for linkedin to Jordan: Hi Jordan, thanks.",
            turn_id="sim-1",
        )
        self.assertTrue(exact_text_approved(req))
        bad = ApprovalRequest("linkedin", "Jordan", "Hi Jordan, thanks.", "Approved.", "sim-1")
        self.assertFalse(exact_text_approved(bad))

    def test_linkedin_connector_gates_sends(self) -> None:
        action = {
            "action": "send.linkedin-message",
            "channel": "linkedin",
            "recipient": "Jordan",
            "text": "Hi Jordan, thanks.",
            "approval": {"text": "Approved.", "turn_id": "sim-1"},
        }
        self.assertIn("missing exact-text approval", " ".join(validate_external_action(action, self.policy)))

    def test_whatsapp_send_forbidden(self) -> None:
        action = {
            "action": "send.whatsapp-message",
            "channel": "whatsapp",
            "recipient": "Group",
            "text": "Hello",
            "approval": {"text": "whatsapp Group Hello", "turn_id": "sim-1"},
        }
        errors = validate_external_action(action, self.policy)
        self.assertTrue(errors)

    def test_public_privacy_validation_blocks_pii(self) -> None:
        errors = privacy_errors("Email me at person@example.com and use /Users/name/private.txt")
        self.assertGreaterEqual(len(errors), 2)


if __name__ == "__main__":
    unittest.main()

