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

**Estimated time:** 30–60 minutes (dictated, not typed)
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

1. **Ask Claude to compile** the full `yohan-voice.md` document (it does this automatically after Q100)
2. **Review the Quick Reference Card** — this is what you'll use in 90% of sessions
3. **Save the file** to `/Users/yohanloyer/Projects/Linkedin posting/yohan-voice.md`
4. **Push to GitHub:**
   ```bash
   cd /Users/yohanloyer/Projects
   git add "Linkedin posting/yohan-voice.md"
   git commit -m "Add yohan-voice.md — voice profile from interview session"
   git push origin main
   ```
5. **Update YOHAN_MASTER_BRIEF.md** — add a line at the top pointing to `yohan-voice.md` as the companion file
6. **Test in a blank session:** Open a fresh Claude chat, paste the Quick Reference Card, ask it to write a LinkedIn post on a topic only you would write. If it sounds like you → ship it.

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

## Anything Else Worth Researching Before?

*These are the open questions worth addressing before or after the interview:*

- **What does Ruben's own `ruben.md` voice file look like?** He references it publicly — studying it could sharpen what depth looks like before you start. Ask Claude to search for it.
- **Your reference creators:** Could be worth doing a quick "voice analysis" of 2–3 posts from Eli Weiss and Nick Shackelford before the interview — to crystallize what you're drawn to and why, so your answers are sharper.
- **Should `yohan-voice.md` cover your business voice too?** Right now this is scoped to LinkedIn. But if you want it to also cover client emails, agency proposals, or internal comms — flag that at the start of the interview so Claude knows to probe those angles too.
- **Portability vs. depth tradeoff:** The interview produces ~20K words compressed to ~4K tokens. You'll want to decide: one master file, or separate LinkedIn vs. agency voice profiles? Both is defensible given your dual public persona.

---

*Source: Ruben Hassid's guide — [I am just a text file](https://ruben.substack.com/p/i-am-just-a-text-file) | Interview prompt extracted and adapted for Yohan's context*
*Created: 2026-05-03*
