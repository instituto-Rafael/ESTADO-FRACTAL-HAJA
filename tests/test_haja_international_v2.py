"""Adversarial offline tests: structure PASS does not mean legal clearance."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_haja_international_v2 import SOURCE, _reject_duplicate_keys, verify

class HajaInternationalV2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = json.loads(SOURCE.read_text(encoding="utf-8"),
                                  object_pairs_hook=_reject_duplicate_keys)
    def falsify(self, mutate):
        d = copy.deepcopy(self.baseline)
        mutate(d)
        self.assertTrue(verify(d), "mutated unsupported assertion was accepted")
    def test_baseline_is_research_only(self):
        self.assertEqual(verify(self.baseline), [])
        self.assertFalse(self.baseline["claim_allowed"])
        self.assertEqual(self.baseline["promotion"], "HOLD")
    def test_sovereignty_promotion_rejected(self):
        self.falsify(lambda d:d.__setitem__("sovereignty_claim", True))
    def test_legal_compliance_promotion_rejected(self):
        self.falsify(lambda d:d.__setitem__("legal_compliance_claim", True))
    def test_release_promotion_rejected(self):
        self.falsify(lambda d:d.__setitem__("release_allowed", True))
    def test_fabricated_counsel_rejected(self):
        self.falsify(lambda d:d.__setitem__("independent_counsel_reviewed", True))
    def test_private_sanctions_rejected(self):
        self.falsify(lambda d:d.__setitem__("automated_sanctions_allowed", True))
    def test_provider_attestation_rejected(self):
        self.falsify(lambda d:d.__setitem__("provider_enforcement", "ENFORCED"))
    def test_no_forged_child_gate(self):
        self.falsify(lambda d:d["gates"][1].__setitem__("state","PASS"))
    def test_remove_p0_rejected(self):
        self.falsify(lambda d:d["gates"].pop(4))
    def test_p0_severity_downgrade_rejected(self):
        self.falsify(lambda d:d["gates"][2].__setitem__("priority","P3"))
    def test_nonhuman_owner_claim_rejected(self):
        self.falsify(lambda d:d["gates"][3].__setitem__("owner","ready"))
    def test_missing_country_rejected(self):
        self.falsify(lambda d:d["country_scope"].pop())
    def test_fake_country_legal_review_rejected(self):
        self.falsify(lambda d:d["country_scope"][0].__setitem__("legal_effect","CERTIFIED"))
    def test_fake_country_counsel_rejected(self):
        self.falsify(lambda d:d["country_scope"][12].__setitem__("local_counsel","APPROVED"))
    def test_duplicate_country_id_rejected(self):
        self.falsify(lambda d:d["country_scope"][1].__setitem__("id",d["country_scope"][0]["id"]))
    def test_not_all_continents_rejected(self):
        self.falsify(lambda d:d["country_scope"][-1].__setitem__("continent","EU"))
    def test_unsupported_country_source_rejected(self):
        self.falsify(lambda d:d["country_scope"][0].__setitem__("source_state","CONFORMITY_PROVED"))
    def test_untrusted_url_rejected(self):
        self.falsify(lambda d:d["country_scope"][0].__setitem__("source","http://invalid/"))
    def test_false_institution_endorsement_rejected(self):
        self.falsify(lambda d:d["organizations"][1].__setitem__("endorsement", True))
    def test_missing_institution_rejected(self):
        self.falsify(lambda d:d["organizations"].pop())
    def test_udhr_not_treaty_rejected(self):
        self.falsify(lambda d:d["international_instruments"][0].__setitem__("kind", "TREATY"))
    def test_wrong_ihl_rejected(self):
        self.falsify(lambda d:next(x for x in d["international_instruments"] if x["id"]=="GENEVA1949").__setitem__("kind","DIGITAL_CHARTER"))
    def test_false_country_ratification_rejected(self):
        self.falsify(lambda d:d["international_instruments"][2].__setitem__("per_country_effect","ALL_RATIFIED"))
    def test_rose_island_sovereignty_rejected(self):
        self.falsify(lambda d:d["special_case"].__setitem__("state","INDEPENDENT_STATE"))
    def test_loss_temporal_boundary_rejected(self):
        self.falsify(lambda d:d["special_case"].__setitem__("legal_limit","UNCLOS proves sovereign 1968"))
    def test_stale_producto_ignored_rejected(self):
        self.falsify(lambda d:d["source_conflicts"].pop(0))
    def test_case_sensitive_license_rewrite_rejected(self):
        self.falsify(lambda d:next(x for x in d["source_conflicts"] if x["key"]=="LICENSE_CASE").__setitem__("resolution","PROMOTE_HISTORIC_LICENSE"))
    def test_wrong_authority_rejected(self):
        self.falsify(lambda d:d["authority"].__setitem__("producer","rafaelmeloreisnovo/Mapa"))
    def test_missing_rollback_rejected(self):
        self.falsify(lambda d:d.__setitem__("rollback",""))
    def test_missing_core_rule_rejected(self):
        self.falsify(lambda d:d["priority_rules"].remove("legal_hierarchy_is_not_superseded_by_virtual_governance"))
    def test_duplicate_json_keys_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"id":"one","id":"two"}',object_pairs_hook=_reject_duplicate_keys)

if __name__=="__main__":
    unittest.main()
