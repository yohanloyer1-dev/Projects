# Abacus AI Setup Guide for n8n Workflows

## What You Need

You already have:
- ✅ API Key: `s2_8ecdc6832cb94ac599ea14ab55b0a928`

You still need:
- ❌ Deployment ID (see steps below)

## How to Get Your Deployment ID

### Step 1: Access Abacus.AI Dashboard
1. Go to https://chatllm.abacus.ai/
2. Log in with your account

### Step 2: Create or Access a ChatLLM App
1. If you don't have a chatbot/app yet, create one:
   - Click "Create New App" or similar
   - Choose a model (Grok, Gemini, etc.)
   - Configure basic settings

2. If you already have an app, select it from your dashboard

### Step 3: Find Your Deployment ID
1. In your app/project, click **"Manage Deployment"**
2. Select **"API"** tab
3. You should see:
   - Deployment ID (copy this - it will look like: `d-xxxxxxxxxxxxx`)
   - API endpoints
   - Option to "Create New Token" (optional, you already have API key)

### Step 4: Update the n8n Workflow Files

Replace these placeholders in the workflow JSON files:
- `YOUR_ABACUS_API_KEY` → `s2_8ecdc6832cb94ac599ea14ab55b0a928`
- `YOUR_DEPLOYMENT_ID` → (the deployment ID you copied)
- `YOUR_GROK_DEPLOYMENT_ID` → (if using Grok specifically)
- `YOUR_GEMINI_DEPLOYMENT_ID` → (if using Gemini specifically)

## Alternative: Use RouteLLM API Instead

If you just want to test with models without creating a deployment, Abacus offers RouteLLM API:

1. Go to https://routellm-apis.abacus.ai/
2. This may allow direct model access without deployment IDs
3. Check if your API key works with their direct model endpoints

## Workflows Ready to Import

I've created these workflows for you:
1. `reddit-abacus-monitor.json` - Easiest to start with
2. `youtube-summarizer-abacus.json` - YouTube analysis
3. `reddit-ideas-miner-abacus.json` - Advanced Reddit mining

## Next Steps After Getting Deployment ID

1. Open the workflow file in a text editor
2. Find and replace the placeholders with your actual values
3. Import into n8n
4. Test the workflow

## Sources
- [Abacus.AI ChatLLM Documentation](https://abacus.ai/help/howTo/chatllm)
- [App Deployment Guide](https://abacus.ai/help/howTo/chatllm/app_deployment_and_custom_domain_how_to)
- [API Reference](https://abacus.ai/help/api)
