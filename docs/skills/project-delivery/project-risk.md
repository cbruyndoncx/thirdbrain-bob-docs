---
description: Identifies and quantifies project risks with a Monte Carlo risk framework and visualization. Use when the user says 'risk register,' 'assess project risks,' 'risk analysis,' 'Monte Carlo simulation,' or 'risk management plan.'
title: project-risk
---

# project-risk

Identifies and quantifies project risks with a Monte Carlo risk framework and visualization. Use when the user says 'risk register,' 'assess project risks,' 'risk analysis,' 'Monte Carlo simulation,' or 'risk management plan.'

- **Area:** Project Delivery
- **Category:** project management
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Identifies and quantifies project risks with a Monte Carlo risk framework and visualization.

## How you ask

- “Create a risk register for our software project”
- “Run a Monte Carlo simulation on our project timeline”
- “Assess and quantify the top 10 project risks”
- “Identify risks that could impact our delivery date”

## Inputs

- risk_register — The register being refreshed. Its risk IDs, response owners, and prior scores are carried forward unless new evidence contradicts them.
- project_charter — Approved charter, read to detect scope or constraint changes since the register was last written (from `project-charter`).
- request — What triggered the refresh — a phase gate, a materialised risk, or new evidence on a specific entry.
- profile — Company or client delivery standards, used to keep the refreshed register consistent with the original.
- project_charter — Approved charter — scope, objectives, and constraints that seed risk identification (from `project-charter`).
- project_context — Tailoring decisions, read to confirm that light depth is the intended setting for this project.
- request — The risk question to answer and any known worry areas to cover.
- profile — Company or client delivery standards used to calibrate the impact scale.
- project_context — Tailoring decisions, read to set analysis depth and any prioritised principles before the simulation is built.
- baseline_duration — Baseline project duration in days. The simulation expresses schedule risk as deviation from this figure.
- baseline_cost — Baseline project budget. Absent, the run produces schedule confidence levels only.
- iterations — Monte Carlo iteration count. Higher values tighten the confidence curve at the cost of runtime; 5000 is used when unset.
- request — The quantification question — which decision the P50/P80/P90 figures are meant to support.
- profile — Company or client delivery standards used to calibrate the impact scale and reserve policy.
- project_context — Declares the delivery approach and priority principles. This route exists because it says adaptive or hybrid; without it the approach cannot be established.
- project_charter — Approved charter, read for the objectives that iteration-level risks are assessed against (from `project-charter`).
- request — The iterations or workstreams in scope and the review cadence the register has to fit.

## Outputs

- 5x5 probability x impact matrix with every risk plotted by its qualitative scores.
- Cumulative probability curve for duration and cost with P50, P80, and P90 confidence levels marked.
- Register combining qualitative scoring and simulation results, with the three visualizations embedded and contingency reserves set from P80.
- Register scoped to iterations or workstreams, with per-iteration review cadence, replanning triggers, and a separate emergent-risk section.
- Register with probability, impact, score, priority, response strategy, and owner per risk, plus an explicit statement that simulation was skipped and why.
- Simulation input — baseline duration and cost plus three-point schedule and cost impacts per risk.
- The updated register with preserved IDs, a changed-entries summary, and the evidence behind each change. Visualizations are regenerated only by re-running the `full-quantitative` route.
- Tornado diagram ranking risks by their sensitivity to total project impact.
- {project-folder}/risk_analysis.svg
- {project-folder}/risk_matrix.svg
- {project-folder}/risk_register.md
- {project-folder}/risks.json
- {project-folder}/s_curve.svg

