#!/usr/bin/env python3
"""
Generate a voice profile from transcript + manifesto.
Usage: python3 generate-voice-profile.py [client-id]

This script prepares the input for Claude to analyse.
The actual analysis is done inside Claude using the voice extraction prompt.
"""

import sys
import os
import json

VOICE_EXTRACTION_PROMPT = """
You are building a voice profile for a LinkedIn ghostwriting client.

Analyse the transcript and manifesto below and extract:

1. TONE — How do they sound? Formal/casual, serious/humorous, warm/direct?
2. SENTENCE PATTERN — Short fragments? Long narrative? Mixed rhythm?
3. WORDS THEY OWN — Phrases and vocabulary they naturally use
4. WORDS THEY NEVER USE — Language that would sound wrong from them
5. HOW THEY OPEN — What hook patterns repeat naturally in how they talk?
6. HOW THEY CLOSE — How do they end stories or make points?
7. THEIR WORLDVIEW — What do they fundamentally believe about their industry?
8. THEIR BEST STORY — The one story from this material most likely to stop a scroll
9. CONTENT PILLARS — 3 topics they speak about with genuine authority
10. WHAT MAKES THEM DIFFERENT — The one thing no other person in their niche says

Be specific. Do not say "casual tone." Say exactly what makes it casual.
Do not say "uses simple language." Name the actual words.

--- TRANSCRIPT ---
{transcript}

--- MANIFESTO ---
{manifesto}

Output the voice profile in the exact format of the voice-profile.md template.
"""

def generate_profile(client_id):
    client_dir  = f"clients/{client_id}"
    transcript_dir = f"{client_dir}/transcripts"
    manifesto_path = f"{client_dir}/manifesto.md"
    
    # Read transcript
    transcript_text = ""
    if os.path.exists(transcript_dir):
        for fname in sorted(os.listdir(transcript_dir)):
            if fname.endswith(".txt"):
                with open(f"{transcript_dir}/{fname}") as f:
                    transcript_text += f.read() + "\n"
    
    # Read manifesto
    manifesto_text = ""
    if os.path.exists(manifesto_path):
        with open(manifesto_path) as f:
            manifesto_text = f.read()
    
    if not transcript_text and not manifesto_text:
        print(f"No transcript or manifesto found for {client_id}")
        print(f"Add files to: {client_dir}/transcripts/ and {client_dir}/manifesto.md")
        return
    
    prompt = VOICE_EXTRACTION_PROMPT.format(
        transcript=transcript_text or "No transcript available",
        manifesto=manifesto_text or "No manifesto available"
    )
    
    output_path = f"{client_dir}/voice-extraction-prompt.txt"
    with open(output_path, "w") as f:
        f.write(prompt)
    
    print(f"""
Voice extraction prompt ready.

Next step:
1. Open Claude
2. Start a new conversation
3. Paste the contents of: {output_path}
4. Copy Claude output into: {client_dir}/voice-profile.md

Or run it automatically in the RocketRush orchestrator:
"Build voice profile for [client name]"
""")

if __name__ == "__main__":
    client_id = sys.argv[1] if len(sys.argv) > 1 else input("Client ID: ").strip()
    generate_profile(client_id)
