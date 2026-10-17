---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: quotation-generator — ThirdBrain BOB skill
  description: Produce the same quotation, the same way, every time — regardless of who prepares it.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: quotation-generator
catLabel: sales
area: sales
desc: Turns structured quotation data into a branded, consistently formatted customer quotation document, with a required-field gate that blocks generation when information is…
summary: Produce the same quotation, the same way, every time — regardless of who prepares it.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- quotation-json — Per-job quotation JSON containing seller and category references plus customer, item, price, and term data.
- quotation-json — Validated quotation JSON with resolvable seller and category configuration references.
- output-path — Confirmed destination for the generated draft quotation — the client or lead folder for a real quotation, the scratch area (`output.scratch`) for a throwaway.
- source-format — Representative quotation template or example used to derive seller identity and category requirements.
outputs:
- Editable Word quotation; a throwaway goes to the scratch area, and a real quotation is written with -o to the confirmed client or lead folder.
- prefer a permanent directory)
- quotation-config (json)
- stdout
- validation-report (text)
- '{configured-assets-folder}/categories.json'
prompts:
- Validate this quotation JSON and list every missing required field without generating Word.
- Generate an editable quotation draft from this validated input and save it to the client folder.
- Onboard this new product-family quotation format before we prepare the first quote.
---
