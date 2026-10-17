---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: profile-cms — ThirdBrain BOB skill
  description: '*Formerly `linkedin-cms`; renamed 2026-08-18 when Indeed became a supported platform. Releases up to and including v2.5.0 shipped it under the old name.*'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: profile-cms
catLabel: marketing-content
area: marketing
desc: Manages LinkedIn and Indeed profile and company-page content offline as structured data, then renders an annotated review view showing character counts, empty fields,…
summary: '*Formerly `linkedin-cms`; renamed 2026-08-18 when Indeed became a supported platform. Releases up to and including v2.5.0 shipped it under the old name.*'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Marketing]'
inputs:
- 'profile_root — The profile root this run writes under — `{me.profile-root}` (your own), `{company.profile-root}` (the company page). NOT `{profile_root}`: routes_schema defines that as the bare company/client root, one level shallower than anything this skill writes'
- source (Capture profile state) — path to LinkedIn export CSVs, or pasted profile text
- document — profile JSON document
- company — company name or existing company JSON document
- profile_url — the lead's LinkedIn profile URL
- source (Indeed resume) — live Indeed profile read, resume PDF export, or existing Indeed JSON document
outputs:
- Headshot, banner, logo or cover image downloaded with curl during capture and referenced from the JSON by relative path; only written when the subject has that image set.
- checklist (markdown)
- company-document (json)
- indeed-document (json)
- lead-document (json)
- profile-document (json)
- review-view (html)
- updated-document (json)
- '{client.leads}/{lead-id}/person_{lead}.json'
- '{company.profile-root}/linkedin/company_{id}.json'
- '{profile_root}/indeed/person_{subject}_indeed.json'
- '{profile_root}/linkedin/assets/{subject}_{image}.jpg'
- '{profile_root}/linkedin/publish_checklist_{date}.md'
- '{profile_root}/linkedin/{kind}_{subject}.json'
- '{profile_root}/linkedin/{name}.html'
prompts:
- Update my LinkedIn profile
- What fields does a LinkedIn company page have?
- Show me what's actually on my profile and where the gaps are
- Capture this lead's LinkedIn profile into the client folder
- Draft a better headline within the limit
---
