# CONTENT AGENT
# Role: writes 5 scripts per week using research + pattern library. Sends Telegram approval checkpoint.

## TRIGGER
Research Agent completion webhook (POST /webhook/content/start)
Validate HMAC: X-Hub-Signature-256

## SESSION START — GitHub reads
1. CLAUDE.md
2. clients/{CLIENT_ID}/memory.md
3. clients/{CLIENT_ID}/pattern-library.md (top 3 patterns + last week top performer)
4. prompts/research-summary-v1.md (Template 1)
5. prompts/script-generator-v1.md (Template 2)
6. prompts/compliance-rewrite-v1.md (Template 3)

## INPUTS (Supabase reads)
- SELECT * FROM client_config WHERE client_id={CLIENT_ID}
- SELECT * FROM content_insights WHERE research_run_id={RESEARCH_RUN_ID} ORDER BY score DESC LIMIT 30
- SELECT * FROM scripts WHERE client_id={CLIENT_ID} AND week_start={PREV_WEEK} ORDER BY script_id LIMIT 5 (for last week top performer)
- SELECT * FROM posts WHERE client_id={CLIENT_ID} ORDER BY perf_72h->>'views' DESC LIMIT 1 (last week top post)

## PROCESS

### Step 1 — INSERT script_batches row
POST /rest/v1/script_batches
Body: {client_id, week_start, status:'generating', prompt_version:'v1'}

### Step 2 — Template 1 (Research Summary)
Claude API call with research-summary-v1.md as system prompt.
Input: client_config fields + top 30 content_insights as JSON array.
Output: strict JSON — 5 content angles with hook patterns, beat blueprints, CTA patterns, compliance risks.
Store output in script_batches.research_summary.

### Step 3 — Template 2 (Batch Script Generator)
Claude API call with script-generator-v1.md as system prompt.
Input: client_config + research_summary JSON + top 3 patterns from pattern-library.md + last week top performer script_json.
Output: strict JSON — exactly 5 scripts per schema.
Validate output JSON schema (check all required fields: idx, topic, hook, beats[], cta, caption, hashtags, compliance).
On schema validation failure: retry once with error appended to prompt. On second failure: INSERT events(level=error), halt batch.

### Step 4 — Template 3 (Compliance Rewrite — conditional)
For each script where compliance.risk_flags is non-empty array:
  Claude API call with compliance-rewrite-v1.md as system prompt.
  Input: single script JSON + client_config (brand_terms_to_avoid, disclaimer_rules).
  Output: rewritten script JSON, same schema.
  Replace original script_json with rewritten version.

### Step 5 — INSERT scripts rows (5 rows)
For each of 5 scripts:
  POST /rest/v1/scripts
  Body: {client_id, script_batch_id, week_start, idx, status:'pending_approval', script_json, approval_attempt:1}

### Step 6 — Telegram Approval Message
Format each script as readable text block:
```
📋 Script {IDX}/5 — Week of {WEEK_START}
Client: {CLIENT_NAME}

TOPIC: {topic}
HOOK (0–3s): {hook}

BEATS:
{t}s: "{voiceover}" | Screen: {on_screen_text}
...

CTA: "{spoken}" | DM/comment prompt: "{dm_prompt}"
CAPTION: {caption}
HASHTAGS: {hashtags}
COMPLIANCE: {disclaimer_line}

⚠️ Risk flags: {risk_flags or "None"}
```

Send to Telegram with inline keyboard:
- ✅ Approve All → POST /webhook/approval/batch-approve {client_id, week_start, script_batch_id}
- ✅ Approve 1/2/3/4/5 individual buttons → POST /webhook/approval/approve {script_id}
- ✏️ Request Revision → POST /webhook/approval/reject {client_id, week_start, feedback}
- (Each button's callback_data encodes client_id + action)

### Step 7 — Handle Approval Response
On APPROVE signal (from Telegram webhook → n8n):
  UPDATE scripts SET status=approved WHERE script_id IN (approved_ids)
  UPDATE script_batches SET status=approved
  Trigger Production Agent: POST {N8N_URL}/webhook/production/start {client_id, week_start, script_ids}

On REJECT signal (from Telegram webhook → n8n):
  If approval_attempt < 3:
    Re-run Template 2 with operator_feedback appended: "Operator rejected. Feedback: {feedback}. Regenerate all 5 scripts addressing this feedback."
    UPDATE scripts SET approval_attempt += 1, operator_feedback={feedback}
    Re-send Telegram approval message
  If approval_attempt >= 3:
    INSERT events(level=critical, message="Max approval attempts reached. Manual intervention required.")
    Telegram alert: "🔴 {CLIENT_ID}: Scripts rejected 3 times. Please review manually."

## SESSION END — GitHub writes
- If any new compliance patterns observed: prepend to clients/{CLIENT_ID}/memory.md
  ```
  ## {DATE} — Compliance Note
  {observation} — applied in week {WEEK_START}
  ```
- Commit: "content: {CLIENT_ID} week {WEEK_START} — 5 scripts pending approval"

## SUPABASE WRITES
- script_batches: INSERT + UPDATE status
- scripts: INSERT 5 rows
- events: info logs per step, error on failures

## ERROR HANDLING
- Claude API timeout (>30s): retry once. On second fail: INSERT events(level=error), halt
- JSON schema validation fail twice: INSERT events(level=error), Telegram alert
- Telegram send fail: INSERT events(level=warning), continue (scripts are in Supabase — operator can approve via direct DB)

## HANDOFF
On approval: UPDATE scripts.status=approved + trigger Production Agent webhook
