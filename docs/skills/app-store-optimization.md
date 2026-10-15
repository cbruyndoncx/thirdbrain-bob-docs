---
description: Turn an app listing into store-ready metadata, a screenshot sequence, and a ranked test plan — with the App Store and Google Play rules applied correctly, because they invert.
title: app-store-optimization
---

# app-store-optimization

Turn an app listing into store-ready metadata, a screenshot sequence, and a ranked test plan — with the App Store and Google Play rules applied correctly, because they invert.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing seo |
| **Level** | beginner |
| **Input** | url |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Product Manager] |

Audits and rewrites App Store and Google Play listings — keyword placement, metadata written to exact character counts, screenshot sequences, icon assessment, ratings…

## How you ask

- “Run an ASO audit on our iOS app”
- “We get impressions but nobody installs — what's wrong with our listing?”
- “Rewrite our Play Store listing”
- “What keywords should we target in the App Store?”
- “Design the screenshot sequence for our launch”
- “Which locales should we localise the listing for?”

## Inputs

- store-url — App Store or Google Play listing URL, or the app name plus store
- store — Which store's rules to apply — app-store, google-play, or both (app-store | google-play | both)
- console-metrics — App Store Connect or Play Console export — impressions, product page views, install rate, retention. Without it the discoverability/conversion split is inferred, not measured.
- brand-context — Company or client profile — positioning, ICP, proof, voice
- app-description — What the app does, who it is for, and the primary conversion action
- store — Which store's field rules and limits to write against (app-store | google-play | both)
- keyword-set — Scored keyword table from a prior aso-audit run; regenerated if absent
- locales — Target store locales, e.g. nl-NL, de-DE, fr-FR
- base-listing — The source-locale listing package to localise

## Outputs

- aso-audit-report (markdown)
- listing-package (markdown)
- localisation-plan (markdown)
- prefer a permanent directory)

