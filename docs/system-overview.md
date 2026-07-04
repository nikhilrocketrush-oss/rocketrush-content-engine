# System Overview

See the full documentation in:
`RocketRush-Content-Engine-Documentation.md`

This file is a quick reference for the team.

## Folder Map

| Folder | Purpose |
|---|---|
| `orchestrator/` | The RocketRush chatbot skill — install this in Claude |
| `skills/` | Install instructions for all 4 GitHub skills |
| `clients/` | One folder per client — voice profile, stories, post history |
| `database/` | Master client index and approved post log |
| `scripts/` | Python scripts for database operations |
| `docs/` | Full documentation |

## Daily Workflow

1. Open Claude Code → open `rocketrush-content-engine` project
2. Type: `/rocketrush-engine`
3. Select client
4. Select what to create
5. Approve calendar
6. Review final posts
7. Log approvals via `scripts/update-post-status.py`

## Client Folder Structure

```
clients/
└── snehall-desai/
    ├── client-config.json     ← niche, ICP, posting frequency
    ├── voice-profile.md       ← tone, vocabulary, banned words
    ├── content-pillars.md     ← 3 core topics with formats
    ├── story-bank.md          ← stories from calls + manifesto
    ├── post-history.json      ← all posts with approval status
    ├── manifesto.md           ← client manifesto document
    └── transcripts/           ← Fathom call transcripts
        └── 2026-06-30-story-call.txt
```
