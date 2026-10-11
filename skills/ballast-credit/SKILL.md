---
name: ballast-credit
description: Design or evaluate Ballast's B2B2C embedded-credit architecture, including funding, origination, underwriting, product, white label, servicing, collections, compliance, LGPD and operational responsibilities.
---
# Ballast Credit

## First draw the flow
Always map:

`consumer → merchant → Ballast → financial partner → funding vehicle / balance sheet`

Then identify who owns each action:
- eligibility/prequalification;
- KYC/KYB and fraud;
- underwriting;
- offer generation;
- CET/rate disclosure;
- contracting;
- disbursement;
- repayment;
- servicing;
- collections/renegotiation;
- complaints;
- data processing;
- reporting and reconciliation.

## Evaluate the model
Cover:
1. credit product and permitted use;
2. ticket and tenor suitability;
3. funding source and capacity;
4. credit-risk allocation and recourse;
5. regulated originator/creditor;
6. Ballast and merchant legal roles;
7. white-label constraints and disclosures;
8. API/webhook/hosted-flow capabilities;
9. SLA and observability;
10. economics, subsidy and settlement;
11. LGPD, consent and incident response;
12. servicing and collections;
13. fraud and merchant risk;
14. concentration and partner portability.

## Output
Create `credit-model.md` style analysis with verified facts, assumptions, unknowns, hard blockers and target architecture. Do not provide legal conclusions; identify what needs regulated-partner or counsel confirmation.
