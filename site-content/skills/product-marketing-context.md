---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: product-marketing-context — ThirdBrain BOB skill
  description: You help users create and maintain a product marketing context document. This captures foundational positioning and messaging that other marketing skills refere
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: product-marketing-context
catLabel: marketing-strategy
area: marketing
desc: Creates or updates the product marketing context document that captures positioning, messaging, competitive landscape, and customer language.
summary: You help users create and maintain a product marketing context document. This captures foundational positioning and messaging that other marketing skills reference.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Product Manager]'
inputs:
- client_product — Client product identity, same schema as the company product note. Read in client mode.
- request — What to produce
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
- products — loaded from your vault context
- mode — write (regenerate) or check (flag drift) (write | check)
outputs:
- marketing-context (markdown)
- '{company.marketing-context}'
- '{scope.marketing-context}'
prompts:
- Set up our product marketing context document
- Create a positioning and messaging foundation for our product
- Update our marketing context with new competitive insights
- Build the context file so other skills can reference it
---
