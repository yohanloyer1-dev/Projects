# Agent Network Architecture — Gorgias Integrations Venture
**Date:** 2026-05-01 | **Status:** ACTIVE — governs all agent design decisions  
**Owner:** Yohan Loyer | **Environment:** Cowork (strategy/design) + Claude Code (build/run)

---

## Why This Exists

The Gorgias Integrations venture must operate at ≤20h/week for Yohan while generating
€2K–5K/mo MRR within 12 months. A single human reviewing research, writing code, synthesizing
decisions, and running outreach cannot hit both constraints simultaneously. The solution is a
network of specialized agents that work autonomously, share a common memory layer (GitHub), and
escalate to Yohan only when a real decision is required.

This is not a future aspiration. It is the operating model. Every task in AGENT-TASKS.md should
ultimately be routed to an agent, not to Yohan.

---

## Architecture Principles [from Anthropic's production research, 2026]

1. **GitHub is the nervous system.** All agents read from and write to the same repo. No agent
   stores state locally. No context lives only in a conversation.

2. **Specialization over generalism.** Each agent has one role, one set of tools, one output
   format. Agents that try to do everything do nothing well.

3. **Parallel over sequential.** Where tasks are independent, agents run simultaneously. The
   lead agent (Cowork Strategy) spawns subagents rather than queuing work.

4. **Escalate by exception.** Agents decide autonomously within defined thresholds. They only
   surface to Yohan when: (a) a gate criterion is ambiguous, (b) a decision has irreversible
   consequences, or (c) a new signal materially changes the strategy.

5. **Prompts are collaboration frameworks, not instructions.** Each agent's context pack defines
   its role, its tools, its output format, its escalation triggers, and its relationship to
   other agents. This is the primary engineering surface.

6. **Tools are as important as prompts.** Poor tool descriptions send agents down wrong paths.
   Every tool an agent uses needs a distinct purpose and a clear description.

---

## The Agent Roster

### AGENT-01: Strategy Agent (Cowork)
**Role:** Synthesizes intelligence, makes architecture decisions, updates roadmap, runs Ohtani Matrix  
**Rhythm:** On-demand (session-based). Future: weekly autonomous synthesis pass  
**Reads:** All of GitHub — decisions/, research/, AGENT-TASKS.md, parking-lot/  
**Writes:** decisions/, roadmap/, AGENT-TASKS.md updates, session-log.md  
**Escalates to Yohan when:** GO/NO-GO decisions, legal gates, pricing strategy  
**Context pack:** `agents/strategy-agent/CONTEXT.md`  
**Current status:** Active (this is the current Cowork session role)

---

### AGENT-02: Research Agent (n8n + Cowork)
**Role:** Continuous market intelligence — competitor moves, demand signals, API changes  
**Rhythm:** Weekly automated scan (n8n scheduler) + on-demand deep dives  
**Sources:** Reddit (r/ecommerce, r/gorgias, r/shopify), G2/Capterra reviews, Gorgias community,
ManoMano seller forums, competitor websites (Juble, ChannelReply, eDesk), Mirakl/ManoMano
developer changelogs  
**Reads:** research/signals-[last].md (for continuity), AGENT-TASKS.md  
**Writes:** research/signals-[date].md, flags competitor changes to decisions/  
**Escalates to Yohan when:** A competitor launches ManoMano support, a major pricing change,
a new API capability that changes Phase 2/3 viability  
**Context pack:** `agents/research-agent/CONTEXT.md`  
**Blockers:** T-016 (Reddit OAuth), T-017 (Firecrawl API) — Yohan must configure n8n credentials  
**Current status:** Not yet running. Must be built in n8n.

---

### AGENT-03: CTO Agent (Claude Code)
**Role:** Technical feasibility, integration builds, API mapping, code review  
**Rhythm:** On-demand, triggered by AGENT-TASKS.md entries reaching unblocked status  
**Reads:** architecture/, decisions/, integrations/ — boots from context pack, no human briefing  
**Writes:** integrations/manomano-gorgias/, architecture/feasibility-[date].md  
**Escalates to Yohan when:** API access denied, architectural ambiguity requiring product decision,
cost/complexity materially exceeds estimate  
**Context pack:** `agents/cto-agent/CONTEXT.md`  
**Current status:** Not yet active. Unblocked when T-008 + T-009 + T-010 are done.

---

### AGENT-04: Validation Agent (Cowork)
**Role:** Runs synthetic merchant/agency conversations before Yohan invests real time  
**Rhythm:** On-demand, before each real validation round  
**Reads:** validation/validation-script-[date].md, research/competitive-intelligence-[date].md  
**Writes:** validation/synthetic-[date].md — pre-filters which conversations are worth running live  
**Escalates to Yohan when:** Synthetic pass reveals script needs rewriting, or a new objection
pattern emerges that changes the value proposition  
**Context pack:** `agents/validation-agent/CONTEXT.md`  
**Current status:** Can run now. No technical blockers.

---

### AGENT-05: Ops Agent (Cowork + n8n)
**Role:** Client onboarding, billing tracking, MRR dashboard, SLA monitoring  
**Rhythm:** Daily automated checks (n8n) + on-demand reporting  
**Reads:** ops/clients.md, ops/mrr-[date].md, integrations/ health status  
**Writes:** ops/mrr-[date].md, ops/incidents-[date].md, flags SLA breaches  
**Escalates to Yohan when:** Client churn signal, billing failure, integration downtime >30min  
**Context pack:** `agents/ops-agent/CONTEXT.md`  
**Current status:** Not yet needed. Activates at first paying client.

---

### AGENT-06: Outreach Agent (Cowork + Gmail MCP)
**Role:** Drafts merchant and agency outreach, follows up on pipeline, manages sequences  
**Rhythm:** On-demand (triggered by pipeline entries in Notion/GitHub)  
**Reads:** roadmap/agency-agreement-template.md, validation/tracking, ops/clients.md  
**Writes:** Drafts only — Yohan reviews and sends. Never sends autonomously.  
**Escalates to Yohan when:** Always — outreach goes to Yohan for review before send  
**Context pack:** `agents/outreach-agent/CONTEXT.md`  
**Current status:** Not yet needed. Activates at T-010 completion.

---

## Shared Memory Layer

All agents read and write to the same GitHub repo: `yohanloyer1-dev/Projects`

```
/Gorgias-Integrations/
├── AGENT-TASKS.md          ← shared task board (all agents read/write)
├── agents/                 ← context packs for each agent role
│   ├── strategy-agent/CONTEXT.md
│   ├── research-agent/CONTEXT.md
│   ├── cto-agent/CONTEXT.md
│   ├── validation-agent/CONTEXT.md
│   ├── ops-agent/CONTEXT.md
│   └── outreach-agent/CONTEXT.md
├── ops/                    ← operational layer (Ops Agent writes here)
│   ├── clients.md
│   ├── mrr-template.md
│   └── incidents/
├── research/               ← Research Agent outputs
├── architecture/           ← CTO Agent inputs/outputs
├── decisions/              ← Strategy Agent outputs
├── validation/             ← Validation Agent outputs
├── integrations/           ← CTO Agent builds here
└── parking-lot/            ← legal gates, blocked items
```

---

## Agent Communication Protocol

Agents do not talk to each other in real-time (no message passing between live sessions).
They communicate through GitHub:

1. **AGENT-TASKS.md** — the shared task board. An agent marks a task `done` and another
   picks up the downstream task on its next run.
2. **Structured output files** — each agent's output is a named, dated Markdown file in the
   correct subfolder. Naming convention: `[type]-[date].md` (e.g., `signals-2026-05-08.md`)
3. **Flags in decisions/** — when an agent discovers something that requires Strategy Agent
   attention, it writes a `flag-[date].md` to `decisions/` with a clear escalation trigger.

---

## Escalation Thresholds (Yohan's decision surface)

Yohan should only be needed for:

| Trigger | Agent | Why Yohan |
|---|---|---|
| GO/NO-GO on a new integration | Strategy | Irreversible resource commitment |
| Legal gate reached | Strategy | Employment/IP risk |
| Competitor launches ManoMano→Gorgias | Research | Changes entire wedge strategy |
| API access permanently denied by ManoMano | CTO | Kills Phase 1 entirely |
| First paying client signs | Ops | Pricing/DPA confirmation |
| Validation pass rate <3/5 | Validation | Pivot or persist decision |
| Outreach draft ready for review | Outreach | Always — Yohan sends manually |

Everything else: agents decide and document.

---

## Keeping This System Current

This architecture document is a living file. It must be updated when:
- A new agent role is identified
- An existing agent's tools change (new MCP, new n8n node)
- Anthropic releases new agent capabilities (Claude Managed Agents, Agent Teams in Claude Code)
- A competitor or partner releases an API that changes what's automatable

**Assigned:** Strategy Agent reviews this file at the start of each monthly synthesis pass.
**Research Agent flag:** Any Anthropic release note mentioning agents, MCP, or orchestration
triggers an update review of this document.

---

## Technology Stack (Current + Planned)

| Layer | Tool | Status |
|---|---|---|
| Strategy reasoning | Cowork (Claude Sonnet/Opus) | Active |
| Code + feasibility | Claude Code (Claude Sonnet) | Ready, awaiting T-008/T-009 |
| Scheduling / routing | n8n (self-hosted or cloud) | Awaiting T-016/T-017 setup |
| Shared memory | GitHub (yohanloyer1-dev/Projects) | Active |
| Agent orchestration (future) | Claude Code Agent Teams (experimental) | Monitor — not yet stable |
| Managed agent runtime (future) | Claude Managed Agents (API beta) | Evaluate Q3 2026 |
| Inter-agent comms | GitHub file protocol (current) | Active |
| Client/ops tracking | Notion + ops/ folder | Ops Agent only, on first client |

