# Database

Two files power the learning loop.

## clients.json
Master index of all RocketRush clients. One entry per client.
Updated when a new client is onboarded.

## approved-posts.json
Every post that was approved. Used to improve future drafts.
Updated every time an editor approves a post.

## How the Learning Loop Works
1. Post drafted by system
2. Editor reviews — approves, approves with edits, or rejects
3. `scripts/update-post-status.py` is called with the decision
4. Database updates automatically
5. Next draft for this client is better
