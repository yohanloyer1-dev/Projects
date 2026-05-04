# CONTENT INTELLIGENCE SYSTEM
# The compounding layer. How the system gets smarter every week.
# Created: 2026-05-04 | Used by: Research Agent, Intelligence Agent, Content Agent

> The difference between a content factory and a content system is whether it gets smarter every week. This document defines the intelligence loop.

---

## a) TRANSCRIPT EXTRACTION SUB-WORKFLOW

**Purpose**: Reusable n8n sub-workflow that takes a TikTok URL and returns structured data.

**Input**: `{ tiktok_url: string, client_id: string, research_run_id: int }`

**Output**: `{ transcript: string|null, hook_type: string, emotional_trigger: string }`

### Implementation (n8n nodes)

```
[Trigger: Webhook /webhook/internal/transcript]
    ↓
[Validate URL format]
    ↓
[HTTP Request: Supadata API]
   POST https://api.supadata.ai/v1/transcript
   Headers: x-api-key: {SUPADATA_API_KEY}
   Body: { url, lang: "en" }
   Timeout: 30s
    ↓
[IF transcript empty/null]
   YES → return { transcript: null, hook_type: null, emotional_trigger: null }
   NO →
    ↓
[Code: Extract first 3 seconds of speech]
   First sentence ≈ hook. Pass to Claude for classification.
    ↓
[HTTP Request: Claude API]
   model: claude-sonnet-4-6
   max_tokens: 200
   Prompt: "Classify this TikTok hook. Return JSON {hook_type: question|statement|statistic|story, emotional_trigger: fear|curiosity|aspiration|relief}. Hook: '{first_3_seconds}'. JSON only."
    ↓
[Parse JSON response]
    ↓
[HTTP Request: PATCH content_insights]
   Update transcript, hook_type, emotional_trigger by tiktok_url
    ↓
[Respond 200 with classified data]
```

**Failure handling**:
- Supadata returns 404/empty: store `transcript=null`, return `hook_type=null`
- Claude classification fails: store transcript, return `hook_type=null` (still useful)
- Total runtime per call: 5-15 seconds. Sub-workflow runs sequentially per URL with 500ms delay.

**Activation**: called by Weekly Research workflow (5b) inside the "Extract Transcripts (top 10)" loop.

---

## b) PATTERN ANALYSIS CLAUDE PROMPT

**Purpose**: Take 10 transcripts + their engagement scores → output ranked hook/beat/CTA patterns.

**Used by**: Research Agent (Pattern Analysis step).

```
SYSTEM PROMPT:
You analyze TikTok content patterns. You are given 10 top-performing videos in a niche, with transcripts and engagement metrics. Identify what's actually driving performance — verbatim phrases, structural patterns, emotional triggers — at a level that lets a script writer replicate them. Return only valid JSON.

USER PROMPT:
Niche: {NICHE}
Target audience: {TARGET_AUDIENCE}

10 top videos this week (sorted by score descending):
{VIDEOS_JSON}
[Each: tiktok_url, caption, transcript, hook_type, stats, score]

Task:
1. For each video with a transcript, identify:
   - Hook (first 3 seconds, verbatim if possible)
   - Hook structure (question | statement | statistic | story)
   - Emotional trigger (fear | curiosity | aspiration | relief)
   - Beat count and approximate timing
   - CTA mechanism (how they ask for engagement)
   - 1-3 distinctive phrases that recur in the video

2. Cross-video pattern summary:
   - Top 3 hook patterns (by frequency in top 10)
   - Top emotional trigger (most-used)
   - Winning beat structure (most common beat count + cadence)
   - Top CTA formats (verbatim CTAs that appeared)
   - Emerging phrases (any phrase that appeared in 3+ videos)

Output JSON:
{
  "videos": [
    { "tiktok_url": "...", "hook_phrase": "...", "hook_type": "...", "emotional_trigger": "...", "beat_count": N, "cta_phrase": "...", "distinctive_phrases": ["..."] }
  ],
  "summary": {
    "top_hook_patterns": [
      { "pattern": "...", "example_verbatim": "...", "appeared_in_count": N }
    ],
    "dominant_emotional_trigger": "...",
    "winning_beat_structure": "...",
    "top_cta_formats": [
      { "format": "...", "example": "..." }
    ],
    "emerging_phrases": [
      { "phrase": "...", "appeared_in_count": N, "context": "..." }
    ]
  }
}

Hard rules:
- Quote verbatim where possible. No paraphrasing of hooks.
- Only count "emerging" phrases that appear in 3+ videos.
- If <5 videos have transcripts, work with what's there but note in summary.
```

---

## c) PATTERN LIBRARY SCHEMA (markdown format for GitHub)

**File**: `clients/{CLIENT_ID}/pattern-library.md`
**Owner**: Research Agent (writes new patterns), Intelligence Agent (re-ranks based on performance)
**Format**: newest entry at top, dated.

### Section structure

```markdown
# Pattern Library — {CLIENT_NAME}
> Updated weekly. Newest at top. Validated patterns ✅ | Emerging 🔬 | Retired ❌

## Hook Patterns
Ranked by performance over time (validated patterns at top).

### ✅ Validated — appeared in top performer 2+ weeks
1. [QUESTION + DIRECT YOU] — "Did you know your {body_system} does {X} when you {Y}?"
   - Appeared in top performers: 2026-04-13, 2026-04-20, 2026-04-27 (3 weeks)
   - Avg views when used: 14,200
   - Best example: "Did you know your nervous system runs on a 90-minute cycle?" (script 3, week 2026-04-20)
   - Date added: 2026-04-13

2. [STATISTIC + EMOTIONAL HOOK] — "{X}% of {target_audience} are {pain_state}, and it's not their fault."
   - Appeared in top performers: 2026-04-27 (1 week — needs more data to validate)
   - ...

### 🔬 Emerging — seen in research, not yet tested
1. [STORY + REVEAL] — "I used to {bad_state}. Then I learned {mechanism}."
   - Source: research week 2026-04-27
   - Why interesting: appeared in 5 of top 10 scraped videos

### ❌ Retired — 3+ weeks bottom performance
1. [GENERIC ASPIRATIONAL] — "If you want to {goal}, here's what worked for me..."
   - Retired: 2026-04-20
   - Reason: bottom 2 of 5 in 3 consecutive weeks

## Beat Structures
1. **5-beat: Hook→Stat→Mechanism→Action→CTA** (35-40s) — ✅ Validated 3 weeks
2. **7-beat: Hook→Story→Twist→Insight→Action→Why→CTA** (40-45s) — 🔬 Emerging

## CTA Formats
1. **"DM me {KEYWORD}, I'll send you {resource}"** — ✅ Validated
2. **"DM me {KEYWORD} for the full {resource}"** — ✅ Validated

## Posting Time Patterns
- Best day: Tuesday (avg +18% views vs. Mon/Wed/Thu/Fri average)
- Best time: 08:30 local
- Last validated: 2026-04-27

## Compliance Patterns Learned
- "Sleep optimization" angles need disclaimer line about consulting a doctor
- Never use "cure," "treat," "fix" verbs
- "Calm the nervous system" is acceptable. "Reduce cortisol" is not (clinical claim).
```

### Update rules
- **Research Agent** writes new patterns to "🔬 Emerging" section weekly.
- **Intelligence Agent** promotes patterns to ✅ Validated after they appear in top performer for 2+ weeks.
- **Intelligence Agent** retires patterns after 3 consecutive weeks in bottom-performance scripts.
- All sections are **prepended** (newest at top of section).
- Never delete a pattern — move to ❌ Retired with reason.

---

## d) INTELLIGENCE AGENT WEEKLY ANALYSIS PROMPT

**Used by**: Intelligence Agent (Saturday 08:00 cron, after 72h perf data is in).

```
SYSTEM PROMPT:
You are the analytical brain of a TikTok content system. You compare what was scripted, what was posted, and what performed — then update the pattern library with what's now validated, what's emerging, and what should be retired. Your output drives future script generation.

You return ONLY valid JSON, plus a markdown block for the pattern library update.

USER PROMPT:
Client: {CLIENT_ID}
Week: {WEEK_START}

This week's 5 posts with full data:
{POSTS_WITH_SCRIPTS_JSON}
[Each: script_json, posted_at, perf_24h, perf_72h, video_job consistency_pass]

Current pattern library (top of file — most recent state):
{PATTERN_LIBRARY_HEAD}

Last 4 weeks performance summaries:
{PERFORMANCE_LOG_HEAD}

This week's research findings (scraped patterns):
{RESEARCH_SUMMARY}

Task:
1. Identify top performer of the week (max perf_72h.views).
2. Extract its: hook_type, emotional_trigger, beat_count, cta_phrase, posted_day_of_week, posted_time.
3. Compare to library — which library patterns appeared in this top performer?
4. Identify bottom performer. Note its patterns.
5. Pattern updates:
   - Promote 🔬 Emerging → ✅ Validated if it appeared in top performer for 2nd+ week
   - Retire ✅ Validated → ❌ Retired if it appeared in bottom 2 of 5 for 3 consecutive weeks
   - Add new emerging patterns observed in this week's research that aren't yet in the library
6. Trend delta: what's NEW this week vs. last week's library?
7. Prompt template assessment: do the results suggest Template 2 should be revised? If yes, describe the change (don't write the new prompt — just describe).

Output JSON:
{
  "top_performer": { "script_idx": N, "views_72h": N, "hook_type": "...", "emotional_trigger": "...", "beat_count": N, "cta_phrase": "...", "posted_day": "...", "posted_time": "..." },
  "bottom_performer": { "script_idx": N, "views_72h": N, "hook_type": "..." },
  "library_updates": {
    "promoted_to_validated": [
      { "pattern": "...", "evidence_weeks": ["..."] }
    ],
    "retired": [
      { "pattern": "...", "reason": "..." }
    ],
    "new_emerging": [
      { "pattern": "...", "source_research_week": "..." }
    ]
  },
  "trend_delta": "string — one paragraph on what shifted this week",
  "prompt_template_recommendation": null OR { "template": "script-generator", "change": "string description of what to change" }
}

After this JSON, output a markdown block (delimited by --- BEGIN MARKDOWN --- and --- END MARKDOWN ---) that contains the new entry to PREPEND to pattern-library.md. Use the schema in CONTENT-INTELLIGENCE.md section c.

Hard rules:
- Never invent data. If perf_72h is missing for a post, note it explicitly.
- Quote scripts verbatim when citing what worked.
- Be conservative with promotion: 2+ weeks of evidence required.
- Be aggressive with retirement: 3 consecutive bottom weeks = retire, no exceptions.
```

---

## e) FEEDBACK LOOP INTEGRATION

**The loop**: Research → Pattern Library → Script Generation → Posting → Performance → Intelligence updates Pattern Library → next week's Script Generation reads updated library.

### Where the library gets injected into Template 2 (Script Generator)

In the n8n Script Generation workflow (5c), the "Fetch Pattern Library from GitHub" node retrieves `clients/{CLIENT_ID}/pattern-library.md`. The Code node then extracts:

```javascript
// Parse top 3 ✅ Validated patterns from each section
const lib = patternLibraryMarkdown;
const validatedHooks = extractSection(lib, "Hook Patterns", "✅ Validated").slice(0, 3);
const validatedBeats = extractSection(lib, "Beat Structures").slice(0, 1);
const validatedCTAs = extractSection(lib, "CTA Formats").slice(0, 2);

// Inject into Template 2 prompt as context
const promptInjection = {
  top_3_validated_hook_patterns: validatedHooks,
  winning_beat_structure: validatedBeats[0],
  top_2_cta_formats: validatedCTAs,
  last_week_top_performer: lastWeekTopPerformerScriptJson
};
```

This injection happens in the "Template 2 — Batch Script Generator" node body construction. The injected fields appear in the user prompt of Template 2 (see prompts/script-generator-v1.md).

### Why the loop compounds

- Week 1: pattern library is empty. Scripts are generated from research only. Some win, some don't.
- Week 2: Intelligence Agent identifies the winning pattern. Adds to library as 🔬 Emerging.
- Week 3: That pattern is used again (now in 🔬 section). If it wins, Intelligence promotes to ✅.
- Week 4+: ✅ Validated patterns are now reliably injected into every Template 2 call. Quality compounds.
- Week 8+: Pattern library has 5-10 ✅ Validated patterns. Bottom performers are rare. Average views climb.

### Anti-pattern: pattern library that just grows
Without the retirement step, the library accumulates noise. Retirement after 3 bottom weeks is non-negotiable.

### Telemetry to verify the loop is working
Monthly check (manual): graph avg perf_72h.views over time. If trendline is flat after week 4, the loop is broken — investigate Intelligence Agent output quality or Template 2 not reading library properly.
