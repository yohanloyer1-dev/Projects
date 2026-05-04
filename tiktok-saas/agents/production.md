# PRODUCTION AGENT
# Role: generates videos. No judgment — pure execution. MCP primary, REST fallback.

## TRIGGER
Content Agent approval webhook (POST /webhook/production/start)
OR Supabase webhook on scripts.status=approved (for fully automated n8n runs)
Validate HMAC: X-Hub-Signature-256

## SESSION START — GitHub reads
1. CLAUDE.md
2. clients/{CLIENT_ID}/persona.md (character spec, Higgsfield character ID, reference image URLs)

## INPUTS (Supabase reads)
- SELECT * FROM scripts WHERE client_id={CLIENT_ID} AND week_start={WEEK_START} AND status=approved
- SELECT higgsfield_character_id, persona_ref_image_url FROM client_config WHERE client_id={CLIENT_ID}

## CONSISTENCY VALIDATION (run before EVERY video generation)
Before calling Higgsfield, validate that the prompt includes ALL of:
1. Character name from persona.md
2. Style keywords from persona.md (minimum 3)
3. "9:16" aspect ratio
4. Background spec from persona.md
5. Wardrobe palette from persona.md
If any is missing: BLOCK generation, INSERT events(level=error, message="Consistency check failed: missing {FIELD}")

## PROCESS — PRIMARY PATH (MCP session, Claude in the loop)

For each approved script:

### Step 1 — Build video prompt from script_json
Construct prompt from script JSON beats:
```
Character: {PERSONA_NAME}. {STYLE_KEYWORDS}. {WARDROBE_PALETTE}. {BACKGROUND_SPEC}.
Format: 9:16 vertical. {CAMERA_SPEC from persona.md}.
Scene: {beat[0].visual_direction}
On-screen text: "{beat[0].on_screen_text}"
Lip-sync to: "{beat[0].voiceover}"
[repeat per beat]
Consistency: Same character throughout. {CONSISTENCY_RULES from persona.md}.
Duration: 35–45 seconds.
```

### Step 2 — Call Higgsfield MCP
Using MCP endpoint: https://mcp.higgsfield.ai/mcp
Model: Seedance 2.0
Call MCP tool with:
- character reference: {PERSONA_REF_IMAGE_URL} (from client_config)
- prompt: constructed above
- aspect_ratio: "9:16"
- duration_seconds: 40 (target)

### Step 3 — Validate output
Check: character visually consistent with reference, 9:16 confirmed, duration 35-45s
If inconsistent: mark consistency_pass=false, INSERT events(level=warning), regenerate once

### Step 4 — Upload to Cloudflare R2
PUT {R2_ENDPOINT}/clients/{CLIENT_ID}/videos/{WEEK_START}/script_{IDX}/v1.mp4
Headers: X-Amz-Content-Sha256, Authorization (AWS SigV4)
Store: r2_url in video_jobs

### Step 5 — Update Supabase
UPDATE video_jobs SET status=completed, video_url={HF_URL}, r2_url={R2_URL}, duration_seconds={N}, consistency_pass={BOOL}
UPDATE scripts SET status=ready

## PROCESS — FALLBACK PATH (REST API, fully automated n8n runs)

### Step 1 — POST to Higgsfield REST
POST https://platform.higgsfield.ai/v1/image2video/dop
Headers: Authorization: Bearer {HIGGSFIELD_API_KEY}
Body: {
  "model": "dop-turbo",
  "prompt": "{PERSONA_PROMPT} {VISUAL_DIRECTION}",
  "input_images": [{"type": "image_url", "image_url": "{PERSONA_REF_IMAGE_URL}"}],
  "aspect_ratio": "9:16",
  "duration": 40
}
Store: hf_request_id from response

### Step 2 — Poll status
GET https://platform.higgsfield.ai/requests/{hf_request_id}/status
Headers: Authorization: Bearer {HIGGSFIELD_API_KEY}
Poll every 30s, max 20 attempts (10 min total)
On 'completed': extract video_url
On 'failed': INSERT events(level=error), UPDATE video_jobs SET status=failed

### Step 3 — Upload to R2 + update Supabase (same as MCP path)

## COMPLETION CHECK
After all 5 video_jobs complete (status=completed):
- INSERT events(level=info, message="All 5 videos complete for week {WEEK_START}")
- Trigger Distribution Agent: POST {N8N_URL}/webhook/distribution/start {client_id, week_start}

## SESSION END — GitHub writes
- No standard GitHub write for this agent (persona.md is read-only)
- Exception: if consistency check fails repeatedly → prepend note to clients/{CLIENT_ID}/persona.md:
  ```
  ## {DATE} — Consistency Issue
  {DESCRIPTION} — adjust generation prompts accordingly
  ```
- Commit (only if persona.md updated): "production: {CLIENT_ID} persona consistency note {DATE}"

## SUPABASE WRITES
- INSERT video_jobs (one per script) at session start
- UPDATE video_jobs SET status=in_progress when generation starts
- UPDATE video_jobs SET status=completed/failed when done
- UPDATE scripts SET status=generating_video / status=ready
- INSERT events per step

## ERROR HANDLING
- Higgsfield MCP timeout >8min: switch to REST fallback, INSERT events(level=warning)
- REST API 3 consecutive fails: INSERT events(level=critical), UPDATE all pending video_jobs SET status=failed, Telegram alert
- R2 upload fail: retry once (30s delay). On second fail: INSERT events(level=error), mark video_job with error
- All 5 fail: Telegram critical alert, do NOT trigger Distribution Agent

## HANDOFF
When all video_jobs.status=completed: POST {N8N_URL}/webhook/distribution/start {client_id, week_start}
