#!/usr/bin/env python3
import json, sys

WEIGHTS = {
    "ticket_need": .25,
    "class_ab_fit": .15,
    "scale": .15,
    "decision_access": .15,
    "financing_gap": .15,
    "operational_fit": .15,
}

def main(path):
    with open(path, encoding="utf-8") as f:
        x=json.load(f)
    s=x["scores"]
    score=sum(float(s[k])*w for k,w in WEIGHTS.items())
    ev=x.get("evidence",{})
    contact=ev.get("contact","UNKNOWN")
    if score >= 8 and contact in {"VERIFIED_PUBLIC","USER_PROVIDED"}: priority="A+"
    elif score >= 7: priority="A"
    elif score >= 5.5: priority="B"
    else: priority="C"
    print(json.dumps({"company":x["company"],"score_10":round(score,2),"priority":priority,"contact_evidence":contact},ensure_ascii=False,indent=2))
if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("usage: lead_score.py lead.json")
    main(sys.argv[1])
