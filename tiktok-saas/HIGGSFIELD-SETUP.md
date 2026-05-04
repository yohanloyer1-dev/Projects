# HIGGSFIELD CHARACTER SETUP — D8
# Step-by-step MCP session guide for creating a consistent AI character persona
# Last updated: 2026-05-04 | Higgsfield model: Seedance 2.0 | MCP endpoint: https://mcp.higgsfield.ai/mcp

> Run this guide once per client. Output: a Higgsfield character ID + reference asset URLs + persona spec, all stored in Supabase + GitHub. After this is done, all weekly video generation reuses the same character automatically.

---

## a) PRE-SESSION PREPARATION (operator does this BEFORE the MCP session)

### Materials needed

| Item | What | Where it goes |
|------|------|---------------|
| Persona description | 4-6 sentences describing who the character is | persona.md sections 1-2 |
| Wardrobe brief | 3 outfit options matching the niche tone | persona.md section 3 |
| Background brief | 2-3 background settings (e.g., "minimal home office, warm light") | persona.md section 4 |
| Tone adjectives | 5-8 adjectives ("calm", "warm", "no-nonsense") | persona.md section 6 |
| 3 reference photos | High-resolution (≥1080×1920), 9:16, well-lit | uploaded to R2 → URLs in persona.md |

### Reference photo sourcing
Use AI image generation (Midjourney, DALL-E 3, Flux) to create 3 candidate reference photos. Each photo must show:
- The character in 9:16 portrait orientation
- Clear face visible (Higgsfield uses face for identity lock)
- Wardrobe consistent across all 3 photos
- Slightly different angles (front, ¾ left, ¾ right) — gives Seedance 2.0 better identity training data
- Same background in all 3 (or at least same lighting style)

Upload all 3 to Cloudflare R2 under: `clients/{CLIENT_ID}/persona/ref_1.jpg`, `ref_2.jpg`, `ref_3.jpg`. Get public URLs.

### Niche tone calibration
For "quiet health optimization for busy professionals":
- Persona age: 28-38
- Vibe: knowledgeable peer, not guru. Like a smart friend who reads research papers.
- Wardrobe: minimal, neutral palette (cream, charcoal, sage), modern fit
- Background: home office or kitchen, soft natural light, plants OK, no clutter
- Voice: warm but direct. Slight French accent acceptable if EU audience.

---

## b) MCP SESSION STEPS (run these in order in a Claude Code session with MCP enabled)

### Step 1 — Verify MCP connection
```
[Claude Code]: List the tools available from the Higgsfield MCP server.
```
Expected: tools like `higgsfield_create_character`, `higgsfield_generate_video`, `higgsfield_check_status`. If MCP is not connected, see Troubleshooting.

### Step 2 — Define the character

Paste the following into Claude Code, replacing placeholders:

```
Using the Higgsfield MCP, create a new character for client {CLIENT_ID} with these specs:

Name: {PERSONA_NAME} (e.g., "Léa")
Reference images:
1. {R2_URL_REF_1}
2. {R2_URL_REF_2}
3. {R2_URL_REF_3}

Description: {PERSONA_DESCRIPTION_PARAGRAPH}

Style keywords: {STYLE_KEYWORDS_COMMA_SEPARATED}

Aspect ratio: 9:16 vertical
Format: short-form vertical video, 35-45 seconds

Confirm character ID after creation.
```

Claude calls Higgsfield MCP `create_character` tool. Returns: `character_id`.

### Step 3 — Generate 3 test videos

```
Using the character ID from Step 2, generate 3 short test videos to validate consistency. For each:

Test 1 — Static-ish:
"Persona sits at home office desk, looks at camera, says: 'Hey. Today's tip is about something most people don't realize.' Cut to insight. End with: 'DM me CALM if you want the full guide.' Style: warm tones, soft natural light, minimal background."

Test 2 — Mid-shot motion:
"Persona stands in kitchen, holds a glass of water, walks slowly toward camera while speaking. Says: 'Most people skip this step. It costs them 30 minutes of focus.' Continues into kitchen scene. End with CTA. Style: cinematic, soft daylight."

Test 3 — Direct talking head:
"Persona sits, looks at camera. Slightly different framing than Test 1. Says: 'Three things I do every Sunday that change my whole week.' Lists 3 things with on-screen text overlay. End with CTA."

For all 3:
- Aspect 9:16
- Duration: 35-45s
- Same character (use character_id)
- Use style keywords from persona spec

After generation, return all 3 video URLs.
```

### Step 4 — Validate consistency

Manually review the 3 videos. Check:

- [ ] Same face across all 3 videos (no morphing, no obvious feature drift)
- [ ] Same wardrobe palette (clothing color/style consistent)
- [ ] Same background tone (lighting, color temperature)
- [ ] Same voice (if Seedance 2.0 generated audio)
- [ ] 9:16 confirmed in all 3
- [ ] Duration 35-45s in all 3
- [ ] Mouth movement matches narration (Seedance 2.0 phoneme lip-sync should be ≥90% accurate)

If any check fails: regenerate Test N with adjusted prompt. If face drifts: re-train character with more reference photos (back to Step 2).

### Step 5 — Lock the character

Once 3 tests pass:
- Mark character ID as production-ready in Supabase
- Store all 3 test video URLs as "consistency baseline" — reference for future drift checks

---

## c) POST-SESSION STORAGE

### Supabase update
```sql
UPDATE client_config 
SET higgsfield_character_id = '{CHARACTER_ID}',
    persona_ref_image_url = '{R2_URL_REF_1}'
WHERE client_id = '{CLIENT_ID}';
```

### GitHub update
Write the full persona spec to `clients/{CLIENT_ID}/persona.md` (template in section d below). Commit with: `persona: {CLIENT_ID} character locked — {CHARACTER_ID}`.

---

## d) PERSONA.md TEMPLATE

```markdown
# Persona — {CLIENT_NAME} ({CLIENT_ID})
> Locked: {DATE} | Higgsfield character ID: {CHARACTER_ID}
> All weekly video generation MUST reference this spec. Never deviate without operator approval.

## 1. Identity
**Name**: {PERSONA_NAME}
**Age range**: {28-38}
**Implied profession/background**: {e.g., "wellness writer who reads research papers"}
**Personality**: {3-5 sentences}

## 2. Description (one paragraph for AI image/video generation)
{4-6 sentence description that captures the character. Used as the base prompt for every video.}

## 3. Wardrobe
- Primary palette: {cream, charcoal, sage}
- Style: {minimal, modern fit, slight oversized}
- Acceptable items: {linen shirts, knit sweaters, neutral t-shirts}
- Never wear: {logos, branded clothing, athletic wear, formal suits}

## 4. Background
- Primary setting: {home office, soft daylight, plants, minimal desk}
- Alternate settings: {kitchen with morning light, reading corner with armchair}
- Lighting: {natural daylight, warm 3500K-4000K when artificial}
- Never: {harsh studio lighting, fluorescent, dark/moody}

## 5. Camera spec
- Aspect ratio: **9:16 vertical (non-negotiable)**
- Default framing: mid-shot (chest-up)
- Camera movement: minimal — slight push-in or static. Never handheld shake.
- Eye contact: looking at camera 80% of the time

## 6. Style keywords (used in every video prompt)
{cinematic, warm tones, soft natural light, minimal, calm, modern}

## 7. Voice rules (if persona speaks audio)
- Pace: medium-slow (140-160 words/minute)
- Tone: warm, knowledgeable, direct
- Never: rushed, salesy, performative excitement
- Filler words OK: "honestly," "look," "the thing is"
- Forbidden: "literally," "trust me bro," "guys"

## 8. Consistency rules (enforced at generation time)
1. Same face across all videos — use character_id
2. Same wardrobe palette across a single week's batch
3. Same background within a single video (no scene cuts unless scripted)
4. 9:16 aspect always
5. Duration 35-45s

## 9. What this character NEVER says
- Medical claims ("cure," "treat," "diagnose")
- Brand names not in client's approved list
- "DM me CALM" — uses {CTA_KEYWORD} from client_config
- "Comment X" — always uses DM-first CTA (regional ManyChat constraint)
- Specific dosages, times-to-effect, or before/after promises

## 10. Higgsfield character data
- Character ID: {CHARACTER_ID}
- MCP endpoint: https://mcp.higgsfield.ai/mcp
- Reference asset URLs:
  - Ref 1: {R2_URL_REF_1}
  - Ref 2: {R2_URL_REF_2}
  - Ref 3: {R2_URL_REF_3}
- Test video URLs (consistency baseline):
  - Test 1: {URL}
  - Test 2: {URL}
  - Test 3: {URL}
- Last consistency validation: {DATE}

## 11. A/B persona variants (added when A/B Persona Agent activates)
- Persona B character ID: {null until activated}
- Persona B wardrobe variation: {null}
- A/B test start date: {null}
```

---

## e) PER-CLIENT REPLICATION INSTRUCTIONS

When onboarding a new client, what changes vs. what stays:

### Changes per client
- Persona name, age range, implied profession (match niche)
- Wardrobe palette (match niche tone)
- Background style (match niche aesthetic)
- Style keywords (match niche)
- Voice rules (match audience expectation)
- Reference photos (3 new ones, niche-appropriate)
- Character ID (new Higgsfield character per client)

### Stays fixed across all clients
- MCP endpoint: https://mcp.higgsfield.ai/mcp
- Aspect ratio: 9:16
- Duration: 35-45s
- Camera movement: minimal
- Lip-sync: Seedance 2.0 default
- Consistency check protocol (3 test videos, manual review)
- Storage path: `clients/{CLIENT_ID}/persona/...` in R2
- File: `clients/{CLIENT_ID}/persona.md` in GitHub

### Estimated time per new client
- Reference photo generation (Midjourney): 30 minutes
- R2 upload: 5 minutes
- MCP session (Steps 2-3): 10 minutes
- Manual consistency review (Step 4): 15 minutes
- persona.md write: 15 minutes
- **Total: ~75 minutes per new client persona setup**

---

## f) AUTOMATED CONSISTENCY VALIDATION

The Production Agent runs this check **before every video generation**:

```javascript
function validateConsistency(prompt, persona) {
  const required = [
    persona.name,
    ...persona.style_keywords.slice(0, 3),  // at least 3
    "9:16",
    persona.background_primary,
    persona.wardrobe_primary_palette
  ];
  
  const missing = required.filter(item => !prompt.toLowerCase().includes(item.toLowerCase()));
  
  if (missing.length > 0) {
    throw new Error(`Consistency check failed. Missing: ${missing.join(', ')}`);
  }
  return true;
}
```

If consistency check throws: BLOCK generation, INSERT events row (level=error), alert via Telegram. Never silently degrade quality.

### Drift detection
Once per month: regenerate one test video and visually compare to the consistency baseline (3 test videos from Step 3). If drift is visible (face, wardrobe, lighting): re-train character with fresh reference photos.

---

## TROUBLESHOOTING

| Problem | Fix |
|---------|-----|
| MCP not connected in Claude Code | Add `https://mcp.higgsfield.ai/mcp` to `.mcp.json` in workspace |
| Character ID returns "not found" | Token may be scoped to a different Higgsfield account. Re-auth and retry. |
| Face drift in test videos | Add 2-3 more reference photos with same wardrobe, regenerate character |
| Lip-sync >10% off | Use shorter sentences in script (12-15 words max per beat) |
| Background changes within one video | Use shorter `visual_direction` per beat, repeat background spec verbatim |
| Generation takes >10 min | Switch from Seedance 2.0 to Seedance 2.0 Turbo (lower quality, faster). Document in events. |
