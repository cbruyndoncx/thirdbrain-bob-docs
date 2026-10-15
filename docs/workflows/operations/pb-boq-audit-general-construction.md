---
title: BOQ Audit General Construction
---

# BOQ Audit General Construction

*BOQ audited for spec gaps, quantity anomalies, and pricing errors; bids levelled into a Schedule of Values; inspection checklist and escalation clauses ready for use*

> The bid came in low.
> Low bids are where the claims come from.

- **Area:** Operations
- **Time savings:** Typical run: 1-2 days for single BOQ; 2-3 days for multi-bid leveling
- **Try it:** "BOQ or contractor bid received for a general construction project (residential, commercial, mixed-use) — needs auditing before award or payment"
- **Compounding:** Each run refines templates and context — 3 automated steps improve with accumulated data
- **Frequency:** Per trigger event

## Inputs

- 📋 Contractor BOQ(s)
- 📋 Project context (sector, region, currency, scope summary)
- 🗺️ Drawings (RCP, plans) if available
- 📅 Tender deadline and award timeline

## What BOB does

1. **boq-audit (audit-boq)** → using `--alias {matter-alias}`, parse the contractor BOQ, run the four audit passes (spec-gap, quantity-validation, EO-pricing, cost-completeness), produce markdown audit report + JSON anomaly array with NLM citations on every flag
2. **boq-audit (level-bids)** → normalise all contractor bids into a Schedule of Values, flag "too good to be true" rates, buried preliminaries, and missing line items
3. **Review audit and SOV findings with owner-rep or QS** — walk through Critical and High flags, agree which to challenge with contractor, agree the lowest responsible bidder advisory
4. **Issue findings to contractor** with 7-day response window for itemised re-bid or clarifications
5. **boq-audit (inspection-checklist)** → derive a site inspection checklist from the audited BOQ — mock-up requirements, MEP coordination points, hold-points before installation
6. **Owner-rep makes award decision** based on audit + SOV + contractor responses + capacity assessment. Award is binding only at this step

