---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: linkedin-searches — ThirdBrain BOB skill
  description: Build precise LinkedIn and Google X-ray queries for recruiting, prospecting, lead generation, and expert discovery.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: linkedin-searches
catLabel: sales
area: sales
desc: Builds LinkedIn Boolean searches for recruiting, prospecting, speaker sourcing, and Google X-ray discovery.
summary: Build precise LinkedIn and Google X-ray queries for recruiting, prospecting, lead generation, and expert discovery.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- request — The target role, profile, or buyer to search for — titles, must-have terms, geography, and exclusions.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- request — The target role, profile, or buyer to search for, with the must-have terms and exclusions that filters cannot express.
- filters — Sales Navigator filter values (company size, seniority, geography) to set alongside the Boolean string instead of folding them into it.
- request — The target role, profile, or buyer to search for; exclusions are expressed with `-term` rather than `NOT`.
- existing-query — The Boolean or X-ray query to widen or tighten, exactly as currently run.
- platform — Which platform the existing query targets; determines whether the broadened/tightened variant keeps the original's exclusion and filter syntax. (native | sales-navigator | google-x-ray)
outputs:
- The Google X-ray query, platform, and broader/narrower variants, saved under the client's sales folder.
- The Google X-ray query, platform, and broader/narrower variants, saved under the company's sales folder.
- The Sales Navigator Boolean string, recommended filter dropdown values, and broader/narrower variants, saved under the client's sales folder.
- The Sales Navigator Boolean string, recommended filter dropdown values, and broader/narrower variants, saved under the company's sales folder.
- The broader and narrower variants of the existing query, each in the original's platform syntax, saved under the client's sales folder.
- The broader and narrower variants of the existing query, each in the original's platform syntax, saved under the company's sales folder.
- The native-search Boolean string, platform, recommended filters, and broader/narrower variants, saved under the client's sales folder.
- The native-search Boolean string, platform, recommended filters, and broader/narrower variants, saved under the company's sales folder.
- '{client.sales}/linkedin-searches-{YYYY-MM-DD}.md'
- '{company.sales}/linkedin-searches-{YYYY-MM-DD}.md'
prompts:
- Build a LinkedIn Boolean search for senior marketing managers in SaaS
- Create a recruiter search for React developers in Berlin
- Find decision makers on LinkedIn at Fortune 500 companies
- Generate a Google X-ray search for LinkedIn profiles
---
