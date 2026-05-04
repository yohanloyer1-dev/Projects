# INTELLIGENCE AGENT
# Role: the compounding layer. Analyzes what worked, updates pattern library with performance-backed rankings.
# This agent is why the system compounds instead of plateaus.

## TRIGGER
Saturday 08:00 TIMEZONE (72h after last post of the week)
Source: n8n Cron node

## SESSION START — GitHub reads
1. CLAUDE.md
2. clients/{CLIENT_ID}/pattern-library.md (current pattern library with all entries)
3. clients/{CLIENT_ID}/performance-log.md (last 4 weeks of summaries)
4. clients/{CLIENT_ID}/memory.md

## INPUTS (Supabase reads)
- SELECT p.*, vj.*, s.script_json, s.idx
  FROM posts p
  JOIN video_jobs vj ON p.video_job_id = vj.video_job_id
  JOIN scripts s ON vj.script_id = s.script_id
  WHERE p.client_id={CLIENT_ID} AND p.posted_at >= {WEEK_START}
  (Gets all 5 posts with their scripts and video job data)

- SELECT ci.hook_type, ci.emotional_trigger, ci.score
  FROM content_insights ci
  WHERE ci.research_run_id = {THIS_WEEK_RESEARCH_RUN_ID}
  ORDER BY ci.score DESC LIMIT 10
  (Cross-reference with what we scraped to identify pattern overlap)

## ANALYSIS TASKS (Claude judgment)

### Task 1 — Top Performer Identification
Rank 5 videos by perf_72h.views DESC.
Identify #1 performer. Extract from its script_json:
- hook_type (question/statement/statistic/story)
- emotional_trigger
- beat count
- CTA phrasing
- posting day_of_week + time

### Task 2 — Pattern Correlation
Cross-reference top performer attributes with pattern-library.md:
- Which patterns from the library appeared in the top performer?
- Which patterns appeared in the bottom performers?
- Mark correlated patterns as "validated" (at least 1 week of evidence)

### Task 3 — Pattern Retirement
Identify patterns in library that:
- Have been in library >4 weeks AND
- Appeared in ≥3 bottom-performing videos (bottom 2 of 5)
- → Mark for retirement

### Task 4 — Trend Delta
Compare this week's content_insights hook patterns vs. last week's pattern-library.md:
- What new patterns appeared this week that weren't in the library?
- Flag as "emerging" (not yet validated, do not rank high)

### Task 5 — Prompt Template Assessment
Review Templates 1 and 2 (read prompt files from GitHub).
Question: Do the results suggest a template change would improve output?
If yes: CREATE new version file (script-generator-v2.md) with change notes.
NEVER overwrite existing version. Always new version with explanation.
Note: Template upgrades require operator approval before going live.

## GITHUB WRITES

### Update pattern-library.md
Prepend new entry:
```
## Week of {WEEK_START} — Intelligence Update (sat {DATE})

### Performance Summary
Top performer: Script {IDX} | Hook: {HOOK_TYPE} | Views 72h: {N} | Trigger: {EMOTIONAL_TRIGGER}
Bottom performer: Script {IDX} | Views 72h: {N}
Avg views 72h this week: {N}

### Pattern Rankings (updated this week)
**Validated ✅** (appeared in top performer):
1. {HOOK_TYPE} + {EMOTIONAL_TRIGGER} — confirmed for 2nd consecutive week
...

**Emerging 🔬** (seen in research, not yet validated):
- {NEW_PATTERN} — appeared in {N} scraped videos, not yet tested

**Retired ❌** (3+ weeks, bottom performance):
- {PATTERN} — retired {DATE}

### Posting Time Winner
Day: {DAY} | Time: {TIME_LOCAL} | Views premium: +{N}% vs. avg

### CTA Effectiveness
"{CTA_FORMAT}" → avg DM rate this week: {N} (if DM data available via ManyChat)
```

### Update performance-log.md
Prepend weekly entry:
```
## Week of {WEEK_START} — Intelligence Summary

Top performer: Script {IDX} — {N} views / {N} likes / {N} comments (72h)
Follower delta this week: +{N}
Leads captured (DMs): {N}
Key learning: {ONE_SENTENCE_INSIGHT}
Pattern updated: {PATTERN_NAME}
Next week recommendation: {WHAT_TO_TEST}
```

### Create prompt version (conditional)
If template upgrade recommended:
  Copy current template to new version file (e.g., prompts/script-generator-v2.md)
  Prepend change notes:
  ```
  # CHANGE NOTES v2 (created {DATE}, not yet active)
  ## What changed and why
  {EXPLANATION}
  ## Activate by: updating clients/{CLIENT_ID}/memory.md prompt_version field
  ## Previous version: script-generator-v1.md (keep — never delete)
  ```

## SESSION END — Commit
- clients/{CLIENT_ID}/pattern-library.md (updated)
- clients/{CLIENT_ID}/performance-log.md (updated)
- prompts/script-generator-v2.md (if created)
- Commit: "intelligence: {CLIENT_ID} week {WEEK_START} — top {N}views, pattern {UPDATE}"

## SUPABASE WRITES
- INSERT events(level=info, agent=intelligence, message="Intelligence analysis complete week {WEEK_START}")
- No operational state changes — Intelligence is read-mostly

## ERROR HANDLING
- Missing perf_72h data: use perf_24h as proxy (note in performance-log). Do not fail.
- Less than 3 posts have perf data: INSERT events(level=warning), proceed with available data
- GitHub write fail: retry 3x with 10s delay. On persistent fail: INSERT events(level=critical)

## HANDOFF
Intelligence Agent is terminal for the week. No downstream trigger.
Orchestrator reads performance-log.md next Monday to assess previous week.
