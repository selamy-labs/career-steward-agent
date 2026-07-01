from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from career_steward.validator import load_yaml


class WriteBoundaryTest(unittest.TestCase):
    def test_write_boundary_declared(self) -> None:
        manifest = load_yaml(ROOT / "agent.manifest.yaml")
        boundary = manifest["policies"]["writeBoundary"]
        self.assertEqual(boundary["liveRuntimeMutation"], "forbidden")
        self.assertFalse(boundary["repoOwnedFilesMutableInPod"])
        self.assertIn("/opt/data/**", manifest["runtime"]["state"]["mutableZones"])
        self.assertIn("/usr/local/bin/**", manifest["runtime"]["state"]["immutableZones"])


if __name__ == "__main__":
    unittest.main()

