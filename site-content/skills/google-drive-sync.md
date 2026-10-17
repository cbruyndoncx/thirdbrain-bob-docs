---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: google-drive-sync — ThirdBrain BOB skill
  description: 'Target Audience: Business owners, operations teams, and consultants who share deliverables via Google Drive and want automated folder resolution without manual '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: google-drive-sync
catLabel: productivity
area: foundational
desc: Upload files to Google Drive with folder resolution, create missing folders, archive large vault files with stub replacement, and manage Drive folder mappings.
summary: 'Target Audience: Business owners, operations teams, and consultants who share deliverables via Google Drive and want automated folder resolution without manual folder-ID lookups.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[api-key, config]'
roles: '[]'
inputs:
- file-path — Local file path to upload
- folder-id — Google Drive folder ID
- workspace-hint — Client name or folder hint for resolution
- folder-name — Name for the new folder
- parent-folder — Parent folder ID or name
- file-path — File or directory to archive
outputs:
- console
- folder-confirmation (markdown)
- same location as original file
- stub-notes (markdown)
- upload-confirmation (markdown)
prompts:
- Upload this deliverable to the shared Drive
- Save this report to the client folder
- Archive all large files in this project to Drive
- Create a new client folder on Drive and upload the proposal
---
