from __future__ import annotations
import copy
import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_legal_governance import validate

BASE = json.loads((ROOT / "data/contracts/haja_legal_governance.v1.json").read_text(encoding="utf-8"))

class LegalGovernanceTests(unittest.TestCase):
    def test_valid_contract(self):
        self.assertEqual(validate(copy.deepcopy(BASE))["status"], "PASS")

    def test_recognized_state_claim_fails(self):
        data = copy.deepcopy(BASE)
        data["scope"]["recognized_state_claim"] = True
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_claim_allowed_fails(self):
        data = copy.deepcopy(BASE)
        data["scope"]["claim_allowed"] = True
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_document_license_fails_closed(self):
        data = copy.deepcopy(BASE)
        data["license_layers"][0]["license"] = "PROPRIETARY"
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_software_license_fails_closed(self):
        data = copy.deepcopy(BASE)
        data["license_layers"][1]["license"] = "UNKNOWN"
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_hash_truth_invariant_required(self):
        data = copy.deepcopy(BASE)
        data["invariants"].remove("hash != legal truth")
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_mpls_encryption_invariant_required(self):
        data = copy.deepcopy(BASE)
        data["invariants"].remove("MPLS != encryption")
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_public_claim_gate_cannot_pass(self):
        data = copy.deepcopy(BASE)
        next(g for g in data["gates"] if g["id"] == "G20")["state"] = "PASS"
        data["promotion"]["blocking_gate_ids"].remove("G20")
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_device_cap_cannot_drift(self):
        data = copy.deepcopy(BASE)
        data["liability_draft"]["ordinary_direct_damage_cap_usd_per_affected_licensed_device"] = "1000"
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_child_harm_carveout_required(self):
        data = copy.deepcopy(BASE)
        data["liability_draft"]["carve_outs"].remove("child_harm")
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_blocking_list_must_match(self):
        data = copy.deepcopy(BASE)
        data["promotion"]["blocking_gate_ids"] = ["G20"]
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_gate_count_fixed(self):
        data = copy.deepcopy(BASE)
        data["gates"].pop()
        self.assertEqual(validate(data)["status"], "FAIL")

if __name__ == "__main__":
    unittest.main()
