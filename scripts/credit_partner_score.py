#!/usr/bin/env python3
import json, sys

WEIGHTS = {
    "architecture_fit": 0.16,
    "funding_fit": 0.13,
    "risk_fit": 0.13,
    "product_fit": 0.09,
    "integration_fit": 0.10,
    "commercial_fit": 0.10,
    "regulatory_fit": 0.12,
    "servicing_fit": 0.07,
    "data_fit": 0.05,
    "pilot_fit": 0.05,
}
HARD_GATES = [
    "supports_multilayer_distribution",
    "funding_source_confirmed",
    "credit_risk_owner_confirmed",
    "servicing_owner_confirmed",
    "regulatory_roles_confirmed",
]
CLOSED = {"VERIFIED_PUBLIC", "USER_PROVIDED"}

def main(path):
    with open(path, encoding="utf-8") as f:
        x = json.load(f)
    scores = x.get("scores", {})
    total = sum(float(scores.get(k, 0)) * w for k, w in WEIGHTS.items())
    gates = x.get("gates", {})
    unresolved = [g for g in HARD_GATES if gates.get(g, "UNKNOWN") not in CLOSED]
    if unresolved:
        verdict = "INSUFFICIENT EVIDENCE"
    elif total >= 8:
        verdict = "PRIORITY PARTNER"
    elif total >= 6.5:
        verdict = "QUALIFIED"
    else:
        verdict = "LOW PRIORITY"
    print(json.dumps({
        "partner": x.get("name"),
        "score_10": round(total, 2),
        "verdict": verdict,
        "unresolved_hard_gates": unresolved,
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: credit_partner_score.py partner.json")
    main(sys.argv[1])
