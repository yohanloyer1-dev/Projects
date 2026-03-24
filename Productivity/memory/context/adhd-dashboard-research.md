# ADHD UX Research — Dashboard Variant
> Compiled: 2026-03-22

## Key Principles for ADHD-Optimized Design

### 1. One Decision Per Screen
- Show only TODAY's tasks by default; future tasks require deliberate click to reveal
- No visible counts of total task backlog (creates ambient anxiety)
- Distraction-free mode as default, "full view" opt-in

### 2. Visual Time Anchoring (Combat Time Blindness)
- Disappearing arc/circle showing how much of the day remains (like Time Timer)
- "X days left" badges with color gradient (green → yellow → orange → red) not just text dates
- Analog clock always visible in footer during focus mode
- "Due in 3 days" always more prominent than "2026-03-25"

### 3. Dopamine-Driven Immediate Wins
- Satisfying completion animations on every checkbox (bounce, particle burst)
- "7 small wins today" micro-counter at top
- Celebrate urgency-specific: "You cleared 2 urgent tasks!"
- Streak is most important gamification element (visible at all times, not buried)
- Avoid abstract XP — concrete progress beats points

### 4. Progressive Disclosure
- Single next action front-and-center ("Do This Now" card)
- All other tasks collapsed behind tabs/sections
- Task detail only reveals on click — no metadata visible by default
- Quick-add: title only → everything else optional

### 5. Bold Visual Salience for Urgent Items
- Largest text/button for the single most urgent task
- High-contrast background (not just text label) for overdue items
- 🔴 overdue, 🟡 due today, ⚪ upcoming — icons not just colors
- "Floating urgent" card pinned above everything else

### 6. Task Micro-Chunking
- Subtasks shown inline as simple checklist (no nesting)
- "Just do this first" highlight on single next subtask
- Estimated time per step (not just total)
- Completion % for multi-step tasks

### 7. Soft Notification Architecture
- Visual-only by default (no sound/system alerts)
- In-app toast, auto-dismiss, small + brief
- Gentle nudge on inactivity + urgent tasks only
- Notification intensity control: Gentle / Moderate / Assertive

### 8. Hyperfocus Support
- "Deep work" mode: hides all tasks except current one, shows timer
- Context-switch reminder after 60+ min: gentle, dismissible
- Customizable focus interval (not fixed 25-min Pomodoro)
- "Return to last task" button after switch

### 9. Sensory/Visual Preferences
- Motion toggle: on/off for all animations
- "Calm" mode: reduced colors, no animations, more whitespace
- Font size + spacing controls
- Color filter options (accessibility)

### 10. Context Preservation
- Notes auto-save as you type
- "Return to last task" quick-access
- In-progress state visible when returning to a task
- No guilt on task switch — UI doesn't penalize

### 11. Completion Philosophy
- "Mark done" is large and obvious; edit requires menu
- No "are you sure?" confirmation dialogs
- No quality rating at completion
- Auto-archive completed tasks after 24h

## Key Differences vs Standard Dashboard

| Standard | ADHD-Optimized |
|----------|---------------|
| Show all tasks | Show only today |
| Text dates | Visual countdown + color gradient |
| XP points | Streaks + micro-win counts |
| Full interface upfront | One thing at a time |
| Small badges for urgency | Bold, high-contrast, largest text |
| Fixed Pomodoro | Customizable focus intervals |
| Push notifications | Visual-only, soft nudges |
| Settings buried | Sensory controls in main UI |

## Apps to Reference for Design Inspiration
- **Structured** (iOS) — time-blocking with visual timeline
- **Focusmate** — body doubling concept
- **Goblin Tools** — AI-powered task breakdown
- **TickTick** — best ADHD-friendly calendar + task hybrid
- **Sunsama** — daily planning ritual

## What to Build for ADHD Variant
1. "Do This Now" hero card — single most urgent task, massive, prominent
2. Visual day arc (% of day remaining)
3. Today-only default view
4. Focus mode (full-screen single task + timer)
5. Calm mode toggle (reduced animations/color)
6. Micro-win counter ("3 wins today")
7. Task breakdown: subtasks inline, one step highlighted
8. Soft notification badge (no popups)
