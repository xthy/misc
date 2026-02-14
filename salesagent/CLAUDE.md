# CLAUDE.md — B2B Sales Agent Project Guide

## Project Identity

- **Name**: B2B Sales Agent
- **Stage**: Pre-code — Playbook & Architecture design phase
- **Domain**: B2B Sales Process Automation for PE portfolio companies
- **Primary Language**: Korean (docs) + English (code, field names, prompts)

## Current State

이 프로젝트는 아직 **코드가 없는 설계 단계**입니다. 현재 자산은 전부 Markdown 문서:

- Playbook (영업 프로세스 표준, 방법론, 스크립트, 템플릿)
- Agent 아키텍처 설계 (BCG 5-Agent model 기반)
- CRM 스키마 설계 (Salesforce/HubSpot 대응)
- 프로젝트 스코프 & 로드맵

실제 CRM, 고객 데이터, LLM 연동은 아직 없습니다.

## Directory Structure

```
salesagent/
├── CLAUDE.md                          # 이 파일. 프로젝트 가이드.
├── agent.md                           # Agent 정의 (아키텍처, 역할, 원칙, 기술스택)
├── scope.md                           # 프로젝트 범위, 15-step 실행 계획, 성공 기준
├── crm/
│   └── schema.md                      # CRM 데이터 모델, Dashboard 5종, API 연동 스펙
└── playbook/
    ├── 00_sales_process_canon.md      # 7단계 영업 프로세스 표준 (Canon)
    ├── 01_icp_and_scoring.md          # ICP 3축 프레임워크 + Account Scoring + Tiering
    ├── 02_meddicc_guide.md            # MEDDICC 7요소 상세 (질문, CRM 필드, 점수 기준)
    ├── 03_call_scripts.md             # Cold call, Discovery, Demo, QBR 스크립트
    ├── 04_email_templates.md          # Outbound cadence + Follow-up + CS 이메일
    ├── 05_objection_handling.md       # 10대 반론 대응 가이드
    └── plays/
        ├── play_01_new_logo_outbound_t2t3.md
        ├── play_02_strategic_account_expansion_t1.md
        ├── play_03_renewal_rescue.md
        ├── play_04_cs_driven_upsell.md
        └── play_05_win_loss_analysis.md
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

### 코드 단계 진입 시 (향후)
- 첫 Agent PoC: Post-Call CRM Updater (Play 01의 Agent 파트 참조)
- Tech stack: n8n (workflow) + Claude/OpenAI API (LLM) + CRM API
- Agent prompt는 각 Play의 "Agent System Prompt 요약" 섹션에서 시작
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

| 순서 | 작업 | 선행 조건 |
|------|------|----------|
| 1 | 파일럿 포트폴리오사 선정 | PE Ops VP 의사결정 |
| 2 | ICP 기준값을 실제 고객 데이터로 검증 | 고객 데이터 접근 |
| 3 | CRM 인스턴스 접근 + 필드 매핑 | CRM admin 권한 |
| 4 | Agent PoC #1 빌드 (Post-Call Updater) | CRM API + LLM API 확보 |
| 5 | Playbook RAG 벡터화 | Vector DB 선정 (pgvector/Pinecone) |
