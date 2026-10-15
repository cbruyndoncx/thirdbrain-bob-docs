---
description: Design survey campaigns, connect to external survey tools, import responses into the vault as `feedback` entities, and synthesize results into actionable reports. Bridges the gap between external collection tools and vault-based decision making.
title: survey-feedback-pipeline
---

# survey-feedback-pipeline

Design survey campaigns, connect to external survey tools, import responses into the vault as `feedback` entities, and synthesize results into actionable reports. Bridges the gap between external collection tools and vault-based decision making.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Product Manager] |

Connects external survey tools (SurveyMonkey, Typeform, Google Forms) to vault storage.

## How you ask

- “Design a client NPS survey for Q1 and set it up in Google Forms”
- “Import the latest responses from our Google Forms feedback sheet”
- “I just got verbal feedback from the client on a call, capture it in the vault”
- “Synthesize all feedback we've collected from the Q4 client satisfaction survey”
- “Show me the status of all active survey campaigns”

## Inputs

- survey_type — Instrument to design — nps, csat, pmf, exit-survey, supplier-review, or custom. Determines the question set and the scoring model. (csat | custom | exit-survey | nps | pmf | supplier-review)
- target_audience — Who receives the survey
- client_id — Client the survey belongs to, when client-scoped
- survey-templates — loaded from your vault context
- profile — loaded from your vault context
- form_url — Google Form or response-sheet URL
- survey_ref — Existing survey note to attach responses to
- csv_path — Response export to import
- responses — Responses entered directly, one object per respondent
- survey_ref — Survey whose responses are to be themed and scored
- client-feedback — Prior feedback records for this client — themed alongside new responses.
- supplier-profile — Supplier context when the survey targets a supplier rather than a client.
- survey_ref — Survey to report on; defaults to all active campaigns
- survey-records — Survey campaign records — the source of active-campaign status.

## Outputs

- One client `feedback` entity per response, dated by its `feedback_date`.
- One supplier `feedback` entity per response from a supplier respondent.
- Supplier-routed synthesis, written when the responses are supplier feedback.
- The campaign record — company-scope `survey` entity holding the question set, target audience, tool and deployment plan; client-scoped campaigns carry `client_id`.
- campaign-dashboard (markdown)
- synthesis-report (markdown)
- {client.feedback}/survey_synthesis_{YYYY-MM-DD}.md
- {client.feedback}/{YYYY-MM-DD}_{feedback-type}-{respondent-slug}.md
- {client.feedback}/{YYYY-MM-DD}_{survey-slug}-{respondent-slug}.md
- {company.operations.surveys}/{campaign-slug}.md
- {company.reports}/survey_campaign_status.md
- {supplier.feedback}/survey_synthesis_{YYYY-MM-DD}.md
- {supplier.feedback}/{YYYY-MM-DD}_{feedback-type}-{respondent-slug}.md
- {supplier.feedback}/{YYYY-MM-DD}_{survey-slug}-{respondent-slug}.md

