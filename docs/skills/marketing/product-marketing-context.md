---
description: You help users create and maintain a product marketing context document. This captures foundational positioning and messaging that other marketing skills reference.
title: product-marketing-context
---

# product-marketing-context

You help users create and maintain a product marketing context document. This captures foundational positioning and messaging that other marketing skills reference.

- **Area:** Marketing
- **Category:** marketing strategy
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing, Product Manager

Creates or updates the product marketing context document that captures positioning, messaging, competitive landscape, and customer language.

## How you ask

- “Set up our product marketing context document”
- “Create a positioning and messaging foundation for our product”
- “Update our marketing context with new competitive insights”
- “Build the context file so other skills can reference it”

## Inputs

- client_product — Client product identity, same schema as the company product note. Read in client mode.
- request — What to produce
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
- products — loaded from your vault context
- mode — write (regenerate) or check (flag drift) (write | check)

## Outputs

- marketing-context (markdown)
- {company.marketing-context}
- {scope.marketing-context}

