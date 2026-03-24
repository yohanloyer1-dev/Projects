# n8n Automation — Memory
> Updated: 2026-03-22

## Status
n8n is already set up. Workflows exist at `/Users/yohanloyer/Projects/N8N/`. Status of running instance (local vs cloud) TBD — confirm with Yohan.

## Existing Workflows
| File | What | Status |
|------|------|--------|
| `reddit-abacus-monitor.json` | Reddit r/technology → AI sentiment analysis → Google Sheets | Ready to import |
| `reddit-ideas-miner-abacus.json` | Reddit r/startups → startup idea extraction (score >6) → Google Sheets | Ready to import |
| `youtube-summarizer-abacus.json` | YouTube URL form → transcript → Gemini 2.0 analysis → Google Sheets | Ready to import |

## Abacus.AI Config
- API Key: `s2_8ecdc6832cb94ac599ea14ab55b0a928`
- Endpoint: `https://routellm.abacus.ai/v1/chat/completions`
- Auth: Bearer token
- Models available: grok-beta, gemini-2.0-flash-exp, gemini-1.5-pro, gpt-4o, gpt-4o-mini, o4-mini, o3, gpt-4.1

## ai_agents_az Course
Full course folder at `N8N/ai_agents_az/` with 25+ episodes. Yohan is learning n8n / AI agent building.

## WhatsApp Agent via Kapso (TO BUILD — replaces Telegram plan)
Goal: Send text or voice note on WhatsApp → Claude reads it → updates TASKS.md → replies on WhatsApp

### Why Kapso (not Telegram)
- WhatsApp is already on Yohan's phone and his main comms channel
- Kapso gives a real WhatsApp number via Meta Cloud API
- Free tier: 2,000 msg/month, 1 number, unlimited agent runs
- CLI tool for terminal management
- Works natively with n8n via webhook

### Architecture
1. **Trigger**: Kapso WhatsApp webhook → n8n
2. **Branch**: Is it audio? → transcribe via Whisper | Is it text? → pass directly
3. **Process**: Send to Claude API with context (TASKS.md content)
4. **Act**: Claude updates TASKS.md / inbox.md with new tasks/notes
5. **Reply**: n8n sends response back via Kapso WhatsApp API

### inbox.md entry format
```
---
**WhatsApp note** — 2026-03-22 14:32
[transcribed or typed text here]
Status: unread
---
```

### Setup steps
1. Confirm n8n is running (check localhost:5678 or cloud URL)
2. Sign up at kapso.ai → get sandbox WhatsApp number (instant, no Meta verification)
3. For permanent number: add deposit to get a real US/FR number
4. Connect Kapso webhook → n8n workflow
5. Build the 5-node workflow: Receive → Branch (voice/text) → Transcribe → Claude → Reply
6. Test with a voice message and a text message
7. Wire Claude to read/update TASKS.md

## Next Steps
- [ ] Confirm n8n running status (local or cloud?)
- [ ] Sign up at kapso.ai and get sandbox number
- [ ] Decide: sandbox number OK for now, or get permanent number immediately?
- [ ] Build WhatsApp workflow in n8n (5 nodes)
- [ ] Import existing Reddit/YouTube workflows if useful
