# Screenshot Renaming - Quick Reference Guide

## ONE-PAGE SUMMARY

### The Method (No Shortcuts!)
1. ✅ Open each screenshot **individually**
2. ✅ State what you see with **certainty** (no guessing)
3. ✅ Compare to current filename
4. ✅ Rename **only if needed**
5. ✅ Preserve timestamp in new name

### Platform Identification Quick Check

**Slack?** → @mentions, message bubbles, workspace name
**Email?** → From/To headers, email address, signature
**WhatsApp?** → Phone bubbles, "Message" style, blue checkmarks
**Discord?** → Server names, role colors, # channels
**Google Calendar?** → Calendar grid, "Google Meet" button, attendees
**CRM?** → Company names, deal stages, pipeline
**Web?** → Browser URL bar, website nav, domain
**System?** → macOS/Windows dialog, file browser, settings

### Red Flag Filenames (Almost Always Need Fixing)

```
email-afternoon-communication-*          → Check content carefully!
email-evening-communication-*            → Probably not an email
gorgias-or-support-interface-*           → Often system dialog/Finder
document-or-webpage-content-*            → Too vague, needs specific
code-or-error-page-*                     → Rarely what it claims
[anything]-or-[anything]-*               → Indicates uncertainty
```

### Good Name Format

```
[PLATFORM]-[SUBJECT]-[KEY-DETAILS]-[DATE-TIME].png

Examples:
✅ slack-conversation-George-Rich-Panel-Gorgias-2025-01-28-10.00.04.png
✅ email-Antoine-Roffler-order-value-meeting-2025-01-17-08.38.52.png
✅ google-calendar-Maud-Mouaad-Arnaud-Gorgias-2025-01-15-15.45.41.png
✅ CRM-partner-referral-form-Yohan-Loyer-2025-01-24-17.45.19.png
✅ WhatsApp-conversation-coffee-alternatives-2025-01-09-21.56.49.png
```

### Common Mistakes to Avoid

❌ Changing "email" to "slack" without reviewing full content
❌ Using generic words: "communication", "interface", "content"
❌ Losing the original timestamp from filename
❌ Renaming multiple files without checking each one
❌ Assuming filename is correct without looking at image
❌ Guessing when unsure — ask instead!

### Workflow Overview

```
1. ASSESS FOLDER
   └─ Count files, identify dimension ranges (under/over 2000px)

2. CHECK HIGH-RISK FILES FIRST
   └─ Files with generic names have 73% correction rate

3. REVIEW REMAINING FILES ONE-BY-ONE
   └─ Specific names are usually accurate (0% error rate)

4. RESIZE FILES OVER 2000px
   └─ Use PIL, maintain aspect ratio, quality 95, backup originals

5. VERIFY
   └─ Spot-check renamed files, confirm readability
```

### Decision Tree

```
Question: Does the filename match what I see in the screenshot?

    Yes + specific details?
    ├─ YES → ✅ ALREADY CORRECT (no rename needed)
    └─ NO  → See question below

    No + generic/ambiguous name?
    ├─ YES → ❌ NEEDS RENAMING
    └─ NO  → Verify platform carefully, may need rename

    Can't determine platform?
    └─ ASK USER before proceeding
```

### Statistics from January Testing

| Metric | Result |
|--------|--------|
| Total files | 98 |
| Generic names | 30 (30%) |
| Specific names | 68 (70%) |
| Correction rate on generic names | 73% (22/30) |
| Correction rate on specific names | 0% |
| Files needing resize | 22 (22%) |
| Total time for thorough review | ~3 hours |

**Key Finding:** Generic/vague names are misclassified 73% of the time. Specific names are reliable.

### Token Budget Notes

- One file one-by-one review: ~1,400-1,500 tokens
- A folder of 98 files: ~130-150k tokens
- 60k tokens remaining = ~40-50 files max

If running low on tokens mid-folder:
1. Stop at current file
2. Document where you stopped
3. Create summary of patterns found
4. Next session resumes from exact stopping point

### When to Ask for Clarification

- Platform looks ambiguous (has features of multiple platforms)
- Content is unclear or partially visible
- File appears sensitive and you want to confirm naming approach
- You see contradictions between filename and content

**Always ask rather than guess!**

---

## FOR FEBRUARY/LATER MONTHS

1. Request folder access
2. Run assessment phase (count files, identify dimensions)
3. Identify high-risk filenames (generic names)
4. Start with high-risk files (highest payoff)
5. Continue systematically through folder
6. Resize files over 2000px when done
7. Document all changes

Use this guide + full SCREENSHOT_RENAMING_SKILL.md for complete methodology.
