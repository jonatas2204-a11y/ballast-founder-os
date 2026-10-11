# Ballast Founder OS — OpenAI Edition

A skills-only OpenAI plugin for rigorous strategy and execution at **Ballast**.
It adapts useful patterns from Jake Schincariol's MIT-licensed `founder-skill`, but is rebuilt around Ballast's actual operating model: architecture/construction distribution plus B2B2C embedded credit.

## What is different from the original Founder Skill

- **Evidence-first, not simulation-first.** Synthetic customer scenarios are qualitative only. They never become a claimed conversion rate.
- **Ballast-specific credit layer.** Dedicated workflows for CaaS/embedded finance, funding, origination, underwriting, white label, regulatory allocation, servicing and collections.
- **B2B2C economics.** Models merchants, end-borrowers, financial partners and Ballast separately.
- **Commercial intelligence.** Lead scoring, verified contact policy, account briefs, personalized outreach and meeting discovery.
- **Decision gates.** A partner or initiative cannot receive a positive recommendation while a hard blocker remains unresolved.
- **Portable across ChatGPT and Codex.** No Claude-only sub-agent calls or `${CLAUDE_SKILL_DIR}` assumptions.

## Skills

Recommended sequence for a major decision:

`setup → ballast-board → ballast-market → ballast-competitors → ballast-customer → ballast-credit → ballast-partners → ballast-prospecting → ballast-sales → ballast-economics → ballast-pricing → ballast-marketing → ballast-ops → ballast-launch → ballast-plan`

Every skill can also run independently.

### Core skills

| Skill | Job |
|---|---|
| `setup` | Establishes the Ballast state file and evidence rules. |
| `ballast-board` | Pressure-tests a decision through independent strategic lenses. |
| `ballast-market` | Sizes and segments the market using traceable public evidence. |
| `ballast-competitors` | Maps direct, indirect and substitute competition. |
| `ballast-customer` | Builds customer evidence, jobs-to-be-done and objection hypotheses. |
| `ballast-credit` | Designs/evaluates the embedded-credit operating model. |
| `ballast-partners` | Runs due diligence on lenders, SCDs, fintechs, CaaS and white-label partners. |
| `ballast-prospecting` | Finds and scores merchant prospects with verified contacts. |
| `ballast-sales` | Produces account-specific outreach, discovery and follow-up. |
| `ballast-economics` | Models transaction, merchant and company economics. |
| `ballast-pricing` | Designs pricing/revenue architecture for merchants and financial partners. |
| `ballast-marketing` | Builds B2B/B2C acquisition plans tied to evidence and economics. |
| `ballast-brand` | Protects Ballast's strategic positioning in messaging and visual decisions. |
| `ballast-ops` | Defines operating model, responsibilities, SLAs, controls and risk register. |
| `ballast-launch` | Designs pilots, success criteria, rollout and kill/scale rules. |
| `ballast-plan` | Compiles the current strategy into an executive operating plan. |

## Workspace behavior

If a writable workspace exists, use `ballast/` as the source-of-truth directory. If it does not, produce the same outputs in chat and maintain a compact `STATE` block that can be copied into a future conversation. Never claim a file was written unless the environment confirms it.

Suggested workspace:

```text
ballast/
  state.md
  evidence.md
  decisions.md
  market.md
  competitors.md
  customers.md
  credit-model.md
  financial-partners.csv
  merchant-pipeline.csv
  sales-playbook.md
  economics.json
  economics.md
  pricing.md
  marketing.md
  brand.md
  ops.md
  pilot.md
  plan.md
```

## Scripts

All scripts use only the Python standard library.

```bash
python3 scripts/lead_score.py examples/lead.example.json
python3 scripts/credit_partner_score.py examples/credit_partner.example.json
python3 scripts/unit_economics.py examples/economics.example.json
python3 scripts/decision_matrix.py --help
python3 scripts/validate_package.py .
python3 -m unittest discover -s tests -v
```

## Install / package

This repository follows the portable Agent Plugins layout: root `plugin.json` plus `skills/<skill>/SKILL.md`. An optional `.codex-plugin/plugin.json` compatibility manifest is included.

For ChatGPT/Codex, add the repository as a plugin source or package the directory as a ZIP according to the current OpenAI plugin flow. Installation itself requires the user's explicit action in the product UI.

## Methodological rule

The OS distinguishes five evidence states:

`VERIFIED_PUBLIC` · `USER_PROVIDED` · `ESTIMATE` · `ASSUMPTION` · `UNKNOWN`

A recommendation must identify which state supports each material claim. Unknowns that can change the decision become explicit due-diligence questions, not invented facts.

## Attribution

Conceptual inspiration and some workflow ideas derive from `Jakeschincariol/founder-skill`, MIT licensed. See `NOTICE.md` and `LICENSE`.
