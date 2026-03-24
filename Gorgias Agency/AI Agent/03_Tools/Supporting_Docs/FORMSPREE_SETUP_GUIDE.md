# Formspree Setup Guide

## Quick Overview
Formspree is a free service (up to 50 submissions/month) that captures form data and emails it to you. The discovery form is pre-configured to use Formspree, but you need to create an account and get your unique Form ID.

---

## Step 1: Create Your Formspree Account

1. Go to [formspree.io](https://formspree.io)
2. Click **"Sign up"** (top right)
3. Enter your email and create a password
4. Verify your email address (check your inbox)
5. You're now logged into Formspree dashboard

---

## Step 2: Create a New Form in Formspree

1. In the Formspree dashboard, click **"New Form"** (or the **+** button)
2. Name your form: **"AI Agent Discovery Form"** (or any name you prefer)
3. Set redirect URL (optional): Where customers go after submitting
   - Suggestion: `https://yourwebsite.com/thank-you` or leave blank
4. Click **"Create"**

---

## Step 3: Get Your Form ID

After creating the form, Formspree will show you a form ID that looks like:
```
xqakwojq  (this is just an example)
```

**This is your FORMSPREE_ID.** You'll need this in the next step.

---

## Step 4: Update the Discovery Form

Open `discovery_form_v2_professional.html` in a text editor:

1. Find this line (near the top of the `<script>` section):
   ```javascript
   const FORMSPREE_ID = 'xqakwojq';
   ```

2. Replace `'xqakwojq'` with your actual Formspree ID:
   ```javascript
   const FORMSPREE_ID = 'YOUR_ACTUAL_ID_HERE';
   ```

3. Save the file

**That's it!** Your form is now connected to Formspree.

---

## Step 5: Test It

1. Open `discovery_form_v2_professional.html` in your browser
2. Click the **"📝 Test with Demo Data"** button to pre-fill the form
3. Click **"Submit"** button
4. You should see a "Thank you!" message

**Check your email:** You should receive an email from Formspree with the submitted data (usually within 1-2 minutes).

---

## How Formspree Works

### Form Submissions
- When a customer fills out the discovery form and clicks "Submit", the data is sent to Formspree
- Formspree emails the data to you in a readable format
- You can also view submissions in the Formspree dashboard

### Support/Error Reports
- The floating **💬** button also sends to the same Formspree endpoint
- Error reports arrive with subject line: **"[ERROR REPORT] Discovery Form Issue"**
- This helps you see what problems customers are experiencing

### Email Format Example
```
From: form@formspree.io
Subject: New submission from AI Agent Discovery Form

Your Information:
- Business Name: Demo Jewelry Store
- Contact Name: Jane Smith
- Email: jane@demojewelry.com
- Business Model: ecommerce

Current Setup:
- Gorgias Duration: 1-2 years
- Monthly Ticket Volume: 3,000-5,000
...
```

---

## Formspree Pricing & Limits

| Plan | Cost | Submissions/Month | Features |
|------|------|-------------------|----------|
| **Free** | $0 | 50 | Basic form submissions, email notifications |
| **Gold** | $25/month | Unlimited | Advanced features, file uploads, analytics |
| **Platinum** | $99/month | Unlimited | Team access, custom domains, webhook support |

**For your use case:** The Free plan is perfect. You'll receive 50 customer submissions per month via email.

---

## Troubleshooting

### I submitted the form but didn't receive an email
- [ ] Check your spam/junk folder (Formspree emails might be filtered)
- [ ] Verify your FORMSPREE_ID is correct in the HTML file
- [ ] Check Formspree dashboard to see if submission was captured
- [ ] Wait 2-3 minutes (emails can take a moment)

### The form shows an error when I submit
- [ ] Make sure you filled in the required fields (marked with *)
- [ ] Check browser console for errors (F12 → Console tab)
- [ ] Verify your internet connection
- [ ] Try a different browser

### I see "Can't submit" or Formspree errors
- [ ] Your FORMSPREE_ID might be incorrect
- [ ] Log into Formspree and verify your form is active
- [ ] Check that your form is set to "Live" status (not draft)

### I want to see past submissions
- Log into [formspree.io](https://formspree.io) dashboard
- Click on your "AI Agent Discovery Form"
- Go to "Submissions" tab to see all received data
- You can download as CSV for analysis

---

## Advanced Options

### Change Where Emails Go To
1. Log into Formspree dashboard
2. Click on your form
3. Go to **"Settings"**
4. Under **"Email"**, you can add multiple email addresses
5. All submissions will go to all addresses

### Customize Reply Email
1. In form settings, you can customize the "From" address
2. This helps customers know the email is from you

### Webhook Integration (Gold/Platinum only)
- Formspree can send data to your own webhook endpoint
- Useful if you want to automate further processing
- Requires Gold or Platinum plan

---

## Next Steps

1. ✅ Create Formspree account
2. ✅ Create new form in Formspree
3. ✅ Get your Form ID
4. ✅ Update discovery_form_v2_professional.html with your ID
5. ✅ Test the form using demo data button
6. ✅ Verify email receipt
7. 📌 **Ready to share!** You can now send the form link to customers

---

## Sharing Your Form

Once Formspree is configured, you can share the discovery form link:

**Option 1: Direct File Link**
- Email customers: "Please fill out this discovery form" + link to your local file
- Only works if file is accessible via URL or shared directly

**Option 2: Host the Form** (Recommended)
- Upload `discovery_form_v2_professional.html` to your website
- Share the web URL instead of local file path
- Customers can access it anytime

**Option 3: Embed in Email**
- Attach the HTML file to email
- Most email clients will render it
- Some security restrictions apply

---

## Support Issues?

If customers experience problems with the form, they can:
1. Click the **💬** button in the bottom-right corner
2. Describe the issue
3. Click "Send Report"

You'll receive an error report email that looks like:
```
Subject: [ERROR REPORT] Discovery Form Issue

Customer Message:
"The form isn't loading correctly in Safari"

Their Form Data Context:
- Email: customer@example.com
- Business Name: (not yet filled)
...
```

This helps you debug what went wrong and improve the form.

---

**Questions?** Check Formspree documentation at [formspree.io/docs](https://formspree.io/docs) or email their support team.
