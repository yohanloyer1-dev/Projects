---
name: screenshot-renaming
description: |
  Systematically review and rename screenshots based on actual visual content with NO assumptions, approximations, or shortcuts. Use this skill whenever you need to organize and accurately name screenshots in folders by examining what's actually displayed in each image.

  Triggers: organizing screenshots, categorizing screenshots by content, renaming screenshots based on visual inspection, documenting screenshot libraries, preparing screenshot archives, reviewing image folders, screenshot naming standards, screenshot organization system.

  This skill MUST be used for ANY screenshot renaming work to ensure consistency with proven methodology.
---

# Screenshot Renaming Skill

## Overview

This skill provides a rigorous, repeatable methodology for reviewing and renaming screenshots based on their actual visual content. It enforces NO ASSUMPTIONS, NO GUESSING, and NO SHORTCUTS — only careful visual analysis and data-driven certainty.

This methodology was field-tested on 98 screenshots across January 2025 and achieved 23% correction rate on files with generic/misleading names, while maintaining accuracy on properly-named files.

## Core Principles

1. **ONE FILE AT A TIME** - Never batch-check multiple files. Review each screenshot individually with full attention.
2. **VISUAL ANALYSIS ONLY** - What you see in the screenshot is the source of truth, never the existing filename.
3. **NO ASSUMPTIONS** - If you cannot determine what you're seeing with certainty, ask the user for clarification.
4. **SPECIFICITY** - Names must describe actual content: who, what, where, when if visible. Avoid generic descriptors like "communication" or "interface".
5. **PRESERVE TIMESTAMPS** - Always maintain the original date-time stamp from the filename in the new name.
6. **PLATFORM IDENTIFICATION** - Be precise about content type: Slack vs WhatsApp vs Discord vs email vs web, CRM vs spreadsheet vs form, etc.

## Pre-Work: Assessment Phase

Before starting review work, analyze the folder to understand scope:

1. **Count total files** and identify dimension distribution
2. **Categorize files by dimension:**
   - Under 2000px (ready to review immediately)
   - Over 2000px (need resizing before analysis)
3. **Identify high-risk naming patterns:**
   - Generic names: `email-afternoon-communication`, `document-or-webpage-content`, `code-or-error-page`
   - Ambiguous platform names: `discord-*` (often Slack, WhatsApp, or email)
   - Mismatched categories: files labeled `gorgias-*` that are actually emails or system dialogs

## Primary Workflow: File-by-File Review

### For Each Screenshot:

**STEP 1: Open and Examine**
- Read the screenshot carefully
- Note ALL visible elements: UI type, text content, people/organizations mentioned, dates/times, specific features
- Identify the PLATFORM/TYPE with certainty:
  - **Email**: Message header, sender/recipient, email interface, signature
  - **Slack**: Message bubbles, @mentions, workspace name, thread indicators
  - **WhatsApp**: Phone number/contact bubbles, "Message" style, blue checkmarks, phone interface
  - **Discord**: Different UI design, server indicators, role colors
  - **Google Calendar**: Calendar grid, event details, "Google Meet" links, attendees section
  - **CRM/Salesforce**: Deal records, pipeline stages, company profiles, activity logs
  - **Web**: Browser URL bar, website interface, navigation menu
  - **System**: macOS/Windows dialog, file browser, system settings
  - **Spreadsheet/Table**: Columns, rows, data structure, formulas
  - **Chat/generic**: Message interface without clear platform markers

**STEP 2: Extract Key Information**
Write down factually what you see:
- **Primary subject**: What is the main content? (meeting, deal, conversation, etc.)
- **Key entities**: Names, company names, products mentioned
- **Specific details**: Numbers, amounts, dates, locations
- **Context**: Why does this screenshot matter? What problem does it document?

**STEP 3: Check Current Name**
- Read the existing filename
- Does it accurately describe what you see?
- Is it too generic? (Red flag: generic names often hide misclassified content)
- Are there contradictions? (File says "email" but shows Slack interface?)

**STEP 4: Propose New Name** (if needed)
Use this structure:
```
[PLATFORM]-[SUBJECT]-[KEY-DETAILS]-[DATE-TIME].png
```

Examples:
- ✅ `slack-conversation-George-Rich-Panel-Gorgias-comparison-Sasha-Nikoli-2025-01-28-10.00.04.png`
- ✅ `email-Antoine-Roffler-meeting-Cindy-Marie-order-value-2025-01-17-08.38.52.png`
- ✅ `google-calendar-meeting-Maud-Mouaad-Arnaud-Gorgias-customer-service-2025-01-15-15.45.41.png`
- ✅ `CRM-direct-intro-referral-form-Yohan-Loyer-Shopify-partner-2025-01-24-17.45.19.png`
- ✅ `WhatsApp-conversation-French-coffee-alternatives-adaptogens-2025-01-09-21.56.49.png`

Bad names (too generic):
- ❌ `email-afternoon-communication`
- ❌ `document-or-webpage-content`
- ❌ `gorgias-or-support-interface`

**STEP 5: Rename if Needed**
Only rename if current name is inaccurate. If accurate, mark as ✅ ALREADY CORRECT.

---

## Common Categorization Issues (Watch For These!)

### Platform Confusion

| Platform | Identifying Markers | Often Mistaken As |
|----------|-------------------|-------------------|
| **Slack** | Message bubbles, @mentions, workspace header, thread marks | Discord, WhatsApp, "chat" |
| **WhatsApp** | Phone number contacts, "Message" style, blue checkmarks, mobile phone UI | Discord, generic chat |
| **Discord** | Server names, role colors, # channels, different message bubble style | Slack, generic chat |
| **Email** | From/To headers, email signatures, "Reply" buttons, message threading | Chat, CRM messages |
| **Google Calendar** | Calendar grid, "Google Meet" buttons, attendees list, event details popup | Generic meeting, document |
| **CRM/Salesforce** | Company names, deal stages, activity records, relationship fields | Website, generic dashboard |

### Filename Red Flags

These patterns almost always indicate misclassification:

- `email-afternoon-communication-*` → Actually: Slack message, CRM dashboard, survey response, website
- `gorgias-or-support-interface-*` → Actually: System error dialog, Finder window, settings menu
- `document-or-webpage-content-*` → Actually: Specific article, product comparison, educational content
- `code-or-error-page-*` → Actually: Email message, product information, DHL error
- Any file with `-or-` in the name is likely uncertain and needs verification

---

## Handling Difficult Cases

### When Platform is Ambiguous

Ask the user with specificity:
- "This appears to be a messaging interface. Is this WhatsApp, Slack, Discord, or another platform?"
- Provide context from what you see: "I see @mentions (which suggests Slack) but also phone number formatting (which suggests WhatsApp)"

### When Content is Sensitive/Private

- Include visible names and details (they're already in the screenshot)
- Don't assume — state what you see: "Screenshot shows personal financial information"
- Respect privacy but don't obscure actual content in the name

### When Name is Partially Correct

Example: File says `email-afternoon-communication` but you can see it's a Slack message about Q1 offers from Charles and Neil.
- Don't just change `email` to `slack` (that's a shortcut)
- Review the whole message content and write a proper descriptive name
- Result: `slack-conversation-Charles-Crabtree-Neil-Forrest-Q1-offer-agreement-2025-01-14-15.14.27.png`

---

## Workflow: Processing a Folder

### Phase 1: Assessment (10-15 min)
```bash
python3 << 'EOF'
from PIL import Image
import os

folder = "/path/to/folder"
files = [f for f in os.listdir(folder) if f.endswith('.png')]

under_2000 = []
over_2000 = []

for f in sorted(files):
    img = Image.open(os.path.join(folder, f))
    width, height = img.size
    max_dim = max(width, height)

    if max_dim <= 2000:
        under_2000.append(f)
    else:
        over_2000.append(f)

print(f"Under 2000px: {len(under_2000)}")
print(f"Over 2000px: {len(over_2000)}")
EOF
```

### Phase 2: High-Risk File Check (20-30 min)
- Identify files with generic/ambiguous names
- Check these first (highest correction rate)
- Look for: `email-*`, `document-*`, `code-*`, `gorgias-or-*`, `-afternoon-`, `-evening-`

### Phase 3: Systematic Review (Remaining files)
- Review ALL remaining files one by one
- Check each against visual content
- Note: Most properly-named files (specific descriptors) are accurate
- Most generic-named files (vague descriptors) need correction

### Phase 4: Resize Over-2000px Files
- Use Python PIL to resize to 2000px max dimension
- Maintain aspect ratio with LANCZOS resampling
- Quality setting: 95 for minimal loss
- Back up originals before resizing
- Review resized files to confirm names are still accurate

### Phase 5: Verification
- Spot-check a sample of renamed files
- Verify resized images are still readable
- Confirm timestamp preservation in all names

---

## Statistics from January Field Test

- **Total files reviewed:** 98
- **Files with generic names:** ~30 (30%)
- **Files with specific names:** ~68 (70%)
- **Correction rate on generic names:** 73% (22 of 30)
- **Correction rate on specific names:** 0% (all were accurate)
- **Files needing resize:** 22 (22%)
- **Review time:** ~3 hours for 98 files with one-by-one methodology

**Key insight:** File naming quality correlates with descriptor specificity. Generic names hide misclassifications; specific names are reliable.

---

## Template: File Review Output

For each file, document:

```
FILE N: [filename]
WHAT I SEE:
- Platform/Type: [email/slack/CRM/etc]
- Subject: [main content]
- Key details: [names, amounts, specific info]
- Date visible: [if any]

CURRENT NAME: [existing filename]
STATUS: [✅ ALREADY CORRECT / ❌ NEEDS RENAMING]

PROPOSED NAME (if needed): [new filename]
REASON: [why the change was needed]

ACTION: [renamed/no change needed]
```

---

## Important Notes

- **DO NOT use bulk operations** - Never rename multiple files at once without reviewing each individually
- **DO preserve timestamps** - Always keep the original date-time in the new filename
- **DO ask for clarification** - If you cannot determine content with certainty, ask rather than guess
- **DO focus on accuracy** - A 100% accurate folder of 20 files is better than a 70% accurate folder of 100 files
- **DO document changes** - Keep a record of what was renamed and why

---

## When to Stop and Create a New Skill Task

If you reach critical token constraints mid-folder:
- Stop reviewing
- Create a summary report of:
  - Files reviewed vs total
  - Correction patterns observed
  - High-risk naming patterns remaining
  - Estimated effort for completion
- Document exact stopping point with filename
- Next session can resume from that exact file

This ensures continuity without losing context.
