#!/usr/bin/env python3
import json, math, sys

def model(x):
    m=x["active_merchants"]
    q=m*x["eligible_quotes_per_merchant_month"]
    applications=q*x["application_rate"]
    approvals=applications*x["approval_rate"]
    funded=approvals*x["funding_rate"]
    volume=funded*x["average_financed_ticket"]
    transaction_revenue=volume*x["ballast_take_rate"]
    recurring=m*x.get("monthly_fee_per_merchant",0)
    revenue=transaction_revenue+recurring
    variable=volume*x.get("variable_cost_rate",0)+applications*x.get("variable_cost_per_application",0)
    contribution=revenue-variable
    fixed=x["fixed_monthly_cost"]
    operating=contribution-fixed
    contrib_per_merchant=contribution/m if m else 0
    be_merchants=math.ceil(fixed/contrib_per_merchant) if contrib_per_merchant>0 else None
    return {
      "eligible_quotes":q,"applications":applications,"approvals":approvals,"funded_transactions":funded,
      "financed_volume":volume,"transaction_revenue":transaction_revenue,"recurring_revenue":recurring,
      "total_revenue":revenue,"variable_cost":variable,"contribution":contribution,"fixed_cost":fixed,
      "monthly_operating_result":operating,"contribution_per_active_merchant":contrib_per_merchant,
      "approx_break_even_active_merchants":be_merchants
    }

def main(path):
    with open(path,encoding="utf-8") as f:x=json.load(f)
    print(json.dumps({k:(round(v,2) if isinstance(v,float) else v) for k,v in model(x).items()},ensure_ascii=False,indent=2))
if __name__=="__main__":
    if len(sys.argv)!=2:raise SystemExit("usage: unit_economics.py economics.json")
    main(sys.argv[1])
