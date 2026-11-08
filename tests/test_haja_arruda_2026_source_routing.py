"""Regression gates: correct user's year to 2026 without rewriting legitimate 2025 metadata."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
V1 = ROOT / "docs/research/HENRIQUE_FERRAZ_DE_ARRUDA_REDES_COMPLEXAS_2025_V1.md"
V2 = ROOT / "docs/research/HENRIQUE_FERRAZ_DE_ARRUDA_REDES_COMPLEXAS_2026_V2.md"
ROUTER = ROOT / "001_PONTEIRO/START_HERE.md"
LEGAL = ROOT / "docs/legal/HAJA_ESTADO_DIREITO_ILHA_DAS_ROSAS_V1.md"

class HajaArruda2026SourceCorrectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v1 = V1.read_text(encoding="utf-8")
        cls.v2 = V2.read_text(encoding="utf-8")
        cls.router = ROUTER.read_text(encoding="utf-8")
        cls.legal = LEGAL.read_text(encoding="utf-8")

    def test_2026_article_title_and_doi(self):
        self.assertIn("Mechanistic interplay between information spreading and opinion polarization", self.v2)
        self.assertIn("10.1093/pnasnexus/pgaf402", self.v2)
        self.assertIn("2026", self.v2)

    def test_online_first_date_not_conflated(self):
        self.assertIn("30/12/2025", self.v2)
        self.assertIn("janeiro de 2026", self.v2)

    def test_2025_preserved_as_historical_source(self):
        self.assertIn("2025", self.v1)
        self.assertIn("HENRIQUE_FERRAZ_DE_ARRUDA_REDES_COMPLEXAS_2026_V2.md", self.v1)
        self.assertIn("supersede", self.v2.lower())

    def test_canonical_router_uses_2026(self):
        self.assertIn("HENRIQUE_FERRAZ_DE_ARRUDA_REDES_COMPLEXAS_2026_V2.md", self.router)
        self.assertIn("2026", self.router)
        self.assertIn("HENRIQUE_FERRAZ_DE_ARRUDA_REDES_COMPLEXAS_2025_V1.md", self.router)

    def test_legal_dossier_uses_2026_not_2025_as_target(self):
        self.assertIn("HENRIQUE_FERRAZ_DE_ARRUDA_REDES_COMPLEXAS_2026_V2.md", self.legal)
        self.assertIn("não é doutrina jurídica", self.legal.lower())
        self.assertIn("TOKEN_VAZIO_TITULO_EXATO", self.legal)

    def test_no_unverified_legal_promotion(self):
        self.assertIn("claim_allowed=false", self.v2)
        self.assertIn("TOKEN_VAZIO_TITULO_EXATO", self.v2)
        self.assertIn("claim_allowed=false", self.legal)

if __name__ == "__main__":
    unittest.main()
