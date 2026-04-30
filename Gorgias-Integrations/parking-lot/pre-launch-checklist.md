# Pre-Launch Checklist — Gorgias Integrations Venture

> Gates are additive. Never remove an existing gate. Add new ones as discovered.
> Status: `not done` | `in progress` | `done`

---

## Legal & IP

- [ ] **IP assignment + non-compete review** — Lawyer must confirm that integration code built outside Gorgias systems does not trigger IP assignment clauses or non-compete restrictions in current employment contract. **BLOCKS: public launch, any merchant contract.**

- [ ] **Gorgias tech partner program — terms review** — Evaluate program terms in full before applying. Apply only after leaving Gorgias or obtaining explicit written clearance from Gorgias. **BLOCKS: marketplace listing, co-selling.**

- [ ] **GDPR / DPA compliance review** — Even pass-through architectures process personal data under GDPR Art. 4(2). Lawyer must verify: (a) DPA clauses in every merchant contract, (b) server log retention policy for PII, (c) data processor registration requirements in France, (d) privacy-first architecture is defensible. **BLOCKS: any live merchant data flowing through the system.**

- [ ] **Gorgias trademark and brand use clearance** — Verify permissible use of "Gorgias" in product name, marketing copy, and integration descriptions. **BLOCKS: public marketing, domain registration.**

- [ ] **Employment conflict check** — All above legal gates resolved before any public launch, press, or public GitHub repo linking to this venture. **MASTER GATE — BLOCKS ALL.**

---

## Technical

- [ ] **Gorgias HTTP widget spec confirmed** — Yohan pastes spec from native browser / Postman workspace before any display integration build begins. Do not build on training data alone.

- [ ] **Channel integration API docs confirmed** — For each marketplace (Amazon, Cdiscount, ManoMano, etc.), Yohan confirms API access tier, rate limits, and ToS before build begins.

- [ ] **Fallback architecture defined** — If Gorgias deprecates HTTP integration layer, fallback plan documented in architecture/fallback-architecture.md.

---

## Business

- [ ] **Go decision from Step 3** — All 4 criteria met (2 independent demand sources, no adequate existing solution, technical feasibility, path to €2K MRR in 12 months). **BLOCKS: any build work.**

- [ ] **5 validation conversations completed** — 3 merchants + 2 agency partners. Output in validation/validation-script-[date].md.

- [ ] **First agency partner agreement drafted** — Template in roadmap/agency-agreement-template-[date].md.

---

_Last updated: 2026-04-30 | Session type: Cowork_
