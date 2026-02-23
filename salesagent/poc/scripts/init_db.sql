-- B2B Sales Agent PoC — Database Initialization
-- pgvector extension + Playbook RAG table + MEDDICC extraction log

-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- ─────────────────────────────────────────────
-- Playbook RAG Store
-- Playbook 문서 청크를 벡터화하여 Agent가 참조
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS playbook_chunks (
    id              SERIAL PRIMARY KEY,
    source_file     TEXT NOT NULL,           -- e.g. 'playbook/02_meddicc_guide.md'
    section_title   TEXT,                    -- e.g. '## M: Metrics'
    chunk_text      TEXT NOT NULL,
    chunk_index     INTEGER NOT NULL,        -- 같은 파일 내 순서
    embedding       vector(1536),            -- text-embedding-3-small dimension
    metadata        JSONB DEFAULT '{}',
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Embedding similarity search index (IVFFlat)
CREATE INDEX IF NOT EXISTS idx_playbook_embedding
    ON playbook_chunks USING ivfflat (embedding vector_cosine_ops)
    WITH (lists = 10);

CREATE INDEX IF NOT EXISTS idx_playbook_source
    ON playbook_chunks (source_file);

-- ─────────────────────────────────────────────
-- MEDDICC Extraction Log
-- Agent가 추출한 MEDDICC 결과를 기록 (감사 추적)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS meddicc_extractions (
    id                  SERIAL PRIMARY KEY,
    opportunity_id      TEXT NOT NULL,           -- CRM Opportunity ID
    opportunity_name    TEXT,
    account_tier        TEXT CHECK (account_tier IN ('T1', 'T2', 'T3')),
    current_stage       TEXT,
    source_type         TEXT DEFAULT 'call_transcript',  -- call_transcript, email, meeting_note
    source_activity_id  TEXT,

    -- MEDDICC Scores (0-3)
    m_score             INTEGER CHECK (m_score BETWEEN 0 AND 3),
    e_score             INTEGER CHECK (e_score BETWEEN 0 AND 3),
    dc_score            INTEGER CHECK (dc_score BETWEEN 0 AND 3),
    dp_score            INTEGER CHECK (dp_score BETWEEN 0 AND 3),
    i_score             INTEGER CHECK (i_score BETWEEN 0 AND 3),
    c_champ_score       INTEGER CHECK (c_champ_score BETWEEN 0 AND 3),
    c_comp_score        INTEGER CHECK (c_comp_score BETWEEN 0 AND 3),
    composite_score     NUMERIC(5,2),

    -- Full extraction result (JSON)
    extraction_result   JSONB NOT NULL,

    -- Stage gate check
    stage_gate_passed   BOOLEAN,
    blocking_elements   JSONB DEFAULT '[]',

    -- Approval tracking
    approval_status     TEXT DEFAULT 'pending' CHECK (approval_status IN ('pending', 'approved', 'rejected', 'modified')),
    approved_by         TEXT,
    approved_at         TIMESTAMPTZ,
    modifications       JSONB DEFAULT '{}',

    -- LLM metadata
    model_used          TEXT DEFAULT 'gpt-4o',
    input_tokens        INTEGER,
    output_tokens       INTEGER,
    latency_ms          INTEGER,
    cost_usd            NUMERIC(8,6),

    created_at          TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_meddicc_opp
    ON meddicc_extractions (opportunity_id);

CREATE INDEX IF NOT EXISTS idx_meddicc_status
    ON meddicc_extractions (approval_status);

-- ─────────────────────────────────────────────
-- Lead Enrichment & Scoring Log
-- Lead Generation Agent가 수행한 계정 enrichment + ICP 스코어링 결과
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS lead_enrichment_log (
    id                  SERIAL PRIMARY KEY,
    account_id          TEXT,
    company_name        TEXT NOT NULL,
    domain              TEXT,

    -- Scores
    fit_score           NUMERIC(5,2),
    fit_grade           TEXT CHECK (fit_grade IN ('A', 'B', 'C', 'D')),
    intent_score        NUMERIC(5,2),
    engagement_score    NUMERIC(5,2),
    total_score         NUMERIC(5,2),
    action_grade        TEXT CHECK (action_grade IN ('Hot', 'Warm', 'Nurture', 'Watch', 'Excluded')),
    tier                TEXT CHECK (tier IN ('T1', 'T2', 'T3')),

    -- Full enrichment + scoring result (JSON)
    enrichment_result   JSONB NOT NULL,

    -- LLM metadata
    model_used          TEXT DEFAULT 'gpt-4o',
    input_tokens        INTEGER,
    output_tokens       INTEGER,
    cost_usd            NUMERIC(8,6),

    created_at          TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_lead_enrich_score
    ON lead_enrichment_log (total_score DESC);

CREATE INDEX IF NOT EXISTS idx_lead_enrich_grade
    ON lead_enrichment_log (action_grade);

CREATE INDEX IF NOT EXISTS idx_lead_enrich_company
    ON lead_enrichment_log (company_name);

-- ─────────────────────────────────────────────
-- Agent Execution Log
-- 모든 Agent 실행 이력 (비용, 성능 추적)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS agent_executions (
    id              SERIAL PRIMARY KEY,
    agent_name      TEXT NOT NULL,            -- 'qualification_agent', 'lead_gen_agent', etc.
    workflow_id     TEXT,                      -- n8n workflow ID
    execution_id    TEXT,                      -- n8n execution ID
    trigger_type    TEXT,                      -- 'webhook', 'schedule', 'manual'
    input_summary   TEXT,                      -- 입력 요약 (트랜스크립트 첫 200자 등)
    output_summary  TEXT,                      -- 출력 요약

    -- Performance
    status          TEXT DEFAULT 'running' CHECK (status IN ('running', 'success', 'error', 'timeout')),
    started_at      TIMESTAMPTZ DEFAULT NOW(),
    completed_at    TIMESTAMPTZ,
    duration_ms     INTEGER,

    -- Cost
    total_tokens    INTEGER,
    total_cost_usd  NUMERIC(8,6),

    -- Error tracking
    error_message   TEXT,
    error_step      TEXT,

    metadata        JSONB DEFAULT '{}'
);

CREATE INDEX IF NOT EXISTS idx_agent_exec_name
    ON agent_executions (agent_name, started_at DESC);
