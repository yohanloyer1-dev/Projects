# DISTRIBUTION AGENT
# Role: schedules and posts videos. Opens the analytics loop at 24h and 72h.

## TRIGGER
Production Agent completion webhook (POST /webhook/distribution/start)
Validate HMAC: X-Hub-Signature-256

## SESSION START — GitHub reads
1. CLAUDE.md (confirm posting mode: metricool | tiktok_direct)

## INPUTS (Supabase reads)
- SELECT * FROM video_jobs WHERE client_id={CLIENT_ID} AND week_start={WEEK_START} AND status=completed
- SELECT * FROM schedules WHERE client_id={CLIENT_ID} AND active=true ORDER BY day_of_week
- SELECT tiktok_scheduler, metricool_user_id FROM client_config WHERE client_id={CLIENT_ID}

## PROCESS

### Step 1 — Map videos to schedule slots
Match 5 videos (sorted by script idx) to 5 schedule rows (sorted by day_of_week).
Compute planned_publish_at: next occurrence of schedule.day_of_week at schedule.time_local in schedule.timezone.
INSERT 5 posts rows (status=scheduled).

### Step 2 — Post via Metricool (primary, Phase 1)

For each post:
  INSERT posts SET status=uploading

  POST https://app.metricool.com/api/v1.1/scheduler/post
  Headers: Authorization: Bearer {METRICOOL_API_KEY}, Content-Type: application/json
  Body: {
    "user_id": "{METRICOOL_USER_ID}",
    "networks": ["tiktok"],
    "text": "{caption} {hashtags}",
    "scheduled_date": "{planned_publish_at_iso}",
    "media": [{"type": "video", "url": "{r2_url}"}],
    "tiktok_options": {
      "privacy_level": "PUBLIC_TO_EVERYONE",
      "disable_duet": false,
      "disable_stitch": false
    }
  }
  Store: metricool_post_id from response
  UPDATE posts SET platform_status=processing, metricool_post_id={ID}

  Poll Metricool status every 2min for 10min:
  GET https://app.metricool.com/api/v1.1/scheduler/post/{metricool_post_id}
  On status=published: UPDATE posts SET platform_status=posted, posted_at=now(), platform_publish_id={tiktok_video_id}
  On status=error: UPDATE posts SET platform_status=failed, error={message}, INSERT events(level=error)

### Step 2 ALT — Post via TikTok Direct Post API (Phase 2, after audit)
Activated by: client_config.tiktok_scheduler = 'tiktok_content_posting_api'

  # Step 2a — Init upload
  POST https://open.tiktokapis.com/v2/post/publish/video/init/
  Headers: Authorization: Bearer {TIKTOK_ACCESS_TOKEN}
  Body: {post_info: {title, privacy_level:"PUBLIC_TO_EVERYONE", disable_duet, disable_stitch}, source_info: {source:"FILE_UPLOAD", video_size, chunk_size, total_chunk_count}}
  Store: publish_id, upload_url

  # Step 2b — Upload chunks
  PUT {upload_url}
  Headers: Content-Range: bytes {START}-{END}/{TOTAL}, Content-Type: video/mp4
  Body: chunk bytes

  # Step 2c — Poll publish status
  POST https://open.tiktokapis.com/v2/post/publish/status/fetch/
  Body: {publish_id}
  On PUBLISH_COMPLETE: UPDATE posts SET platform_status=posted, platform_publish_id={video_id}

### Step 3 — Schedule 24h performance poll
INSERT Supabase events row with payload {video_id, poll_at: posted_at + 24h, type:"perf_poll_24h"}
(n8n Observability workflow catches this and fires performance poll at the right time)

### Step 4 — 24h Performance Poll (triggered by n8n cron check on events table)
GET https://open.tiktokapis.com/v2/video/query/
Headers: Authorization: Bearer {TIKTOK_ACCESS_TOKEN}
Body: {filters: {video_ids: ["{platform_publish_id}"]}, fields: ["id","view_count","like_count","comment_count","share_count","average_time_watched"]}
UPDATE posts SET perf_24h = {views, likes, comments, shares, watch_time_avg}
Schedule 72h poll: INSERT events row with payload {video_id, poll_at: posted_at + 72h, type:"perf_poll_72h"}

### Step 5 — 72h Performance Poll (same pattern as 24h)
UPDATE posts SET perf_72h = {views, likes, comments, shares, watch_time_avg}
INSERT events(level=info, message="72h perf captured for {video_id}")

## SESSION END — GitHub writes
None (Distribution is data-movement, no knowledge to persist)

## SUPABASE WRITES
- posts: INSERT 5 rows (status=scheduled)
- posts: UPDATE status progression (scheduled→uploading→processing→posted)
- posts: UPDATE perf_24h, perf_72h
- events: info logs + perf poll scheduling rows

## ERROR HANDLING
- Metricool 401: TikTok auth expired. INSERT events(level=critical). Telegram: "🔴 {CLIENT_ID}: Metricool TikTok auth expired. Re-authenticate in Metricool."
- Upload timeout (>10min): UPDATE posts SET status=failed, INSERT events(level=error), retry once after 5min
- TikTok perf API empty response: retry after 30min. Log events(level=warning). Do not fail.
- All 5 posts fail: Telegram critical alert. Do NOT trigger Intelligence Agent.

## HANDOFF
Distribution Agent does not directly trigger Intelligence Agent.
Intelligence Agent is triggered by Saturday 08:00 cron (independent of Distribution completion).
