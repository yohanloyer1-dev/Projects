# Gorgias Tools

Tools for automating Gorgias AI Agent action creation.

## 1. Chrome Extension - Curl Importer

Converts curl commands from API documentation into Gorgias HTTP request actions.

### Features
- Parses curl commands (method, URL, headers, body)
- Populates request name from API endpoint
- Fills in URL field
- Adds headers with correct key-value pairs
- Populates request body for POST/PUT/PATCH

### Known Issue
- HTTP method dropdown automation doesn't work reliably
- **Workaround:** Manually set the HTTP method to POST/PUT/PATCH before clicking the extension

### Installation

1. Open Chrome → `chrome://extensions/`
2. Enable "Developer mode" (toggle in top-right)
3. Click "Load unpacked"
4. Select folder: `/Users/fraserbruce/gorgias-curl-importer`

### Usage

1. In Gorgias, create a new HTTP request action
2. **Manually set HTTP method** (e.g., POST) if needed
3. Click the extension icon
4. Paste your curl command
5. Click "Import to Gorgias"
6. If any fields don't populate correctly, hard refresh the page (Cmd+Shift+R) and try again

---

## 2. Bulk Action Creator - Node.js Script

Programmatically create bulk AI Agent actions in Gorgias via their internal API.

### Quick Start (3 Steps)

**Step 1: Install**
```bash
cd /Users/fraserbruce/gorgias-curl-importer
npm install
```

**Step 2: Run Setup (Interactive)**
```bash
npm run setup
```

This will guide you through:
- Finding your store name
- Getting your auth token from Chrome DevTools

**Step 3: Create Actions**

**Option A - Use CSV (Easiest for Bulk)**

1. Open `actions-template.csv` in Excel or Google Sheets
2. Replace the example rows with your actions
3. Save as CSV
4. Run:
```bash
npm run csv your-file.csv
npm start
```

**Option B - Edit JSON Directly**

1. Edit `actions-config.json`:
```json
{
  "actions": [
    {
      "name": "Check Order Status",
      "description": "Fetches the current status of a customer's order",
      "requestName": "Get Order Status",
      "url": "https://api.example.com/orders/{order_id}",
      "method": "GET",
      "headers": {
        "authorization": "Bearer YOUR_API_KEY"
      },
      "requiresConfirmation": false
    }
  ]
}
```

2. Run:
```bash
npm start
```

### Action Configuration Options

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | The action name shown in Gorgias |
| `description` | Yes | Instructions for the AI on when to use this action |
| `requestName` | Yes | Internal name for the HTTP request step |
| `url` | Yes | API endpoint to call |
| `method` | No | HTTP method (GET, POST, PUT, etc.). Default: GET |
| `headers` | No | HTTP headers object. Default: {} |
| `variables` | No | Array of variables for the request. Default: [] |
| `requiresConfirmation` | No | Whether AI needs approval before executing. Default: false |

### How It Works

1. **Generates ULIDs** for all required IDs (config, steps, transitions)
2. **Constructs payload** matching Gorgias's internal structure
3. **Makes PUT requests** to create each action
4. **Reports results** with success/failure summary

### Example Output

```
Starting bulk action creation...

Creating action: Check Order Status
URL: https://api.gorgias.work/stores/shopify/your-store/configurations/01KF0QV605...
✓ Success! Action created with ID: 01KF0QV605GXK9J450QAJFPWRR

Creating action: Update Customer Address
URL: https://api.gorgias.work/stores/shopify/your-store/configurations/01KF0QV70X...
✓ Success! Action created with ID: 01KF0QV70XGVK3J562RBKGQXSS

==================================================
SUMMARY
==================================================
Total: 2
Successful: 2
Failed: 0
```

### Notes

- The script uses ULIDs for ID generation (same format as Gorgias)
- Includes 500ms delay between requests to avoid rate limiting
- All actions are created as LLM-triggered conversation actions
- Actions default to the HTTP request → Success/Error flow pattern

### CSV Format

Download [actions-template.csv](actions-template.csv) to see the format. Columns:

| Column | Required | Example |
|--------|----------|---------|
| name | Yes | Check Order Status |
| description | Yes | Fetches order status for the customer |
| requestName | No | Get Order (defaults to name) |
| url | Yes | https://api.example.com/orders/{order_id} |
| method | No | GET (default), POST, PUT, etc. |
| headers | No | {"authorization":"Bearer token"} |
| requiresConfirmation | No | false (default) or true |

**Tips:**
- Use Google Sheets or Excel to edit the CSV easily
- Copy-paste multiple rows for bulk creation
- Headers must be valid JSON (use double quotes inside: `"{""key"":""value""}"`)

### Troubleshooting

**"No configuration found"**: Run `npm run setup` first

**401 Unauthorized**: Your auth token expired. Run `npm run setup` again

**404 Not Found**: Check your store name in setup

**400 Bad Request**: Check your action configuration matches the format above

---

## Files

### Chrome Extension
- `manifest.json` - Extension config
- `popup.html` / `popup.js` - Extension UI and curl parser
- `content.js` - Gorgias form automation
- `icon*.png` - Extension icons

### Bulk Creator
- `setup.js` - Interactive setup wizard
- `create-actions.js` - Main script for bulk action creation
- `csv-to-actions.js` - CSV to JSON converter
- `actions-config.json` - Action definitions (JSON format)
- `actions-template.csv` - CSV template for easy bulk editing
- `config.js` - Generated by setup (don't edit manually)
- `package.json` - Node dependencies
