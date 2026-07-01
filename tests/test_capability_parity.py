from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from career_steward.validator import load_yaml


class CapabilityParityTest(unittest.TestCase):
    def test_every_capability_has_surface_and_test(self) -> None:
        inventory = load_yaml(ROOT / "docs" / "capability-parity-inventory.yaml")
        capabilities = inventory["capabilities"]
        self.assertGreaterEqual(len(capabilities), 12)
        for capability in capabilities:
            self.assertTrue(capability["currentCapability"])
            self.assertTrue(capability["declarativeSurface"])
            self.assertTrue(capability["test"])
            self.assertTrue((ROOT / "tests" / capability["testFile"]).exists())


if __name__ == "__main__":
    unittest.main()

