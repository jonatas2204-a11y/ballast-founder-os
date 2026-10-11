#!/usr/bin/env python3
import argparse, csv

def main():
    p=argparse.ArgumentParser(description="Weighted decision matrix. CSV columns: option,<criteria...>; weights use criterion=weight.")
    p.add_argument("csv_path")
    p.add_argument("--weight", action="append", default=[])
    a=p.parse_args()
    weights={}
    for item in a.weight:
        k,v=item.split("=",1); weights[k]=float(v)
    with open(a.csv_path, newline="", encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    if not rows: raise SystemExit("empty CSV")
    criteria=[c for c in rows[0] if c!="option"]
    if not weights: weights={c:1/len(criteria) for c in criteria}
    denom=sum(weights.get(c,0) for c in criteria)
    if denom <= 0: raise SystemExit("weights must sum above zero")
    ranked=[]
    for r in rows:
        s=sum(float(r[c])*weights.get(c,0) for c in criteria)/denom
        ranked.append((s,r["option"]))
    for s,o in sorted(ranked, reverse=True): print(f"{s:.2f}\t{o}")
if __name__=="__main__": main()
