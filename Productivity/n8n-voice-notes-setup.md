# n8n Voice Notes Setup — WhatsApp/Telegram → Claude inbox

## Why n8n can't run in Cowork's VM
Cowork's sandbox is a lightweight, ephemeral Linux container. n8n needs to run persistently on your Mac (or a cloud server) to listen for incoming messages 24/7.

---

## Option A — Run n8n locally on your Mac (free, recommended to start)

### Step 1: Install n8n
```bash
# Open Terminal on your Mac
npm install -g n8n
```
If you don't have Node.js: download from https://nodejs.org (LTS version)

### Step 2: Start n8n
```bash
n8n start
```
n8n opens at: http://localhost:5678

### Step 3: Make it accessible from the internet (for WhatsApp/Telegram webhooks)
Install ngrok (free tunnel):
```bash
brew install ngrok/ngrok/ngrok
ngrok http 5678
```
Copy the `https://xxxx.ngrok.io` URL — this is your webhook base URL.

---

## Option B — Deploy n8n to Railway (free tier, always-on cloud)
1. Go to https://railway.app
2. Create a new project → Deploy from template → search "n8n"
3. Click deploy — takes ~2 minutes
4. Your n8n URL will be something like: `https://n8n-production-xxxx.up.railway.app`

---

## The Workflow (build this in n8n)

### Trigger: Telegram Bot (easier than WhatsApp)
1. Create a Telegram bot: open @BotFather on Telegram → /newbot → copy the API token
2. In n8n: Add node → Trigger → Telegram Trigger → paste token → set for "message" events
3. Send yourself a voice note on Telegram to the bot to test

### Node 2: Download voice note audio
- Add node → HTTP Request
- GET `https://api.telegram.org/bot{TOKEN}/getFile?file_id={{$json.message.voice.file_id}}`
- Outputs: file_path

### Node 3: Transcribe with OpenAI Whisper
- Add node → HTTP Request (POST)
- URL: `https://api.openai.com/v1/audio/transcriptions`
- Auth: Bearer YOUR_OPENAI_KEY
- Body: form-data with `model=whisper-1` and `file` = audio download
- Outputs: transcribed text

### Node 4: Append to inbox.md
- Add node → Write Binary File (or SSH/Write File)
- Append to: `/Users/yohanloyer/Projects/Productivity/inbox.md`
- Content:
```
---
**Voice note** — {{$now.format('YYYY-MM-DD HH:mm')}}
{{$node["Whisper"].json.text}}

Status: unread
---
```

### For WhatsApp (more complex)
WhatsApp requires the Meta Business API or a third-party service like Twilio.
Easier path: Use Telegram for voice notes, WhatsApp for everything else.

---

## What Claude does with inbox.md

At the start of every session, Claude reads `inbox.md` and:
1. Processes any items marked `Status: unread`
2. Links them to the relevant task/project
3. Updates TASKS.md or memory files as needed
4. Marks the item as `Status: processed`

---

## Current Status
- n8n: NOT running (needs to be set up on your Mac or Railway)
- Telegram bot: NOT created yet
- inbox.md: Will be created automatically on first voice note
