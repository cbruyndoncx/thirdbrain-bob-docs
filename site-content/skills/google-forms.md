---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: google-forms — ThirdBrain BOB skill
  description: Prepare a Google Forms API `forms.create` plus `forms.batchUpdate` request from a local question draft. The live write is deliberately gated until the Google Fo
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: google-forms
catLabel: productivity
area: foundational
desc: Builds a Google Forms API request (offline, no live form is created) from a vault question draft.
summary: Prepare a Google Forms API `forms.create` plus `forms.batchUpdate` request from a local question draft. The live write is deliberately gated until the Google Forms OAuth scope is added to the shared Google Workspace auth configuration.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[google-workspace, config, api-key]'
roles: '[]'
inputs:
- question-draft — JSON draft containing the form title, optional description, and ordered questions.
- output-path — Destination for the generated offline request JSON.
outputs:
- form-request (json)
- prefer a permanent directory)
prompts:
- Turn this reviewed question draft into an offline Google Forms API request.
- Build the form request JSON and verify that all questions stay in the same order.
- Prepare this survey for Google Forms, but do not publish anything yet.
---
