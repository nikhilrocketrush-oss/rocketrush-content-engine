# Scripts

Python scripts for database operations and automation.

| Script | What it does |
|---|---|
| `add-client.py` | Onboard a new client into the database |
| `update-post-status.py` | Mark a post approved / rejected / edited |
| `fetch-fathom-transcript.py` | Pull transcript from Fathom via MCP |
| `generate-voice-profile.py` | Build voice profile from transcript + manifesto |

## Requirements
```
pip install requests python-dotenv
```

## Setup
Create a `.env` file in the root:
```
GITHUB_TOKEN=your_token_here
FATHOM_API_KEY=your_fathom_key_here
```
