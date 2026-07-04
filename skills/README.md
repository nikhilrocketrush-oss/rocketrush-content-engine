# Skills Installation Guide

Install these four skills in this exact order.

---

## Skill 1 — Algorithm Scorer (install first — zero setup)
**Repo:** `attainmentlabs/linkedin-algorithm-skill`
**Command:**
```
git clone https://github.com/attainmentlabs/linkedin-algorithm-skill.git
cp -r linkedin-algorithm-skill ~/.claude/skills/linkedin-algorithm
```
**Test:** Ask Claude: `/linkedin-algorithm score this post: [paste any post]`

---

## Skill 2 — LinkedIn Post Writer
**Repo:** `marian-kamenistak/linkedin-post-writing-skill`
**Command:**
```
git clone https://github.com/marian-kamenistak/linkedin-post-writing-skill.git
cp -r linkedin-post-writing-skill ~/.claude/skills/linkedin-post-writer
```
**Test:** Ask Claude: `write a LinkedIn post about [topic]`

---

## Skill 3 — Humanizer
**Repo:** `sergebulaev/linkedin-skills`
**Install via Claude Code:**
```
/plugin install linkedin-skills
```
**Test:** Ask Claude: `/humanizer clean this draft: [paste any post]`

---

## Skill 4 — Trend Research (/last30days)
**Repo:** `mvanhorn/last30days-skill`
**Install via Claude Code:**
```
/plugin marketplace add mvanhorn/last30days-skill
```
**First run:** The setup wizard activates automatically.
**Test:** `/last30days B2B founder branding India`

---

## Verification
After all four are installed, run:
```
/last30days test
/linkedin-algorithm score this: Hello world
```
If both respond, the stack is live.
