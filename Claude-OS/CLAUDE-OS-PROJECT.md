# Claude OS — Project Hub

**Status:** 🟡 Discovery & Definition  
**Started:** 2026-04-20  
**Owner:** Yohan Loyer (yohanloyer1@gmail.com)  
**Ohtani fit:** ✅ Active cash (consulting/setup) → Scalable asset (product/content) → compounding

---

## The Idea

A productized, done-with-you Claude-powered operating system for entrepreneurs and busy professionals. Not a template. Not a chatbot. A real, working system built around their specific life and business — installed, configured, and running — that handles organization, prioritization, automation, and memory.

**Yohan is customer #0.** Everything being built for Yohan's own workflow is the product. The system is being dog-fooded in real time.

---

## Suggested Product Name

**ClarisOS** — from Latin *claris* (clear, bright). Positioning: clarity through systems.  
Alternatives: **Operator**, **Basecamp AI**, **Clarity OS**, **Claude Stack**

---

## The Market Gap (from research)

- **getclaudeos.com** exists — $49 DIY template bundle, 33 modes, 158 skill files. No setup support, no customization, no consulting.
- **Notion OS templates** (August Bradley, Forte Labs) — $100–$249, pure DIY, abandoned within weeks.
- **Enterprise AI consulting** — $15K–$35K projects, not accessible to solopreneurs.
- **The gap:** Premium ($500–$2,500), done-with-you, personalized, working system — with proof. Nobody owns this.

---

## Business Model

| Tier | What | Price |
|------|------|-------|
| **Self-serve** | Downloadable template + instructions | $97–$197 one-time |
| **Done-with-you** | 3-session setup + 30 days support | $500–$1,500 |
| **Done-for-you** | Full custom build + 3 months retainer | $2,500–$5,000 setup + $500/mo |

Target: 5–8 DWY/DFY clients/month = €4K–€12K MRR within 6 months.

---

## Ideal Customer

- Solopreneur or 1–3 person agency/consultancy
- Revenue exists ($5K–$30K/month) but growth stalling due to chaos, not market
- Tried Notion, Todoist, ClickUp — abandoned all of them
- Works 50+ hours/week, still feels behind
- Often "ADHD-ish" — smart, motivated, but traditional systems don't stick
- Age 28–42, primarily LinkedIn/Twitter/Reddit active
- Willing to pay for something that actually works

---

## Core Pain Points We Solve

1. **Prioritization void** — 17 things all feel urgent, paralysis sets in
2. **Tool graveyard** — 40 min/day maintaining the system instead of working
3. **Context switching** — no single system holds all threads together
4. **Memory loss** — decisions, context, project state disappear between sessions
5. **Reactive trap** — inbox/fires always win over strategic work
6. **No automation** — repetitive tasks still done manually every week

---

## What the System Includes

- **CLAUDE.md** — personal memory file (who you are, your projects, your context)
- **TASKS.md** — master task list, always in sync
- **Session protocol** — 6-step startup that loads full context every time
- **Memory routing** — maps projects to the right context files automatically
- **Scheduled wrap-up** — daily 5:30pm task that pushes everything to GitHub
- **Dashboard** — interactive task manager (GitHub Pages, Gist sync)
- **Project memory files** — deep context per client/project
- **Ohtani Matrix** — decision OS that filters every task against your locked goal
- **MCP integrations** — Calendar, Gmail, Notion, Slack, Linear, Granola, n8n connected
- **Voice notes inbox** — WhatsApp/Telegram → Whisper → inbox.md via n8n

---

## Acquisition Strategy

**Primary channel: LinkedIn** (Yohan already has 5,945 followers, Gorgias/CX authority)
**Secondary: Reddit** — organic, search-indexed, high-trust pain point conversations
**Content types:** infographics, system demos, before/after automation screenshots, short-form video walkthroughs, "building in public" series

**Content pillars for Claude OS:**
1. "Here's how I run my entire business with Claude" (proof)
2. "The system that replaced Notion, Todoist, and 4 other apps" (contrast)
3. "Building in public: selling a Claude OS" (journey)
4. "Entrepreneur pain point" posts + soft CTA to the system (acquisition)
5. Demo videos: 60-second walkthrough of a session startup (hook)

---

## Tech Stack

| Layer | Tool |
|-------|------|
| AI backbone | Claude (Cowork + API) |
| Memory/files | GitHub (source of truth) |
| Task manager | dashboard.html (GitHub Pages) |
| Automation | n8n (self-hosted or cloud) |
| Website | Lovable (dark, minimalist) |
| Payments | Stripe |
| CRM | Notion or Attio MCP |
| Content | LinkedIn + Reddit + short-form video |
| MCP integrations | Calendar, Gmail, Notion, Slack, Granola, Linear |

---

## MCP Ecosystem (available now)

**Already covered by existing MCPs:**
- Google Calendar, Gmail, Notion, Slack, Granola (meetings), Linear, Asana, HubSpot, n8n, Make, Zapier

**Gaps to build custom:**
- WhatsApp/Telegram ingestion (n8n + Whisper — already planned)
- Financial tracking (Stripe/Wise — no MCP yet)
- LinkedIn/Twitter publishing (no native MCP)
- Reddit monitoring (no MCP — build via n8n Reddit API)
- Time tracking (no Toggl/Harvest MCP)

---

## File Structure

```
Claude-OS/
├── CLAUDE-OS-PROJECT.md        ← This file (project hub)
├── memory/
│   └── claude-os-memory.md    ← Session memory for this project
├── research/
│   ├── market-research.md     ← Market landscape + competitors
│   ├── pain-points.md         ← Customer pain points + ICP
│   └── pricing-positioning.md ← Pricing models + positioning
├── product/
│   ├── product-definition.md  ← What's included, tiers, delivery
│   └── install-guide.md       ← How to install for a client
└── marketing/
    ├── content-strategy.md    ← Pillars, formats, cadence
    └── content-backlog.md     ← Post ideas + drafts
```

---

## Next Steps

1. [ ] Populate research files from agent findings (this session)
2. [ ] Define product tiers in detail (product-definition.md)
3. [ ] Create Lovable website brief
4. [ ] Draft first 5 LinkedIn posts (building in public series)
5. [ ] Build Reddit monitoring via n8n (pain point listening)
6. [ ] Name decision — ClarisOS or alternatives?

---

## Memory Routing

When working on Claude OS → Read: `Claude-OS/memory/claude-os-memory.md`
