"""HAJA legal source boundary regression tests; not a legal certification."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOSSIER = ROOT / "docs/legal/HAJA_ESTADO_DIREITO_ILHA_DAS_ROSAS_V1.md"
POINTER = ROOT / "001_PONTEIRO/START_HERE.md"

class HajaRuleOfLawBoundaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dossier = DOSSIER.read_text(encoding="utf-8")
        cls.pointer = POINTER.read_text(encoding="utf-8")

    def test_legal_claims_stay_blocked(self):
        for token in ("CLAIM_ALLOWED=false", "recognized_state_claim=false", "counsel_review=TOKEN_VAZIO"):
            self.assertIn(token, self.dossier)
        self.assertIn("Estado reconhecido = false", self.pointer)

    def test_sources_and_adverse_limits_are_explicit(self):
        for token in ("INT-MONTEVIDEO-1933", "INT-UNCLOS-1982", "INT-ICJ-KOSOVO-2010",
                      "EU-ECHR-BESSARABIA-2001", "BR-STF-ADI6387-2020",
                      "INT-ROSAS-HIST-1968", "Limite adversarial", "TOKEN_VAZIO"):
            self.assertIn(token, self.dossier)

    def test_historical_license_is_not_accidentally_promoted(self):
        self.assertIn("LICENSE.md", self.dossier)
        self.assertIn("License.md", self.dossier)
        self.assertIn("histórico", self.pointer)
        self.assertIn("não validadas", self.pointer)

    def test_custody_and_router_are_explicit(self):
        self.assertIn("SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM", self.dossier)
        self.assertIn("SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM", self.pointer)
        self.assertIn("Rollback", self.pointer)
        self.assertIn("001_PONTEIRO/START_HERE.md", self.dossier)

if __name__ == "__main__":
    unittest.main()
