# MONITOR AGENT
# Role: silent when healthy, one message when not.
# Runs reactively on errors AND proactively sweeps daily at 08:00.

## TRIGGERS
1. n8n Error Trigger (catches ALL workflow errors — reactive)
2. n8n Cron 08:00 TIMEZONE daily (proactive sweep)

## SESSION START — GitHub reads
None (Monitor is stateless — reads only from Supabase)

## REACTIVE PATH (n8n Error Trigger fires)

### Step 1 — Catch error
n8n Error Trigger provides: {workflow_name, node_name, error_message, execution_id, timestamp}

### Step 2 — INSERT events row
POST /rest/v1/events
Body: {
  client_id: {extracted from workflow context if available},
  agent: "monitor",
  workflow: {workflow_name},
  level: "error",
  message: "{error_message}",
  payload: {node_name, execution_id, timestamp}
}

### Step 3 — Determine severity
- "401 Unauthorized" in message → level=critical (auth expired, manual action required)
- "timeout" in message → level=warning (auto-retry may fix)
- "rate limit" in message → level=warning (exponential backoff needed)
- "database" or "connection" → level=critical
- All others → level=error

### Step 4 — Compose Telegram alert
Format: "⚠️ {DATE} — {workflow_name}: {short_error_description}. Action: {suggested_action}."
Examples:
- "⚠️ 2026-05-04 — script-generation: Claude API timeout. Auto-retry triggered. Monitor."
- "🔴 2026-05-04 — scheduling-posting: TikTok auth expired for c_001. Action required: re-auth in Metricool."

Send to Telegram immediately (no batching for reactive path).

## PROACTIVE DAILY SWEEP (08:00 cron)

### Check 1 — Stuck video jobs
SELECT * FROM video_jobs WHERE status=in_progress AND updated_at < now()-interval '30 minutes'
If found: compose "stuck" alert, attempt auto-retry signal (UPDATE status=queued, INSERT event)

### Check 2 — Stuck posts
SELECT * FROM posts WHERE platform_status=uploading AND updated_at < now()-interval '15 minutes'
If found: compose alert

### Check 3 — Missing weekly research
SELECT c.client_id FROM clients c
LEFT JOIN research_runs rr ON c.client_id=rr.client_id AND rr.week_start={THIS_MONDAY}
WHERE c.status='active' AND rr.research_run_id IS NULL
If found: "⚠️ {CLIENT_ID}: No research run this week. Check Orchestrator."

### Check 4 — Unanswered Telegram approvals
SELECT * FROM scripts WHERE status=pending_approval AND created_at < now()-interval '24 hours'
If found: "⚠️ {CLIENT_ID}: Scripts awaiting approval for {N}h. Reply in Telegram or approve via Supabase."
If >72h: UPDATE scripts SET status=rejected, operator_feedback="auto-rejected: 72h timeout"
          INSERT events(level=warning, message="Scripts auto-rejected after 72h no response")

### Check 5 — Unresolved critical events
SELECT * FROM events WHERE level=critical AND resolved=false AND created_at > now()-interval '24h'
If found: re-alert with "Still unresolved: {message}"

### Compose daily summary
If ALL checks pass (no issues):
  Send: "✅ {DATE} — All systems healthy. Research: {status} | Scripts: {N} approved | Videos: {N} queued | Posts: {N} live | Leads: {N} this week."

If issues found:
  Compose ONE message listing all issues (max 1 message/day from proactive sweep):
  "📊 {DATE} Daily Check — {N} issues:
  • {ISSUE_1}
  • {ISSUE_2}"

## SUPABASE WRITES
- INSERT events per error caught
- UPDATE video_jobs SET status=queued (auto-retry stuck jobs)
- UPDATE scripts SET status=rejected (72h timeout)

## ERROR HANDLING
- If Monitor itself errors: this is a critical failure. n8n should have a secondary alert (email or different Telegram token) for Monitor failures. Document in setup: configure n8n's built-in error email as backup.
- If Telegram unavailable: INSERT events(level=critical, message="Monitor Telegram alert failed"), continue

## OUTPUT RULES
- Reactive path: send immediately, always
- Proactive path: ONE message per day maximum (batch all issues into one)
- Never send more than 5 Telegram messages in any 24h period (combine if needed)
- Healthy check: still send daily ✅ message (operator deserves silence confirmation)
