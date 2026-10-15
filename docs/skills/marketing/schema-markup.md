---
description: Implement schema.org structured data in JSON-LD format to enable rich results in search.
title: schema-markup
---

# schema-markup

Implement schema.org structured data in JSON-LD format to enable rich results in search.

- **Area:** Marketing
- **Category:** marketing seo
- **Level:** advanced
- **Input:** url
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing

Generates JSON-LD structured data, validates existing schema against Google's requirements, and implements Organization, Article, Product, FAQ, and BreadcrumbList markup…

## How you ask

- “Generate FAQ schema markup for our help center pages”
- “Create JSON-LD structured data for our product pages”
- “Validate our existing schema against Google's requirements”
- “Add BreadcrumbList and Organization schema to our site”

## Inputs

- marketing_context — Company name, description, logo and social profiles used to fill the Organization and publisher properties without asking for facts the vault already holds.
- url — Canonical URL of the page the markup describes; every absolute URL written into the JSON-LD is resolved against it.
- schema-type — Rich-result target for the page. The choice decides which properties Google treats as required, and therefore what has to be confirmed on the page before anything is drafted. Left unset, the route infers it from the page type and states the inference. (Organization | WebSite | Article | Product | SoftwareApplication | FAQPage | HowTo | BreadcrumbList | LocalBusiness | Event)
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- existing-markup — The JSON-LD currently on the page, copied from the live source or its template — the markup whose property coverage, value formats and page-content match are checked.
- url — Canonical URL of the page carrying the markup, used to compare declared values against what a visitor actually sees.
- marketing_context — Company facts used to confirm the Organization and publisher values in the existing markup are still current rather than left over from an earlier brand.
- platform — Target stack or CMS — static site generator, React/Next.js app, or WordPress and its schema plugin. Decides whether the guidance is a template include, a server-rendered component, or plugin and custom-field configuration.
- url — Page the markup will be deployed to, supplied when the guidance has to name a specific template or route rather than a general pattern.
- schema-type — The type being deployed. It decides whether the markup can be hard-coded once in a layout or has to be generated per record from CMS data. (Organization | WebSite | Article | Product | SoftwareApplication | FAQPage | HowTo | BreadcrumbList | LocalBusiness | Event)

## Outputs

- Complete JSON-LD block for the page, carrying every required property for the chosen type and only values that appear in the visible content.
- The submitted markup rewritten so every required property is present, every value is correctly formatted, and nothing is asserted that the page does not show.
- Where the JSON-LD goes on the named platform, how it is generated per page, and the post-deploy verification step that confirms it renders.
- missing required properties, invalid dates, URLs or enumerations, and mismatches against the visible content.
- {scope.marketing.seo}/schema/schema-{type}-{YYYY-MM-DD}.json

