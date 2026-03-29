# Morning Instructions — 2026-03-30
**Written by Claude while you slept.**

---

## What I Did Tonight

### Dashboard fixes (all applied to dashboard.html — ready to push)
1. **Fixed Personal/Work toggle** — it now works properly:
   - Brief view is mode-aware (personal cards hidden in Work mode, project snapshot hidden in Personal mode)
   - Clicking a Brief card auto-switches to the correct mode before navigating
   - Toggle colors: Personal = pink, Work = blue (matches the dashboard palette)
   - Topbar subtitle updates to "Personal Dashboard" / "Work Dashboard"
2. **Fixed done tasks showing as active:**
   - LTVPlus follow-up (done 27 Mar) → now pre-seeded as done
   - Cancel BP account (done 28 Mar) → now pre-seeded as done
   - Negotiate NL translation (done 28 Mar) → now pre-seeded as done
   - Removed `urg` styling from tasks that are already done
3. **Updated TASKS.md** — dashboard version, Netlify status, NL translation marked done
4. **Updated CLAUDE.md** — dashboard system section fully updated (v2.5, URL, deploy workflow, features)

### Docs created (in memory/projects/)
- **agency-name-brainstorm.md** — 10 name candidates, top 3 recommendations, next steps
- **gorgias-role-optimisation.md** — full analysis of where time goes, high-leverage tools + tactics, quick wins, session prompts
- **agency-service-packages.md** — full 5-package framework with pricing, positioning, revenue projections

---

## Your First Task This Morning: Push to GitHub

Run this in Terminal (2 commands):

```bash
# Step 1: Fix gitignore (stops N8N/ai_agents_az appearing in git status)
echo "N8N/ai_agents_az/" >> /Users/yohanloyer/Projects/.gitignore

# Step 2: Push everything
cd /Users/yohanloyer/Projects && git add Productivity/dashboard.html Productivity/TASKS.md Productivity/CLAUDE.md Productivity/versions/ Productivity/memory/ .gitignore && git commit -m "Dashboard v2.5: toggle fix, done-task cleanup, agency docs, memory updates" && git push origin main
```

Netlify will auto-deploy the dashboard in ~10 seconds once pushed.

---

## Netlify Situation

Netlify free plan has hit its monthly bandwidth limit again. Options:
1. **Wait** — resets April 1 (tomorrow). Free.
2. **Upgrade** — Netlify Pro is $19/mo. Permanent solution. Worth it if you use the dashboard daily.
3. **GitHub Pages** — Free, no bandwidth limits. Manual setup needed in GitHub UI (Settings → Pages → deploy from main branch → /Productivity folder). URL would be: yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html

Recommendation: upgrade Netlify to Pro. $19/mo for your primary daily tool is nothing.

---

## High-Value Things to Review Today

### 1. Agency name — 10 min
Open: `memory/projects/agency-name-brainstorm.md`
Top picks: **Kairo**, **Reflow**, **Celio**
This is the blocker for website + packages. Pick one today.

### 2. Service packages — 15 min
Open: `memory/projects/agency-service-packages.md`
5 packages drafted with pricing and positioning. Review and adjust the numbers based on what you know from the market.

### 3. Role optimisation quick wins — 30 min
Open: `memory/projects/gorgias-role-optimisation.md`
4 quick wins that take 10-20 min each with Claude. You have HubSpot and Granola MCPs connected — use them.

---

## Dashboard — Personal vs Work toggle behavior

When you open the dashboard after pushing:
- Default mode is **Personal** (reads from localStorage — remembered)
- Toggle top-right: 🏠 Personal / 💼 Work
- In Personal: shows Personal tab only + personal priority cards in Brief
- In Work: shows Freelance + Professional tabs + project snapshot in Brief
- Brief, Claude Tasks, Done always visible in both modes

---

## One thing to do if Netlify is still down

Open the dashboard from your local file directly:
```
open /Users/yohanloyer/Projects/Productivity/dashboard.html
```
All features work except cloud sync (Gist sync needs HTTPS). Notes, XP, streaks all work locally.
