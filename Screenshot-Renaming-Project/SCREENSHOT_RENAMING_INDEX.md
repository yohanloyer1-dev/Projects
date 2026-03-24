# Screenshot Renaming Project - Master Index

## 📋 Documentation Files

All documentation is stored in `/sessions/adoring-quirky-goodall/`

### Core Methodology Documents

1. **`SCREENSHOT_RENAMING_SKILL.md`** (Comprehensive)
   - Full methodology guide
   - Detailed platform identification
   - Common categorization issues
   - Workflow phases
   - Handling edge cases
   - **USE THIS:** When starting work on a new folder or need complete reference

2. **`SCREENSHOT_RENAMING_QUICK_REFERENCE.md`** (Quick Lookup)
   - One-page summary
   - Platform identification checklist
   - Red flag filenames
   - Good name format examples
   - Common mistakes
   - Decision tree
   - **USE THIS:** During active file review as quick lookup guide

3. **`JANUARY_COMPLETION_REPORT.md`** (Results & Data)
   - Complete work summary
   - All 23 corrected files listed
   - Key findings and statistics
   - Naming patterns analysis
   - Files resized (22 total)
   - Lessons learned
   - **USE THIS:** To understand what was done and replicate approach

### Project Status

This project is structured in **phases by month**:

#### ✅ JANUARY 2025 - COMPLETE
- **Status:** Fully reviewed and optimized
- **Files:** 98 total
- **Corrections:** 23 files renamed
- **Resized:** 22 files (over 2000px)
- **Location:** `/sessions/adoring-quirky-goodall/mnt/01-Jan/`
- **Backups:** `/sessions/adoring-quirky-goodall/mnt/01-Jan-originals/`

#### ⏳ FEBRUARY 2025 - PENDING
- **Estimated files:** ~90-100
- **Estimated corrections:** ~20-25
- **Estimated time:** 3-4 hours for complete review
- **Estimated tokens:** 130-150k for full one-by-one review

#### ⏳ MARCH 2025 - PENDING
- Similar scope to February

#### ⏳ APRIL-DECEMBER 2025 - PENDING
- 9 more months to process

---

## 🎯 Quick Start for New Session

### If Starting a New Month:

1. **Prepare**
   - Read `SCREENSHOT_RENAMING_QUICK_REFERENCE.md` (5 min)
   - Request folder access for the target month

2. **Assess**
   - Count files and identify dimension distribution
   - Identify high-risk filenames (generic names)

3. **Review**
   - Start with high-risk files (highest correction payoff)
   - Follow one-by-one visual analysis method
   - Document each correction

4. **Optimize**
   - Resize files over 2000px
   - Verify all names are still accurate

5. **Document**
   - Create completion report following January template

### Token Budget Management

**Per file cost:** ~1,400 tokens (one-by-one analysis)
**Per folder cost:** ~130-150k tokens (full folder, 98 files)
**Remaining budget:** Monitor and stop before critical

**Strategy for limited tokens:**
- Complete high-risk files first (highest value)
- Stop when tokens get low
- Document stopping point
- Resume exactly where you left off next session

---

## 📊 Key Statistics

### January Results
| Metric | Value |
|--------|-------|
| Total files | 98 |
| Files corrected | 23 (23%) |
| Files verified accurate | 75 (77%) |
| Generic name error rate | 73% |
| Specific name error rate | 0% |
| Files requiring resize | 22 (22%) |
| Platform corrections (Discord/Slack/WhatsApp) | 2 |

### Projected for All Months
| Month | Est. Files | Est. Corrections | Est. Tokens |
|-------|-----------|-----------------|-------------|
| January | 98 | 23 | 140k |
| February | ~95 | ~22 | 135k |
| March | ~95 | ~22 | 135k |
| April-December | ~1,050 | ~250 | 1,500k |
| **TOTAL** | **~1,400** | **~330** | **2,000k** |

---

## 🔴 Red Flag Filenames (High Error Risk)

**These patterns indicate misclassification 70%+ of the time:**

- `email-afternoon-communication-*`
- `email-evening-communication-*`
- `gorgias-or-support-interface-*`
- `document-or-webpage-content-*`
- `code-or-error-page-*`
- Any filename with `-or-` in the middle

**Priority:** Check these files first in any folder (highest correction rate)

---

## ✅ Established Naming Standard

### Format Structure
```
[PLATFORM]-[SUBJECT]-[KEY-DETAILS]-[DATE-TIME].png
```

### Platform Prefixes
- `slack-` or `slack-conversation-` or `slack-message-`
- `email-`
- `WhatsApp-`
- `Discord-`
- `google-calendar-`
- `CRM-` or `Salesforce-`
- `website-`
- `system-error-`
- `analytics-`
- `spreadsheet-`
- And more as needed

### Examples of Good Names
✅ `slack-conversation-George-Rich-Panel-Gorgias-nine-pref-pilot-Sasha-Nikoli-2025-01-28-10.00.04.png`
✅ `email-Antoine-Roffler-meeting-Cindy-Marie-order-value-2025-01-17-08.38.52.png`
✅ `google-calendar-meeting-Maud-Mouaad-Arnaud-Gorgias-customer-service-2025-01-15-15.45.41.png`
✅ `CRM-direct-intro-referral-form-Yohan-Loyer-Shopify-partner-2025-01-24-17.45.19.png`
✅ `WhatsApp-conversation-French-coffee-alternatives-adaptogens-2025-01-09-21.56.49.png`

### Examples of Bad Names (DO NOT USE)
❌ `email-afternoon-communication-2-2025-01-15-14.12.30.png`
❌ `document-or-webpage-content-morning-2-2025-01-27-11.03.13.png`
❌ `gorgias-or-support-interface-afternoon-5-2025-01-04-20.41.11.png`

---

## 🛠️ Tools & Scripts

### Python Script for Dimension Analysis
```python
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
        over_2000.append((f, width, height))

print(f"Under 2000px: {len(under_2000)}")
print(f"Over 2000px: {len(over_2000)}")
```

### Python Script for Batch Resizing
```python
from PIL import Image
import os
import shutil

folder = "/path/to/folder"
backup_folder = "/path/to/backups"
os.makedirs(backup_folder, exist_ok=True)

files = [f for f in os.listdir(folder) if f.endswith('.png')]

for f in sorted(files):
    img_path = os.path.join(folder, f)
    img = Image.open(img_path)
    width, height = img.size
    max_dim = max(width, height)

    if max_dim > 2000:
        # Backup
        shutil.copy2(img_path, os.path.join(backup_folder, f))

        # Calculate new dimensions
        if width > height:
            new_width = 2000
            new_height = int((2000 / width) * height)
        else:
            new_height = 2000
            new_width = int((2000 / height) * width)

        # Resize and save
        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        img_resized.save(img_path, quality=95)

        print(f"✅ {f}: {width}x{height} → {new_width}x{new_height}")
```

---

## 📁 File Organization

```
/sessions/adoring-quirky-goodall/
├── SCREENSHOT_RENAMING_INDEX.md           (this file)
├── SCREENSHOT_RENAMING_SKILL.md           (full methodology)
├── SCREENSHOT_RENAMING_QUICK_REFERENCE.md (quick lookup)
├── JANUARY_COMPLETION_REPORT.md           (January results)
└── /mnt/01-Jan/                           (January screenshots)
    ├── [98 PNG files - reviewed & renamed]
    └── /01-Jan-originals/                 (backups of resized files)
        └── [22 PNG files - original size]
```

---

## ⚠️ Important Reminders

### DO ✅
- ✅ Review files ONE BY ONE
- ✅ Look at actual content, not filename
- ✅ Ask for clarification when unsure
- ✅ Preserve timestamps in new names
- ✅ Use specific descriptors (names, amounts, details)
- ✅ Check high-risk filenames first
- ✅ Back up files before resizing
- ✅ Stop before tokens run critical

### DON'T ❌
- ❌ Batch rename without individual review
- ❌ Assume filename is correct
- ❌ Use generic descriptors
- ❌ Lose the date-time timestamp
- ❌ Guess about platform/content
- ❌ Skip the backup step
- ❌ Continue into token danger zone

---

## 📞 Contact Points

When starting work on a new month:
1. Reference this index
2. Read quick reference guide
3. Read full skill document
4. Request folder access
5. Follow assessed workflow
6. Document changes using January report template

---

## 📈 Progress Tracking

```
✅ January:       Complete (98/98 files, 23 corrected, 22 resized)
⏳ February:      Ready to start (~95 files expected)
⏳ March-Dec:     8 months remaining
```

**Total Project Scope:**
- ~1,400 files across 12 months
- Estimated 330 files needing correction (23%)
- Estimated 2,000k tokens total for complete project
- Estimated 40+ hours for complete one-by-one review

---

**Last Updated:** February 22, 2025
**Status:** January complete, Ready for February
**Methodology:** Proven and documented
