---
name: ballast-economics
description: Model Ballast transaction, merchant and company unit economics for embedded credit with traceable inputs and scenario sensitivity.
---
# Ballast Economics

## Separate four economic layers
1. End borrower economics — principal, rate/CET, term and repayment.
2. Merchant economics — sale value, financing subsidy/fee, incremental contribution, cancellations/refunds.
3. Financial partner economics — only when known; never infer lender margin from borrower rate alone.
4. Ballast economics — transaction take rate, merchant SaaS/fee, integration fees, variable processing costs and fixed operating costs.

## Funnel model
At minimum model:

`active merchants × eligible quotes × application rate × approval rate × funding rate × financed ticket`

Then calculate financed volume and Ballast revenue from explicit commercial assumptions.

Use `scripts/unit_economics.py` for deterministic calculations when inputs exist.

## Sensitivity
Test the decision against approval, application, funded ticket, take rate, merchant activation, variable costs and fixed cost. Identify the top two elastic assumptions.

## Rules
Every input has evidence state. Never insert market-standard approval rates or take rates as facts. Scenarios are allowed only when labelled assumptions.

## Output
Base / downside / upside, break-even, contribution per active merchant, required merchant scale, unknown inputs and experiments that can replace assumptions with evidence.
