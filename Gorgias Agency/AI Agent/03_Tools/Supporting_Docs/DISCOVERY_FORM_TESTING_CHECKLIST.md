# Discovery Form Testing Checklist

## Before Sharing with Customers

Use this checklist to verify your discovery form is fully functional.

---

## Phase 1: Setup Verification

- [ ] Formspree account created at [formspree.io](https://formspree.io)
- [ ] Form created in Formspree dashboard
- [ ] Form ID retrieved (looks like: `xqakwojq`)
- [ ] `discovery_form_v2_professional.html` updated with correct FORMSPREE_ID
- [ ] File saved successfully

---

## Phase 2: File & Browser Check

- [ ] `discovery_form_v2_professional.html` opens in browser
- [ ] Page loads without errors (no blank page)
- [ ] All form sections are visible (1-7)
- [ ] Sidebar progress indicator shows on left side
- [ ] Demo data button visible ("📝 Test with Demo Data")
- [ ] Support button visible (red 💬 in bottom-right corner)

---

## Phase 3: Demo Data Test

- [ ] Click "📝 Test with Demo Data" button
- [ ] Form fields auto-populate with sample data:
  - Business Name: "Demo Jewelry Store"
  - Contact Name: "Jane Smith"
  - Email: "jane@demojewelry.com"
  - Other fields filled with realistic values
- [ ] Progress sidebar updates as you check the form
- [ ] No error messages appear

---

## Phase 4: PDF Download Test

- [ ] After demo data populates, scroll to bottom
- [ ] Click "⬇️ Download as PDF" button
- [ ] PDF file downloads to your computer (named something like `Discovery_Form_[date].pdf`)
- [ ] Open the PDF and verify:
  - [ ] All sections are included
  - [ ] Customer data is visible
  - [ ] Formatting looks clean and professional
  - [ ] No missing information

---

## Phase 5: Form Submission Test

- [ ] With demo data still filled, click "Submit" button
- [ ] Success message appears: "Thank you! Your discovery form has been submitted."
- [ ] Message displays for 3-5 seconds then clears
- [ ] Form resets (all fields cleared)

---

## Phase 6: Email Verification

- [ ] **Wait 1-2 minutes** after submitting
- [ ] Check your email inbox
- [ ] Look for email from: `form@formspree.io`
- [ ] Subject should mention: "submission" and "AI Agent Discovery Form"
- [ ] Email body contains:
  - [ ] All customer information (Business Name, Contact Name, Email, etc.)
  - [ ] All 7 sections of data
  - [ ] Readable, well-formatted text
- [ ] **If no email received:**
  - [ ] Check spam/junk folder
  - [ ] Log into Formspree dashboard and check "Submissions" tab
  - [ ] Verify FORMSPREE_ID is correct in HTML file
  - [ ] Try submitting again

---

## Phase 7: Required Field Validation

- [ ] Click "Submit" with **no data filled in**
- [ ] Error message appears: "Please fill in required fields (marked with *)"
- [ ] Form does NOT submit (stays on same page)
- [ ] Fill in only "Business Name" field
- [ ] Click "Submit"
- [ ] Error message still appears (all 3 required fields needed)
- [ ] Fill in "Contact Name" (now 2/3 required fields)
- [ ] Click "Submit"
- [ ] Error message still appears
- [ ] Fill in "Contact Email" (now 3/3 required fields)
- [ ] Click "Submit"
- [ ] Form submits successfully

**Required Fields (marked with *):**
- Business Name
- Contact Name
- Contact Email

---

## Phase 8: Support/Error Reporting Test

- [ ] Click red **💬** button in bottom-right corner
- [ ] Support modal appears with:
  - [ ] Text field for customer message
  - [ ] "Send Report" button
- [ ] Type a test message: "Test error report - form working well"
- [ ] Click "Send Report"
- [ ] Modal closes and you see success message
- [ ] **Check email:** You should receive error report with subject `[ERROR REPORT] Discovery Form Issue`
- [ ] Error report email includes:
  - [ ] Your test message
  - [ ] Any form data that was filled in
  - [ ] Customer context

---

## Phase 9: Field Interactions

Test that form responds properly to user input:

- [ ] Click on each text field - cursor appears
- [ ] Type text - text displays as typed
- [ ] Radio buttons (Business Model) - can select each option
- [ ] Checkboxes - can toggle on/off
- [ ] Textarea fields (Additional Info) - can type multiple lines
- [ ] All dropdowns expand when clicked
- [ ] Progress sidebar updates when you navigate to different sections

---

## Phase 10: Navigation & Flow

- [ ] Progress sidebar clickable - click on different steps
- [ ] Form jumps to clicked section
- [ ] Sidebar highlights current section
- [ ] Back button functionality works
- [ ] Can skip sections and come back to them
- [ ] Sidebar shows number of completed steps

---

## Phase 11: Visual Check

- [ ] Professional two-column layout displays correctly
- [ ] Sidebar progress indicator is clear
- [ ] Form sections are easy to read
- [ ] No overlapping text or formatting issues
- [ ] Colors are consistent (blues and grays)
- [ ] Buttons are clearly clickable
- [ ] Required field indicators (*) are visible and red
- [ ] Form looks professional (not "AI-generated")

---

## Phase 12: Mobile/Responsive Check

- [ ] Open form on mobile device or resize browser window
- [ ] Form layout adjusts for smaller screens
- [ ] All buttons remain clickable
- [ ] Text is readable (not too small)
- [ ] Sidebar and form content stack appropriately
- [ ] No horizontal scrolling required

---

## Phase 13: Edge Cases

- [ ] Submit form with very long text in textarea field
- [ ] Submit form with special characters (émojis, accents, etc.)
- [ ] Submit form with numbers in text fields
- [ ] Submit form with spaces/whitespace in required fields
- [ ] Verify all variations arrive correctly in your email

---

## Phase 14: Production Readiness

- [ ] All tests above pass ✓
- [ ] No console errors (check browser F12 → Console tab)
- [ ] Formspree account is active and ready
- [ ] Form can be shared with customers
- [ ] You know how to handle incoming submissions
- [ ] Error reporting system is working

---

## Ready to Share!

Once you complete all phases above, your form is ready to share with customers.

### Sharing Options

**Option 1: Email Link**
```
"I'd like to learn more about your support automation needs.
Please fill out this quick discovery form:

[link to discovery_form_v2_professional.html or hosted version]

It takes about 5-10 minutes and helps me understand your business.
I'll review and send recommendations within 2 business days."
```

**Option 2: Website Embed**
Upload the form to your website and share the URL for easy access.

**Option 3: Scheduled Discovery Call**
Send form link before the call so you have initial information.

---

## Post-Submission Handling

When you receive submissions:

1. **Review the data** in your email (or Formspree dashboard)
2. **Note key metrics:**
   - Current automation rate
   - Monthly ticket volume
   - Existing outsourcing costs
3. **Schedule analysis** - plan your audit timeline
4. **Reference client profile** - use their data for audit planning

---

## Troubleshooting Quick Links

| Issue | Solution |
|-------|----------|
| Form doesn't load | Verify file path, try different browser |
| Submit button doesn't work | Check FORMSPREE_ID, try clearing browser cache |
| No email received | Check spam folder, verify FORMSPREE_ID, wait 2+ min |
| PDF download fails | Try different browser, check browser download settings |
| Support button doesn't work | Verify FORMSPREE_ID, check internet connection |
| Form looks broken on mobile | Test on different devices, check responsive design |

---

**Remember:** The discovery form is your first touchpoint with potential clients. A smooth, professional experience sets the tone for your engagement.

Good luck! 🚀
