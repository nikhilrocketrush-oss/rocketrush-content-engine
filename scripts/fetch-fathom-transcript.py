#!/usr/bin/env python3
"""
Fetch a client transcript from Fathom.
Usage: python3 fetch-fathom-transcript.py [client-id]

Note: Fathom is connected via MCP in Claude.
This script documents the manual fallback process.
For automatic Fathom fetch, use the orchestrator chatbot.
"""

import sys

def fetch_transcript(client_id):
    print(f"""
=== Fathom Transcript Fetch — {client_id} ===

Fathom is connected to your RocketRush Claude project via MCP.

To fetch automatically inside Claude, type:
  "Search Fathom for [client name] and pull the latest story call transcript"

Claude will:
  1. Search Fathom meetings by client name
  2. Pull the full transcript
  3. Feed it into voice extraction automatically

Manual fallback (if MCP is not active):
  1. Go to app.fathom.video
  2. Search for the client's name
  3. Open the meeting → Export transcript
  4. Save as: clients/{client_id}/transcripts/[date]-story-call.txt
  5. Then run: python3 scripts/generate-voice-profile.py {client_id}
""")

if __name__ == "__main__":
    client_id = sys.argv[1] if len(sys.argv) > 1 else input("Client ID: ").strip()
    fetch_transcript(client_id)
