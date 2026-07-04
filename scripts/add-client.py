#!/usr/bin/env python3
"""
Add a new client to the RocketRush Content Engine database.
Usage: python3 add-client.py
"""

import json
import os
import shutil
from datetime import datetime

def add_client():
    print("\n=== RocketRush — New Client Onboarding ===\n")
    
    client_name = input("Client full name: ").strip()
    client_id   = client_name.lower().replace(" ", "-")
    niche       = input("Niche / industry: ").strip()
    icp         = input("Who is their audience: ").strip()
    posts_week  = input("Posts per week (default 3): ").strip() or "3"
    
    # Create client folder from template
    template_dir = "clients/_template"
    client_dir   = f"clients/{client_id}"
    
    if os.path.exists(client_dir):
        print(f"\nClient folder already exists: {client_dir}")
    else:
        shutil.copytree(template_dir, client_dir)
        print(f"\nCreated folder: {client_dir}")
    
    # Update client-config.json
    config_path = f"{client_dir}/client-config.json"
    with open(config_path, "r") as f:
        config = json.load(f)
    
    config["client_id"]       = client_id
    config["client_name"]     = client_name
    config["niche"]           = niche
    config["icp"]             = icp
    config["posts_per_week"]  = int(posts_week)
    config["onboarded_date"]  = datetime.now().strftime("%Y-%m-%d")
    
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    
    # Update master database
    db_path = "database/clients.json"
    with open(db_path, "r") as f:
        db = json.load(f)
    
    # Check if client already exists
    existing = [c for c in db["clients"] if c["client_id"] == client_id]
    if not existing:
        db["clients"].append({
            "client_id":      client_id,
            "client_name":    client_name,
            "niche":          niche,
            "active":         True,
            "onboarded_date": config["onboarded_date"],
            "posts_approved": 0,
            "posts_rejected": 0
        })
        db["total_clients"]  += 1
        db["last_updated"]    = datetime.now().isoformat()
        
        with open(db_path, "w") as f:
            json.dump(db, f, indent=2)
    
    print(f"""
Client added successfully.

Next steps:
1. Fill in: {client_dir}/voice-profile.md
2. Fill in: {client_dir}/content-pillars.md
3. Add stories: {client_dir}/story-bank.md
4. Run Fathom fetch if story call exists:
   python3 scripts/fetch-fathom-transcript.py {client_id}

Ready to generate content for {client_name}.
""")

if __name__ == "__main__":
    add_client()
