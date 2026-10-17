---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: google-keep — ThirdBrain BOB skill
  description: Manage Google Keep notes directly from the command line using a single-file Python script with `uv run`.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: google-keep
catLabel: productivity
area: foundational
desc: Manages Google Keep notes via CLI; reminder management is unsupported.
summary: Manage Google Keep notes directly from the command line using a single-file Python script with `uv run`.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[api-key]'
roles: '[]'
inputs:
- request — The read operation — list, search, get, or export — plus any filters (pinned, archived, limit) or search terms.
- note-id — Specific note ID to fetch with `get`; absent for list, search, and export.
- format — Output format for a `get` or `export` result; absent uses the command default (text for get, JSON for export). (text | json | markdown)
- request — The note title and content, or checklist items, to create.
- labels — Label names to attach to the new note; each is created if it does not already exist.
- content-file — Local file supplying the note body via `--file`, used instead of inline text.
- note-id — Target note ID to modify; required so the update is unambiguous rather than title-matched.
- request — What to change — new title, text, color, pin state, or archive status.
- content-file — Local file supplying replacement note content via `--file`.
- note-id — Target note ID to trash or permanently delete.
- permanent — Whether to permanently delete rather than move to trash; defaults to trash, which is recoverable.
- confirmed — Whether the note's existence and ID were verified with `get` and the user confirmed the action; required before a permanent delete runs.
outputs:
- Confirmation of the note ID removed and whether the removal was trash or permanent.
- Confirmation of the note ID updated and which fields changed.
- The created note's ID and confirmation of its title, content, labels, and pin/color state.
- The exported note set, produced only when the export command writes to a file instead of stdout.
- The note list, search results, or single note content printed for the user.
- prefer a permanent directory)
prompts:
- List my Google Keep notes about project ideas
- Create a shopping list in Google Keep
- Search my Keep notes for meeting reminders
- Export my Google Keep notes to markdown
---
