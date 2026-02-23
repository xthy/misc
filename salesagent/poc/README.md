# B2B Sales Agent — PoC (Proof of Concept)

## Overview

3개의 PoC 워크플로우로 B2B Sales Agent 시스템의 핵심 기능을 검증합니다.

| PoC | 워크플로우 | 트리거 | Agent 역할 |
|-----|-----------|--------|-----------|
| **#1** | Post-Call CRM Updater | Webhook (콜 트랜스크립트) | Qualification Agent — MEDDICC 추출 |
| **#2** | Weekly Ops Report | Schedule (매주 월요일 08:00) | Ops Analyst — 파이프라인 분석 리포트 |
| **#3** | Lead Enrichment & ICP Scoring | Webhook (신규 계정) | Lead Gen Agent — ICP 3축 스코어링 |

## Prerequisites

- Docker & Docker Compose
- OpenAI API key (`gpt-4o`)
- (Optional) Slack Webhook URL for notifications

## Quick Start

```bash
# 1. Setup
chmod +x scripts/setup.sh
./scripts/setup.sh

# 2. API 키 설정
vim .env   # OPENAI_API_KEY 입력

# 3. n8n 접속
open http://localhost:5678
# User: admin / Password: salesagent

# 4. 워크플로우 Import
# n8n UI → Import → workflows/*.json 파일 업로드

# 5. n8n Credentials 설정
# - OpenAI API (GPT-4o)
# - PostgreSQL (localhost:5432, salesagent/salesagent_dev)
# - Slack Webhook (optional)

# 6. 워크플로우 활성화 후 테스트
./scripts/test_webhook.sh           # PoC #1
./scripts/test_ops_report.sh        # PoC #2
./scripts/test_lead_enrich.sh       # PoC #3
```

## Directory Structure

```
poc/
├── README.md                  # 이 파일
├── .env.example               # 환경 변수 템플릿
├── docker-compose.yml         # n8n + PostgreSQL/pgvector
├── workflows/
│   ├── post_call_crm_updater.json   # PoC #1 — MEDDICC 추출
│   ├── weekly_ops_report.json       # PoC #2 — 주간 리포트
│   └── lead_enrichment_scorer.json  # PoC #3 — 리드 스코어링
├── prompts/
│   ├── meddicc_extractor.md         # PoC #1 시스템 프롬프트
│   ├── weekly_ops_report.md         # PoC #2 시스템 프롬프트
│   └── lead_enrichment_scorer.md    # PoC #3 시스템 프롬프트
├── fixtures/
│   ├── sample_transcript.json       # PoC #1 테스트 데이터 (한국어 콜)
│   ├── sample_pipeline_data.json    # PoC #2 테스트 데이터
│   └── sample_new_account.json      # PoC #3 테스트 데이터
└── scripts/
    ├── init_db.sql                  # DB 초기화 (pgvector + 4 tables)
    ├── setup.sh                     # 최초 설정 스크립트
    ├── test_webhook.sh              # PoC #1 테스트
    ├── test_ops_report.sh           # PoC #2 테스트
    ├── test_lead_enrich.sh          # PoC #3 테스트
    └── ingest_playbook_rag.py       # Playbook RAG 벡터화 스크립트
```

## Architecture

```
                    ┌─────────────────────┐
                    │   n8n (port 5678)   │
                    │   Workflow Runtime   │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                     │
   PoC #1: Webhook      PoC #2: Schedule     PoC #3: Webhook
   /webhook/post-call   매주 월 08:00 KST    /webhook/lead-enrich
          │                    │                     │
          ▼                    ▼                     ▼
   ┌─────────────┐    ┌──────────────┐    ┌──────────────────┐
   │ OpenAI API  │    │  OpenAI API  │    │    OpenAI API     │
   │ MEDDICC 추출 │    │  리포트 생성  │    │  Enrichment + ICP │
   └──────┬──────┘    └──────┬───────┘    └────────┬─────────┘
          │                  │                      │
          ▼                  ▼                      ▼
   ┌─────────────────────────────────────────────────────┐
   │           PostgreSQL + pgvector (port 5432)          │
   │                                                      │
   │  playbook_chunks       — RAG 벡터 스토어             │
   │  meddicc_extractions   — MEDDICC 추출 이력           │
   │  agent_executions      — Agent 실행 로그             │
   │  lead_enrichment_log   — 리드 스코어링 이력          │
   └──────────────────┬──────────────────────────────────┘
                      │
                      ▼
               ┌────────────┐
               │   Slack     │
               │  (Optional) │
               └────────────┘
```

## Database Tables

| Table | PoC | Purpose |
|-------|-----|---------|
| `playbook_chunks` | 공통 | Playbook 문서 벡터 임베딩 (RAG) |
| `meddicc_extractions` | #1 | MEDDICC 추출 결과 감사 추적 |
| `agent_executions` | 공통 | Agent 실행 이력 (비용, 성능) |
| `lead_enrichment_log` | #3 | ICP 스코어링 결과 이력 |

## Operations

```bash
# 로그 확인
docker compose logs -f

# 서비스 중지
docker compose down

# 데이터 포함 초기화 (주의!)
docker compose down -v

# DB 직접 접속
docker compose exec postgres psql -U salesagent
```

## Cost Estimation

| PoC | Trigger | LLM Tokens/Run | Est. Cost/Run |
|-----|---------|-------------------|---------------|
| #1 | Per call | ~3K input + ~2K output | ~$0.02 |
| #2 | Weekly | ~5K input + ~3K output | ~$0.04 |
| #3 | Per lead | ~2K input + ~2K output | ~$0.02 |

> GPT-4o 기준 ($2.50/M input, $10/M output). 실제 비용은 트랜스크립트 길이, 파이프라인 규모에 따라 변동.

## Next Steps

1. `.env`에 OpenAI API 키 설정 후 PoC #1 실행 검증
2. CRM API 연동 (Salesforce/HubSpot n8n 노드 설정)
3. Playbook 벡터화: `python3 scripts/ingest_playbook_rag.py` (878 chunks, ~160K tokens)
4. Production: n8n → CrewAI + FastAPI 전환 (agent.md 참조)
