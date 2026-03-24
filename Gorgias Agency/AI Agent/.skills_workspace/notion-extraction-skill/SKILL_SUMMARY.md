# 🎯 Notion Content Extraction Skill - Summary

## Skill Overview

**Name:** `notion-content-extraction`

**Purpose:** Extract Notion documents to Markdown with 100% fidelity and complete accuracy, preventing fabrication, missing sections, missing links, and incomplete extraction.

**When to Use:** Whenever extracting Notion pages, databases, or playbooks to structured documentation that requires guaranteed completeness and accuracy.

## What This Skill Prevents

Based on extraction work from Feb 24, 2026, this skill prevents the following errors:

### 1. ❌ Fabricated Content
**Problem:** Creating content that doesn't exist in Notion (e.g., "Key Questions to Ask During Audit" section)

**Solution:**
- Only extract content that actually exists in Notion
- Verify every section exists before including it
- Use a pre-extraction checklist comparing source to extracted content

### 2. ❌ Missing Sections
**Problem:** Selectively extracting only sections deemed "important" (missing Methodology, Stand-ups, Calendly, Vitally, Templates, Macros, Admin, Auditing Accounts details, Additional Resources)

**Solution:**
- Extract ALL sections without judgment
- Create a complete checklist before extracting
- Mark supplementary sections with clear notation if needed
- Never skip sections - extract everything

### 3. ❌ Missing Links
**Problem:** Not systematically capturing all URLs (missing 25+ links: Calendly, ChatGPT tools, Periscope, HEX, Loom, Google Drive)

**Solution:**
- Systematically scan each section for links
- Extract every link type: URLs, email links, UTM parameters
- Check inside toggles, tables, lists, and collapsed sections
- Verify each URL is complete with full path and parameters

### 4. ❌ Renaming/Shortening Sections
**Problem:** Changing exact section names from source ("Step 1 - AI Agent Implementation Kick-off (Basic setup)" → "Step 1 - Basic Setup")

**Solution:**
- Copy section titles exactly from Notion
- Preserve emoji and symbols exactly
- Don't abbreviate or clarify titles
- Maintain exact hierarchy

### 5. ❌ Incomplete Extraction
**Problem:** Missing nested content (inside toggles), partial lists, abbreviated content

**Solution:**
- Extract content inside all collapsed/toggle sections
- Include all content in tables, lists, nested items
- Complete extraction before marking done
- Verify nothing was condensed or summarized

## Skill Structure

The skill provides:

### Core Components

1. **5 Extraction Principles** - Foundational rules to prevent errors
2. **3-Phase Workflow**
   - Phase 1: Pre-Extraction Preparation (checklist, structure review)
   - Phase 2: Systematic Extraction (section-by-section, link preservation)
   - Phase 3: Verification & Completeness Check (spot-checking, link validation)

3. **Comprehensive Error Reference** - 8 common errors with avoidance strategies
4. **Quality Checklist** - 8-point verification before delivery
5. **Red Flags List** - Signals to stop and verify

### Key Workflows

**Pre-Extraction Preparation:**
- Identify Notion source (URL, title, context)
- Review full document structure
- Create section checklist before extracting

**Systematic Extraction:**
- Section-by-section with no skipping
- Comprehensive link preservation (all URL types)
- Special handling for tables, toggles, code, lists
- Exact naming and structure preservation

**Verification:**
- Checklist verification (all sections present)
- Link verification (all URLs captured completely)
- Content verification (no fabrication)
- Final spot-checking against source

## How to Use This Skill

### When Extracting a Notion Document:

1. **Read the Pre-Extraction Preparation section** (3.1-3.3)
2. **Create a checklist** of all sections you see in Notion
3. **Work through Systematic Extraction** (section by section)
4. **Perform verification** before delivery
5. **Mark as complete only when** all verification items pass

### Key Commands to Follow:

- "Extract section-by-section" - Don't consolidate or skip
- "Comprehensive link preservation" - Get every link type
- "Preserve exact naming" - Copy titles exactly
- "Pre-delivery verification" - Verify before finishing
- "Spot-check against source" - Verify accuracy with examples

## Test Scenarios

Three evaluation scenarios test the skill:

### Test 1: Extract Playbook with Links
- Extracts a complex playbook document
- Verifies all sections, subsections, links (including Calendly with UTM, ChatGPT tools, dashboards)
- Expected output: Complete extraction with 25+ links, all sections, verification passed

### Test 2: Verify Against Audit Checklist
- Uses pre-extraction checklist method
- Tests systematic section-by-section extraction
- Verifies no sections were missed
- Expected output: Checklist, extraction, verification showing 100% completeness

### Test 3: Identify Extraction Errors
- Tests error detection capabilities
- Identifies fabricated content, missing sections, missing links
- Shows how verification process would prevent each error
- Expected output: Complete error analysis with prevention strategies

## Metrics for Success

An extraction using this skill is **successful** when:

✅ **Completeness:** 100% of sections from source are extracted
✅ **Link Preservation:** 100% of URLs captured with full paths/parameters
✅ **No Fabrication:** All content verified to exist in Notion
✅ **Exact Naming:** Section names match Notion exactly
✅ **Verification:** Spot-checked and confirmed accurate against source
✅ **Quality:** Passes 8-point quality checklist

## Version Control Integration

The skill includes version control guidance:
- Save as `filename_v1_LATEST.md`
- Include Notion URL in document
- Archive previous versions as `filename_v#.md`
- Maintain audit trail for transparency

## Token Efficiency

The skill is designed to be efficient:
- Focuses on prevention of rework (complete extraction first time)
- Emphasis on pre-extraction checklist reduces back-and-forth
- Clear verification steps prevent incomplete work
- Saves tokens by avoiding partial extractions that need rework

## How This Skill Was Developed

This skill was created based on actual extraction work on Feb 24, 2026:

- **Phase 1:** Extracted Notion documents with initial incompleteness
- **Phase 2:** Discovered critical gaps through verification
  - Q3: Fabricated content identified
  - Q4: Missing sections (80% of Auditing Accounts)
  - Q5: 9 ChatGPT tools completely missing
- **Phase 3:** Complete re-extraction with 100% fidelity
- **Phase 4:** Merged Standard Helpdesk content with proper attribution
- **Learnings:** Documented all lessons into bulletproof process

The skill encodes these hard-learned lessons to prevent future extraction errors.

## References

See `SKILL.md` for the complete extraction workflow and detailed procedures.

Test cases defined in `evals.json` for evaluating skill effectiveness.

---

**Ready to use:** This skill is complete and ready for use on any Notion extraction task.
