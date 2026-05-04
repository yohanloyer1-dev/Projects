# A/B PERSONA AGENT
# Role: tests whether persona visual variations improve performance.
# IMPLEMENT AFTER 30 DAYS OF FIRST CLIENT RUNNING — not before.

## STATUS: DEFERRED
Activate after: 30 days of stable c_001 operation, minimum 20 posts with perf_72h data.
Activation: set ab_persona_active=true in client_config (add column on activation).

## DESIGN

### Persona Variants
- Persona A: the established character (defined in persona.md)
- Persona B: slight visual variation only — different wardrobe palette, slightly faster pace
- Everything else identical: niche, topic, hooks, CTA, compliance
- Persona B spec stored in: clients/{CLIENT_ID}/persona-b.md (same format as persona.md)

### Selection Logic (built into Production Agent)
- Week N: check if A/B is active for this client
- If active: scripts idx=1,2,3,4 → Persona A. Script idx=5 → Persona B (20% = 1/5 videos)
- Store persona_variant in video_jobs (column already in schema)
- All 5 videos use the same script_json — only persona spec changes

### Tracking
Intelligence Agent reads video_jobs.persona_variant when computing weekly performance:
- Filter posts by persona_variant='A' → avg views, likes, watch_time
- Filter posts by persona_variant='B' → same metrics
- Track over 4 weeks minimum before drawing conclusions

### Decision at Week 4
If Persona B consistently outperforms A (>15% better avg views over 4 weeks):
  → Update persona.md to incorporate Persona B's winning elements
  → Keep Persona A spec archived in persona-a-archive.md
  → Note in memory.md: "Persona updated {DATE} based on A/B test"

If Persona A consistently outperforms B:
  → Archive Persona B spec as persona-b-retired.md
  → Note in memory.md: "Persona B retired {DATE} — Persona A wins"

If no significant difference (±5%):
  → Continue test 4 more weeks OR discontinue (operator decision)
  → Note in memory.md

## IMPLEMENTATION NOTES
- No separate n8n workflow needed — A/B logic is a branch inside Production Agent
- No new Supabase table needed — persona_variant column already on video_jobs
- Intelligence Agent already reads video_jobs — just needs filter by persona_variant
- Minimal footprint: this is a 20-line branch in Production Agent, not a separate system

## TRIGGER FOR ACTIVATION
Operator action: set client_config.higgsfield_character_id_b = {PERSONA_B_CHARACTER_ID}
When this field is non-null AND ab_persona_active=true → A/B kicks in for Production Agent
