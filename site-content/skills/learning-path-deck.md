---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: learning-path-deck — ThirdBrain BOB skill
  description: 'Three-phase automation: capture screenshots and/or video during the learning path, then assemble into a branded PPTX deck.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: learning-path-deck
catLabel: documents
area: foundational
desc: Captures screenshots or recordings across the 10-stage learning path and assembles them into a branded PPTX walkthrough deck.
summary: 'Three-phase automation: capture screenshots and/or video during the learning path, then assemble into a branded PPTX deck.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[config, install]'
roles: '[]'
inputs:
- request — Which stage(s) to capture and why — drives stage selection and labelling for this run.
- stage — Learning-path stage number (1-10) the capture belongs to; sets the output filename prefix.
- label — Suffix appended to the screenshot filename to distinguish multiple captures of the same stage.
- mode — Which screen area PowerShell captures for this run, overriding the host config default. (primary | monitor | all | window | region)
- monitor — 1-based monitor number to capture when `mode` is `monitor`.
- region — `X,Y,Width,Height` pixel rectangle to capture when `mode` is `region`.
- host-config — Per-host default mode, monitor, and delay so capture behaves consistently across machines without CLI flags.
- output-dir — Directory the screenshots are written to, if the caller wants a location other than the default.
- request — Which stage is being recorded and why — drives labelling for this run.
- stage — Learning-path stage number (1-10) the recording belongs to; sets the output filename prefix.
- action — Whether this call begins or ends the ffmpeg recording for the stage. (start | stop)
- label — Suffix appended to the recording filename to distinguish multiple takes of the same stage.
- mode — What ffmpeg captures — the full desktop, one monitor, or a window matched by title. (desktop | monitor | title)
- title — Partial window-title match used to locate the capture target when `mode` is `title`.
- fps — Frames per second for the recording; trades file size against smoothness.
- screenshot-interval — Seconds between auto-captured, deduplicated screenshots taken during the recording; 0 disables auto-capture.
- host-config — Per-host default video mode, monitor, title, and fps so recording behaves consistently across machines.
- output-dir — Directory the recording is written to, if the caller wants a location other than the default.
- request — What the assembled deck is for — drives which optional flags (embed, pack, quality) are used.
- screenshots — Screenshot directory from the screenshot route, read back and assembled into slides.
- recordings — Recording directory from the recording route, read back and embedded or linked into the matching stage slides when present.
- video-quality — Re-encode preset applied to linked or embedded recordings, trading file size against fidelity. (original | hd | tiny)
- embed-video — Embed recordings directly in the PPTX instead of linking to external HTML player files.
- pack — Produce a self-contained distributable folder and zip alongside the PPTX.
- output-dir — Path the assembled PPTX is written to, if the caller wants a location other than the default.
- request — The end-to-end deck being requested — stage range, capture mode, and any assembly options.
- stage — Learning-path stage numbers (1-10) to capture and assemble in this run.
- mode — Capture mode applied across the requested stages, overriding the host config default. (primary | monitor | all | window | region | desktop | title)
- monitor — 1-based monitor number to capture when `mode` selects a specific monitor.
- label — Suffix appended to filenames to distinguish this run's captures from prior ones.
- video-quality — Re-encode preset applied to recordings during the assembly stage of this run. (original | hd | tiny)
- output-dir — Directory the screenshots, recordings, and deck are written to, if the caller wants a location other than the default.
outputs:
- Branded PPTX walkthrough deck assembled from all captured stages.
- Branded PPTX walkthrough deck assembled from the captured screenshots and recordings.
- Captured MP4 for the stage, from start to stop.
- Captured MP4s for every requested stage where recording was run.
- Captured PNG(s) for the requested stage(s), one file per capture.
- Captured PNGs for every requested stage.
- prefer a permanent directory)
prompts:
- Capture the learning path into a branded PPTX deck
- Build a visual walkthrough deck from the 10 onboarding stages
- Create a presentation of the learning path with screenshots
---
