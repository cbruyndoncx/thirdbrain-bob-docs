---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: operating-dashboard — ThirdBrain BOB skill
  description: Use this skill to generate a Business Operating Dashboard as a JSON Canvas (`.canvas`) file from `business-baseline` artifacts. The dashboard is a source-derive
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: operating-dashboard
catLabel: business
area: strategy
desc: Generates or updates a Business Operating Dashboard as a JSON Canvas (`.canvas`) file from business-baseline source data.
summary: Use this skill to generate a Business Operating Dashboard as a JSON Canvas (`.canvas`) file from `business-baseline` artifacts. The dashboard is a source-derived operational view, not a hand-authored diagram.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Operations Manager, Finance Manager]'
inputs:
- session_state — Business baseline session state — primary source of truth for the header, bow-tie, analysis, and roadmap rows.
- client_processes — Client-scope process notes feeding the Processes row; override `expanded_processes` in session-state when present.
- request — Confirmation that no dashboard canvas exists yet and the first dashboard should be generated.
- 'scope — The client-id whose business baseline the dashboard reads (`client.root`). Client scope only: business-baseline writes `session-state.yaml` only under `{client.business-baseline}`, so a company run has no source of truth and no output path.'
- session_state — Business baseline session state, re-read in full so the regenerated canvas reflects every change since the last generation rather than being patched.
- request — Confirmation that an existing dashboard should be regenerated after the source data changed.
- session_state — Business baseline session state, checked for presence and completeness rather than assumed to exist — its absence is a finding, not a blocker to this route.
- client_processes — Client-scope process notes checked for presence when assessing whether the Processes row is ready.
- request — Confirmation that a readiness/gap check is wanted rather than a full generation or refresh.
outputs:
- The generated Business Operating Dashboard canvas, together with a summary of the rows generated, the rows omitted, and why.
- The regenerated dashboard canvas, rebuilt whole from source data and overwriting the previous file.
- Which rows can be generated now, which rows are blocked by missing source data, and which source artifacts are still missing.
- '{client.business-baseline}/{client-id}-operating-dashboard.canvas'
prompts:
- Generate an operating dashboard from my business baseline data
- Refresh my business dashboard canvas with the latest metrics
- Create a visual overview of my business operations as a canvas
---
