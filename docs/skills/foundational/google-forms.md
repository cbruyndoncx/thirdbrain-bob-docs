---
description: Prepare a Google Forms API `forms.create` plus `forms.batchUpdate` request from a local question draft. The live write is deliberately gated until the Google Forms OAuth scope is added to the shared Google Workspace auth configuration.
title: google-forms
---

# google-forms

Prepare a Google Forms API `forms.create` plus `forms.batchUpdate` request from a local question draft. The live write is deliberately gated until the Google Forms OAuth scope is added to the shared Google Workspace auth configuration.

- **Area:** Foundational
- **Category:** productivity
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** google-workspace, config, api-key
- **Roles:** 

Builds a Google Forms API request (offline, no live form is created) from a vault question draft.

## How you ask

- “Turn this reviewed question draft into an offline Google Forms API request.”
- “Build the form request JSON and verify that all questions stay in the same order.”
- “Prepare this survey for Google Forms, but do not publish anything yet.”

## Inputs

- question-draft — JSON draft containing the form title, optional description, and ordered questions.
- output-path — Destination for the generated offline request JSON.

## Outputs

- form-request (json)
- prefer a permanent directory)

