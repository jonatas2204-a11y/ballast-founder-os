---
name: ballast-partners
description: Research, compare and diligence financial partners for Ballast—banks, SCDs, fintechs, CaaS/embedded-finance providers and funding structures—using hard gates and traceable evidence.
---
# Ballast Partners

## Research sequence
1. Confirm legal/company identity and regulated entities.
2. Confirm actual B2B credit/CaaS capabilities from primary sources.
3. Map product, ticket, term, target borrower and geography.
4. Determine whether Ballast → merchant → consumer distribution is supported.
5. Determine funding source, credit-risk owner and recourse.
6. Map origination, contract, KYC/fraud, servicing and collections.
7. Map integration and white-label capabilities.
8. Identify economics available publicly, then questions for commercial confirmation.
9. Check implementation/pilot requirements and exclusivity/minimums.
10. Score only after evidence is separated from assumptions.

Use `scripts/credit_partner_score.py` when structured scores exist. A strong score never overrides an unresolved hard gate.

## Due-diligence call
Prioritize the questions that can kill the model first: multi-layer distribution, funding, risk, regulatory role, servicing, product fit, economics, integration and pilot.

## Output
Partner dossier, evidence table, score, unresolved hard gates, first-call question list, red flags, next contact and recommendation: `PRIORITY`, `QUALIFIED`, `WATCH`, `NO FIT`, or `INSUFFICIENT EVIDENCE`.
