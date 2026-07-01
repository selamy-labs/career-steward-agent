#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from career_steward.reconciler import reconcile
from career_steward.validator import load_yaml, validate_repo


def main() -> int:
    result = validate_repo(ROOT)
    out_dir = ROOT / "generated" / "verify"
    generated = reconcile(ROOT, out_dir)
    summary = {
        "validation": result,
        "generated": {key: str(path.relative_to(ROOT)) for key, path in generated.items()},
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

