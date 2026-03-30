# Telegram Bot Setup Guide — Yohan's Dashboard Assistant

**Total setup time: ~30 minutes**
**Cost: Free (Railway 30-day trial, then ~$1/mo)**

---

## What You'll Have When Done

One Telegram bot that does 4 things:
- 💬 **Ask Claude** — chat naturally, get answers about your projects
- ✅ **Task commands** — `done: task name` / `add: task name`
- 🎤 **Voice notes** — send a voice note → transcribed → saved to inbox.md
- ☀️ **Daily briefing** — morning push of your top urgent/important tasks (9am Mon-Fri)

---

## Step 1 — Create Your Telegram Bot (2 min)

1. Open Telegram, search for **@BotFather**
2. Send: `/newbot`
3. Choose a name: `Yohan Ops` (display name)
4. Choose a username: `yohan_ops_bot` (or anything ending in `bot`)
5. BotFather gives you a token like: `7412345678:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
6. **Save this token** — you'll need it in Step 3

**Get your Chat ID:**
1. Message **@userinfobot** on Telegram
2. It replies with your user ID, e.g. `123456789`
3. **Save this number** — needed for the daily briefing workflow

---

## Step 2 — Deploy n8n to Railway (10 min)

1. Go to **https://railway.app** → Sign up with GitHub
2. Click **"New Project"** → **"Deploy from template"**
3. Search **"n8n"** → select the official n8n template → click **Deploy**
4. Wait ~2 minutes for deployment
5. Once running, click **"Settings"** → **"Generate Domain"** — you get a URL like:
   `https://n8n-production-xxxx.up.railway.app`
6. Open that URL → n8n setup wizard → create your admin account

**Important Railway settings:**
- Add environment variable: `N8N_BASIC_AUTH_ACTIVE` = `true`
- Add environment variable: `N8N_BASIC_AUTH_USER` = your username
- Add environment variable: `N8N_BASIC_AUTH_PASSWORD` = your password

---

## Step 3 — Connect Your Files (the key step)

Since n8n runs in the cloud on Railway, it can't directly access your Mac's filesystem (`/Users/yohanloyer/Projects/`). You have two options:

### Option A — GitHub (Recommended, already set up)
The workflows read/write TASKS.md via the **GitHub API** instead of the filesystem.
- Your repo: `github.com/yohanloyer1-dev/Projects` (private)
- Create a **Personal Access Token**: github.com → Settings → Developer Settings → Personal Access Tokens → Fine-grained → select repo `Projects`, permissions: `Contents: Read and Write`
- Save token as: `GITHUB_TOKEN` in Railway environment variables

The task command workflow is pre-built to use GitHub API — just swap the file path calls for GitHub API calls (see Step 4 note).

### Option B — Local n8n on Mac (simpler but needs Mac on)
If you want to run n8n locally instead of Railway:
```bash
npm install -g n8n
n8n start
```
Then use ngrok for webhook access:
```bash
brew install ngrok/ngrok/ngrok
ngrok http 5678
```
Copy the ngrok HTTPS URL as your webhook base URL in Telegram trigger settings.

**Downside:** n8n stops when your Mac sleeps. Not recommended for daily briefing.

---

## Step 4 — Import the Workflows

All 4 workflow JSON files are in: `Productivity/telegram-bot/`

In n8n (Railway URL):
1. Click **"Workflows"** in sidebar → **"Add Workflow"** → **"Import from File"**
2. Import each file:
   - `workflow-1-ask-claude.json` — Claude chat
   - `workflow-2-task-commands.json` — done:/add: commands
   - `workflow-3-voice-notes.json` — voice → inbox.md
   - `workflow-4-daily-briefing.json` — 9am briefing

---

## Step 5 — Configure Each Workflow

### All workflows: Add Telegram credential
1. Open any workflow → click the Telegram Trigger node
2. Click "Credentials" → "New" → "Telegram API"
3. Paste your **Bot Token** from Step 1
4. Name it: `Telegram Bot`
5. This credential is shared across all workflows

### Workflow 1 (Ask Claude):
- The Abacus.AI API key is already hardcoded: `s2_8ecdc6832cb94ac599ea14ab55b0a928`
- Test: send any message to your bot → should get a Claude reply

### Workflow 2 (Task Commands):
- **If using GitHub API** (Option A): Replace the `fs.readFileSync` code nodes with GitHub API calls:
  - GET: `https://api.github.com/repos/yohanloyer1-dev/Projects/contents/Productivity/TASKS.md`
  - Headers: `Authorization: Bearer YOUR_GITHUB_TOKEN`
  - The file content is base64-encoded in the response → decode → modify → PUT back
- **If using local n8n** (Option B): Change path `/data/Productivity/TASKS.md` to `/Users/yohanloyer/Projects/Productivity/TASKS.md`

### Workflow 3 (Voice Notes):
- Add your **OpenAI API key** in the Whisper node (replace `YOUR_OPENAI_API_KEY`)
- Language is set to `fr` (French) — change to `en` or remove for auto-detect
- **File path:** same as Workflow 2 — change to inbox.md path

### Workflow 4 (Daily Briefing):
- Replace `YOUR_TELEGRAM_CHAT_ID` with your chat ID from Step 1
- Schedule is set to `0 8 * * 1-5` = 8am UTC = 9am Paris CET (7am UTC in summer CEST)
- **File path:** same as Workflow 2

---

## Step 6 — Test Everything

Send these to your bot:

| Test | Message | Expected |
|------|---------|----------|
| Chat | `What's my top priority today?` | Claude answers |
| Add task | `add: test task from telegram` | Confirmation reply |
| Done | `done: test task from telegram` | ✅ confirmation |
| Help | `/help` | Command list |
| Voice | Send a voice note | Transcription confirmation |
| Briefing | Trigger workflow manually in n8n | Morning message |

---

## Automation Goal — Where to Update

The **50% automation target** for Nébuleuse appears in 4 places in `dashboard.html`:

| Line | Location | What to change |
|------|----------|----------------|
| ~723 | Progress bar label | `16% automation` → update percentage |
| ~724 | Progress bar fill | `style="width:16%"` → update fill % |
| ~782 | Stats row | `Nébuleuse 50% target` → update if target changes |
| ~834-835 | Brief snapshot card | `8.1%→50%` and `width:16%` |
| ~1054 | Freelance view card | `8.1% → 50%` and `width:16%` |

**To update the current automation rate:** search for `width:16%` and `16% automation` — change `16` to the new number. The `50%` target is separate.

---

## Commands Reference

Once running, your bot accepts:

```
done: <task name>       → mark task done in TASKS.md
add: <task name>        → add task to inbox
/brief                  → show top priorities now
/help                   → show all commands
[any text]              → ask Claude
[voice note]            → transcribe → inbox.md
```

---

## Files Created

| File | Purpose |
|------|---------|
| `telegram-bot/workflow-1-ask-claude.json` | Import into n8n |
| `telegram-bot/workflow-2-task-commands.json` | Import into n8n |
| `telegram-bot/workflow-3-voice-notes.json` | Import into n8n |
| `telegram-bot/workflow-4-daily-briefing.json` | Import into n8n |
| `telegram-bot/SETUP-GUIDE.md` | This file |

---

## Troubleshooting

**Bot doesn't respond:** Check webhook is set in n8n — Telegram Trigger nodes register webhooks automatically when workflow is active.

**"Cannot find task":** Task name must match exactly (case-insensitive). Use the task name as it appears in TASKS.md.

**Railway sleeping:** Railway doesn't sleep on paid plan. On free trial, check Railway dashboard to confirm service is running.

**Daily briefing not sending:** Verify your Chat ID is correct and the schedule trigger timezone matches UTC.
