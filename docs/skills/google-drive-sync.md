---
description: 'Target Audience: Business owners, operations teams, and consultants who share deliverables via Google Drive and want automated folder resolution without manual folder-ID lookups.'
title: google-drive-sync
---

# google-drive-sync

Target Audience: Business owners, operations teams, and consultants who share deliverables via Google Drive and want automated folder resolution without manual folder-ID lookups.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | productivity |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [api-key, config] |
| **Roles** | [] |

Upload files to Google Drive with folder resolution, create missing folders, archive large vault files with stub replacement, and manage Drive folder mappings.

## How you ask

- “Upload this deliverable to the shared Drive”
- “Save this report to the client folder”
- “Archive all large files in this project to Drive”
- “Create a new client folder on Drive and upload the proposal”

## Inputs

- file-path — Local file path to upload
- folder-id — Google Drive folder ID
- workspace-hint — Client name or folder hint for resolution
- folder-name — Name for the new folder
- parent-folder — Parent folder ID or name
- file-path — File or directory to archive

## Outputs

- console
- folder-confirmation (markdown)
- same location as original file
- stub-notes (markdown)
- upload-confirmation (markdown)

