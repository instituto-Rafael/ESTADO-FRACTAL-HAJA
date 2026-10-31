#!/usr/bin/env python3
"""HAJA international V2: deterministic offline evidence/authority gate; research only."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "governance/international/v2/source_registry.v2.json"
REVIEW = ROOT / "governance/international/v2/REVIEW_AND_FAILSAFE.md"
COUNTRIES = {"GB","FR","DE","CH","RU","IT","ES","CN","JP","IN","ID","KR",
             "BR","US","CA","MX","AR","CL","ZA","KE","NG","AU","NZ"}
ORGANIZATIONS = {"UN","OHCHR","UNESCO","UNICEF","ICRC","WHO","ILO","UNHCR",
                 "WIPO","ITU","UNEP","UNWOMEN"}
INSTRUMENTS = {"UDHR","ICCPR","ICESCR","CRC","UNESCO2005","BERNE",
               "GENEVA1949","IHR2024","ILO169","REFUGEE1951",
               "UNCLOS60_8","MONTEVIDEO1933"}
GATES = {f"G{i:02d}" for i in range(1,15)}
REGIONS = {"EU","AS","AM","AF","OC"}
SHA1 = re.compile(r"^[a-f0-9]{40}$")
ALLOWED_SOURCE = {"OFFICIAL_PAGE_OBSERVED","OFFICIAL_TRANSLATION_VERSIONED",
                  "OFFICIAL_NONAUTHORITATIVE_EN_TRANSLATION",
                  "OFFICIAL_LINK_IDENTIFIED","PORTAL_POINTER_ONLY"}
GAP = "TOKEN_VAZIO_NOT_ATTESTED"

def verify(d: object) -> list[str]:
    failures: list[str] = []
    def check(ok: bool, msg: str) -> None:
        if not ok:
            failures.append(msg)
    if not isinstance(d, dict):
        return ["INVALID_ROOT"]
    check(d.get("schema") == "haja.international.multidimensional.v2", "SCHEMA")
    check(d.get("source_repo") == "instituto-Rafael/ESTADO-FRACTAL-HAJA", "OWNER")
    check(d.get("source_base_commit") == "9f978bc71a912dc5f1920123e9dbf1d07167542c",
          "BASELINE")
    check(d.get("state") == "RESEARCH_SOURCE_ROUTING_ONLY", "RESEARCH_STATE")
    check(d.get("promotion") == "HOLD", "PROMOTION")
    for key in ("claim_allowed","legal_compliance_claim","sovereignty_claim",
                "independent_counsel_reviewed","automated_sanctions_allowed","release_allowed"):
        check(d.get(key) is False, "FALSE_CLAIM_" + key.upper())
    check(d.get("provider_enforcement") == GAP, "PROVIDER_ATTESTATION")
    auth = d.get("authority")
    if not isinstance(auth, dict) or auth.get("producer") != d.get("source_repo"):
        failures.append("PRODUCER_AUTHORITY")
    conflicts = d.get("source_conflicts")
    if not isinstance(conflicts, list) or {x.get("key") for x in conflicts if isinstance(x,dict)} != {
        "PRODUCTO_VISIBILITY","PRODUCTO_MERGES","LICENSE_CASE","NO_AGENTS"} or len(conflicts) != 4:
        failures.append("PREDECESSOR_CONFLICTS_MISSING")
    else:
        for c in conflicts:
            check(c.get("resolution") in {"STALE_SNAPSHOT_NOT_REWRITTEN",
                "DO_NOT_PROMOTE_HISTORIC_LICENSE","POINT_TO_EXISTING_README_AND_POLICY_AND_THIS_SUCCESSOR"},
                "CONFLICT_RESOLUTION_INVALID")
    countries = d.get("country_scope")
    if not isinstance(countries, list):
        failures.append("COUNTRIES_TYPE")
    else:
        ids = [x.get("id") for x in countries if isinstance(x, dict)]
        check(len(countries) == len(COUNTRIES) and set(ids) == COUNTRIES
              and len(ids) == len(set(ids)), "COUNTRIES_EXACT_SCOPE")
        region_values = {x.get("continent") for x in countries if isinstance(x,dict)}
        check(region_values == REGIONS, "FIVE_CONTINENTS")
        for x in countries:
            if not isinstance(x, dict):
                failures.append("INVALID_COUNTRY"); continue
            check(x.get("source_state") in ALLOWED_SOURCE, "COUNTRY_SOURCE_CLASS")
            check(x.get("legal_effect") == "TOKEN_VAZIO_NOT_REVIEWED"
                  and x.get("operational_nexus") == GAP
                  and x.get("local_counsel") == "TOKEN_VAZIO_NOT_ASSIGNED",
                  "FALSE_COUNTRY_REVIEW")
            check(str(x.get("source","")).startswith("https://")
                  and x.get("review_rule"), "COUNTRY_PROVENANCE")
    def scoped(section: str, expected: set[str]) -> list[dict]:
        records = d.get(section)
        if not isinstance(records, list):
            failures.append("INVALID_"+section.upper()); return []
        ids = [x.get("id") for x in records if isinstance(x,dict)]
        check(len(records) == len(expected) and len(ids) == len(set(ids))
              and set(ids) == expected, "SCOPE_"+section.upper())
        for x in records:
            if not isinstance(x,dict):
                failures.append("BAD_RECORD_"+section.upper())
        return [x for x in records if isinstance(x,dict)]
    orgs = scoped("organizations", ORGANIZATIONS)
    for o in orgs:
        check(o.get("endorsement") is False
              and bool(o.get("limit")) and str(o.get("source","")).startswith("https://"),
              "FALSE_INSTITUTION_ENDORSEMENT")
    ins = scoped("international_instruments", INSTRUMENTS)
    for i in ins:
        check(i.get("per_country_effect") == GAP
              and i.get("applicability") == "REQUIRES_NEXUS_AND_REVIEW"
              and bool(i.get("limitation")) and str(i.get("source","")).startswith("https://"),
              "FALSE_TREATY_APPLICABILITY")
    byid = {i.get("id"):i for i in ins}
    check(byid.get("UDHR",{}).get("kind") == "DECLARATION", "UDHR_NOT_TREATY")
    check(byid.get("GENEVA1949",{}).get("kind") == "IHL_TREATY", "IHL_WRONG_SCOPE")
    check(byid.get("IHR2024",{}).get("kind") == "HEALTH_REGULATIONS", "IHR_WRONG_SCOPE")
    gs = scoped("gates", GATES)
    for g in gs:
        check(g.get("priority") == ("P0" if g.get("id") in
              {"G01","G02","G03","G04","G05","G06"} else "P1"), "GATE_PRIORITY")
        check(g.get("state") == ("POLICY_DOCUMENTED" if g.get("id") == "G01" else GAP)
              and g.get("claim_promotion_effect") == "NONE"
              and g.get("owner") == "TOKEN_VAZIO_NOT_ASSIGNED"
              and bool(g.get("negative_case")) and bool(g.get("required_evidence")),
              "FALSE_GATE_CLOSURE")
    case = d.get("special_case")
    check(isinstance(case,dict) and case.get("id") == "ROSE_ISLAND_1968"
          and case.get("state") == "HISTORICAL_UNRECOGNIZED_MICRONATION_CASE"
          and "1982" in str(case.get("legal_limit", ""))
          and "1968" in str(case.get("legal_limit","")),
          "FALSE_RETROACTIVE_SOVEREIGNTY")
    rules = d.get("priority_rules")
    check(isinstance(rules,list) and len(rules) == 10 and
          "missing_hard_gate_blocks_promotion" in rules and
          "legal_hierarchy_is_not_superseded_by_virtual_governance" in rules,
          "RULES_DOWNGRADED")
    check(bool(d.get("rollback")) and bool(d.get("next")) and
          "HOLD" in d.get("promotion",""), "ROLLBACK_MISSING")
    return sorted(set(failures))

def main() -> int:
    try:
        data = json.loads(SOURCE.read_text(encoding="utf-8"),
                          object_pairs_hook=_reject_duplicate_keys)
        errors = verify(data)
        if not REVIEW.is_file():
            errors.append("MISSING_HUMAN_REVIEW")
        elif "SOURCE ≠ ARTEFATO ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM" not in REVIEW.read_text(encoding="utf-8"):
            errors.append("HUMAN_DOC_CLAIM_BOUNDARY")
    except (OSError, ValueError, UnicodeError, TypeError) as exc:
        errors = ["INPUT_ERROR_"+type(exc).__name__]
    print(json.dumps({"schema":"haja.international-gate.result.v2",
                      "status":"PASS_SCOPED_RESEARCH_ONLY" if not errors else "FAIL_CLOSED",
                      "errors":sorted(set(errors)),
                      "jurisdictional_counsel":"NOT_RUN",
                      "provider_security":GAP,
                      "live_legal_effect":GAP,
                      "claim_allowed":False,
                      "promotion":"HOLD"},ensure_ascii=False,sort_keys=True))
    return 0 if not errors else 1

def _reject_duplicate_keys(pairs):
    out = {}
    for k,v in pairs:
        if k in out:
            raise ValueError("duplicate JSON key")
        out[k] = v
    return out

if __name__ == "__main__":
    sys.exit(main())
