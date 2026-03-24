---
name: notion-content-extraction
description: |
  Extract Notion documents to Markdown with complete fidelity and verification. This skill implements a bulletproof process to prevent fabrication, missing sections, missing links, and incomplete extraction. Use this whenever you need to extract Notion pages, databases, or playbooks to Markdown files with guaranteed completeness and accuracy. Essential when creating documentation, playbooks, knowledge bases, or any structured content that requires 100% fidelity to the source.
compatibility: Notion connector access required
---

# 🚀 Bulletproof Notion Content Extraction

This skill guides the extraction of Notion documents to Markdown format with complete accuracy and fidelity to source material.

## 🎯 Core Extraction Principles

**These principles prevent the most common extraction errors:**

1. **No Fabrication** - Extract ONLY content that exists in Notion. Never synthesize, create, or assume content.
2. **Complete Extraction** - Extract ALL sections, subsections, and content. No selective extraction.
3. **Preserve All Links** - Capture every URL, link, and reference exactly as it appears in Notion.
4. **Exact Naming** - Use section titles and names exactly as they appear in Notion. Do not rename or shorten.
5. **Pre-Delivery Verification** - Verify completeness before delivering the extraction to prevent rework.

## 📋 Extraction Workflow

### Phase 1: Pre-Extraction Preparation

**1.1 Identify the Notion Source**
- Obtain the exact Notion document URL
- Record the document title exactly as shown in Notion
- Note any parent pages or database context
- Check the last update date in Notion

**1.2 Review the Full Document Structure**
- Open the document and scroll through the entire page
- Count total sections and subsections
- Identify all tabs, toggles, and expandable sections
- List all embedded content types (images, videos, links, tables, code blocks)
- Create a checklist of every section you will extract

**1.3 Document All Content Sources**
- Identify where content comes from (Notion native, synced blocks, embedded content)
- Note any related documents that contribute content
- Understand the document's structure before beginning extraction

### Phase 2: Systematic Extraction

**2.1 Extract Section-by-Section**
- Start from the top of the document
- Extract each section completely before moving to the next
- Preserve the exact heading hierarchy (# ## ### etc.)
- Include ALL content under each section (text, lists, tables, code)
- Do not skip or consolidate sections

**2.2 Comprehensive Link Preservation**
Extract every type of link with full URLs:
- **Notion internal links** - Links to other Notion pages/databases
- **External URLs** - Web links, documents, dashboards
- **Email links** - mailto: addresses if present
- **Custom links** - In tables, lists, descriptions
- **UTM parameters** - Preserve all query parameters exactly
- **Embedded content** - Links in toggle sections, collapsed content
- **Reference links** - Links in footer, appendix, resource sections

Use a systematic approach:
```
For each section:
  1. Identify all clickable text (underlined/blue in Notion)
  2. Extract the full URL from the link
  3. Preserve surrounding context
  4. Verify the URL is complete (includes protocol, path, parameters)
```

**2.3 Handle Special Content Types**

**Tables:**
- Extract as Markdown tables with | separators
- Preserve all rows and columns
- Include table headers
- Keep alignment markers (---| :---:| etc.)

**Toggles/Expandable Sections:**
- Extract toggle names exactly
- Include all content inside toggles
- Use `<details>` tags to maintain expandable structure
- Verify content inside each toggle is complete

**Code Blocks:**
- Include language specification (```python, ```bash, etc.)
- Preserve exact formatting and indentation
- Include all code comments

**Lists:**
- Preserve list type (ordered, unordered, nested)
- Keep indentation exactly as shown
- Include all list items without skipping

**2.4 Preserve Exact Naming and Structure**
- Copy section titles exactly from Notion (don't shorten or rephrase)
- Use exact emoji/symbols as they appear
- Preserve hierarchy (don't flatten structure)
- Keep the exact ordering of sections

### Phase 3: Content Verification & Completeness Check

**3.1 Verify Against Your Pre-Extraction Checklist**
- [ ] Every section from your checklist is present
- [ ] No sections were skipped or consolidated
- [ ] All subsections under each section are included
- [ ] All content inside collapsed/toggle sections is extracted

**3.2 Link Verification**
- [ ] All visible URLs in the document have been captured
- [ ] Each URL is complete (includes protocol, full path, parameters)
- [ ] No link text was included as content (only actual URLs)
- [ ] Links in tables, lists, and toggles are all captured
- [ ] UTM parameters and query strings are preserved exactly

**3.3 Content Verification**
- [ ] No content was fabricated or synthesized
- [ ] Section names match Notion exactly
- [ ] Hierarchy and structure matches Notion
- [ ] All special formatting (bold, italic, code) preserved
- [ ] Tables, lists, and special structures are intact
- [ ] No content was condensed or summarized

**3.4 Final Verification Before Delivery**
Compare extracted document to Notion:
1. **Spot Check:** Open 3-5 random sections and verify content matches exactly
2. **Link Validation:** Click 5-10 links to confirm URLs are correct
3. **Count Verification:** Compare section counts - should match exactly
4. **Size Comparison:** File size should be proportional to source (larger documents = larger Markdown)
5. **Completeness:** Run through your pre-extraction checklist one final time

## ⚠️ Common Extraction Errors to Avoid

| Error | How to Avoid | Example |
|-------|-------------|---------|
| **Fabricated Content** | Only extract what exists in Notion. Don't create or assume. | ❌ "Key Questions to Ask During Audit" - verify this section actually exists in Notion before including |
| **Missing Sections** | Use a checklist. Extract every section without selective choices. | ❌ Skipping "Methodology" because it seems supplementary. Instead: extract it and note if supplementary |
| **Missing Links** | Systematically scan each section for all URLs. Don't assume only main text has links. | ❌ Missing Loom video links in toggle sections, missing Calendly booking links in tables |
| **Renaming Sections** | Copy exact titles from Notion. Don't shorten or clarify. | ❌ Changing "Step 1 - AI Agent Implementation Kick-off (Basic setup)" to "Step 1 - Basic Setup" |
| **Incomplete URLs** | Capture the FULL URL including query parameters and fragments. | ❌ Copying only `calendly.com/user/call` instead of full URL with UTM parameters |
| **Nested Content Loss** | Check inside all collapsed sections, toggles, and nested items. | ❌ Missing content inside `<details>` tags or expandable sections |
| **Table Content Skipped** | Extract every cell in every row of every table. | ❌ Skipping table rows because they seemed repetitive |
| **Partial List Items** | Include ALL text in list items, including sub-bullets. | ❌ Abbreviating long list items or skipping nested bullets |

## 📊 Extraction Quality Checklist

Before marking extraction as complete:

- [ ] **100% Section Coverage** - Every section from Notion is extracted
- [ ] **100% Link Preservation** - Every URL captured with full path and parameters
- [ ] **No Fabrication** - All content verified to exist in Notion source
- [ ] **Exact Naming** - Section names match Notion exactly
- [ ] **Complete Content** - No content condensed, summarized, or omitted
- [ ] **Structure Preserved** - Hierarchy, lists, tables, toggles match source
- [ ] **Verification Pass** - Spot-checked against source and confirmed accurate
- [ ] **Link Validation** - Sample of links verified to work/be complete

## 🔄 Version Control Protocol

When extraction is complete:

1. **Save with version number:** `filename_v1_LATEST.md`
2. **Document what was extracted:** Include source Notion URL in the file
3. **Create VERSION_HISTORY entry:** Track version, date, any issues found
4. **When updated:** Archive old version as `filename_v1.md`, create `filename_v2_LATEST.md`
5. **Maintain audit trail:** Keep all versions for transparency and rollback capability

## ✅ How to Know Extraction is Complete

Your extraction is **done** when:

1. ✅ You've verified every section from your pre-extraction checklist
2. ✅ You've confirmed every link in the document is captured
3. ✅ You've spot-checked 5+ sections against the Notion source and found exact matches
4. ✅ You've identified zero fabricated content
5. ✅ You can state with confidence: "This extraction has 100% fidelity to the Notion source"

## 🚨 Red Flags During Extraction

If you encounter these, **STOP and verify**:

- Content that you don't see in Notion (might be fabricated)
- Sections you skipped as "not important" (extract everything)
- Links that seem to be missing from sections that reference them
- Section names that differ from Notion (double-check exact wording)
- Content that feels "synthesized" or generalized (extract what's actually there)

---

**Remember:** When in doubt, extract more rather than less. It's better to include supplementary content and mark it as such than to miss critical information.
