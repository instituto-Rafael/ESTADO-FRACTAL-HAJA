#!/usr/bin/env python3
"""Emit a HEAD-bound receipt for the HAJA legal-governance software gate.

This is a software/governance contract receipt, not a legal opinion,
certification, recognized-state claim, or authorization to make public claims.
"""
from __future__ import annotations

import hashlib
import json
import os
import platform
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "reproducibility" / "haja-governance-core-receipt.json"
REPORT = ROOT / "artifacts" / "reproducibility" / "governance-report.json"
INPUTS = (
    ".github/workflows/reproducible-governance-core.yml",
    "scripts/validate_legal_governance.py",
    "scripts/write_governance_repro_receipt.py",
    "tests/test_legal_governance.py",
    "data/contracts/haja_legal_governance.v1.json",
    "LICENSE.md",
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    return value or "TOKEN_VAZIO"


def main() -> int:
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    inputs = {rel: {"sha256": sha256(ROOT / rel), "bytes": (ROOT / rel).stat().st_size} for rel in INPUTS}
    payload = {
        "schema": "rafaelia.haja-governance-repro-receipt/v1",
        "repository": env("GITHUB_REPOSITORY"),
        "head_sha": env("GITHUB_SHA"),
        "ref": env("GITHUB_REF"),
        "run_id": env("GITHUB_RUN_ID"),
        "run_attempt": env("GITHUB_RUN_ATTEMPT"),
        "execution_scope": "HAJA legal-governance JSON contract validator plus stdlib negative/positive unit tests",
        "container": env("REPRO_CONTAINER_IMAGE"),
        "actions": {
            "checkout_commit": env("REPRO_CHECKOUT_SHA"),
            "upload_artifact_commit": env("REPRO_UPLOAD_ARTIFACT_SHA"),
        },
        "runtime": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "machine": platform.machine(),
        },
        "gate_outcomes": {
            "py_compile": env("GATE_COMPILE"),
            "contract_validation": env("GATE_CONTRACT"),
            "unit_tests": env("GATE_TESTS"),
        },
        "contract_report": report,
        "contract_report_sha256": sha256(REPORT),
        "inputs": inputs,
        "legal_opinion": False,
        "legal_certification": False,
        "recognized_state_claim": False,
        "claim_allowed": False,
        "boundary": "This receipt proves deterministic software validation of the repository's governance contract and negative tests. It is not legal advice, legal compliance certification, recognition by a state, or permission to elevate draft legal language into binding law.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    payload["canonical_payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"receipt={OUT}")
    print(f"payload_sha256={payload['canonical_payload_sha256']}")
    print(f"contract_status={report.get('status', 'TOKEN_VAZIO')}")
    print(f"claim_allowed={str(payload['claim_allowed']).lower()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
