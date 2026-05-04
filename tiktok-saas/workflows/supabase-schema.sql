-- TikTok SaaS — Supabase Schema
-- Run this in Supabase SQL Editor (Project > SQL Editor > New Query)
-- RLS enabled on all tables from day one. Service role key bypasses RLS.
-- Version: 1.0 | Date: 2026-05-04

-- ============================================================
-- CLIENTS
-- ============================================================
create table if not exists clients (
  client_id text primary key,
  client_name text not null,
  status text not null default 'active' check (status in ('active','paused','churned')),
  timezone text not null default 'Europe/Paris',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- ============================================================
-- CLIENT CONFIG
-- ============================================================
create table if not exists client_config (
  client_id text primary key references clients(client_id) on delete cascade,
  niche text not null,
  target_audience text not null,
  tone_guide text not null,
  cta_keyword text not null,
  brand_terms_to_avoid text[] not null default '{}',
  disclaimer_rules jsonb not null default '{}'::jsonb,
  free_resource_url text not null,
  email_provider text not null default 'ConvertKit',
  tiktok_scheduler text not null default 'metricool',
  chatfuel_bot_id text,
  manychat_workspace_id text, -- DEPRECATED 2026-05-04, kept for backward-compat. Remove in v2 schema.
  higgsfield_character_id text,
  persona_ref_image_url text,
  convertkit_form_id text,
  convertkit_tag_id text,
  metricool_user_id text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- ============================================================
-- SCHEDULES
-- ============================================================
create table if not exists schedules (
  schedule_id bigserial primary key,
  client_id text not null references clients(client_id) on delete cascade,
  day_of_week int not null check (day_of_week between 1 and 7),
  time_local time not null,
  timezone text not null,
  active boolean not null default true,
  unique (client_id, day_of_week, time_local)
);

-- ============================================================
-- RESEARCH RUNS
-- ============================================================
create table if not exists research_runs (
  research_run_id bigserial primary key,
  client_id text not null references clients(client_id) on delete cascade,
  week_start date not null,
  status text not null default 'queued' check (status in ('queued','in_progress','completed','failed')),
  inputs jsonb not null default '{}'::jsonb,
  outputs jsonb not null default '{}'::jsonb,
  error text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (client_id, week_start)
);

-- ============================================================
-- CONTENT INSIGHTS
-- ============================================================
create table if not exists content_insights (
  insight_id bigserial primary key,
  client_id text not null references clients(client_id) on delete cascade,
  research_run_id bigint references research_runs(research_run_id) on delete cascade,
  source text not null,
  tiktok_url text not null,
  author_handle text,
  caption text,
  transcript text,
  hook_type text check (hook_type in ('question','statement','statistic','story',null)),
  emotional_trigger text check (emotional_trigger in ('fear','curiosity','aspiration','relief',null)),
  stats jsonb not null default '{}'::jsonb,
  score numeric not null default 0,
  created_at timestamptz not null default now(),
  unique (client_id, tiktok_url)
);

-- ============================================================
-- SCRIPT BATCHES
-- ============================================================
create table if not exists script_batches (
  script_batch_id bigserial primary key,
  client_id text not null references clients(client_id) on delete cascade,
  week_start date not null,
  status text not null default 'queued' check (status in ('queued','generating','pending_approval','approved','failed')),
  prompt_version text not null default 'v1',
  research_summary jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (client_id, week_start)
);

-- ============================================================
-- SCRIPTS
-- ============================================================
create table if not exists scripts (
  script_id bigserial primary key,
  client_id text not null references clients(client_id) on delete cascade,
  script_batch_id bigint references script_batches(script_batch_id) on delete cascade,
  week_start date not null,
  idx int not null,
  status text not null default 'pending_approval' check (status in ('pending_approval','approved','rejected','generating_video','ready')),
  script_json jsonb not null,
  approval_attempt int not null default 1,
  operator_feedback text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (client_id, week_start, idx)
);

-- ============================================================
-- VIDEO JOBS
-- ============================================================
create table if not exists video_jobs (
  video_job_id bigserial primary key,
  client_id text not null references clients(client_id) on delete cascade,
  script_id bigint references scripts(script_id) on delete cascade,
  status text not null default 'queued' check (status in ('queued','in_progress','completed','failed')),
  generation_mode text not null default 'mcp' check (generation_mode in ('mcp','rest_api')),
  persona_variant text not null default 'A' check (persona_variant in ('A','B')),
  hf_request_id text,
  hf_raw jsonb not null default '{}'::jsonb,
  video_url text,
  r2_url text,
  duration_seconds numeric,
  consistency_pass boolean,
  error text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (client_id, script_id)
);

-- ============================================================
-- POSTS
-- ============================================================
create table if not exists posts (
  post_id bigserial primary key,
  client_id text not null references clients(client_id) on delete cascade,
  video_job_id bigint references video_jobs(video_job_id) on delete cascade,
  planned_publish_at timestamptz not null,
  posted_at timestamptz,
  platform text not null default 'tiktok',
  platform_publish_id text,
  metricool_post_id text,
  platform_status text not null default 'scheduled' check (platform_status in ('scheduled','uploading','processing','posted','failed')),
  perf_24h jsonb,
  perf_72h jsonb,
  error text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (client_id, video_job_id)
);

-- ============================================================
-- DM LEADS
-- ============================================================
create table if not exists dm_leads (
  lead_id bigserial primary key,
  client_id text not null references clients(client_id) on delete cascade,
  chatfuel_user_id text, -- replaces manychat_contact_id from original spec
  manychat_contact_id text, -- DEPRECATED 2026-05-04, kept null for backward compat
  tiktok_user_id text,
  trigger_source text check (trigger_source in ('comment','dm',null)), -- new field per Chatfuel
  keyword text,
  email text,
  consent boolean not null default false,
  double_opt_in_confirmed boolean not null default false,
  email_provider_subscriber_id text,
  payload jsonb not null default '{}'::jsonb,
  deleted_at timestamptz,
  created_at timestamptz not null default now()
);

-- ============================================================
-- EVENTS (observability log)
-- ============================================================
create table if not exists events (
  event_id bigserial primary key,
  client_id text,
  agent text,
  workflow text,
  level text not null default 'info' check (level in ('info','warning','error','critical')),
  message text not null,
  payload jsonb not null default '{}'::jsonb,
  resolved boolean not null default false,
  created_at timestamptz not null default now()
);

-- ============================================================
-- UPDATED_AT TRIGGER (apply to all tables with updated_at)
-- ============================================================
create or replace function set_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create trigger clients_updated_at before update on clients
  for each row execute function set_updated_at();
create trigger client_config_updated_at before update on client_config
  for each row execute function set_updated_at();
create trigger research_runs_updated_at before update on research_runs
  for each row execute function set_updated_at();
create trigger script_batches_updated_at before update on script_batches
  for each row execute function set_updated_at();
create trigger scripts_updated_at before update on scripts
  for each row execute function set_updated_at();
create trigger video_jobs_updated_at before update on video_jobs
  for each row execute function set_updated_at();
create trigger posts_updated_at before update on posts
  for each row execute function set_updated_at();

-- ============================================================
-- ROW LEVEL SECURITY — enable on all tables
-- ============================================================
alter table clients enable row level security;
alter table client_config enable row level security;
alter table schedules enable row level security;
alter table research_runs enable row level security;
alter table content_insights enable row level security;
alter table script_batches enable row level security;
alter table scripts enable row level security;
alter table video_jobs enable row level security;
alter table posts enable row level security;
alter table dm_leads enable row level security;
alter table events enable row level security;

-- Service role bypasses RLS by default (Supabase behavior).
-- Anon role: no access until SaaS auth policies are added.
-- Operator note: use service role key in n8n and all agent API calls.
-- When adding SaaS auth: add tenant-scoped policies using auth.uid() and a users->client_id mapping table.

-- ============================================================
-- INDEXES for common query patterns
-- ============================================================
create index if not exists idx_content_insights_client_week
  on content_insights (client_id, research_run_id);

create index if not exists idx_scripts_status
  on scripts (client_id, status, week_start);

create index if not exists idx_video_jobs_status
  on video_jobs (client_id, status);

create index if not exists idx_posts_status
  on posts (client_id, platform_status, planned_publish_at);

create index if not exists idx_events_created
  on events (client_id, level, created_at desc);

create index if not exists idx_research_runs_status
  on research_runs (client_id, status, week_start);

-- ============================================================
-- TEST INSERT — run after schema creation to verify
-- ============================================================
-- insert into clients (client_id, client_name, status) values ('c_test', 'Test Client', 'active');
-- select * from clients where client_id = 'c_test';
-- delete from clients where client_id = 'c_test';
