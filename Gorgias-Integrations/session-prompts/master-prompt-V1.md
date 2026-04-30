Session initialization — run this before anything else:

Check whether /Gorgias-Integrations/ exists in yohanloyer1-dev/Projects on GitHub.

If it does not exist:

Create the folder structure: research/, architecture/, roadmap/, validation/, decisions/, parking-lot/, integrations/, agents/
Create /Gorgias-Integrations/parking-lot/pre-launch-checklist.md with the following hard gates — do not remove any before launch:
not done
IP assignment + non-compete review with a lawyer
not done
Gorgias tech partner program — evaluate terms, apply only after leaving Gorgias or getting explicit clearance
not done
GDPR/DPA compliance review — data processing agreements verified by a lawyer for every merchant contract
not done
Gorgias trademark and brand use clearance
not done
Employment conflict check — no public launch before all above are resolved
Create /Gorgias-Integrations/decisions/venture-decisions.md with frontmatter (last_updated, session_type: cowork, status: active) and a summary of decisions already made: dual delivery architecture (HTTP widget for display / polling service for channels), dual GTM, agency moat approach, Notion as operational layer, GitHub as technical memory, cockpit scope
Commit both files to main with message: Init: Gorgias Integrations venture folder structure
If the commit fails for any reason: stop, report the full error, and do not proceed to Step 1. Retry up to 2 times with 30-second gaps. If still failing, ask Yohan to confirm GitHub access before continuing. Do not proceed with partial initialization.
Confirm in chat before proceeding to Step 1
If the folder already exists: pull latest from main, read decisions/venture-decisions.md and parking-lot/pre-launch-checklist.md to resume with full context, confirm in chat, then proceed.

Who I am: Yohan Loyer. Partner Manager at Gorgias EMEA — 5+ years on the platform, currently managing agency partnerships across Europe. I'm building a Gorgias-specialist agency on the side with two active freelance clients. My strategic goal: €50K net/year within 3 years, ≤20h/week, without full-time employment. Tech stack: Claude (Cowork + Code), n8n, Notion, GitHub as shared state layer.

The idea: Build a paid integration layer between Gorgias and tools that have no native connection — that neither Gorgias nor its app partners are actively building. Two delivery architectures depending on integration type:

(1) Data-display integrations (loyalty points, review history, subscription status visible inside the Gorgias sidebar) — delivered as a Gorgias HTTP widget: Gorgias calls your endpoint when an agent opens a ticket, you return data, it renders in the sidebar. No separate app install required by the merchant, configured via Gorgias Settings. Target build time: 15–25 days.

(2) Channel integrations (Amazon, Cdiscount, ManoMano messages flowing into Gorgias as tickets) — delivered as a polling/push service: n8n or a lightweight server polls the marketplace API on a schedule and creates Gorgias tickets via the REST API. These are NOT HTTP widgets. Target build time: 45–90 days. The CTO Agent must specify which architecture applies to each integration before any build begins.

Revenue model: fixed monthly fee for data-display integrations, usage/ticket-based pricing for channel integrations.

GTM model — dual channel:

Direct to merchants: monthly subscription, self-serve or agency-assisted onboarding
Through Gorgias agencies: agencies charge clients a one-time implementation fee and earn recurring revenue by recommending or reselling the integration — making building it themselves economically irrational
Agency pricing placeholder to validate: €500–2,000 one-time setup per client + €20–50/mo per merchant they manage on the platform
My unfair advantages:

Deep insider knowledge of which integrations Gorgias customers request most — I'll use this to form hypotheses, but validate them against public sources only before committing
Direct relationships with Gorgias agency partners across EMEA who could become the first resellers
Technical familiarity with the Gorgias API, HTTP integration layer, and widget system
This could be a product arm of my existing agency or a standalone SaaS venture
Non-negotiable constraints (Ohtani Matrix):

Must reach €2K–5K/mo MRR within 12 months
Must not require more than 15–20h/week to operate once built
Must be lean — no full team, automated wherever possible
Must be buildable with: Claude, n8n, Gorgias API, standard REST integrations
Must not conflict with my Gorgias employment — no use of internal Gorgias systems, no applying to the Gorgias tech partner program until after leaving or getting explicit clearance
Do not proceed to Steps 4–5 until Step 3 produces a clear go decision. If the idea doesn't survive validation, we pivot — not build.
Session architecture — enforce this throughout:

Before recommending any action, specify:

(a) Environment: Cowork for strategy, research synthesis, writing, client ops, agency relationships; Claude Code for API reading, integration building, agent tooling, feasibility assessment; n8n for scheduling, triggering, and routing only — do not assign LLM reasoning to n8n

(b) GitHub output: every output writes to yohanloyer1-dev/Projects under /Gorgias-Integrations/ — subfolders: research/, architecture/, roadmap/, validation/, decisions/, parking-lot/, integrations/, agents/ — date-prefixed filenames — so any future session resumes without relying on conversation history

(c) Notion (via MCP): operational layer only — pipeline, agency CRM, ideation. GitHub is technical memory. If Notion MCP is unavailable, log items to parking-lot/notion-queue-[date].md and move manually. Do not block on MCP availability.

(d) One-time vs recurring: flag whether each task is a one-time output or a recurring automated process. Nothing lives only in a conversation.

Tooling layer:

Skills (gorgias-helpcenter-scrape, mcp-builder, partner-customer-extractor, schedule): confirm availability before invoking. If unavailable, use Bash or GitHub MCP as fallback and note the gap in parking-lot/pre-launch-checklist.md.
Gorgias MCP (Composio): evaluate as a building block vs competitor before building anything custom.
Web research — environment-aware: In Cowork sessions (Steps 1–3): Use Cowork's native browsing as the primary tool — it may access pages, including auth-gated ones, that WebFetch cannot. If a page fails, fall back to WebSearch. For Gorgias developer docs, try native browsing first — if it fails, access the Gorgias Public API Postman workspace (no Gorgias login required) in your browser and paste relevant sections into the session. In Claude Code sessions (Steps 4–5): (1) WebSearch — baseline; (2) Chrome MCP if configured — for auth-gated pages using Yohan's existing browser session; (3) Firecrawl API — for bot-protected pages and scheduled n8n research jobs; (4) WebFetch — last resort only; (5) Yohan pastes content — when all else fails for Gorgias docs. In both environments: every demand signal claim must be grounded in a live source. Not training data.
Gorgias API docs: before any technical build, Yohan provides the HTTP widget spec, ticket creation endpoint, and channel integration guide — from native browsing, the Postman workspace, or direct copy from browser. The CTO Agent must not proceed on training data alone — flag if context is missing.
Parking lot: Maintain parking-lot/pre-launch-checklist.md throughout every session. Add any new pre-launch gates discovered. Never remove existing gates.

Work through these in order. Do not skip ahead.

Step 1 — Challenge the idea.

Be a demanding co-founder, not a validator. Address all of the following:

Moat: Could Gorgias build this natively? What signals exist they will or won't? What's the realistic window?
Competition: Does anything already adequately solve this for Gorgias merchants? Check: Gorgias App Store, Composio, Zapier MCP, Truto, Merge, Alloy. Where are their gaps?
TAM: Show the math at €50/mo, €100/mo, and €200/mo per direct merchant. Then show agency channel math separately.
Revenue model: Comparable tools (Alloy, Truto, Merge) charge developers and agencies, not merchants. Should I charge agencies instead, or both? What are the channel conflict risks?
Agency moat: What stops an agency from building this themselves once they've seen it work? At what agency size does in-house become rational, and how do I stay ahead of that threshold?
Employment + IP risk: What specifically would a lawyer need to verify before launch? Does the tech partner program create a second conflict given my employment?
Technical form risk: Downside scenario if Gorgias deprecates the HTTP integration layer? Fallback architecture? For channel integrations, risk if a marketplace restricts API access?
GDPR: Even pass-through processes personal data under GDPR Article 4(2). Flag: (a) DPA clauses needed in every merchant contract, (b) server log retention policy for PII, (c) data processor registration requirements in France, (d) what the privacy-first architecture must include beyond no-storage to be defensible.
Tech partner program as asset: Separately from the compliance risk — what does the program offer (marketplace listing, co-selling, customer introductions, revenue share)? Is there a path to membership post-employment or with written clearance? What would a Gorgias marketplace listing be worth in annual distribution value? This may be the most important growth lever available — assess it as an asset, not just a gate.
Fallback: If the idea isn't viable, recommend 2 alternative directions using the same unfair advantages before ending the session.
Step 2 — Map the opportunity.

Using public sources only — validate my insider hypothesis, do not rely on it:

(a) Which tools have the most Gorgias customer overlap but no integration today?
(b) Which categories are highest-pain: marketplaces, ERPs, loyalty/reviews/subscriptions, returns, other?
(c) Which are feasible — HTTP widget (15–25 days) or channel integration (45–90 days)? Apply timeline by architecture type.

My strongest hypothesis: loyalty/reviews/subscription tools — Yotpo, Okendo, Smile.io, LoyaltyLion, Stamped, Recharge. Challenge or confirm with evidence.

Citation requirement: For every demand signal claim, quote the source URL, date, and exact supporting text. If no live source is available, mark as [UNVERIFIED — training data only] and flag for Yohan to validate manually. Unverified claims cannot count toward the 2-source threshold.

For the top 2–3 opportunities, produce a merchant profile: Gorgias plan tier, monthly order volume range, primary platform. This feeds Step 3 directly — do not leave Step 2 without it.

Step 3 — Define the wedge.

Recommend the single best first integration: highest demand, lowest complexity, fastest path to €500 MRR. State reasoning explicitly, including which delivery architecture it uses.

For the first 3 merchant customer types: Gorgias plan tier, monthly order volume, platform, and why highest willingness to pay.

For the first 2 agency partner profiles: typical client size, implementation vs strategy-only, and what arrangement makes them more money recommending me than building themselves.

Go decision — all four required. If any are missing, it's a no:

Demand signal from at least 2 independent public sources — no [UNVERIFIED] claims counting toward threshold
No existing solution that adequately solves this for Gorgias merchants today
Technical feasibility within architecture-appropriate timeline (HTTP widget: 15–25 days; channel: 45–90 days)
Realistic path to €2,000 MRR within 12 months — show the math for the recommended wedge specifically. Model direct and agency channels separately. The €50/mo price point is only viable if the agency channel adds sufficient volume.
If it's a no, recommend a pivot before proceeding.

Step 4 — Design the intelligence layer.

Architect a lightweight research radar using Claude + n8n:

Reddit monitoring: use n8n's native Reddit node with OAuth — not scraping
G2/Capterra monitoring: use Firecrawl via n8n HTTP node
API doc parsing: Claude Code only using Firecrawl or Chrome MCP — not n8n
Weekly output: research/signals-[date].md
For each component: environment, GitHub output path, how the next session resumes without conversation history.

Define AGENT-TASKS.md schema in /Gorgias-Integrations/ — columns: Task ID | Task | Owner (Cowork/Code/n8n) | Status (todo/in-progress/blocked/done) | Blocked by (Task ID or blank) | GitHub output path | Success metric | Last updated. Every task needs a success metric. Blocked tasks name the blocking Task ID explicitly.

Step 5 — 90-day execution roadmap.

Week 1–2: Validate wedge with 5 conversations — 3 merchants, 2 agency partners. Provide two scripts: merchant version and agency version (4–5 questions each, confirm demand without revealing the idea). Output: validation/validation-script-[date].md
Week 3–6: Build v1. CTO Agent (Claude Code) reads API docs provided by Yohan, produces architecture/[integration-name]-feasibility-[date].md, scaffolds code in integrations/[integration-name]/
Week 7–10: First 3 paying customers, at least 1 via agency. First partner agreement drafted. Output: roadmap/agency-agreement-template-[date].md
Week 11–12: Systematize delivery. Define second integration. Build ops cockpit as static HTML dashboard at /Gorgias-Integrations/ops/cockpit.html, deployed via GitHub Pages — same pattern as Yohan's existing dashboard. Claude Code builds it. Shows: MRR by channel, active integrations, agency pipeline, weekly research output. This is what enables ≤20h/week at scale — do not skip it.
For each phase: environment, GitHub output path, success metric — including one agency-specific metric per phase.

Start with Step 1. Do not proceed to Step 2 until Step 1 stress-test is complete. Do not proceed to Steps 4–5 until Step 3 produces a clear go decision.
