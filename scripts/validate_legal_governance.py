#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any

ALLOWED_GATE_STATES = {"PASS", "TOKEN_VAZIO", "BLOCKED"}
REQUIRED_INVARIANTS = {
    "manifesto != recognized state",
    "hash != legal truth",
    "public access != public domain",
    "license != software registration",
    "MPLS != encryption",
    "allegation != finding",
    "belief != coercion",
    "metadata != harmless data",
}
REQUIRED_CARVE_OUTS = {
    "fraud", "intentional_misconduct", "death_or_personal_injury",
    "privacy_or_security_violation", "child_harm", "discrimination",
    "third_party_ip", "mandatory_law",
}

def validate(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if data.get("schema") != "haja_legal_governance_v1":
        errors.append("invalid schema")
    scope = data.get("scope", {})
    for field in ("claim_allowed", "legal_compliance_claim", "certification_claim", "recognized_state_claim"):
        if scope.get(field) is not False:
            errors.append(f"{field} must be false")
    layers = data.get("license_layers", [])
    layer_ids = [x.get("id") for x in layers]
    if len(layers) != 4 or len(set(layer_ids)) != 4:
        errors.append("license layers must contain four unique records")
    by_id = {x.get("id"): x for x in layers}
    if by_id.get("LIC-DOC", {}).get("license") != "CC-BY-NC-SA-4.0":
        errors.append("documentation license mismatch")
    if by_id.get("LIC-SW", {}).get("license") != "PolyForm-Noncommercial-1.0.0":
        errors.append("software license mismatch")
    invariants = set(data.get("invariants", []))
    missing_invariants = sorted(REQUIRED_INVARIANTS - invariants)
    if missing_invariants:
        errors.append("missing invariants: " + ", ".join(missing_invariants))
    gates = data.get("gates", [])
    ids = [x.get("id") for x in gates]
    if len(gates) != 20 or len(set(ids)) != 20:
        errors.append("must contain 20 unique gates")
    gate_map = {x.get("id"): x for x in gates}
    for gate in gates:
        if gate.get("state") not in ALLOWED_GATE_STATES:
            errors.append(f"invalid state for {gate.get('id')}")
        if gate.get("mandatory") is not True:
            errors.append(f"gate {gate.get('id')} must be mandatory")
    if gate_map.get("G20", {}).get("state") != "BLOCKED":
        errors.append("public claim gate must remain blocked")
    liability = data.get("liability_draft", {})
    if liability.get("status") != "NON_BINDING_DRAFT":
        errors.append("liability draft cannot be binding")
    try:
        cap = float(liability.get("ordinary_direct_damage_cap_usd_per_affected_licensed_device"))
        if cap != 1.0:
            errors.append("device cap must be 1.00 in this draft")
    except (TypeError, ValueError):
        errors.append("invalid device cap")
    missing_carveouts = sorted(REQUIRED_CARVE_OUTS - set(liability.get("carve_outs", [])))
    if missing_carveouts:
        errors.append("missing carve-outs: " + ", ".join(missing_carveouts))
    promotion = data.get("promotion", {})
    blocking = set(promotion.get("blocking_gate_ids", []))
    actual_blocking = {g["id"] for g in gates if g["state"] != "PASS"}
    if blocking != actual_blocking:
        errors.append("blocking gate list does not match gate states")
    if promotion.get("all_mandatory_gates_closed") is not False:
        errors.append("all_mandatory_gates_closed must be false")
    if promotion.get("public_claim_allowed") is not False:
        errors.append("public_claim_allowed must be false")
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "gate_count": len(gates),
        "pass_count": sum(g.get("state") == "PASS" for g in gates),
        "token_vazio_count": sum(g.get("state") == "TOKEN_VAZIO" for g in gates),
        "blocked_count": sum(g.get("state") == "BLOCKED" for g in gates),
        "claim_allowed": False,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", default="data/contracts/haja_legal_governance.v1.json")
    parser.add_argument("--write-report")
    args = parser.parse_args()
    data = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    report = validate(data)
    if args.write_report:
        Path(args.write_report).parent.mkdir(parents=True, exist_ok=True)
        Path(args.write_report).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
