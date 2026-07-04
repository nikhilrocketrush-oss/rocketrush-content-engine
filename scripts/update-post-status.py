#!/usr/bin/env python3
"""
Update post status after editor review.
Usage: python3 update-post-status.py
"""

import json
from datetime import datetime

def update_post():
    print("\n=== RocketRush — Post Review Logger ===\n")
    
    client_id  = input("Client ID (e.g. snehall-desai): ").strip()
    post_topic = input("Post topic (brief description): ").strip()
    status     = input("Status — approved / approved-with-edits / rejected: ").strip()
    score      = input("Algorithm score (e.g. 7.8): ").strip()
    notes      = input("Editor notes (optional): ").strip()
    
    post_record = {
        "client_id":   client_id,
        "topic":       post_topic,
        "status":      status,
        "algo_score":  float(score) if score else None,
        "editor_notes": notes,
        "date":        datetime.now().strftime("%Y-%m-%d"),
        "timestamp":   datetime.now().isoformat()
    }
    
    # Update client post-history.json
    history_path = f"clients/{client_id}/post-history.json"
    try:
        with open(history_path, "r") as f:
            history = json.load(f)
        history["posts"].append(post_record)
        with open(history_path, "w") as f:
            json.dump(history, f, indent=2)
        print(f"  ✓ Updated: {history_path}")
    except FileNotFoundError:
        print(f"  ✗ Client folder not found: {client_id}")
        return
    
    # Update approved-posts.json if approved
    if "approved" in status:
        db_path = "database/approved-posts.json"
        with open(db_path, "r") as f:
            db = json.load(f)
        db["posts"].append(post_record)
        db["total_approved"] += 1
        db["last_updated"]    = datetime.now().isoformat()
        with open(db_path, "w") as f:
            json.dump(db, f, indent=2)
        print(f"  ✓ Added to approved-posts database")
    
    # Update client totals in master database
    clients_path = "database/clients.json"
    with open(clients_path, "r") as f:
        clients_db = json.load(f)
    for c in clients_db["clients"]:
        if c["client_id"] == client_id:
            if "approved" in status:
                c["posts_approved"] = c.get("posts_approved", 0) + 1
            elif status == "rejected":
                c["posts_rejected"] = c.get("posts_rejected", 0) + 1
    clients_db["last_updated"] = datetime.now().isoformat()
    with open(clients_path, "w") as f:
        json.dump(clients_db, f, indent=2)
    
    print(f"""
Post logged successfully.
Client: {client_id}
Status: {status}
The system will use this to improve future drafts.
""")

if __name__ == "__main__":
    update_post()
