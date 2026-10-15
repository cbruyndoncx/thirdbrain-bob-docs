---
description: 'Target Audience: business owners and consultants who need to explain an automation, pipeline or process to a non-technical client, colleague or prospect.'
title: doodle
---

# doodle

Target Audience: business owners and consultants who need to explain an automation, pipeline or process to a non-technical client, colleague or prospect.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | diagramming |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | diagram |
| **Setup** | [install] |
| **Roles** | [] |

Draws a hand-drawn explainer strip (PNG, optional SVG) that shows how a system, pipeline or process works for non-technical readers: 3-6 left-to-right scenes, a small…

## How you ask

- “/doodle how our lead routing works”
- “Make a napkin sketch of the client onboarding flow for the proposal”
- “Explain the invoice-collection automation to the client in one picture”

## Inputs

- subject — What to explain, e.g. 'how our lead routing works'
- source-material — Code, logs, docs or a process note that describe what the system really does

## Outputs

- Editable strip source; {slug} is a short kebab-case name for the subject.
- Optional (--svg): self-contained vector strip with logos and font embedded, for slides, print and carousels.
- Rendered strip at 2x, width = scenes x 340 + 60 px.
- prefer a permanent directory)

