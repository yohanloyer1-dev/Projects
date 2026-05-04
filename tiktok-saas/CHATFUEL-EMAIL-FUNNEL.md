# CHATFUEL + EMAIL FUNNEL — D9 (revised 2026-05-04)
# Lead capture from TikTok comment OR DM → Kit (ConvertKit) sequence
# Replaces ManyChat (which doesn't work in EU at all).

> **Critical change vs. original spec**: ManyChat cannot connect to TikTok in EU at all (TikTok-side GDPR restriction). Chatfuel works in EU AND has comment-to-DM (which ManyChat lacks in any Western market). CTAs can use comment-first OR DM-first — Chatfuel handles both.

---

## a) CHATFUEL CHANNEL CONNECTION

### Step 1 — Sign up for Chatfuel
1. chatfuel.com → Sign up.
2. Choose plan: Pro plan covers TikTok integration (~$15-20/mo at base, scales with audience).

### Step 2 — Connect TikTok account
1. Chatfuel dashboard → Channels → TikTok → "Connect."
2. Authorize Chatfuel via TikTok OAuth (must be a TikTok Business account — free upgrade).
3. After connection: bot ID is shown in the URL/dashboard. Store as `client_config.chatfuel_bot_id` in Supabase.

### Step 3 — Get API token
1. Chatfuel → Settings → API Access → Generate token.
2. Store as `CHATFUEL_API_KEY` in n8n environment.

### Why Chatfuel works in EU (and ManyChat doesn't)
- Chatfuel uses TikTok's official Business Messaging API endpoint, which IS available in EU.
- ManyChat appears to use a different integration path that's blocked in EU/UK.
- Chatfuel's GDPR policies + DPA are publicly documented.

---

## b) TRIGGER MODES (NEW vs. ManyChat)

Chatfuel supports BOTH trigger modes simultaneously. Pick per-script.

### Mode 1 — Comment-to-DM (DEFAULT, lower friction)
1. Chatfuel → Automations → New automation → "TikTok comment trigger"
2. Trigger: keyword in comment matches `{CTA_KEYWORD}`
3. Action: send private DM to the commenter with the welcome message
4. The viewer's barrier to entry: just type one word in comments. Conversion rate is meaningfully higher than DM-first.

### Mode 2 — DM keyword trigger (fallback / for niches where comments are noisy)
1. Trigger: user sends DM containing `{CTA_KEYWORD}`
2. Action: same flow as Mode 1
3. Use this when comment automation feels off-brand or the niche has comment noise

### Per-script selection
The script_json schema gains a `cta.mode: "comment" | "dm"` field. Default: `"comment"`. Production Agent reads this and prompt template adjusts the spoken/on-screen CTA accordingly:
- Comment mode: "Comment CALM and I'll send you the guide."
- DM mode: "DM me CALM for the guide."

Both modes route to the same Chatfuel flow → same n8n webhook.

---

## c) 6-STEP MESSAGE FLOW (in Chatfuel flow editor)

### Message 1 — Instant reply (0s, in DM)
```
Hey 👋

Got your message about {CTA_KEYWORD}. Sending the resource now.

What's the best email for it?
```
User Input → Email field. Chatfuel built-in email validator.

### Message 2 — Email retry (if invalid)
```
Hmm, that email looks off. Try once more?
```
Max 2 retries. After 2 fails: "Try again later from the original video."

### Message 3 — Consent (GDPR double opt-in)
```
Quick check before I send: do you agree to receive a few emails per week with practical tips, plus the {RESOURCE_NAME}?

[Yes, send it] [No thanks]
```
Buttons set: User Field → consent = true/false.

### Message 4 — Resource delivery (if consent=Yes)
```
Sending it now.

Check your email — should land in the next minute. Spam folder if you don't see it.

I post 5 of these per week. Reply anytime if you want to chat.

— {PERSONA_NAME}
```

### Message 5 — External Request (HTTP) to n8n
**Action**: Chatfuel "JSON API plugin" → External Request
- URL: `{N8N_URL}/webhook/chatfuel/lead`
- Method: POST
- Headers: `Content-Type: application/json`, `X-Hub-Signature-256: {HMAC}`
- Body:
```json
{
  "client_id": "{CLIENT_ID}",
  "chatfuel_user_id": "{{user_id}}",
  "tiktok_user_id": "{{tiktok_user_id}}",
  "trigger_source": "comment|dm",
  "keyword": "{CTA_KEYWORD}",
  "email": "{{user_email}}",
  "consent": true,
  "free_resource_url": "{FREE_RESOURCE_URL}"
}
```

### Message 6 — Success confirmation (via n8n response)
n8n returns Chatfuel's expected response with success message + `set_attribute: lead_captured=true`. Chatfuel renders the success text.

### If n8n times out
Fallback: "Got you on the list. Check your inbox in a few minutes." + tag `capture_pending`.

---

## d) n8n RESPONSE FORMAT (Chatfuel JSON API)

```json
{
  "messages": [
    { "text": "✅ You're in! Check your email for {RESOURCE_NAME}." }
  ],
  "set_attributes": {
    "lead_captured": "true",
    "lead_source": "tiktok_comment"
  }
}
```

Simpler than ManyChat's v2 format. The n8n workflow `5f. chatfuel-leadcapture.json` returns this shape.

---

## e) FAILURE HANDLING

| Failure mode | Detection | Recovery |
|--------------|-----------|----------|
| Invalid email | Chatfuel email validator | Retry message (max 2 attempts) |
| Webhook timeout >10s | n8n responds late, Chatfuel moves on | Show fallback message + tag `capture_pending` |
| Kit (ConvertKit) API error | n8n catches in subscribe step | Insert events row, retry tag, alert operator |
| Empty consent | n8n validation fails | Chatfuel shows "Try again" message |
| Duplicate email | Kit returns 200 with existing subscriber | Treat as success, dedupe in Supabase by email |

---

## f) POST-CAPTURE EMAIL SEQUENCE (Kit / ConvertKit) — UNCHANGED FROM ORIGINAL SPEC

| Day | Subject | Goal |
|-----|---------|------|
| 0 | "your {RESOURCE_NAME}" | Resource delivery + first-person welcome |
| 1 | "the thing most people miss about {NICHE_TOPIC}" | One insight from the channel |
| 3 | "weekly rhythm" | Soft TikTok follow CTA |
| 7 | "{SECOND_RESOURCE_TITLE}" | Deeper resource + community signal question |
| 14 | "{SUBJECT}" | First soft brand mention slot (placeholder) |

All emails: plain text, first-person, no HTML, no images, <200 words. Subject lines lowercase preferred for the niche. Email body templates preserved from prior version.

### Day 0 — Resource delivery
```
Subject: your {RESOURCE_NAME}

Hey,

You messaged me {CTA_KEYWORD} — here's the {RESOURCE_NAME}: {FREE_RESOURCE_URL}

Quick context: {1-2 SENTENCES}

I'll send one practical thing per week. Reply if anything resonates.

— {PERSONA_NAME}

P.S. Channel: {TIKTOK_HANDLE}
```

(Days 1, 3, 7, 14 templates same as in the prior version — preserved in commit history.)

---

## g) GDPR — STRENGTHENED FOR EU OPERATOR

Operator (Yohan) is in France → full GDPR applies.

- **Lawful basis**: explicit consent collected in Message 3, stored in `dm_leads.consent=true`.
- **Double opt-in**: Kit form requires email confirmation click before subscription active.
- **Confirmation tracking**: Kit webhook → n8n updates `dm_leads.double_opt_in_confirmed=true`.
- **Right to deletion**: `/webhook/gdpr/delete` workflow removes Kit subscriber + soft-deletes Supabase row + R2 prefix.
- **Data minimization**: only email + chatfuel_user_id + tiktok_user_id stored. No name/address/phone.
- **Privacy policy**: link from every email footer. Hosted on Lovable landing page or GitHub Pages.
- **Data controller**: operator entity (you for c_001; for DFY clients: client is controller, you are processor under DPA).

---

## h) CHATFUEL VS MANYCHAT — REFERENCE

| Feature | ManyChat | Chatfuel | Impact |
|---------|----------|----------|--------|
| Works in EU | ❌ NO | ✅ YES | Critical for Yohan |
| Comment-to-DM in US/EU | ❌ | ✅ | Lower-friction CTA |
| TikTok integration | Yes (limited regions) | Yes (full) | Chatfuel wins |
| Visual flow builder | Excellent | Good | Acceptable tradeoff |
| Pricing | $15-25/mo | ~$15-20/mo | Comparable |
| API + webhooks | v2 JSON | Plain JSON | Chatfuel slightly simpler |

**Verdict**: Chatfuel is strictly better for this use case. ManyChat was wrong for an EU operator.

---

## i) KEY LINKS

- Chatfuel TikTok: https://chatfuel.com/tiktok
- Chatfuel JSON API plugin docs
- Kit (ConvertKit) API: https://developers.convertkit.com/
- Kit double opt-in: Settings → Email → Confirmation → "Require"
