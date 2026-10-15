---
title: BOQ Audit Interior Fit Out
---

# BOQ Audit Interior Fit Out

*Fit-out BOQ audited with sector-specific spec depth (RCP coordination, false ceiling fascia, joinery EO pricing, finish brands), bids levelled, hold-points and escalation clauses generated*

> The fit-out quote looks fine.
> Until someone checks the ceiling and the joinery.

- **Area:** Operations
- **Time savings:** Typical run: 1-2 days for single BOQ; 2-3 days for multi-bid leveling
- **Try it:** "Interior fit-out BOQ received (commercial office, retail, hospitality, institutional fit-out) — needs auditing before award or payment"
- **Compounding:** Each run refines templates and context — 3 automated steps improve with accumulated data
- **Frequency:** Per trigger event

## What BOB does

1. **Validate fit-out context** — confirm tenant tier, RCP availability, mock-up policy. Flag the sector context pack for the audit
2. **boq-audit (audit-boq)** → using `--alias {matter-alias}` and the fit-out context pack, run the four audit passes; spec-gap pass uses the NLM-grounded fit-out brand list, EO-pricing pass uses fit-out patterns; every flag carries an NLM citation
3. **boq-audit (level-bids)** → with fit-out SOV extensions, split joinery into Fixed/Movable/Fascia, ensure mock-up line item appears
4. **Review with interior designer + owner-rep** — fit-out audits often require designer sign-off on finish specifications and brand acceptability
5. **Issue findings to contractor** — 7-day response window. Specifically request mock-up scheduling.
6. **boq-audit (inspection-checklist)** → fit-out checklist heavily emphasises mock-up approval gates, MEP-RCP coordination at every fixture, and finish verification at delivery
7. **Owner-rep + designer make award decision** — designer carries authority on aesthetic intent; owner-rep on commercial. Award is binding only at this step

