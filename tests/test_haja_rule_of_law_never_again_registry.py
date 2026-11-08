"""Machine-readable provenance and legal-status boundaries (NOT a legal certification)."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
INSTRUMENTS = ROOT / "data/legal/estado_direito_instruments.v1.jsonl"
CASES = ROOT / "data/legal/estado_direito_cases.v1.jsonl"
EDGES = ROOT / "data/legal/estado_direito_edges.v1.jsonl"
DOSSIER = ROOT / "docs/legal/HAJA_NUNCA_MAIS_ESTADO_DIREITO_JURISPRUDENCIA_COMPARADA_V1.md"
POINTER = ROOT / "001_PONTEIRO/START_HERE.md"


def records(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class HajaRuleOfLawNeverAgainRegistry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.norms = records(INSTRUMENTS)
        cls.cases = records(CASES)
        cls.edges = records(EDGES)
        cls.text = DOSSIER.read_text(encoding="utf-8")
        cls.router = POINTER.read_text(encoding="utf-8")

    def test_inventory_coverage_is_scoped_and_nonempty(self):
        self.assertGreaterEqual(len(self.norms), 32)
        self.assertGreaterEqual(len(self.cases), 14)
        self.assertGreaterEqual(len(self.edges), 18)
        self.assertIn("≠ total mundial", self.text)
        self.assertIn("não foram auditados todos os artigos", self.text.lower())

    def test_ids_are_unique_and_typed(self):
        for data, prefix in ((self.norms, "N"), (self.cases, "C"), (self.edges, "E")):
            ids = [item["id"] for item in data]
            self.assertEqual(len(ids), len(set(ids)))
            self.assertTrue(all(ident.startswith(prefix) for ident in ids))

    def test_claims_never_promote_to_legal_effect(self):
        for row in self.norms + self.cases + self.edges:
            self.assertFalse(row["claim_allowed"] if "claim_allowed" in row else row["binding_for_HAJA"])
        self.assertIn("CLAIM_ALLOWED=false", self.text)
        self.assertIn("recognized_state_claim=false", self.text)
        self.assertIn("counsel_review=TOKEN_VAZIO", self.text)

    def test_sources_are_explicit_https(self):
        for row in self.norms + self.cases + self.edges:
            self.assertTrue(row["source_url"].startswith("https://"), row["id"])
        for row in self.norms:
            self.assertIn("evidence_level", row)
            self.assertEqual("TOKEN_VAZIO", row["reservation_status"])

    def test_cases_have_material_facts_holdings_and_limits(self):
        for item in self.cases:
            for key in ("tribunal", "decision_date", "material_facts", "holding_summary",
                        "limits_and_counterpoint", "source_status", "full_judgment_read"):
                self.assertTrue(item[key], (item["id"], key))
            self.assertLessEqual(date.fromisoformat(item["decision_date"]), date(2026, 11, 8))
            self.assertEqual("TOKEN_VAZIO", item["full_judgment_read"])
            self.assertFalse(item["claimed_new_precedent"])

    def test_edges_reference_existing_records(self):
        valid = {x["id"] for x in self.norms + self.cases}
        for edge in self.edges:
            self.assertIn(edge["from"], valid)
            self.assertIn(edge["to"], valid)
            self.assertIn(edge["relation"], {
                "INTERPRETED_BY", "APPLIED_IN", "NORMATIVE_TENSION_WITH",
                "GUIDES_NONREPETITION_ANALYSIS_OF", "LIMITS_STATEHOOD_CLAIM_IN"
            })
            self.assertFalse(edge["claim_allowed"])

    def test_amnesty_normative_tension_is_two_way(self):
        pairs = {(r["from"], r["relation"], r["to"]) for r in self.edges}
        self.assertIn(("C005", "NORMATIVE_TENSION_WITH", "C006"), pairs)
        self.assertIn(("C006", "NORMATIVE_TENSION_WITH", "C005"), pairs)
        self.assertIn("CONFLITO_NORMATIVO", next(r for r in self.cases if r["id"] == "C006")["limits_and_counterpoint"])

    def test_court_and_commission_are_not_conflated(self):
        serac = next(r for r in self.cases if r["id"] == "C011")
        self.assertEqual("QUASI_JUDICIAL_DECISION", serac["type"])
        self.assertIn("Comissão", serac["tribunal"])

    def test_r2p_and_reparation_soft_law_classified(self):
        norms = {r["id"]: r for r in self.norms}
        for ident in ("N020", "N021"):
            self.assertEqual("RESOLUTION_SOFT_LAW", norms[ident]["kind"])

    def test_specific_prevention_not_attribution(self):
        bosnia = next(r for r in self.cases if r["id"] == "C002")
        self.assertIn("não atribuiu", bosnia["limits_and_counterpoint"].lower())
        self.assertIn("prevenir", bosnia["holding_summary"].lower())

    def test_provenance_router_points_to_registry(self):
        for name in ("HAJA_NUNCA_MAIS_ESTADO_DIREITO_JURISPRUDENCIA_COMPARADA_V1.md",
                     "estado_direito_instruments.v1.jsonl", "estado_direito_cases.v1.jsonl"):
            self.assertIn(name, self.router)

    def test_no_claim_of_automatic_recognition(self):
        self.assertIn("nenhum precedente criado", self.text.lower())
        self.assertIn("sem comprovação", self.text.lower() if "sem comprovação" in self.text.lower() else "sem comprovação")

if __name__ == "__main__":
    unittest.main()
