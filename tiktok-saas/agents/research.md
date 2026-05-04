# RESEARCH AGENT
# Role: finds what is working in the niche. Extracts transcripts, analyzes patterns, updates pattern library.

## TRIGGER
Monday 06:00 TIMEZONE OR Orchestrator webhook (POST /webhook/research/start)
Validate HMAC: X-Hub-Signature-256 header using N8N_SHARED_SECRET before processing

## SESSION START — GitHub reads
1. CLAUDE.md
2. clients/{CLIENT_ID}/pattern-library.md (current pattern library)
3. clients/{CLIENT_ID}/memory.md (compliance context)

## INPUTS
- Supabase: SELECT client_config WHERE client_id = {CLIENT_ID}
- Payload: {client_id, week_start, research_run_id}
- UPDATE research_runs SET status=in_progress WHERE research_run_id={ID}

## PROCESS

### Step 1 — Scrape (n8n handles, Research Agent receives results)
n8n makes parallel HTTP calls to ScrapeCreators (Header: x-api-key: {SCRAPECREATORS_API_KEY}):
- GET https://api.scrapecreators.com/v1/tiktok/search/keyword?query={NICHE}&date_posted=this-week&sort_by=most-liked
- GET https://api.scrapecreators.com/v1/tiktok/search/keyword?query={TARGET_AUDIENCE}&date_posted=this-week&sort_by=most-liked
- GET https://api.scrapecreators.com/v1/tiktok/search/top?query={NICHE}&publish_time=this-week&sort_by=most-liked
- GET https://api.scrapecreators.com/v1/tiktok/search/hashtag?hashtag={NICHE_HASHTAG_1}
- GET https://api.scrapecreators.com/v1/tiktok/search/hashtag?hashtag={NICHE_HASHTAG_2}
- GET https://api.scrapecreators.com/v1/tiktok/get-trending-feed
Inter-request delay: 1200ms (ScrapeCreators rate limit safety)

### Step 2 — Score & Deduplicate
For each video result:
score = play_count×0.5 + digg_count×0.25 + comment_count×0.15 + share_count×0.10
Deduplicate by tiktok_url. Keep top 30 unique URLs sorted by score descending.

### Step 3 — Transcript Extraction (top 10 only)
For each of top 10 URLs:
  POST https://api.supadata.ai/v1/transcript
  Headers: x-api-key: {SUPADATA_API_KEY}, Content-Type: application/json
  Body: {"url": "{TIKTOK_URL}", "lang": "en"}
  On null transcript: mark transcript=null, continue (do not fail run)
  Delay: 500ms between calls

### Step 4 — Claude Pattern Analysis (Research Agent core judgment)
Input to Claude: array of top 10 {tiktok_url, caption, transcript, score, stats}
Task: For each video with transcript, analyze:
- hook_type: question | statement | statistic | story
- emotional_trigger: fear | curiosity | aspiration | relief
- Hook exact phrasing (first 3 seconds estimated)
- Beat structure (how many beats, approximate timing)
- CTA format (how they ask for engagement or DMs)
- Key phrase patterns (recurring words/phrases in high-scoring videos)
Output: structured JSON per video + cross-video pattern summary

### Step 5 — Upsert to Supabase
For each of top 30 videos:
  POST {SUPABASE_URL}/rest/v1/content_insights
  Headers: Authorization: Bearer {SERVICE_KEY}, Prefer: resolution=merge-duplicates,return=minimal
  Body: {client_id, research_run_id, source, tiktok_url, author_handle, caption, transcript, hook_type, emotional_trigger, stats, score}

### Step 6 — Update Pattern Library (GitHub)
Prepend to clients/{CLIENT_ID}/pattern-library.md:
```
## Week of {WEEK_START} — Research Findings

### Top Hook Patterns This Week
1. {HOOK_TYPE}: "{EXACT_PHRASE}" — avg score {N}
2. ...

### Top Emotional Triggers
- {TRIGGER}: appeared in {N} of top 10 videos

### Emerging Phrases
- "{PHRASE}" — appeared {N} times in top videos

### Beat Structure Winner
{N}-beat structure at {TIMING} — {N} of top 5 used this

### CTA Patterns
- "{CTA_FORMAT}" — appeared in {N} top videos
```

### Step 7 — Complete
- UPDATE research_runs SET status=completed, outputs={summary_json}
- INSERT events (level=info, agent=research, message="Research complete: {N} insights, {N} transcripts")
- Trigger Content Agent: POST {N8N_URL}/webhook/content/start {client_id, week_start, research_run_id}

## SESSION END — GitHub writes
- Updated clients/{CLIENT_ID}/pattern-library.md (prepended, as above)
- Commit: "research: {CLIENT_ID} week {WEEK_START} — {N} insights, {N} patterns"

## ERROR HANDLING
- ScrapeCreators 429: wait 60s, retry once. On second fail: INSERT events(level=error), continue with partial results if ≥10 videos found
- Supadata null/error: mark transcript=null, do NOT fail the run. Proceed with caption-only analysis.
- <10 videos found: INSERT events(level=warning), continue with what exists
- Total failure: UPDATE research_runs SET status=failed, INSERT events(level=critical), Telegram alert

## HANDOFF
Completion: UPDATE research_runs SET status=completed
Signal: POST {N8N_URL}/webhook/content/start with {client_id, week_start, research_run_id}
