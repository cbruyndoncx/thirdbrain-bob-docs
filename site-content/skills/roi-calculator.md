---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: roi-calculator — ThirdBrain BOB skill
  description: Generate an Excel workbook that models the time and cost savings of vault skills for 8 SMB roles.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: roi-calculator
catLabel: business
area: strategy
desc: Generates an Excel ROI calculator showing time and cost savings per SMB role across all vault skills.
summary: Generate an Excel workbook that models the time and cost savings of vault skills for 8 SMB roles.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[CEO / Founder, Head of Sales]'
inputs:
- request — The ROI question the workbook has to answer — which roles, which pricing tiers, and who the workbook is for.
- metadata — Skill inventory written by the `metadata-refresh` route, read back so the workbook rows match the corpus that was last scanned.
- rate-card — Role labels, hourly rates and currency the savings columns are computed from. There is no built-in fallback — the run halts if this is missing or empty.
- role-relevance — Per-skill relevance score and hours-saved-per-use for each role, which is what turns a skill list into a savings model.
- currency — Currency symbol baked into the workbook number formats. Fixed at generation time, so setting it wrong means regenerating rather than editing cells.
- output-path — Destination for the workbook. Must not point at a file Excel currently has open.
- request — Who the pivot is for. The layout is fixed by `add_pivot_table.ps1` — Category/Skill rows, Role columns, Annual Savings values, tier filter preset to starter and *-free — so any other slicing is done in Excel afterwards.
- metadata — Skill inventory written by the `metadata-refresh` route, read back as the pivot's source data.
- rate-card — Role labels, hourly rates and currency behind the Annual Savings values the pivot aggregates.
- role-relevance — Per-skill relevance and hours-saved figures the pivot totals by category and role.
- currency — Currency symbol baked into the workbook number formats before the pivot is built on top of them.
- output-path — Destination for the workbook. The pivot step opens this file through Excel COM, so it must be closed and unlocked before the run.
- request — What changed in the corpus, so the refresh can be checked against the skills the caller expects to appear or disappear.
- skill-corpus — Every skill's frontmatter, scanned for name, description, category, dev status, pricing tier and folder.
- output-path — Destination for the metadata JSON. Point it at the same path the workbook routes will read, or they will model a stale corpus.
- request — What moved in the corpus or the pricing tiers, and whether the refreshed workbook still has to match a previously shared version.
- skill-corpus — Every skill's frontmatter, rescanned so the rebuilt workbook reflects the current library rather than the last metadata run.
- rate-card — Role labels, hourly rates and currency for the rebuild. Point at a regional card here when the refresh is for a different market than the original.
- role-relevance — Per-skill relevance and hours-saved figures. Skills added since the last run need entries here or they contribute nothing to the model.
- currency — Currency symbol for the rebuilt workbook. Omitting it re-uses the rate card's own currency rather than the previous workbook's.
- pivot — Rebuilds the native pivot sheet as well. Leave it off and the refreshed workbook comes back with four sheets even if the previous one had five.
- output-path — Destination for the rebuilt workbook. Overwriting the previously shared path is the usual intent, so confirm it is closed in Excel first.
outputs:
- Five-sheet workbook — the four formula sheets plus a native pivot with Category/Skill rows, Role columns, Annual Savings values and a pricing-tier filter.
- Four-sheet formula-driven workbook — skills, per-role relevance and hours, ROI by role with live-editable rates, and the summary.
- One JSON record per skill — name, description, category, dev status, pricing tier and folder — used as the row source for every workbook route.
- Rebuilt workbook carrying the current corpus, in four-sheet form or five if the pivot was requested.
- Rescanned skill inventory, rewritten as part of the same pass so the workbook and its row source cannot disagree.
- prefer a permanent directory)
prompts:
- Generate an ROI calculator for our skill set
- Show the time savings per role across all vault skills
- Create an Excel workbook showing the value of our AI skills
---
