# B2B Sales Agent — Progress Report
**Date**: 2026-02-14
**Session**: Initial project setup

---

## 한 줄 요약

> 리서치 자료를 기반으로 **Playbook 전체 + CRM 스키마 + Agent 아키텍처**를 best practice 기본값으로 완성함. 코드는 아직 없고, 실제 데이터 투입 전 설계 단계.

---

## 완료된 작업

### 1. 프로젝트 뼈대 (2건)

| 파일 | 내용 | 줄 수 |
|------|------|-------|
| `agent.md` | BCG 5-Agent 아키텍처, Tier별 Human-AI 역할, 기술스택, 거버넌스 원칙 | 151 |
| `scope.md` | 5-Phase 로드맵, 15-step 실행 계획, 성공 기준, 리스크, In/Out of Scope | 174 |

### 2. Playbook Canon & Framework (3건)

| 파일 | 내용 | 줄 수 |
|------|------|-------|
| `playbook/00_sales_process_canon.md` | **7단계 영업 프로세스 표준** — Stage 정의, Entry/Exit criteria, KPI, Agent 역할, Cross-stage 규칙 (Handoff, Escalation, Data Hygiene) | 445 |
| `playbook/01_icp_and_scoring.md` | **ICP 3축 프레임워크** (Firmographic 40% + Technographic 30% + Needs 30%) + Tiered Weighted Scoring 모델 + T1/T2/T3 분류 기준 + Agent Spec | 240 |
| `playbook/02_meddicc_guide.md` | **MEDDICC 7요소 상세 가이드** — 요소별 Discovery 질문, CRM 필드 매핑, Scoring Rubric (0-3), Composite Score 계산, Stage별 최소 기준 | 372 |

### 3. Top 5 Plays (5건)

모든 Play는 **Input → Process → Output → Metric → Tool/Agent** 5-블록 구조:

| 파일 | Play | 핵심 내용 | 줄 수 |
|------|------|----------|-------|
| `plays/play_01_new_logo_outbound_t2t3.md` | 신규 고객 발굴 | 14일 멀티채널 cadence, SDR→AE handoff, T2 co-pilot / T3 AI-led 구분, 이메일 템플릿 3종 포함 | 272 |
| `plays/play_02_strategic_account_expansion_t1.md` | T1 계정 확장 | White-space 분석 자동화, QBR 연동, Stakeholder mapping, Land & Expand 전략 | 213 |
| `plays/play_03_renewal_rescue.md` | 갱신 리스크 구출 | Health Score 기반 자동 감지, Red/Yellow 프로토콜, Save Plan 메뉴, 결과 평가 루프 | 227 |
| `plays/play_04_cs_driven_upsell.md` | CS→AE Expansion | Signal 감지 (Usage spike, NPS, 새 부서), CS Qualification → AE Handoff 구조화 문서 | 212 |
| `plays/play_05_win_loss_analysis.md` | Win/Loss 분석 | Per-deal debrief + Buyer interview + 분기 집계 분석, Insight→Action 전환, Playbook/Agent 업데이트 루프 | 270 |

### 4. 실전 스크립트 & 템플릿 (3건)

| 파일 | 내용 | 줄 수 |
|------|------|-------|
| `playbook/03_call_scripts.md` | Cold call 스크립트, SPIN+Gap Selling 통합 Discovery 질문 플로우, Demo 스크립트, QBR 스크립트, Agent Pre/Post-call 자동화 | 260 |
| `playbook/04_email_templates.md` | Outbound 14일 cadence 5종, 미팅 확인/Follow-up, Proposal, CS 온보딩/Health check/QBR/Renewal 이메일, Trigger→Problem 매핑 테이블 | 386 |
| `playbook/05_objection_handling.md` | 10대 B2B 반론 (가격, 경쟁, 타이밍, 권한, 기능 등) 상세 대응 프레임, Agent 실시간 지원 구상 | 278 |

### 5. CRM & 인프라 (1건)

| 파일 | 내용 | 줄 수 |
|------|------|-------|
| `crm/schema.md` | Account/Contact/Opportunity/Activity/Case 오브젝트 전체 필드 정의, MEDDICC 커스텀 필드, Opp Stage 매핑, Dashboard 5종 스펙, Validation Rule, Auto-Update Rule, API 연동 포인트 | 357 |

### 6. 프로젝트 가이드 (2건)

| 파일 | 내용 | 줄 수 |
|------|------|-------|
| `CLAUDE.md` | 프로젝트 컨텍스트, 디렉토리 구조, 핵심 개념, 문서 컨벤션, 수정/추가 규칙, 코드 진입 가이드 | 132 |
| `progress.md` | 이 파일 | - |

---

## 전체 현황

```
총 파일: 16개 (progress.md 포함)
총 분량: ~3,900줄 (중복 제외 실 라인)
소요 시간: 1 세션
데이터 소스: 사용자 리서치 자료 (BCG, KPMG, MEDDICC 등) + best practice 지식
```

---

## 현재 위치 (scope.md 15-step 기준)

```
Step  What                           Status
───────────────────────────────────────────────────
 1    Map current sales process       ✅ Done (best practice 기반, 실제 프로세스는 미반영)
 2    Define 7-stage canon            ✅ Done (00_sales_process_canon.md)
 3    Build ICP + Tiering model       ✅ Done (01_icp_and_scoring.md)
 4    Write Top 5 Plays               ✅ Done (plays/ 5건)
 5    Design CRM schema               ✅ Done (crm/schema.md)
 6    Build CRM dashboards            📝 스펙 작성 완료, 실제 구축은 미진행
 7    Set up n8n + LLM infra          ⬜ Not started
 8    Build Agent PoC #1              ⬜ Not started
 9    Build Agent PoC #2              ⬜ Not started
10    Build Agent PoC #3              ⬜ Not started
11    Vectorize playbook (RAG)        ⬜ Not started
12    User testing & iteration        ⬜ Not started
13    T3 autonomous outbound pilot    ⬜ Not started
14    Portfolio rollout planning      ⬜ Not started
15    Deploy + monitor                ⬜ Not started
```

**진행률**: Step 1-5 완료 + Step 6 스펙 완료 = **설계 단계 100% / 전체 ~35%**

---

## 남은 작업

### 🔴 Blocker: 실제 데이터 필요 (Step 6 이후 진행 전 필수)

| 필요 데이터 | 용도 | 없으면 |
|-------------|------|--------|
| **파일럿 포트폴리오사** 선정 | 모든 커스터마이징의 대상 | 범용 template에서 전진 불가 |
| **실제 고객 리스트** (Top 20+) | ICP 기준값 검증, Scoring 가중치 백테스트 | Scoring이 이론적 수준에 머무름 |
| **CRM 인스턴스 접근** | 필드 매핑, Dashboard 구축, API 연동 | Agent가 읽고 쓸 곳이 없음 |
| **콜 녹음/트랜스크립트** | Post-Call Agent PoC의 입력 데이터 | 첫 Agent를 만들 수 없음 |
| **LLM API 키** (Claude/OpenAI) | Agent의 두뇌 | 코드 작성 불가 |
| **n8n 인스턴스** (또는 대안) | Workflow 오케스트레이션 | Agent 실행 환경 없음 |

### 🟡 데이터 없이도 가능한 작업

| 작업 | 설명 | 의존성 |
|------|------|--------|
| 추가 Play 작성 | 현재 5개 외 추가 (예: Partner Channel Play, Inbound Handling) | 없음 |
| Competitive Battle Card 템플릿 | 경쟁사별 강/약점 + 대응 전략 문서 구조 | 없음 |
| Agent System Prompt 상세화 | 각 Agent의 전체 프롬프트 작성 (few-shot 예시 포함) | 없음 |
| Pricing/Discount Matrix 템플릿 | 할인 승인 체계 상세 문서 | 없음 |
| Sales Onboarding Curriculum | 신규 Rep 온보딩 교육 과정 설계 | 없음 |
| KPI Benchmark 조사 | 산업별/규모별 영업 KPI 벤치마크 수집 | Web research 필요 |

### 🟢 데이터 확보 후 즉시 가능한 작업

| 작업 | 선행 조건 | 예상 산출물 |
|------|----------|-----------|
| ICP 기준값 커스터마이징 | 실제 고객 데이터 | 검증된 Scoring 모델 |
| CRM 필드 실제 구축 | CRM admin 접근 | 라이브 CRM 스키마 |
| Dashboard 구축 | CRM + 데이터 | 5종 대시보드 라이브 |
| Agent PoC #1 (Post-Call Updater) | CRM API + LLM API + 콜 트랜스크립트 | 작동하는 첫 Agent |
| Playbook RAG 벡터화 | Vector DB + 현재 문서들 | Agent가 참조 가능한 지식 베이스 |

---

## 문서 간 관계도

```
                    scope.md (전체 로드맵)
                        │
                    agent.md (아키텍처)
                        │
            ┌───────────┼───────────┐
            │           │           │
    00_canon.md    crm/schema.md  CLAUDE.md
    (7단계 표준)    (데이터 모델)   (프로젝트 가이드)
            │           │
    ┌───────┼─────┐     │
    │       │     │     │
 01_icp  02_meddicc  03~05_scripts
 (스코어링) (자격검증)   (실전 도구)
    │       │
    └───┬───┘
        │
   plays/ (5건)
   (실행 플레이북)
```

- `00_canon.md`을 바꾸면 → plays, crm/schema, agent.md 모두 영향
- `crm/schema.md`의 필드를 바꾸면 → 해당 Play의 CRM 섹션 동기화 필요
- Play 추가 시 → `scope.md`, `CLAUDE.md` 디렉토리 구조 업데이트

---

## 권장 다음 액션

| 우선순위 | 액션 | 결정 주체 |
|---------|------|----------|
| **1** | 파일럿 포트폴리오사 선정 | PE Ops VP |
| **2** | CRM 접근 권한 확보 (Salesforce or HubSpot) | IT/Admin |
| **3** | LLM API 키 확보 (Claude API 또는 OpenAI) | 기술팀 |
| **4** | 기존 문서 리뷰 → 실제 영업 프로세스와 gap 식별 | Sales Leadership |
| **5** | 콜 녹음 데이터 소스 확인 (Gong/Chorus/자체) | Sales Ops |
