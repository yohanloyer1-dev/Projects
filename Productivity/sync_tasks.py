#!/usr/bin/env python3
"""
sync_tasks.py
Reads DASHBOARD-TASKS.md, injects new task cards into dashboard.html for any
task not already present, saves a version snapshot, updates the changelog,
and pushes to GitHub via the API.

Usage:
    python3 sync_tasks.py            # inject + push
    python3 sync_tasks.py --dry-run  # preview without making changes
"""

import re, json, base64, urllib.request, urllib.error, shutil, os, sys, ssl
from datetime import datetime
from html import escape as he

try:
    import certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    _SSL_CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

# ── Config ────────────────────────────────────────────────────────────────────
REPO       = "yohanloyer1-dev/Projects"
TOKEN_PATH = os.path.expanduser("~/Projects/.github-token")
DASH_PATH  = "/Users/yohanloyer/Projects/Productivity/dashboard.html"
TASKS_PATH = "/Users/yohanloyer/Projects/Productivity/DASHBOARD-TASKS.md"
CHLOG_PATH = "/Users/yohanloyer/Projects/Productivity/memory/dashboard-changelog.md"
VER_DIR    = "/Users/yohanloyer/Projects/Productivity/versions"

DASH_API  = f"https://api.github.com/repos/{REPO}/contents/Productivity/dashboard.html"
CHLOG_API = f"https://api.github.com/repos/{REPO}/contents/Productivity/memory/dashboard-changelog.md"

DEFAULT_XP = 10

# Maps DASHBOARD-TASKS.md ### section headers → data-project used in dashboard.html
SECTION_PROJECT = {
    "Strategy & Vision":                        "Strategy",
    "Tools & Integrations":                     "Tech",
    "Dashboard & Productivity System":          "Productivity",
    "Admin & Finance":                          "Admin & Finance",
    "Health":                                   "Health",
    "Real Estate":                              "Real Estate",
    "Japan Trip":                               "Japan Trip",
    "Travel & Errands":                         "Travel",
    "Tech & Accounts":                          "Tech",
    "Network & Others":                         "Network",
    "Bots & Automation (Personal)":             "Bots",
    "Nébuleuse (personal idea)":                "Nébuleuse",
    "Productivity":                             "Productivity",
    "Work Travel & Expenses":                   "Work Travel",
    "Presentations & Events":                   "Work Travel",
    "Role Optimization":                        "Gorgias Role",
    "Follow-ups":                               "Gorgias Role",
    "Nébuleuse Bijoux":                         "Nébuleuse",
    "Accessory Partners":                       "Accessory Partners",
    "Gorgias Agency (name TBD)":               "Agency",
    "LinkedIn Content — Voice Profile Project": "LinkedIn",
    # "Claude OS" intentionally omitted — no project card in dashboard.html yet.
    # Add a card manually, then add the section here.
}

STATUS_MAP = {'!': 'urg', '>': 'hi', '~': 'hi', '?': 'wt', '_': 'sd', ' ': ''}

# ── GitHub helpers ────────────────────────────────────────────────────────────

def read_token():
    with open(TOKEN_PATH) as f:
        return f.read().strip()

def gh_get(url, token):
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    })
    with urllib.request.urlopen(req, context=_SSL_CTX) as r:
        return json.loads(r.read())

def gh_put(url, token, content_str, sha, message):
    payload = json.dumps({
        "message": message,
        "content": base64.b64encode(content_str.encode("utf-8")).decode("ascii"),
        "sha": sha,
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="PUT", headers={
        "Authorization": f"token {token}",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, context=_SSL_CTX) as r:
        return json.loads(r.read())

# ── Slug / normalize helpers ──────────────────────────────────────────────────

def slugify(title):
    s = title.lower()
    s = re.sub(r"[^\w\s-]", " ", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")

def norm_match(s):
    """Normalize for dedup matching: lowercase, remove non-word/space, collapse spaces."""
    s = s.lower()
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return re.sub(r"\s+", " ", s).strip()

def strip_step(title):
    """Remove 'STEP N [TAG] ' prefix (e.g. 'STEP 1 [YOU] ...')."""
    return re.sub(r"^STEP\s+\d+\s+\[[^\]]*\]\s*", "", title, flags=re.IGNORECASE).strip()

# ── Parse DASHBOARD-TASKS.md ──────────────────────────────────────────────────

def parse_tasks(md_text):
    tasks = []
    section = None
    for line in md_text.splitlines():
        s = line.strip()
        if line.startswith("### "):
            section = line[4:].strip()
            continue
        if line.startswith("#") or s.startswith("---") or s.startswith("<!--"):
            continue
        if not s.startswith("- [") or section is None:
            continue

        m = re.match(r"^- ((?:\[[!>~?_x ]\])+)\s*", s)
        if not m:
            continue
        markers = re.findall(r"\[([!>~?_x ])\]", m.group(1))
        if "x" in markers:
            continue  # skip done

        rest = s[m.end():]
        tm = re.match(r"\*\*(.+?)\*\*", rest)
        if not tm:
            continue
        title_raw = tm.group(1).strip()
        after = rest[tm.end():]

        estimate = None
        em = re.match(r"\s*_\((.+?)\)_", after)
        if em:
            estimate = em.group(1).strip()
            after = after[em.end():]

        description = None
        dm = re.match(r"\s*[—-]+\s*(.+)", after)
        if dm:
            description = dm.group(1).strip()

        is_cl = "🤖" in line
        title_clean = re.sub(r"[🤖🎙️]", "", title_raw).strip()
        desc_clean  = re.sub(r"[🤖🎙️]", "", description).strip() if description else None

        status_classes = []
        for mk in markers:
            cls = STATUS_MAP.get(mk, "")
            if cls and cls not in status_classes:
                status_classes.append(cls)

        tasks.append({
            "section":        section,
            "title":          title_clean,
            "status_classes": status_classes,
            "is_cl":          is_cl,
            "estimate":       estimate,
            "description":    desc_clean,
            "data_id":        None,  # assigned in assign_slugs()
        })
    return tasks

def assign_slugs(tasks, existing_ids):
    """Assign unique data-id slugs, avoiding collisions with existing HTML ids."""
    allocated = set(existing_ids)
    for t in tasks:
        base = slugify(t["title"])
        slug, n = base, 2
        while slug in allocated:
            slug = f"{base}-{n}"
            n += 1
        t["data_id"] = slug
        allocated.add(slug)

# ── Deduplication ─────────────────────────────────────────────────────────────

def get_existing_ids(html):
    return set(re.findall(r'data-id="([^"]+)"', html))

def get_existing_tns(html):
    return re.findall(r'<span class="tn">(.+?)</span>', html)

def _words(s, min_len=4):
    return [w for w in re.findall(r"\w+", norm_match(s), re.UNICODE) if len(w) >= min_len]

def word_overlap(title_md, tn_html, min_match=3):
    """True if ≥ min_match significant words (≥4 chars) from title_md appear in tn_html."""
    wa = _words(title_md)
    if not wa:
        return False
    wb = set(_words(tn_html))
    hits = sum(1 for w in wa if w in wb)
    return hits >= min(min_match, len(wa))

def already_in_html(task, existing_ids, tns_norm_set, tns_raw):
    # 1. Exact slug
    if task["data_id"] in existing_ids:
        return True, "slug"

    # 2. Exact normalized title
    nt = norm_match(task["title"])
    if nt in tns_norm_set:
        return True, "title-exact"

    # 3. Character substring (≥6 chars): handles "SMS fix" ↔ "SMS fix — normalize…"
    for tn in tns_raw:
        tn_n = norm_match(tn)
        if len(nt) >= 6 and nt in tn_n:
            return True, "char-sub"
        if len(tn_n) >= 6 and tn_n in nt:
            return True, "char-sub"

    # 4. Word overlap (≥3 significant words match): catches "Create my Network Pokedex"
    #    ↔ "Create Network Pokedex", and step-prefixed titles ↔ clean HTML titles.
    for candidate in dict.fromkeys([task["title"], strip_step(task["title"])]):
        if not candidate:
            continue
        for tn in tns_raw:
            if word_overlap(candidate, tn, min_match=3):
                return True, "word-overlap"

    return False, None

# ── Insertion point ───────────────────────────────────────────────────────────

def find_insertion_point(html_lines, data_project):
    """
    Return (last_note_panel_line_idx, indent_str) for the given data-project.
    Finds the LAST note-panel whose preceding task div has this data-project.
    """
    dp_esc   = data_project.replace("&", "&amp;")
    dp_plain = data_project
    last_idx, last_indent = -1, "        "

    for i, line in enumerate(html_lines):
        if f'data-project="{dp_esc}"' in line or f'data-project="{dp_plain}"' in line:
            # The note-panel should be the next non-empty line
            for j in range(i + 1, min(i + 4, len(html_lines))):
                if 'class="note-panel"' in html_lines[j]:
                    last_idx = j
                    raw = html_lines[i]
                    last_indent = " " * (len(raw) - len(raw.lstrip()))
                    break
    return last_idx, last_indent

# ── HTML generation ───────────────────────────────────────────────────────────

def make_task_html(task, indent):
    classes = ["t"] + task["status_classes"]
    if task["is_cl"]:
        classes.append("cl")

    project   = SECTION_PROJECT.get(task["section"], "Unknown")
    title_esc = he(task["title"])

    td_parts = []
    if task["estimate"]:
        td_parts.append(task["estimate"])
    if task["description"]:
        td_parts.append(task["description"])
    td_html = f'<span class="td">{he(" — ".join(td_parts))}</span>' if td_parts else ""

    badge = '<span class="tbadge bc">🤖 Claude</span>' if task["is_cl"] else ""

    task_div = (
        f'{indent}<div class="{" ".join(classes)}" data-id="{task["data_id"]}" '
        f'data-xp="{DEFAULT_XP}" data-project="{he(project)}">'
        f'<div class="chk"></div>'
        f'<div class="tb"><span class="tn">{title_esc}</span>{td_html}</div>'
        f'<button class="note-btn" title="Add note">📝</button>'
        f'{badge}'
        f'</div>'
    )
    note_div = f'{indent}<div class="note-panel" data-for="{task["data_id"]}"></div>'
    return task_div, note_div

# ── Version snapshot ──────────────────────────────────────────────────────────

def save_snapshot(dash_path, ver_dir):
    today = datetime.now().strftime("%Y-%m-%d")
    max_v = 0.0
    for f in os.listdir(ver_dir):
        mm = re.match(r"dashboard_v(\d+\.\d+)_", f)
        if mm:
            max_v = max(max_v, float(mm.group(1)))
    next_v = round(max_v + 0.1, 1)
    name = f"dashboard_v{next_v}_{today}_pre-sync-tasks.html"
    shutil.copy2(dash_path, os.path.join(ver_dir, name))
    return name, next_v

# ── Changelog ─────────────────────────────────────────────────────────────────

def update_changelog(chlog_path, injected):
    today = datetime.now().strftime("%Y-%m-%d")
    bullets = "\n".join(
        f'  - `{t["data_id"]}` [{",".join(t["status_classes"]) or "normal"}] — {t["title"]}'
        for t in injected
    )
    entry = (
        f"## {today} | sync_tasks.py: inject {len(injected)} task(s) | pending\n\n"
        f"### Changes\n"
        f"- Auto-injected via sync_tasks.py from DASHBOARD-TASKS.md:\n"
        f"{bullets}\n"
        f"- No structural or JS changes\n\n"
        f"---\n\n"
    )
    with open(chlog_path, "r", encoding="utf-8") as f:
        content = f.read()
    sep = "\n---\n\n"
    idx = content.find(sep)
    new = (content[:idx + len(sep)] + entry + content[idx + len(sep):]) if idx != -1 else entry + content
    with open(chlog_path, "w", encoding="utf-8") as f:
        f.write(new)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("=== DRY RUN — no files modified, no push ===\n")

    token = read_token()

    print("Reading local files...")
    with open(TASKS_PATH, "r", encoding="utf-8") as f:
        md_text = f.read()
    with open(DASH_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    tasks = parse_tasks(md_text)
    print(f"  {len(tasks)} active tasks parsed from DASHBOARD-TASKS.md")

    existing_ids = get_existing_ids(html)
    tns_raw      = get_existing_tns(html)
    tns_norm_set = {norm_match(t) for t in tns_raw}
    print(f"  {len(existing_ids)} task IDs already in dashboard.html")

    assign_slugs(tasks, existing_ids)

    to_inject, skipped, unmapped = [], [], []
    for t in tasks:
        if t["section"] not in SECTION_PROJECT:
            unmapped.append(t)
            continue
        found, reason = already_in_html(t, existing_ids, tns_norm_set, tns_raw)
        (skipped if found else to_inject).append(t)

    print(f"\nResults:")
    print(f"  Will inject:  {len(to_inject)}")
    print(f"  Already present (skipped): {len(skipped)}")
    print(f"  Unmapped section (skipped): {len(unmapped)}")

    if unmapped:
        print("\nUnmapped sections — no project card in dashboard.html:")
        for t in unmapped:
            print(f"  [{t['section']}] {t['title']}")

    if not to_inject:
        print("\nNothing to inject — dashboard is up to date.")
        return

    print("\nWill inject:")
    for t in to_inject:
        print(f"  + [{t['section']}→{SECTION_PROJECT[t['section']]}] {t['title']} (id={t['data_id']})")

    if dry_run:
        return

    # ── Snapshot ──
    print("\nSaving version snapshot...")
    snap, ver = save_snapshot(DASH_PATH, VER_DIR)
    print(f"  {snap}")

    # ── Inject into HTML ──
    html_lines = html.splitlines(keepends=True)
    injected, failed = [], []

    for t in to_inject:
        dp = SECTION_PROJECT[t["section"]]
        idx, indent = find_insertion_point(html_lines, dp)
        if idx == -1:
            print(f"  WARN: No .tl div found for data-project={dp!r}  Skipping: {t['title']}")
            failed.append(t)
            continue
        task_line, note_line = make_task_html(t, indent)
        html_lines.insert(idx + 1, note_line + "\n")
        html_lines.insert(idx + 1, task_line + "\n")
        injected.append(t)
        print(f"  ✓ [{dp}] {t['title']}  →  data-id={t['data_id']}")

    if not injected:
        print("No tasks successfully injected.")
        return

    new_html = "".join(html_lines)
    with open(DASH_PATH, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"\nSaved dashboard.html  (+{len(injected)} tasks)")

    update_changelog(CHLOG_PATH, injected)
    print("Updated dashboard-changelog.md")

    # ── Push ──
    print("\nPushing to GitHub...")
    dash_info = gh_get(DASH_API, token)
    chlog_info = gh_get(CHLOG_API, token)

    today = datetime.now().strftime("%Y-%m-%d")
    summary = ", ".join(t["title"][:28] for t in injected[:3])
    if len(injected) > 3:
        summary += f" +{len(injected)-3} more"
    commit_msg = f"sync_tasks: inject {len(injected)} task(s) — {summary}"

    with open(DASH_PATH, "r", encoding="utf-8") as f:
        dash_content = f.read()
    gh_put(DASH_API, token, dash_content, dash_info["sha"], commit_msg)
    print("  ✓ Pushed dashboard.html")

    with open(CHLOG_PATH, "r", encoding="utf-8") as f:
        chlog_content = f.read()
    gh_put(CHLOG_API, token, chlog_content, chlog_info["sha"],
           f"changelog: sync_tasks {today} — {len(injected)} task(s)")
    print("  ✓ Pushed dashboard-changelog.md")

    print(f"\n✅ Done — {len(injected)} task(s) injected and pushed.")
    if failed:
        print(f"⚠️  {len(failed)} task(s) skipped (no .tl div): {', '.join(t['title'] for t in failed)}")
    print("   Live URL: https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html")


if __name__ == "__main__":
    main()
