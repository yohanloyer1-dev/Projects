# Quick Start Guide - For Non-Technical Users

## What This Does

Creates multiple Gorgias AI Agent actions automatically instead of clicking through the UI for each one.

## Prerequisites

- Node.js installed (download from nodejs.org if you don't have it)
- Access to your Gorgias account
- Chrome browser

## Step-by-Step Instructions

### 1. Install Dependencies

Open Terminal and run:

```bash
cd /Users/fraserbruce/gorgias-curl-importer
npm install
```

Wait for it to finish (should take 10-30 seconds).

### 2. Run Setup

```bash
npm run setup
```

You'll be asked two questions:

**Question 1: Store Name**
- Open Gorgias in Chrome
- Look at the URL: `https://YOUR-STORE-NAME.gorgias.com/`
- Type in just the store name part
- Example: If URL is `https://fraserdemo1.gorgias.com/`, type: `fraserdemo1`

**Question 2: Auth Token**
- Keep Gorgias open in Chrome
- Press F12 to open DevTools
- Click "Network" tab at the top
- Click anywhere in Gorgias (or refresh the page)
- Look for a request to "api.gorgias.work" in the list
- Click on it
- Scroll down to "Request Headers"
- Find "authorization:" and copy the ENTIRE value (starts with "Bearer eyJ...")
- Paste it into the terminal

The setup will save your config. You're done with setup!

### 3. Prepare Your Actions

**Easy Way - Use CSV (Recommended for Bulk)**

1. Open `actions-template.csv` in Excel or Google Sheets
2. You'll see example actions - delete them
3. Add your actions, one per row:
   - **name**: What to call the action (e.g., "Check Order Status")
   - **description**: Tell the AI when to use this (e.g., "Use this to get the current status of a customer's order")
   - **url**: The API endpoint to call
   - **method**: GET, POST, PUT, etc.
   - **headers**: API authentication (use format: `{"authorization":"Bearer YOUR_KEY"}`)
   - **requiresConfirmation**: true or false
4. Save the file as CSV

**Alternative - Edit JSON**

Edit `actions-config.json` if you prefer JSON format.

### 4. Create the Actions

**If using CSV:**
```bash
npm run csv your-file.csv
npm start
```

**If using JSON:**
```bash
npm start
```

You'll see output like:
```
Creating action: Check Order Status
✓ Success! Action created

Creating action: Update Address
✓ Success! Action created

SUMMARY
Total: 2
Successful: 2
Failed: 0
```

Done! Go check your Gorgias AI Agent settings to see the new actions.

## Common Issues

**"No configuration found"**
- You skipped step 2. Run: `npm run setup`

**"401 Unauthorized"**
- Your auth token expired (they expire after a while)
- Run setup again: `npm run setup`
- Get a fresh token from Chrome DevTools

**"Cannot find module"**
- You skipped step 1. Run: `npm install`

**Actions not showing in Gorgias**
- Refresh your Gorgias page
- Check the terminal output for errors
- Make sure the script said "Success!" for each action

## Tips

- **Bulk creation**: Add 50+ actions to the CSV and run once
- **Update actions**: Edit the CSV and run again (creates new versions)
- **Test first**: Create 1-2 test actions first to make sure everything works
- **Token expires**: If you get 401 errors later, just run `npm run setup` again

## Need Help?

1. Check the terminal output for specific error messages
2. Make sure your CSV format matches the template exactly
3. Verify your auth token is fresh (run setup again if unsure)
