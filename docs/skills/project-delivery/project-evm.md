---
description: Calculate Earned Value Management metrics and output an SVG trend chart with traffic-light status for CPI, SPI, and cost variance. Use when user mentions 'earned value,' 'EVM analysis,' 'project performance report,' 'CPI SPI analysis,' 'cost variance,' or 'earned value metrics.' This is the EVM methodology.
title: project-evm
---

# project-evm

Calculate Earned Value Management metrics and output an SVG trend chart with traffic-light status for CPI, SPI, and cost variance. Use when user mentions 'earned value,' 'EVM analysis,' 'project performance report,' 'CPI SPI analysis,' 'cost variance,' or 'earned value metrics.' This is the EVM methodology.

- **Area:** Project Delivery
- **Category:** project management
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Finance Manager

Calculate Earned Value Management metrics and output an SVG trend chart with traffic-light status for CPI, SPI, and cost variance.

## How you ask

- “Turn our estimate into a trackable budget with control accounts”
- “Calculate earned value metrics for our project”
- “Generate a CPI/SPI analysis with traffic-light reporting”
- “What's our cost variance and schedule performance?”
- “Create an earned value trend visualization”

## Inputs

- estimate — Estimate lines as JSON or CSV — code, description, amount, optional trade
- mapping — Control-account mapping JSON — how estimate lines roll up for tracking
- profile — Company or client profile — delivery standards and project context.
- evm_data — Cumulative BAC/PV/EV/AC dataset seeded by the `baseline-setup` route and extended each reporting cycle. Absent, the figures are collected from the user and this file is written before the calculator runs.
- schedule — Schedule — activities, durations, dependencies (from `project-schedule`)
- risk_register — Risk register — risks, scores, responses (from `project-risk`)
- project_context — Tailoring decisions — read to set analysis depth and delivery approach before the metrics are computed (from `project-context`).
- source (Full EVM Analysis) — Project EVM data (BAC, PV, EV, AC) or project reference
- evm_data — BAC plus the single period's PV/EV/AC. Absent, the figures are collected from the user and this file is written before the calculator runs.
- project_context — Tailoring decisions — a `light` depth setting is the documented case for this route (from `project-context`).
- source (Single-Period Snapshot) — The single reporting cut — BAC, PV, EV, AC and the period cut-off date
- evm_data — The dataset the calculator could not process, or the figures already computed elsewhere, read so the manual metrics rest on the same numbers.
- project_context — Tailoring decisions — read to set depth and delivery approach for the hand-built analysis (from `project-context`).
- source (Manual EVM Interpretation) — The figures to interpret, plus the reason the calculator is not being run — script error, missing dependency, or interpretation-only request

## Outputs

- CPI and SPI trend lines with the green/yellow/red threshold bands.
- Metrics and recommendations reasoned by hand, carrying an explicit note that the report was generated without the script and that the SVG visualizations are not available.
- Metrics table with RAG status per period, forecasting section, and recommendations tied to the actual CPI/SPI signal.
- PV, EV and AC plotted over the reporting periods against the BAC reference line.
- Single-cut metrics with RAG status and forecasting, stating explicitly that trend analysis needs a second reporting period.
- cost-baseline (markdown)
- cost-baseline-data (json)
- evm-seed (json)
- {project-folder}/cost_baseline.json
- {project-folder}/cost_baseline.md
- {project-folder}/evm_data.json
- {project-folder}/evm_report.md
- {project-folder}/evm_scurve.svg
- {project-folder}/evm_trends.svg

