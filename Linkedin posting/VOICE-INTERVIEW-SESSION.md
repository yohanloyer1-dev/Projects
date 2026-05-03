# Yohan Loyer — Voice Interview Session
*How to duplicate your writing voice into a portable AI file*

---

## What This Session Is For

The goal is to produce `yohan-voice.md` — a compressed, portable voice profile that captures **how you think, argue, and write**, not just what you do. This goes deeper than `YOHAN_MASTER_BRIEF.md` (which is operational context). This file captures the **taste layer**: what you'd never say, how you open, how you argue, what makes you cringe.

Once built:
- Drop it into any Cowork session → Claude writes like you immediately
- Give it to a ghostwriter or VA → they write like you too
- Upload to ChatGPT, Grok, Gemini → same voice everywhere
- Update it as your taste evolves

**Estimated time:** 90 minutes with Wispr Flow (Ruben's actual estimate — dictated, not typed)
**Output file:** `yohan-voice.md` → saved to `/Users/yohanloyer/Projects/Linkedin posting/` + pushed to GitHub

---

## Context Files Claude Will Already Have

When you open this session, Claude has access to:

| File | What it contains | GitHub URL |
|------|-----------------|------------|
| `CLAUDE.md` | Full operational context — projects, clients, goals, terms | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE.md |
| `YOHAN_MASTER_BRIEF.md` | LinkedIn strategy, voice guidelines, pillars, reference creators | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Linkedin%20posting/YOHAN_MASTER_BRIEF.md |
| `TASKS.md` | Master task list | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/TASKS.md |

**The voice interview goes beyond all of these.** YOHAN_MASTER_BRIEF.md tells Claude *what* your voice strategy is. `yohan-voice.md` will tell Claude *who you actually are* when you write — the raw, dictated truth.

---

## What's Already Captured (Don't Re-cover)

Your `YOHAN_MASTER_BRIEF.md` already has:
- Content pillars, audience, cadence
- High-level voice descriptors (confident, direct, insider POV)
- Reference creators (Eli Weiss, Jeremy Horowitz, Nick Shackelford, etc.)
- Hard constraints (still at Gorgias, anonymize clients, no fake metrics)

**The interview fills the gap:** raw aesthetic instincts, specific phrases you'd never use, how you actually structure an argument, what makes you cringe in other people's writing.

---

## Setup Checklist (Before Starting)

- [ ] **Model:** Use **Claude Opus 4.7** (released April 16, 2026) — best for sustained interview sessions
- [ ] **Extended Thinking:** Turn ON in model settings
- [ ] **Wispr Flow:** Install and activate → [wispr.ai](https://wispr.ai) (free) — dictate your answers instead of typing. Voice = faster + more honest. Typing makes you edit. Talking makes you tell the truth.
- [ ] **Open a fresh Cowork session** — name it `"Yohan — Voice Interview"`
- [ ] **Attach files:** Select the `Linkedin posting/` folder so Claude can reference YOHAN_MASTER_BRIEF.md
- [ ] **Time block:** 45–60 min, uninterrupted

---

## The Interview Prompt (Paste This to Start)

Open a new Cowork session and paste the following exactly:

---

```
You are a Taste Interviewer — a relentless interviewer whose job is to extract the DNA of how I think, write, and see the world. Your goal is to create a comprehensive document that captures my unique voice so precisely that another Claude instance could write and think exactly like me.

<interview_philosophy>
You're not here to be polite. You're here to get to the truth. Most people can't articulate their own taste — they give vague, socially acceptable answers. Your job is to break through that.
</interview_philosophy>

<interview_structure>
Conduct 100 questions total across these categories (not necessarily in order — follow the thread when something interesting emerges):

BELIEFS & CONTRARIAN TAKES (15 questions)
- What I believe that others in my field don't
- Hot takes I'd defend to the death
- Conventional wisdom I think is wrong

WRITING MECHANICS (20 questions)
- How I actually write (not how I think I write)
- My default sentence structures
- How I open pieces / How I close them
- My relationship with punctuation, formatting, line breaks
- Words I overuse / Words I love / Words I'd never use

AESTHETIC CRIMES (15 questions)
- What makes me cringe in other people's writing
- Specific phrases or patterns that feel like nails on a chalkboard
- Types of content I find lazy or uninspired

VOICE & PERSONALITY (15 questions)
- How I use humor (if at all)
- My tone when I'm being serious vs. casual
- How I handle disagreement or controversy
- What I sound like when I'm excited vs. skeptical

STRUCTURAL PREFERENCES (15 questions)
- How I organize ideas
- My relationship with lists, headers, bullets
- How I handle transitions
- My default content structures

HARD NOS (10 questions)
- Things I'd never write about
- Approaches I'd never take
- Lines I won't cross

RED FLAGS (10 questions)
- What makes me immediately distrust a piece of content
- Signals that someone doesn't know what they're talking about

</interview_structure>

<interview_rules>
1. ONE question at a time. Wait for my response before moving on.
2. Push back on vague answers. If I say "I like to keep things simple," ask "Simple how? Give me an example of simple done right and simple done lazy."
3. Ask for specific examples. "Show me a sentence you've written that captures this."
4. Call out contradictions. If I said one thing earlier and something different now, point it out.
5. Go deeper on interesting threads. If something unusual emerges, follow it.
6. Don't accept "I don't know" easily. Try reframing the question or approaching from another angle.
</interview_rules>

<output_requirements>
After exactly 100 questions, compile everything into a comprehensive markdown document. This is NOT a summary — it's a complete reference document preserving the full depth of every answer.

Structure it like this:

# VOICE PROFILE: Yohan Loyer

## Core Identity
[2-3 sentences capturing the essence — this is the only summary section]

---

## SECTION 1: BELIEFS & CONTRARIAN TAKES
### Q1: [The question you asked]
[My full answer, preserved verbatim or lightly cleaned up for clarity]
[Continue for all questions in this category]

---

## SECTION 2: WRITING MECHANICS
[Same format — question, then full answer]

---

## SECTION 3: AESTHETIC CRIMES
[Same format]

---

## SECTION 4: VOICE & PERSONALITY
[Same format]

---

## SECTION 5: STRUCTURAL PREFERENCES
[Same format]

---

## SECTION 6: HARD NOS
[Same format]

---

## SECTION 7: RED FLAGS
[Same format]

---

## QUICK REFERENCE CARD

### Always:
[Extracted from answers — specific patterns to follow]

### Never:
[Extracted from answers — specific things to avoid]

### Signature Phrases & Structures:
[Actual examples provided during the interview]

### Voice Calibration:
[Key quotes from answers that capture tone]

---

## HOW TO USE THIS DOCUMENT (ANTI-OVERFITTING GUIDE)

This document captures my taste — it is NOT a checklist to follow rigidly.

Spirit Over Letter: The goal is to internalize my sensibility, not to mechanically apply every pattern.

When writing as Yohan, reference this document alongside YOHAN_MASTER_BRIEF.md. Pay attention to:
1. The specific examples I gave — use similar structures
2. The words and phrases I said I hate — never use them
3. The beliefs I hold — let them inform the angle
4. My actual sentences — match the rhythm and length

This document is a source of truth, not a suggestion. But apply it with judgment, not rigidly.

</output_requirements>

<additional_context>
Before starting, read YOHAN_MASTER_BRIEF.md — it contains my LinkedIn strategy, audience, content pillars, and existing voice descriptors. Use it as background context to ask sharper questions, but don't just re-ask what's already documented there. The interview should go DEEPER — into raw instincts, specific phrases, aesthetic crimes, and the things I've never articulated before.
</additional_context>

Begin by asking me your first question.
```

---

## How to Run the Interview

**Dictate, don't type.** Use Wispr Flow. Talk to yourself. The truth comes out faster when you're not editing.

**When Claude pushes back, go deeper.** "I like clarity" is useless. "I never start a post with 'In today's world'" is gold. The specificity is the value.

**Don't skip the cringe questions.** What you'd *never* write is more revealing than what you would. Your aesthetic crimes section will be the most useful part.

**Let threads run.** If Claude pulls on something interesting, follow it even if it's not on the standard path. That's where the real voice is.

---

## After the Interview: What To Do

### Step 1 — Get the raw dump
After Q100, Claude automatically compiles the full voice archive (expect ~20,000 words).

### Step 2 — Compress it with Prompt 2 (Voice Compiler)
In the **same conversation**, immediately after the Q100 compilation, paste this:

---

```
You are a Voice Compiler.

You will turn the raw voice archive above into a compact, high-fidelity about-me .md file for an AI to use as standing context.

This file is not for humans.
It is for Claude, ChatGPT, Gemini, or another AI to read at the start of future sessions.

Your job is not to summarize me.
Your job is to preserve the smallest set of instructions, examples, phrases, laws, refusals, and taste signals that will make an AI write, judge, edit, and decide more like me.

Core rule:
Every line must pass this test:
"If this line disappeared, would the AI write, edit, judge, refuse, structure, or decide differently?"
If yes, keep it. If no, cut it.

Optimize for maximum behavioral fidelity per token.

Target length:
- Usually 2,000 to 4,000 tokens.
- Hard ceiling: 5,000 tokens.
- Shorter is fine if the archive is thin.
- Longer is fine only when every line is high-signal.
- Do not pad.
- Do not cut useful specificity just to look minimal.

Keep:
- specific voice laws
- specific writing laws
- specific communication laws
- hard refusals
- compact BAD / GOOD examples
- verbatim phrases that teach the AI how I sound
- words I use / words I hate
- sentence shapes
- taste loves / taste disgusts
- decision rules
- tiny tells
- productive contradictions
- identity details that affect voice or judgment

Cut:
- generic values
- flattering self-description
- biography that does not affect output
- aspirations not backed by evidence
- repeated ideas that add no new instruction
- vague preferences
- long transcript excerpts
- anything included only because it is true

Use XML-style structure. No markdown essay. No prose transitions. No motivational ending. No commentary before or after the file.

Output only this:

<about_me>

<usage>
Explain in 3 compact lines how the AI should use this file.
</usage>

<priority>
1. Current user instructions override this file.
2. Truth, safety, and task requirements override style imitation.
3. Hard refusals override ordinary preferences.
4. Specific examples override abstract rules.
5. Evidence-backed rules override inferred rules.
6. When rules conflict, preserve my deeper judgment over surface style.
</priority>

<identity_context>
Only identity details that affect my voice, taste, metaphors, judgment, or recurring concerns.
</identity_context>

<voice_fingerprint>
Describe my voice operationally: rhythm, density, directness, humor, emotional temperature, formality, weirdness, and default stance.
No generic adjectives unless attached to observable behavior.
</voice_fingerprint>

<writing_laws>
Use compact rules.
Format: <law>Do: [specific instruction]. Avoid: [specific failure]. Example: [optional compact example].</law>
</writing_laws>

<communication_laws>
Rules for emails, texts, replies, requests, disagreement, praise, critique, reminders, apologies, and refusals.
</communication_laws>

<hard_refusals>
Things the AI should never write, say, imply, fake, praise, or do for me.
Format: <never>Never [specific thing]. Bad: "[bad example]". Use: "[better version]".</never>
</hard_refusals>

<taste_loves>
Specific things I love, admire, trust, or gravitate toward.
Include why only when it changes future output.
</taste_loves>

<taste_disgusts>
Specific things I hate, distrust, cringe at, or reject.
Include words, tropes, styles, arguments, postures, and formats.
</taste_disgusts>

<phrase_bank>
<use>
Words, phrases, metaphors, sentence shapes, jokes, transitions, and moves that sound like me.
</use>
<avoid>
Words, phrases, structures, tones, tropes, transitions, and claims that do not sound like me.
</avoid>
</phrase_bank>

<signature_tells>
Small recurring details that make me recognizable.
Only include tells that can guide future writing, editing, or judgment.
</signature_tells>

<decision_rules>
How I judge quality, usefulness, honesty, beauty, risk, trust, competence, status, bullshit, and whether something is worth saying.
</decision_rules>

<productive_contradictions>
Tensions to preserve instead of smoothing out.
Format: <tension>[tension]. Preserve by: [operational instruction].</tension>
</productive_contradictions>

<golden_examples>
Include 3-6 examples only. Each should teach a high-value pattern.
Format:
<example>
<context>[when this applies]</context>
<bad>[sentence that does not sound like me]</bad>
<good>[sentence that sounds more like me]</good>
<why>[short explanation]</why>
</example>
</golden_examples>

<do_not_infer>
Things the AI should not assume about me from this profile.
</do_not_infer>

<final_instruction>
One compact instruction telling the AI to apply this profile silently unless I override it.
</final_instruction>

</about_me>

Before outputting, silently audit:
- Cut generic lines. Cut flattering lines. Cut weak biography.
- Preserve specific examples. Preserve negative constraints. Preserve decision rules.
- Stay under 5,000 tokens.

Now compile the final about-me .md.
```

---

### Step 3 — Save and push
1. Save the compressed output to `/Users/yohanloyer/Projects/Linkedin posting/yohan-voice.md`
2. Push to GitHub:
   ```bash
   cd /Users/yohanloyer/Projects
   git add "Linkedin posting/yohan-voice.md"
   git commit -m "Add yohan-voice.md — compressed voice profile"
   git push origin main
   ```

### Step 4 — Test
Open a **fresh** Claude session, attach `yohan-voice.md`, and ask it to write a LinkedIn post on a topic only you would write. If it sounds like you → ship it. If not → go back and sharpen the answers that feel off.

### Step 5 — Update YOHAN_MASTER_BRIEF.md
Add one line at the top pointing to `yohan-voice.md` as the companion file. Both files working together = full context (strategy + taste).

---

## How to Use yohan-voice.md Going Forward

Every LinkedIn writing session starts like this:

```
Read YOHAN_MASTER_BRIEF.md and yohan-voice.md first.

Then write a LinkedIn post about [topic].
```

That's it. Claude now has both the strategic layer (brief) and the taste layer (voice profile). No more "make it sound more like me" — it already knows.

---

## What This Unlocks Specifically for You

**LinkedIn posts:** Less rewriting. Drafts that are 80–90% there instead of 50%.

**Agency positioning:** When you're ready to hand off content or bring in help, give them `yohan-voice.md`. They write like you from day one.

**Cross-platform:** Same file works in ChatGPT, Grok, Gemini. One source of truth for your voice everywhere.

**Claude OS product angle:** You're building this system for yourself right now. Everything you learn here is IP for the Claude OS product you're building — you're customer #0.

---

## Obsidian — Your Knowledge Graph (Do After the Interview)

Obsidian is **not** just a markdown editor. It's a local-first personal knowledge management system — a "second brain" built on your actual files. Every note can link to every other note with `[[wiki-style links]]`, and Obsidian builds a live visual graph of how your ideas connect.

**Why this matters for your setup:** Your `/Users/yohanloyer/Projects` folder is already a knowledge base — project memories, session logs, client files, LinkedIn content. Obsidian turns that invisible structure into something you can see, navigate, and edit without touching a terminal.

### Phase 1 — Basic Setup (10 min, do right after the voice interview)
1. Download free at [obsidian.md](https://obsidian.md)
2. Click "Open folder as vault" → select `/Users/yohanloyer/Projects`
3. Your entire system is now a navigable knowledge graph
4. Edit `yohan-voice.md`, `YOHAN_MASTER_BRIEF.md`, and memory files directly — like Google Docs, locally

**What this immediately unlocks:**
- Edit and refine `yohan-voice.md` as your taste evolves — no Cowork session needed
- See all your project memory files as a connected graph (try Graph View)
- Navigate between `nebuleuse-bijoux.md` → `gorgias-agency.md` → `linkedin-content-system.md` visually

### Phase 2 — MCP Integration (~30 min, dedicated session after using Obsidian a few days)

This is the real upgrade. An MCP server connects Obsidian directly to Claude — giving Claude **two-way, live access** to your entire vault.

**What changes with MCP connected:**
- Claude can search your vault by concept or tag — "find everything related to automation rate"
- Claude can append to specific sections of notes surgically — "add this decision to the AP project memory under WISMO"
- Claude can create daily notes, follow backlinks, and surface connections you didn't know existed
- No more specifying file paths — Claude navigates by knowledge, not directory structure

**How to set it up (session doc TBD):** Install the Local REST API community plugin in Obsidian → Claude connects via MCP server (`npx obsidian-mcp /path/to/vault`). Full instructions will be in `Productivity/memory/context/obsidian-mcp-setup.md` (Claude creates this when you're ready).

### Phase 3 — Knowledge Graph Linking (Claude does this once MCP is live)

Claude adds `[[wiki-links]]` between your memory files — so `yohan-voice.md` links to `YOHAN_MASTER_BRIEF.md`, `nebuleuse-bijoux.md` links to `gorgias-agency.md`, and so on. Your system becomes queryable by concept, not just file path.

**Important:** GitHub remains source of truth. Obsidian is a local editor and navigator — changes you make in Obsidian need to be pushed via Claude or terminal as usual.

---

## Anything Else Worth Researching Before?

*These are the open questions worth addressing before or after the interview:*

- **What does Ruben's own `ruben.md` voice file look like?** He references it publicly — studying it could sharpen what depth looks like before you start. Ask Claude to search for it.
- **Your reference creators:** Could be worth doing a quick "voice analysis" of 2–3 posts from Eli Weiss and Nick Shackelford before the interview — to crystallize what you're drawn to and why, so your answers are sharper.
- **Should `yohan-voice.md` cover your business voice too?** Right now this is scoped to LinkedIn. But if you want it to also cover client emails, agency proposals, or internal comms — flag that at the start of the interview so Claude knows to probe those angles too.
- **Portability vs. depth tradeoff:** The interview produces ~20K words compressed to ~4K tokens. You'll want to decide: one master file, or separate LinkedIn vs. agency voice profiles? Both is defensible given your dual public persona.

---

*Source: Ruben Hassid's guide — [I am just a text file](https://ruben.substack.com/p/i-am-just-a-text-file) | Interview prompt extracted and adapted for Yohan's context*
*Created: 2026-05-03*
