---
description: 'Every skill in this library was written against one folder tree — , , <!-- context-pack: ok — definition: the pack documents the default layout it maps --> — and most of them name those folders literally, so moving the library to a workspace <!-- context-pack: ok — definition: the pack documents the default layout it maps --> whose folders are called something else makes every one of those references wrong. A context pack is a skill folder carrying a `context.yaml` manifest that maps logical keys (`company.profile`, `client.deliverables`, `output.scratch`) to that workspace''s real paths, plus a one-line `summary` per key so an agent knows what it will find before opening it, plus the workspace''s own filing conventions. Skills resolve keys through this skill; the pack is data and can be swapped per customer or per environment.'
title: context-pack
---

# context-pack

Every skill in this library was written against one folder tree — , , <!-- context-pack: ok — definition: the pack documents the default layout it maps --> — and most of them name those folders literally, so moving the library to a workspace <!-- context-pack: ok — definition: the pack documents the default layout it maps --> whose folders are called something else makes every one of those references wrong. A context pack is a skill folder carrying a `context.yaml` manifest that maps logical keys (`company.profile`, `client.deliverables`, `output.scratch`) to that workspace's real paths, plus a one-line `summary` per key so an agent knows what it will find before opening it, plus the workspace's own filing conventions. Skills resolve keys through this skill; the pack is data and can be swapped per customer or per environment.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Resolves where company, client, project, resource and output files live through a portable context.yaml manifest, so skills ask for logical keys like company.profile or…

## How you ask

- “Create a context pack for the prototype vault — clients live under Customers/ there”
- “Where does a meeting note for acme-industries go?" · "Make proposal-writer portable”
- “Which pack is active and where did it come from?”

## Inputs

- key — Logical key such as company.profile or client.meetings; mutually exclusive with route
- route — Entity type whose new-note destination is wanted, e.g. meeting or deal
- id — Client, project, lead or partner id for keys and routes containing {id}
- pack — Manifest file or pack folder to use instead of discovery
- pack-id — Kebab-case id; the folder becomes context-{pack-id}
- title — Human name of the workspace, e.g. Acme Consulting
- layout — Start from every framework key (default, edit down) or only the nine core keys (minimal, build up); pick minimal for a workspace that is nothing like the numbered tree (default | minimal)
- output — Folder to create; defaults to the skills root of the current workspace
- pack — Manifest file or pack folder; defaults to the active pack
- strict — Fail on warnings too — use before shipping a pack to a customer
- pack — Manifest file or pack folder describing the workspace to build; defaults to the active pack
- output — Workspace root to create or fill in
- templates — Source templates folder to render from; defaults to the templates of the workspace the running skills belong to
- write — Create the folders and files; without it the run is a dry run
- skill-name — Skill folder to migrate
- skill-md — The skill contract being made path-independent

## Outputs

- Human-readable side of the same pack
- Same skill, paths expressed as keys; audit --check exits 0
- The note templates rendered for this pack, including a client template named with its client.* keys
- The pack copied to the new workspace's root, so every skill discovers it there
- The workspace map; every path and summary edited from the scaffold
- context.yaml
- resolved-path (text)
- scaffold-report (text)
- stdout
- validation-report (text)
- {skills.root}/context-{pack-id}/
- {skills.root}/context-{pack-id}/context.yaml
- {skills.root}/{skill-name}/
- {vault.templates}/

