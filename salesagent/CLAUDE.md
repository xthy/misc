# CLAUDE.md — B2B Sales Agent Project Guide

## Project Identity

- **Name**: B2B Sales Agent
- **Stage**: Pre-code — Playbook & Architecture design phase
- **Domain**: B2B Sales Process Automation for PE portfolio companies
- **Primary Language**: Korean (docs) + English (code, field names, prompts)

## Current State

이 프로젝트는 **설계 완료 + PoC 스캐폴딩 단계**입니다.

- Playbook (영업 프로세스 표준, 방법론, 스크립트, 템플릿) — 9개 문서 + 7개 Play
- Agent 아키텍처 설계 (BCG 5-Agent model 기반) — 5개 Agent 상세 프롬프트 완료
- CRM 스키마 설계 (Salesforce/HubSpot 대응)
- 산업 리서치 & 벤치마크 — KPI, AI 사례, 기술스택 비교
- Agent PoC 3종 코드 스캐폴딩 (n8n + Claude API + pgvector)
- 프로젝트 스코프 & 로드맵

실제 CRM, 고객 데이터, LLM 연동은 아직 없습니다. PoC 실행에는 API 키와 Docker가 필요합니다.

## Directory Structure

```
salesagent/
├── CLAUDE.md                          # 이 파일. 프로젝트 가이드.
├── agent.md                           # Agent 정의 (아키텍처, 역할, 원칙, 기술스택)
├── scope.md                           # 프로젝트 범위, 15-step 실행 계획, 성공 기준
├── todo.md                            # 작업 목록 및 다음 작업 추천
├── agent/                             # Agent별 상세 프롬프트 & 스펙
│   ├── 01_qualification_agent.md      # MEDDICC 추출, 딜 스코어링, stage gate 검증
│   ├── 02_orchestration_agent.md      # 라우팅, 핸드오프, 에스컬레이션, 우선순위 관리
│   ├── 03_lead_generation_agent.md    # ICP 스코어링, 리드 enrichment, 아웃바운드 메시지
│   ├── 04_deal_conversion_agent.md    # 제안서, 가격 협상, 계약 검토, 온보딩
│   └── 05_customer_success_agent.md   # Health Score, 리스크 감지, expansion, QBR
├── crm/
│   └── schema.md                      # CRM 데이터 모델, Dashboard 5종, API 연동 스펙
├── poc/                               # Agent PoC 3종 코드 스캐폴딩
│   ├── README.md                      # PoC 가이드 (Quick Start, Architecture, Cost)
│   ├── docker-compose.yml             # n8n + PostgreSQL/pgvector
│   ├── .env.example                   # API 키 템플릿
│   ├── workflows/
│   │   ├── post_call_crm_updater.json # PoC #1: MEDDICC 추출 (Webhook → Claude → DB → Slack)
│   │   ├── weekly_ops_report.json     # PoC #2: 주간 파이프라인 리포트 (Schedule → SQL → Claude → Slack)
│   │   └── lead_enrichment_scorer.json # PoC #3: ICP 3축 스코어링 (Webhook → Claude → DB → Slack)
│   ├── prompts/
│   │   ├── meddicc_extractor.md       # PoC #1 시스템 프롬프트
│   │   ├── weekly_ops_report.md       # PoC #2 시스템 프롬프트
│   │   └── lead_enrichment_scorer.md  # PoC #3 시스템 프롬프트
│   ├── scripts/
│   │   ├── init_db.sql                # DB 초기화 (pgvector + 4 tables)
│   │   ├── setup.sh                   # 초기 셋업 스크립트
│   │   ├── test_webhook.sh            # PoC #1 테스트
│   │   ├── test_ops_report.sh         # PoC #2 테스트
│   │   └── test_lead_enrich.sh        # PoC #3 테스트
│   └── fixtures/
│       ├── sample_transcript.json     # PoC #1 테스트 데이터 (한국어 콜)
│       ├── sample_pipeline_data.json  # PoC #2 테스트 데이터 (18 deals)
│       └── sample_new_account.json    # PoC #3 테스트 데이터 (CloudMetrics Inc.)
├── research/                          # 산업 리서치 & 벤치마크
│   ├── 01_kpi_benchmarks.md           # 산업별 영업 KPI 벤치마크 (Win Rate, ACV, Cycle 등)
│   ├── 02_ai_sales_agent_cases.md     # AI Sales Agent 실제 도입 사례 & 성과 분석
│   └── 03_tech_stack_comparison.md    # n8n vs Zapier vs LangChain 기술스택 비교
└── playbook/
    ├── 00_sales_process_canon.md      # 7단계 영업 프로세스 표준 (Canon)
    ├── 01_icp_and_scoring.md          # ICP 3축 프레임워크 + Account Scoring + Tiering
    ├── 02_meddicc_guide.md            # MEDDICC 7요소 상세 (질문, CRM 필드, 점수 기준)
    ├── 03_call_scripts.md             # Cold call, Discovery, Demo, QBR 스크립트
    ├── 04_email_templates.md          # Outbound cadence + Follow-up + CS 이메일
    ├── 05_objection_handling.md       # 10대 반론 대응 가이드
    ├── 06_competitive_battle_card.md  # 경쟁사 Battle Card 템플릿 + 예시
    ├── 07_pricing_discount_matrix.md  # 가격 체계, 할인 승인 매트릭스, 번들 규칙
    ├── 08_sales_onboarding_curriculum.md # 신규 Rep 30/60/90일 온보딩 커리큘럼
    └── plays/
        ├── play_01_new_logo_outbound_t2t3.md
        ├── play_02_strategic_account_expansion_t1.md
        ├── play_03_renewal_rescue.md
        ├── play_04_cs_driven_upsell.md
        ├── play_05_win_loss_analysis.md
        ├── play_06_inbound_lead_handling.md
        └── play_07_partner_channel_sales.md
```

## Key Concepts

### 7-Stage Sales Canon
이 프로젝트의 뼈대. 모든 Play, Agent, CRM 필드, KPI가 이 7단계에 매핑됨:
1. Market Strategy → 2. Account Planning → 3. Pipeline Generation →
4. Pipeline Progression → 5. Close & Onboard → 6. Retention & Growth →
7. Ops & Analytics → (feedback loop)

### Account Tier Model
모든 설계의 핵심 축. Agent 자동화 수준이 Tier에 따라 달라짐:
- **T1 Strategic**: Human-led. Agent는 보조만.
- **T2 Core**: Co-pilot. Agent 초안 → 사람 검토/발송.
- **T3 Long-tail**: AI-led. Agent 자율 실행, 사람은 예외만 처리.

### MEDDICC
딜 적격성 검증 프레임워크. CRM의 Opportunity 필드와 1:1 매핑됨:
Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion, Competition

### Play 구조
모든 Play는 5-블록 구조: **Input → Process → Output → Metric → Tool/Agent**
이 구조가 나중에 Agent Spec으로 직접 변환됨.

## Document Conventions

### 문서 작성 규칙
- 본문은 **한국어**, 필드명/변수명/프롬프트는 **영어**
- 표(table)를 적극 활용 — 긴 문장보다 구조화된 정보 선호
- 각 Play에는 Agent System Prompt 요약이 포함됨 (코드 블록)
- CRM 필드명은 Salesforce API 네이밍 컨벤션 (`Field_Name__c`)

### 파일 넘버링
- `playbook/` 하위 파일은 `00_`, `01_` ... 순서로 넘버링
- `plays/` 하위는 `play_01_`, `play_02_` ... 순서
- 새 문서 추가 시 기존 넘버링 뒤에 이어서 부여

### Placeholder 표기
문서 내 `[brackets]`로 표기된 부분은 실제 데이터로 교체 필요한 placeholder:
- `[Company Name]` → 실제 회사명
- `[trigger event]` → Agent가 자동 추출할 이벤트
- `[peer company]` → 실제 고객 사례

## Design Principles

1. **Playbook-first**: Agent 코드 전에 반드시 해당 Play 문서가 존재해야 함
2. **CRM-native**: Agent의 모든 읽기/쓰기는 CRM을 통해야 함 (shadow DB 금지)
3. **Graduated autonomy**: T3 → T2 → T1 순으로 자동화 확대
4. **Measurable**: 모든 Agent 행동은 KPI에 연결. "있으면 좋겠다" 자동화 금지
5. **Portfolio-portable**: 특정 회사에 하드코딩하지 않음. Canon 구조로 범용성 유지

## Working with This Project

### 문서 수정 시
- 7-Stage Canon (`00_sales_process_canon.md`)은 다른 모든 문서의 근간이므로 변경 시 영향 범위를 확인
- CRM 필드를 추가/변경하면 `crm/schema.md`와 해당 Play 문서 양쪽을 동기화
- Play의 Agent System Prompt를 변경하면 `agent.md`의 Agent 역할 테이블도 확인

### 새 Play 추가 시
1. `playbook/plays/play_0N_[name].md` 생성
2. 5-블록 구조(Input → Process → Output → Metric → Tool/Agent) 준수
3. CRM 필수 필드가 있으면 `crm/schema.md`에 추가
4. `scope.md`의 Phase 해당 위치에 반영

### PoC 실행 시
- **PoC #1 스캐폴딩 완료**: `poc/` 디렉토리 참조
- **실행 방법**: `cd poc && ./scripts/setup.sh` (Docker 필요)
- **Tech stack**: n8n (self-hosted Docker) + OpenAI GPT-4o API + CRM n8n nodes + pgvector + Helicone
- **Production 전환**: CrewAI + n8n + pgvector + Langfuse (상세: `research/03_tech_stack_comparison.md` §7)
- Agent prompt는 `agent/` 하위 상세 스펙에서 시작 (PoC용 축약 버전: `poc/prompts/`)
- RAG 구축 시 이 playbook 문서들이 벡터 DB에 임베딩될 소스

## References

이 프로젝트의 설계 기반이 된 핵심 자료:
- **BCG**: How AI Agents Will Transform B2B Sales (5-Agent 모델)
- **Revenue Architecture** (Jacco van der Kooij): Bow-Tie 수익 모델
- **MEDDICC** (Andy Whyte): Enterprise 딜 qualification 표준
- **Predictable Revenue** (Aaron Ross): Outbound SDR 모델, 역할 분리
- **Gap Selling** (Keenan): Current State → Future State → Gap 프레임워크
- **SPIN Selling** (Neil Rackham): S-P-I-N 질문 구조
- **Salesforce Playbook Guide**: Play 문서 구조의 베이스라인

## Next Steps (현재 기준)

| 순서 | 작업 | 선행 조건 | 상태 |
|------|------|----------|------|
| 1 | PoC #1 실행 (Post-Call CRM Updater) | OpenAI API 키 + Docker | 스캐폴딩 완료 (`poc/`) |
| 2 | 파일럿 포트폴리오사 선정 | PE Ops VP 의사결정 | 대기 |
| 3 | ICP 기준값을 실제 고객 데이터로 검증 | 고객 데이터 접근 | 대기 |
| 4 | CRM 인스턴스 접근 + 필드 매핑 | CRM admin 권한 | 대기 |
| 5 | PoC #2-3 빌드 (Ops Report + Lead Enrichment) | PoC #1 검증 완료 | 대기 |
| 6 | Playbook RAG 벡터화 | pgvector 구축 (PoC Docker에 포함) | 대기 |
