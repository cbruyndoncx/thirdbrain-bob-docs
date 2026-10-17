---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: skool-classroom-builder — ThirdBrain BOB skill
  description: 'Creates and edits modules (sets/folders), lessons (pages) and Community feed posts in a Skool.com community, with one browser route: `playwright-cli`. It drives'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: skool-classroom-builder
catLabel: integrations
area: foundational
desc: Publishes modules and lessons into a Skool.com classroom AND posts to the Skool Community feed (incl.
summary: 'Creates and edits modules (sets/folders), lessons (pages) and Community feed posts in a Skool.com community, with one browser route: `playwright-cli`. It drives a single headed browser session with a persistent profile (log in once; the login is kept), and ships the helper scripts for the edit operations that Skool''s editor makes fragile: text edits that keep formatting, file attachments, file removal, draft/publish and pinning.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[playwright-cli]'
roles: '[Content Manager]'
inputs:
- community_id — Skool community slug (e.g. 'my-community' from skool.com/my-community)
- module_title — Title for the new module/set
- lesson_title — Title for the first lesson inside the module
- lesson_body — Lesson content — plain text, Markdown, or HTML
- community_id — Skool community slug
- module_title — Exact title of the existing module to add the lesson into
- lesson_title — Title for the new lesson
- lesson_body — Lesson content
- community_id — Skool community slug (e.g. 'thirdbrain-tech-3102')
- post_title — Post title (shown as the headline in the feed)
- post_body — Post body — plain text; newlines become paragraphs in the ProseMirror editor
- category — Exact name of an existing admin-defined category (e.g. 'General discussion', 'Announcements'). Categories cannot be created via this skill.
- pin — If true, pin the post to the feed after publishing (admin only). Default false.
- email_members — If true, enable 'Send email to all members'. Default false — leave off for evergreen/FAQ posts.
outputs:
- prefer a permanent directory)
- result (markdown)
prompts:
- Create a Skool module from this text
- Upload this lesson to my Skool course
- Post this to my Skool community
---
