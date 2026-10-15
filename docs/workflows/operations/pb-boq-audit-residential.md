---
title: BOQ Audit Residential
---

# BOQ Audit Residential

*Residential BOQ audited with sector-specific depth (kitchens, bathrooms, built-in wardrobes, finishes), bids levelled, escalation clauses and hold-points generated*

> The villa quote is a spreadsheet.
> The kitchens and wardrobes are a guess.

- **Area:** Operations
- **Time savings:** Typical run: 1 day for single BOQ; 2 days for multi-bid leveling
- **Try it:** "Residential construction or renovation BOQ received (single-family, multi-family, villa, apartment renovation) — needs auditing before award or payment"
- **Compounding:** Each run refines templates and context — 3 automated steps improve with accumulated data
- **Frequency:** Per trigger event

## What BOB does

1. **Validate residential context** — confirm new build vs renovation, kitchen/bath schedule, owner selection book. Load residential context pack
2. **boq-audit (audit-boq)** → using `--alias {matter-alias}` and the residential context pack, run the four audit passes; spec-gap pass uses NLM-grounded owner brand preferences; quantity-validation pass uses residential benchmarks; every flag carries an NLM citation
3. **boq-audit (level-bids)** → with residential SOV extensions, normalise kitchen and bathroom categories across bidders
4. **Review with owner** — residential audits centre owner aesthetic decisions; walk through finish choices and pricing implications
5. **Issue findings to contractor** — 5-7 day response. For renovations, flag site-condition allowances explicitly.
6. **boq-audit (inspection-checklist)** → residential checklist emphasises waterproofing acceptance (wet areas), kitchen-module pre-installation check, finish snagging at handover

