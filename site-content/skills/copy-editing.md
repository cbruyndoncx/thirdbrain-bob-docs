---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: copy-editing — ThirdBrain BOB skill
  description: Edit marketing copy through seven sequential passes while preserving the core message.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: copy-editing
catLabel: marketing-content
area: marketing
desc: Edits marketing copy through seven sequential passes—clarity, voice, benefit bridging, proof verification, specificity, emotional impact, and risk removal.
summary: Edit marketing copy through seven sequential passes while preserving the core message.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- draft — The copy to edit, pasted or as a file path, with any approved facts, forbidden claims or keep/remove instructions.
- request — What to produce, including audience, CTA and any exact output sections the user wants.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- marketing-context — Audience, voice and positioning for the active scope (company or client marketing context).
- variants — Two or more versions of the same copy, pasted or as file paths, with any approved facts, forbidden claims or keep/remove instructions.
outputs:
- Edited copy, a short change summary, and open questions or missing proof.
- Edited copy, change summary by sweep, and open questions or missing proof.
- Edited copy, change summary for Sweeps 4 and 7, and the claims that still need proof, legal review or product confirmation.
- Variant comparison with the pick and its reasons, then the edited winner, change summary by sweep, and open questions or missing proof.
- '{scope.marketing}/content/copy-editing-{YYYY-MM-DD}.md'
prompts:
- Edit this marketing copy for clarity and impact
- Run a copy sweep on my landing page text
- Review and polish this email campaign draft
- Give me feedback on this product description copy
---
