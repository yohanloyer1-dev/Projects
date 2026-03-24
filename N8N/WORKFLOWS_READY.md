# ✅ n8n Workflows Ready to Import

All workflows have been updated to use **Abacus.AI RouteLLM API** - no deployment ID needed!

## 🎯 What's Configured

### API Settings (Already Done)
- ✅ Endpoint: `https://routellm.abacus.ai/v1/chat/completions`
- ✅ API Key: `s2_8ecdc6832cb94ac599ea14ab55b0a928`
- ✅ Authorization: Bearer token format
- ✅ Response parsing: OpenAI-compatible format (`choices[0].message.content`)

## 📦 Three Workflows Ready

### 1. **reddit-abacus-monitor.json** ⭐ EASIEST TO START
**What it does:**
- Searches Reddit r/technology for "AI" posts (limit: 5)
- Analyzes sentiment with Grok
- Saves to Google Sheets

**Model used:** `grok-beta`

**Nodes:**
1. Manual Trigger
2. Search Reddit Posts
3. Analyze with Grok (Abacus AI)
4. Format Results
5. Save to Google Sheets

**To customize:**
- Line 15: Change `"subreddit": "technology"` to any subreddit
- Line 16: Change `"keyword": "AI"` to search different topics
- Line 17: Change `"limit": 5` to get more/fewer posts
- Line 45: Change `"model": "grok-beta"` to use different model

---

### 2. **reddit-ideas-miner-abacus.json** 🚀 ADVANCED
**What it does:**
- Searches Reddit r/startups for "AI" posts (limit: 10)
- Uses Grok to analyze for startup ideas
- Extracts: problem, solution, market size, confidence score
- Filters for high-confidence ideas (score > 6)
- Saves good ideas to Google Sheets

**Model used:** `grok-beta`

**Nodes:**
1. Start Workflow
2. Search Reddit for AI Posts
3. Analyze with Grok (Abacus AI)
4. Parse & Structure Data (JavaScript)
5. Filter High-Confidence Ideas
6. Save Good Ideas to Sheets

**To customize:**
- Line 15: Change `"subreddit": "startups"` to different subreddit
- Line 16: Change `"keyword": "AI"` to search different topics
- Line 18: Change `"limit": 10` for more/fewer posts
- Line 44: Change `"model": "grok-beta"` to use different model
- Line 68: Change `"value2": 6` to adjust confidence threshold

---

### 3. **youtube-summarizer-abacus.json** 📺 YOUTUBE ANALYSIS
**What it does:**
- Web form to submit YouTube URLs
- Extracts video transcript
- Analyzes with Gemini 2.0
- Provides summary, takeaways, and content ideas
- Saves to Google Sheets
- Returns JSON response

**Model used:** `gemini-2.0-flash-exp`

**Nodes:**
1. Submit YouTube URL (Form Trigger)
2. Get YouTube Page
3. Extract Video ID
4. Get Transcript
5. Parse Transcript
6. Analyze with Gemini (Abacus AI)
7. Format Final Output
8. Save to Google Sheets
9. Return Results

**To customize:**
- Line 84: Change `"model": "gemini-2.0-flash-exp"` to use different model

---

## 🎨 Available Models

Based on what you saw in Abacus.AI:
- `grok-beta` - X.AI's Grok model
- `gemini-2.0-flash-exp` - Google's Gemini 2.0 Flash
- `gemini-1.5-pro` - Google's Gemini 1.5 Pro
- `route-llm` - Auto-routing to best model
- `gpt-4o-2024-11-20` - OpenAI GPT-4o
- `gpt-4o-mini` - OpenAI GPT-4o Mini
- `o4-mini`, `o3-pro`, `o3`, `gpt-4.1` - Other models

## 📝 How to Import to n8n

1. **Open n8n** (your n8n instance)
2. **Click "Import workflow"** (or similar button)
3. **Select one of the JSON files**:
   - Start with `reddit-abacus-monitor.json` (simplest)
4. **Configure Google Sheets** (if you want to save results):
   - Click the "Save to Google Sheets" node
   - Connect your Google account
   - Create a new spreadsheet or select existing one
   - Map the columns
5. **Test the workflow**:
   - Click "Execute Workflow" or "Test workflow"
   - Check if Reddit posts are fetched
   - Verify AI analysis works
   - Confirm data saves to Sheets

## 🔧 What Needs Configuration

### For ALL workflows:
- **Google Sheets** node needs:
  - Google authentication
  - Document ID selection
  - Sheet name selection

### For Reddit workflows:
- **Reddit** node may need:
  - Reddit API credentials (if hitting rate limits)
  - Or keep using public API (works without auth, but limited)

### For YouTube workflow:
- **Form Trigger** creates a webhook URL
- Access the form at: `https://your-n8n-instance.com/form/youtube-summarizer`

## 🎯 Quick Test Without Google Sheets

If you want to test without setting up Google Sheets:

1. Import the workflow
2. **Delete** or **disable** the "Save to Google Sheets" node
3. Add a "Set" or "No Operation" node at the end
4. Run the workflow
5. Check the output in n8n's execution view

## 💡 Python Script Reference

The workflows match this Abacus.AI format:

```python
url = "https://routellm.abacus.ai/v1/chat/completions"
headers = {
    "Authorization": "Bearer s2_8ecdc6832cb94ac599ea14ab55b0a928",
    "Content-Type": "application/json"
}
payload = {
    "model": "grok-beta",  # or "gemini-2.0-flash-exp", etc.
    "messages": [
        {"role": "system", "content": "System prompt"},
        {"role": "user", "content": "User message"}
    ]
}
```

## 🚀 Next Steps

1. Choose a workflow (recommend #1 to start)
2. Import to n8n
3. Set up Google Sheets authentication
4. Run a test
5. Customize to your needs
6. Set up scheduling (optional - use Schedule Trigger instead of Manual Trigger)

## 📊 Expected Results

### Reddit Monitor:
- Timestamp, Subreddit, Title, URL, Upvotes, AI Analysis

### Reddit Ideas Miner:
- Timestamp, Subreddit, Title, URL, Upvotes, Comments, Problem, Solution, Market Size, Score, Reasoning

### YouTube Summarizer:
- Timestamp, Video URL, Video ID, Transcript Preview, AI Analysis

---

**All workflows are 100% ready to import and use!** 🎉

No deployment ID needed, no additional configuration required for the Abacus AI part.
