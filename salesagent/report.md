# B2B Sales Agent — 프로젝트 종합 보고서

**작성일**: 2026-03-09
**상태**: 설계 완료 + PoC 스캐폴딩
**대상**: 경영진 + 기술팀 (하이브리드)

---

## 목차

1. [Executive Summary](#1-executive-summary)
2. [프로젝트 개요](#2-프로젝트-개요)
3. [7-Stage Sales Canon](#3-7-stage-sales-canon)
4. [Playbook 체계](#4-playbook-체계)
5. [Agent 아키텍처](#5-agent-아키텍처)
6. [CRM 데이터 모델](#6-crm-데이터-모델)
7. [기술 스택 & PoC](#7-기술-스택--poc)
8. [산업 벤치마크 & 사례](#8-산업-벤치마크--사례)
9. [로드맵 & Next Steps](#9-로드맵--next-steps)
10. [부록](#부록)

---

## 1. Executive Summary

### 프로젝트 목적

PE 포트폴리오사의 B2B 영업 프로세스를 표준화하고, AI Agent 시스템으로 자동화하여 **영업 생산성 3배 향상**과 **파이프라인 속도 30% 개선**을 달성한다.

### 범위

- 7단계 영업 프로세스 표준(Sales Canon) 수립
- BCG 5-Agent 모델 기반 AI Agent 아키텍처 설계
- 9개 Playbook 문서 + 7개 Play 작성
- CRM 데이터 모델(Salesforce/HubSpot 호환) 설계
- Agent PoC 3종 스캐폴딩(n8n + Claude API + pgvector)

### 현재 상태

Phase 1-2(Foundation + Playbook) 완료, Phase 3(CRM) 설계 완료, Phase 4(Agent PoC) 스캐폴딩 완료. 실제 CRM 연동과 LLM API 실행은 미착수.

### 핵심 성과 지표

| 메트릭 | 목표 | 시점 | 벤치마크 대비 |
|--------|------|------|--------------|
| T3 계정 커버리지 | 100% (현 ~30%) | Month 12 | 업계 평균 대비 3x |
| 계정/rep | 현재 대비 3x | Month 12 | — |
| CRM MEDDICC 완성도 | >80% | Month 9 | 업계 평균 40-50% |
| 파이프라인 속도 | +30% | Month 12 | 상위 25% 수준 |
| Rep 행정업무 절감 | 10+ hrs/week | Month 9 | AI 도입사 평균 5-8hrs |
| Post-call CRM 업데이트율 | >90% (24hr 내) | Month 6 | 현재 업계 ~30% |
| 예측 정확도 | <15% 오차 | Month 12 | 업계 평균 20-30% 오차 |

### 주요 산출물 요약

| 카테고리 | 산출물 | 수량 |
|----------|--------|------|
| Playbook | 영업 프로세스 문서 | 9개 문서 |
| Plays | 실행 Play | 7개 Play |
| Agent Spec | Agent 상세 프롬프트 | 5개 Agent |
| CRM | 데이터 모델 + Dashboard | 5 Object + 5 Dashboard |
| PoC | Agent PoC 스캐폴딩 | 3종 (n8n workflow) |
| Research | 산업 리서치 | 3개 보고서 |

---

## 2. 프로젝트 개요

### 배경 & 필요성

PE 포트폴리오사들은 공통적으로 다음의 영업 운영 과제를 겪고 있다:

- **프로세스 비표준화**: 포트폴리오사마다 영업 방법론이 다르고, cross-portfolio 벤치마킹 불가
- **데이터 사일로**: CRM 데이터 품질 낮음 (MEDDICC 필드 완성도 평균 40-50%), 의사결정 근거 부재
- **리소스 비효율**: AE/SDR이 행정 업무(데이터 입력, 리서치, 리포트)에 과다 시간 소비
- **T3 Long-tail 방치**: 전체 계정의 60-70%를 차지하는 소규모 계정이 체계적 관리 없이 방치

AI Agent 시스템은 이 네 가지를 동시에 해결한다: 표준 프로세스를 코드화하고, CRM 데이터를 자동 보강하며, 반복 업무를 자동화하고, T3 계정을 AI가 자율 관리한다.

### 프로젝트 범위

| 구분 | In Scope | Out of Scope |
|------|----------|-------------|
| **프로세스** | 7-Stage Sales Canon, MEDDICC, 7 Plays | 마케팅 자동화, PLG |
| **시스템** | CRM 연동(SF/HS), AI Agent, RAG | 커스텀 CRM 개발, 음성 AI(초기) |
| **대상** | B2B Sales-led 모델 | Self-serve, B2C |
| **자동화** | 데이터 입력, 리서치, 리포트, T3 아웃바운드 | 계약 자동 체결, 보상 설계 |

### 5-Phase 로드맵

```
Phase 1 (M1-3)     Phase 2 (M3-5)     Phase 3 (M4-6)     Phase 4 (M5-9)     Phase 5 (M9-12+)
Foundation       → Playbook Doc    → CRM Data Model → Agent PoC Build → Scale & Deploy
                                                            │
Sales Canon         Top 5 Plays        CRM Schema          PoC #1-3            T3 Autonomous
ICP Framework       Call Scripts        Dashboards          Playbook RAG        Portfolio Rollout
Account Tiering     Email Templates     Data Quality        System Prompts      Monitoring
KPI Set             MEDDICC Guide       Integration Map     User Testing        Governance

────────────────────────────────────────────────────────────────────────────────────────────
[████████████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]
Phase 1-2 완료 ────────────────────────── Phase 3 설계 완료 ── Phase 4 스캐폴딩 완료
                                                                현재 위치 ▲
```

### 성공 기준

| # | 메트릭 | 목표 | 시점 | 측정 방법 |
|---|--------|------|------|----------|
| 1 | T3 계정 커버리지 | 100% | Month 12 | CRM Activity 기록 기준 |
| 2 | 계정/rep 비율 | 3x 현재 | Month 12 | CRM Account Assignment |
| 3 | MEDDICC 완성도 | >80% | Month 9 | CRM 필드 채움률 |
| 4 | 파이프라인 속도 | +30% | Month 12 | Sales Velocity 공식 |
| 5 | 행정업무 절감 | 10+ hrs/week | Month 9 | Rep 서베이 + Activity 로그 |
| 6 | Post-call 업데이트율 | >90% (24hr) | Month 6 | CRM 타임스탬프 |
| 7 | 예측 정확도 | <15% 오차 | Month 12 | Forecast vs Actual |

---

## 3. 7-Stage Sales Canon

### 개요

7-Stage Sales Canon은 PE 포트폴리오 전체에 적용되는 B2B 영업 프로세스 표준이다. 모든 Play, Agent, CRM 필드, KPI가 이 7단계에 매핑된다.

### 프로세스 흐름도

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Stage 1  │───▶│ Stage 2  │───▶│ Stage 3  │───▶│ Stage 4  │
│ Market   │    │ Account  │    │ Pipeline │    │ Pipeline │
│ Strategy │    │ Planning │    │   Gen    │    │Progression│
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                                                      │
┌──────────┐    ┌──────────┐    ┌──────────┐          │
│ Stage 7  │◀───│ Stage 6  │◀───│ Stage 5  │◀─────────┘
│ Ops &    │    │Retention │    │ Close &  │
│Analytics │    │ & Growth │    │ Onboard  │
└──────────┘    └──────────┘    └──────────┘
      │
      └──────────▶ (Feedback Loop → Stage 1)
```

### 각 단계별 상세

| Stage | 이름 | 목적 | 핵심 활동 | Exit Criteria |
|-------|------|------|----------|--------------|
| **1** | Market Strategy | "누구에게, 어떤 방식으로 팔 것인가" 확정 | ICP 정의, 시장 세분화, Territory 설계, Coverage Model | ICP 문서 승인, Target Account List 배포 |
| **2** | Account Planning | 개별 계정 전략 수립, 자원 배분 우선순위 결정 | Account Enrichment, Tier 분류, Relationship Map, Account Plan | Tier 분류 완료, T1/T2 Account Plan 승인 |
| **3** | Pipeline Generation | 적격 리드 생성 및 SQL 전환 | Outbound 시퀀스, 인바운드 응대, 이벤트, CS expansion signal | SQL 기준 충족, Discovery meeting 확보 |
| **4** | Pipeline Progression | 파이프라인 기회를 체계적으로 진행 (MEDDICC 기반) | Discovery, Qualification, Demo, Technical Validation | MEDDICC 4+ 필드 Green, 의사결정 일정 확인 |
| **5** | Close & Onboard | 계약 체결 및 가치 실현 착수 | Proposal, 가격 협상, 계약 검토, 핸드오프 | 계약 서명, 온보딩 킥오프 완료 |
| **6** | Retention & Growth | 기존 고객 유지 및 확장 | Health Score 모니터링, QBR, Renewal, Expansion | GRR >90%, NRR >110% |
| **7** | Ops & Analytics | 데이터 기반 의사결정, 프로세스 개선 | 파이프라인 리포트, 예측, Win/Loss 분석 | 주간 리포트 발행, Playbook 업데이트 |

### Stage별 KPI

| Stage | 핵심 KPI | 목표 |
|-------|---------|------|
| 1 | TAM Coverage / ICP Match Rate | >60% / >40% |
| 2 | Account Data Completeness / Tier Coverage | >80% / T1 100%, T2 >80% |
| 3 | Meetings Booked / SQL Conversion Rate | 12-18/month, >25% |
| 4 | Stage Conversion Rate / MEDDICC Score | >40% S1→S2, 평균 18+ |
| 5 | Win Rate / Sales Cycle Length | >30%, <90일 |
| 6 | GRR / NRR / Health Score | >90%, >110%, 평균 >75 |
| 7 | Forecast Accuracy / Report Cadence | <15% 오차, 주간 발행 |

### Agent 매핑

| Stage | 담당 Agent | 자동화 수준 |
|-------|-----------|------------|
| 1 | Lead Generation Agent | 시장 데이터 수집, ICP 자동 스코어링 |
| 2 | Lead Gen + Qualification Agent | 계정 enrichment, 스코어 계산 |
| 3 | Lead Generation Agent | 시퀀스 초안, 응답 분류, CRM 기록 |
| 4 | Qualification Agent | MEDDICC 추출, 딜 리스크 감지, stalled deal 알림 |
| 5 | Deal Conversion Agent | 제안서 초안, 가격 검증, 핸드오프 문서 |
| 6 | Customer Success Agent | Health Score, QBR 자료, 갱신 예측 |
| 7 | Ops Analyst Agent | 리포트 생성, 예측, Win/Loss 패턴 분석 |

### 핸드오프 & 에스컬레이션 규칙

| 조건 | 핸드오프 방향 | 트리거 |
|------|-------------|--------|
| Lead → Opportunity | Lead Gen → Qualification | SQL 기준 충족 (ICP Score ≥60, BANT 3/4+) |
| Stalled Deal | Qualification → Orchestration | 14일 이상 Stage 변화 없음 |
| T3 → T2 승격 | AI-led → Co-pilot | 딜 규모 >ACV 기준 or 복잡성 증가 |
| CS Expansion Signal | CS Agent → Deal Conversion | Usage spike + NPS ≥8 + 추가 부서 관심 |
| Health Score Red | CS Agent → 에스컬레이션 | Health Score <40, 48시간 내 개입 |
| Manager 에스컬레이션 | Agent → Human Manager | 할인 >20%, 비표준 계약, 전략 고객 |

---

## 4. Playbook 체계

> 이 섹션은 9개 Playbook 문서와 7개 Play의 핵심 실행 컨텐츠를 포함합니다. 원본 문서(총 ~4,100줄)에서 "이걸 보고 따라할 수 있는" 수준의 operational detail을 추출했습니다.

### 4.1 ICP 3축 스코어링 모델

#### 프레임워크 구조

```
         ┌──────────────┐
         │ Firmographic │  기업의 객관적 속성
         │    (40%)     │  산업, 규모, 지역, 매출
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │Technographic │  기술 환경 적합성
         │    (30%)     │  기술스택, 인프라, 도구
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │  Needs-based │  과제와 구매 의도
         │    (30%)     │  Pain, Budget, Timeline
         └──────────────┘
```

#### Firmographic Criteria (40%)

| 속성 | Ideal (5점) | Good (3점) | Poor (1점) |
|------|------------|-----------|-----------|
| **산업** | Primary verticals: SaaS, FinTech, HealthTech | Adjacent: Manufacturing, Retail | Misfit: Government, Non-profit |
| **직원 수** | 200-2,000 (Mid-Market sweet spot) | 50-199 or 2,001-10,000 | <50 or >10,000 |
| **연매출** | $20M-$500M | $5M-$19M or $501M-$2B | <$5M or >$2B |
| **지역** | Primary markets | Secondary markets | No-go regions |
| **성장률** | >20% YoY | 10-20% YoY | <10% or declining |
| **자금 조달** | Series B-D or PE-backed | Series A or Public | Pre-seed/Seed |

#### Technographic Criteria (30%)

| 속성 | Ideal (5점) | Good (3점) | Poor (1점) |
|------|------------|-----------|-----------|
| **CRM** | Salesforce | HubSpot, Dynamics | None or custom |
| **기술 성숙도** | Cloud-native, API-first | Hybrid (cloud + on-prem) | Legacy on-prem only |
| **현재 솔루션** | Competitor X or manual process | Partial solution in place | Committed to competitor Y (3yr lock-in) |
| **통합 필요** | 표준 API 통합 가능 | 커스텀 통합 필요 | 통합 불가능 |
| **보안 요구** | Standard (SOC2 충분) | Enhanced (HIPAA 등) | Government-level (FedRAMP) |

#### Needs-based Criteria (30%)

| 속성 | Ideal (5점) | Good (3점) | Poor (1점) |
|------|------------|-----------|-----------|
| **핵심 Pain** | 우리 솔루션이 직접 해결하는 문제 보유 | 관련 문제 인식하나 우선순위 낮음 | 문제 인식 없음 |
| **Budget** | 예산 확보됨 또는 확보 진행 중 | 예산 미확보이나 ROI case로 가능 | 예산 없음, ROI 불명확 |
| **Timeline** | 6개월 내 도입 의향 | 6-12개월 내 | 12개월+ 또는 미정 |
| **의사결정 복잡도** | 단일 부서 결정 | 2-3개 부서 합의 | 전사 위원회 승인 필요 |
| **Champion 존재** | 내부 옹호자 확인됨 | 관심 있는 담당자 있음 | 접점 없음 |

#### Fit Score 계산 공식

```
Fit Score = (Firmo 합계/30 × 40) + (Techno 합계/25 × 30) + (Needs 합계/25 × 30)
```

| Fit 등급 | 점수 | 의미 |
|---------|------|------|
| A-Fit | 80-100 | ICP에 매우 적합 |
| B-Fit | 60-79 | 적합하나 일부 gap |
| C-Fit | 50-59 | 최소 기준 충족 |
| D-Fit | <50 | **제외** — 추가 스코어링하지 않음 |

#### Intent Score (0-30)

| 신호 | 점수 | 소스 |
|------|------|------|
| 관련 키워드 검색 (intent data) | +5 | Bombora, G2, TrustRadius |
| 경쟁사 리뷰/비교 페이지 방문 | +5 | Intent data provider |
| 관련 직무 채용공고 게시 | +4 | LinkedIn, Indeed |
| 자금 조달/인수 이벤트 | +4 | Crunchbase, PitchBook |
| 기존 벤더 계약 만기 근접 | +5 | 영업 인텔 |
| 산업 규제 변화로 솔루션 필요 | +3 | 뉴스, 규제 모니터링 |
| 경영진 교체 (관련 직급) | +4 | LinkedIn, 뉴스 |

#### Engagement Score (0-30)

| 신호 | 점수 | 소스 |
|------|------|------|
| 웹사이트 방문 (3회+ /월) | +3 | Web analytics |
| 콘텐츠 다운로드 | +4 | Marketing automation |
| 웨비나/이벤트 참석 | +5 | Event platform |
| 이메일 응답 | +5 | CRM / Sequencer |
| 미팅 참석 | +8 | CRM |
| 데모/PoC 요청 | +10 | CRM |
| 복수 부서 접촉 (Multi-threading) | +5 | CRM |

#### Total Score → Tier 변환 및 Action

| Total Score | 등급 | Action | Tier |
|-------------|------|--------|------|
| 120-160 | **Hot** | 즉시 AE 배정, 24시간 내 접촉 | T1 Strategic |
| 90-119 | **Warm** | SDR 우선 시퀀스, 1주 내 접촉 | T2 Core |
| 60-89 | **Nurture** | 자동 nurture 시퀀스, 월간 터치 | T3 Long-tail |
| 50-59 | **Watch** | 마케팅 리드 풀, 분기 모니터링 | T3 Long-tail |
| <50 | **Excluded** | Fit 미달, 추적 중단 | 제외 |

#### Account Tier Coverage Model

| 구분 | T1 Strategic | T2 Core | T3 Long-tail |
|------|-------------|---------|-------------|
| **Ownership** | Named AE (1:10-20) | Pooled AE (1:50-80) | Agent-led / Pooled SDR (1:200+) |
| **Interaction** | Human-led | Co-pilot (AI draft, human review) | AI-led (human escalation only) |
| **Meeting Frequency** | Monthly+ (대면 포함) | Quarterly | On-demand |
| **Account Plan** | 필수 (상세) | 필수 (간략) | 자동 생성 |
| **Outbound Cadence** | 맞춤 (100% 개인화) | 반자동 (50% 개인화) | 자동 (템플릿 기반, AI 개인화) |
| **Response SLA** | 4시간 이내 | 24시간 이내 | 48시간 이내 |

#### Tier 변동 규칙 (Guard Rails)

| 변동 | Trigger | 프로세스 |
|------|---------|---------|
| T3 → T2 승격 | 사용량 급증, 대형 expansion 기회 발견 | Agent 알림 → Manager 승인 |
| T2 → T1 승격 | ACV $100K+ 달성, 전략적 중요성 확인 | 분기 리뷰에서 결정 |
| T1 → T2 강등 | 매출 감소, engagement 하락, churn 리스크 | 분기 리뷰에서 결정 |
| **T1 승격 자동 차단** | Agent가 자동으로 T1 승격 불가 | 반드시 사람 승인 필요 |

#### Agent 자동 스코어링 트리거

| Trigger | Action | 주기 |
|---------|--------|------|
| 신규 계정 CRM 등록 | Fit Score 자동 계산 | Real-time |
| Intent data 업데이트 | Intent Score 재계산 | Weekly |
| 웹/이메일/미팅 활동 | Engagement Score 갱신 | Daily |
| Account Score 등급 변화 | Tier 재분류 추천 + 알림 | Daily |
| 분기 시작 | 전체 계정 Full Rescore | Quarterly |
| Score 30일 내 20pt+ 하락 | 이상 신호 Manager 알림 | Real-time |

### 4.2 MEDDICC 적격성 검증

> MEDDICC는 한 번 채우는 체크리스트가 아니라, 딜이 진행되면서 **지속적으로 깊어지는 이해**입니다. 교육 후 6개월 내 40-50% 준수율 하락이 일반적이므로, AI Agent의 지속적 nudge가 필수입니다.

#### 7요소 Scoring Rubric

| 요소 | CRM 필드 | 0점 (Red) | 1점 (Yellow) | 2점 (Light Green) | 3점 (Green) |
|------|---------|----------|-------------|------------------|-------------|
| **M**etrics | `Metrics__c` | 미확인 | 정성적 언급 ("더 빠르게") | 정량 지표 확인 ("30% 개선") | ROI 분석 완료 + EB 검증 |
| **E**conomic Buyer | `Economic_Buyer__c` | 미식별 | 이름/직급 파악 | 1회+ 접촉, 우선순위 파악 | 공개적 지지 + 예산 확보 확인 |
| **D**ecision Criteria | `Decision_Criteria__c` | 미파악 | 일부 기준 언급 | 전체 목록 파악 + alignment 분석 | 기준을 우리에게 유리하게 설정 |
| **D**ecision Process | `Decision_Process__c` | 미파악 | 대략적 파악 | 전체 단계/관여자/일정 문서화 | Paper process 파악 + 일정 영향력 |
| **I**dentify Pain | `Identified_Pain__c` | 미파악 | 표면적 문제 | 구체적 Pain + 임팩트 정량화 | 다수 stakeholder 공감 + EB 우선순위 |
| **C**hampion | `Champion_Name__c` | 없음 | 관심 담당자 (3조건 미충족) | Power+Access 확인, 일부 내부 활동 | 3조건 충족 + EB 대변 + 장애물 제거 |
| **C**ompetition | `Competitor__c` | 미파악 | 존재 인지, 상세 미파악 | 강/약점 분석 + DC 포지셔닝 완료 | Do-nothing 포함 전체 대응 확보 |

**Champion의 3가지 필수 조건**: Power(의사결정 영향력) + Access(EB 접근 가능) + Vested Interest(프로젝트 성공 = 자신의 이익)

#### 요소별 Discovery Question Bank

**Metrics (측정 지표)**:

| 단계 | 질문 |
|------|------|
| 초기 | "이 프로젝트의 성공을 어떤 수치로 측정하실 계획인가요?" |
| 심화 | "현재 그 지표의 수준은 어느 정도이고, 목표치는 얼마인가요?" |
| 심화 | "그 개선이 연간 매출/비용에 미치는 영향을 금액으로 환산하면 어느 정도일까요?" |
| 검증 | "이 ROI 분석을 경영진에게 공유하셨을 때 반응은 어떠셨나요?" |
| 확장 | "비슷한 규모의 다른 회사가 [X% 개선]을 달성했는데, 이 수준이 의미 있으시겠어요?" |

**Economic Buyer (경제적 의사결정자)**:

| 단계 | 질문 |
|------|------|
| 초기 | "이번 투자의 최종 승인은 누가 하시나요?" |
| 심화 | "그 분이 이번 프로젝트에 대해 어느 정도 알고 계신가요?" |
| 심화 | "그 분의 올해 핵심 우선순위 3가지는 무엇인가요?" |
| 전략 | "그 분과 직접 미팅할 기회가 있을까요? 저희가 ROI 분석을 공유드리고 싶습니다" |
| 검증 | "EB가 이 프로젝트에 공개적으로 지지를 표명하셨나요?" |

**Decision Criteria & Process**:

| 단계 | 질문 |
|------|------|
| DC 초기 | "벤더 선정 시 가장 중요한 3가지 기준은 무엇인가요?" |
| DC 영향 | "보안 인증이나 통합 용이성도 중요한 기준이 되시는지요?" (우리 강점 방향 유도) |
| DP 초기 | "내부 구매 승인 프로세스는 어떤 단계를 거치시나요?" |
| DP 심화 | "법무 검토나 조달 프로세스가 별도로 있나요?" |
| DP 확인 | "총 X주 정도 소요된다고 이해하면 될까요?" |

**Identify Pain (Gap Selling 프레임워크)**:

```
┌─────────────────┐              ┌─────────────────┐
│  Current State  │──── GAP ────▶│  Future State   │
│  (고객의 현재)   │              │  (고객이 원하는) │
│ - 현재 프로세스  │              │ - 원하는 프로세스 │
│ - 현재 성과 수치 │              │ - 목표 성과 수치 │
│ - 감정적 영향    │              │ - 기대 감정      │
└─────────────────┘              └─────────────────┘
```

| 유형 | 질문 |
|------|------|
| **Situation** | "현재 이 업무를 어떤 방식으로 처리하고 계신가요?" |
| **Problem** | "그 과정에서 가장 불편하거나 비효율적인 부분은 무엇인가요?" |
| **Implication** | "이 문제가 해결되지 않으면 향후 6-12개월간 어떤 영향이 예상되시나요?" |
| **Need-payoff** | "만약 이 프로세스가 개선된다면, 팀에 어떤 변화가 생길까요?" |
| **Gap** | "현재 상태와 원하시는 상태 사이의 가장 큰 차이는 무엇인가요?" |

**Champion & Competition**:

| 대상 | 질문 |
|------|------|
| Champion 식별 | "내부에서 이 프로젝트를 가장 강력히 지지하는 분은 누구인가요?" |
| Champion 검증-Power | "그 분이 이 결정에 어떤 영향력을 행사할 수 있나요?" |
| Champion 검증-Access | "그 분이 [EB 이름]에게 직접 미팅을 잡을 수 있나요?" |
| Champion 코칭 | "다음 내부 미팅에서 어떤 포인트를 강조하면 좋을까요?" |
| Competition 초기 | "현재 다른 솔루션이나 벤더를 검토 중이신가요?" |
| Competition 방어 | "내부 개발도 고려하고 계신가요?" |

#### Composite Score 가중 계산

```
MEDDICC Score = (M×0.15 + E×0.20 + DC×0.10 + DP×0.10 + I×0.20 + C_champ×0.20 + C_comp×0.05) × 100 / 3
```

| 요소 | 가중치 | 이유 |
|------|--------|------|
| Metrics | 15% | 가치 정량화 |
| Economic Buyer | **20%** | 최종 결정 권한 |
| Decision Criteria | 10% | 평가 기준 |
| Decision Process | 10% | 프로세스 이해 |
| Identify Pain | **20%** | 구매 동기의 근원 |
| Champion | **20%** | 내부 추진력 |
| Competition | 5% | 경쟁 상황 |

#### Score → Action Mapping

| Score 구간 | 해석 | Action |
|-----------|------|--------|
| 80-100 | **Strong** — 이길 가능성 높음 | Accelerate, resource 집중 |
| 60-79 | **Developing** — 진행 중, gap 존재 | 미충족 요소에 집중 |
| 40-59 | **Weak** — 리스크 높음 | Gap 30일 내 해소 or disqualify 검토 |
| 0-39 | **Critical** — 이기기 어려움 | Disqualify 또는 전략 전면 재검토 |

#### Stage Gate 매트릭스

| Opp Stage | 필수 Score 기준 | 미달 시 |
|-----------|----------------|--------|
| S1 Discovery | I ≥ 1 (Pain 초기 확인) | Stage 진행 차단 + Agent 알림 |
| S2 Qualification | M ≥ 1, I ≥ 2, C(champ) ≥ 1 | 차단 + 추천 질문 제공 |
| S3 Solution Design | M ≥ 2, E ≥ 1, DC ≥ 2, I ≥ 2, C(champ) ≥ 2 | 차단 + gap 분석 |
| S4 Proposal | 모든 요소 ≥ 2, E ≥ 2 | 차단 + Manager 리뷰 |
| S5 Negotiation | 모든 요소 ≥ 2, DP ≥ 2, E ≥ 2 | 차단 + 에스컬레이션 |
| S6 Verbal Commit | Composite Score ≥ 80 | 차단 + VP 리뷰 |

#### Agent MEDDICC 자동화

| 기능 | 설명 |
|------|------|
| **콜 후 자동 추출** | 트랜스크립트에서 MEDDICC 7요소 정보 추출 → CRM 필드 업데이트 초안 |
| **필드 완성도 체크** | Stage 대비 필수 기준 미달 시 자동 알림 |
| **코칭 피드백** | "Champion Score 1인데, S3 진행에 2 필요 → 검증 미팅 추천" |
| **주간 딜 리뷰 요약** | 모든 활성 Opp의 MEDDICC 상태 + 리스크 딜 하이라이트 |
| **Win/Loss 패턴** | 과거 CW/CL 딜의 MEDDICC 점수 패턴 → 예측 정확도 향상 |

### 4.3 Call Scripts & Discovery Framework

#### Cold Call Script (Outbound SDR)

**오프닝 (패턴 인터럽트 방식)**:
```
"[Name]님, 안녕하세요. [Your Name]입니다, [Company]에서 전화드렸습니다.
솔직히 말씀드리면 콜드콜이에요.
30초만 주시면, 관련 없으시면 바로 끊겠습니다. 괜찮으시겠어요?"
```

**가치 가설 (30초)**:
```
"[Company Name]이 최근 [trigger: 채용 확대/자금 조달/제품 출시]하신 것 봤습니다.
보통 이 단계에서 [industry] 기업들이 겪는 문제가 [specific problem]인데요.
혹시 [their company]에서도 이 부분이 과제로 느껴지시는지 궁금해서요."
```

**반응별 대응**:

| 반응 | 대응 |
|------|------|
| "네, 맞아요" | "구체적으로 어떤 부분이 가장 큰 과제인가요?" → Discovery 전환 |
| "좀 다른데요" | "어떤 부분이 다르신가요? 오히려 더 듣고 싶습니다" → 수정된 가설 |
| "지금 바쁩니다" | "이해합니다. 15분 미팅을 잡으면 될까요? [2-3개 시간 옵션]" |
| "관심 없습니다" | "[problem area] 담당하시는 다른 분을 소개해주실 수 있나요?" |
| "자료 보내주세요" | "어떤 내용이 가장 도움 되실까요? 한 가지만 여쭤봐도 될까요" |

**미팅 잡기**:
```
"[Problem]에 대해 [peer company]가 어떻게 해결했는지 15분 공유드리면
판단하시는 데 도움이 될 것 같은데, 이번 주 [화/목] 오전은 어떠세요?"
```

#### Discovery Call Framework (SPIN + Gap Selling)

**미팅 세팅 (첫 5분)**:
```
"오늘 제가 이해하고 싶은 건:
1. 현재 [area] 관련해서 어떤 상황이신지
2. 어떤 부분을 개선하고 싶으신지
3. 저희가 도움 될 수 있는 부분이 있는지

먼저 [Name]님 상황을 충분히 듣고 싶습니다.
그 전에 — 오늘 이 미팅에서 가장 얻고 싶은 것이 무엇인가요?"
```

**Phase 1: Situation (5-7분)** — 현재 환경 파악

| # | 질문 | 목적 |
|---|------|------|
| S1 | "현재 [area]를 어떤 방식으로 처리하고 계신가요?" | 프로세스 이해 |
| S2 | "이 업무에 어떤 도구/시스템을 사용하시나요?" | 기술 환경 |
| S3 | "팀 구성은? 몇 명이 관여하시나요?" | 규모/복잡도 |
| S4 | "현재 이 분야의 KPI나 목표 수치가 있으시다면요?" | Baseline 확보 |

> **주의**: Situation 질문은 5개 이내. 사전 리서치로 대체 가능한 건 미리 파악.

**Phase 2: Problem (7-10분)** — 문제 식별

| # | 질문 | 목적 |
|---|------|------|
| P1 | "현재 방식에서 가장 불편하거나 비효율적인 부분은요?" | 표면적 Pain |
| P2 | "이상적이지 않다고 느끼시는 구체적 상황을 하나 말씀해주시겠어요?" | 사례 확보 |
| P3 | "이 문제가 얼마나 자주 발생하나요?" | 빈도/심각도 |
| P4 | "수동으로 해결하고 계신 workaround가 있나요?" | 숨겨진 비용 |
| P5 | "이전에 이 문제를 해결하려고 시도하신 적이 있나요?" | 과거 학습 |

**Phase 3: Implication (10-12분)** — 가장 중요

| # | 질문 | 목적 |
|---|------|------|
| I1 | "그 문제가 매출/파이프라인에 직접적으로 어떤 영향을 미치나요?" | 재무적 임팩트 |
| I2 | "팀이 [workaround]에 쓰는 시간을 주당으로 환산하면요?" | 시간 비용 정량화 |
| I3 | "이 문제가 해결 안 되면 6-12개월 후에는 어떻게 될까요?" | 미래 리스크 |
| I4 | "다른 부서나 팀에도 영향이 가나요?" | 영향 범위 확대 |
| I5 | "경영진이 이 문제를 인지하고 있나요?" | EB awareness |
| I6 | "올해 목표를 달성하는 데 이 문제가 걸림돌이 되나요?" | 전략적 중요도 |

> 이 단계에서 침묵을 두려워하지 말 것. 질문 후 3초 이상 기다리면 더 깊은 답변이 나옴.

**Phase 4: Need-Payoff (5-7분)** — 해결 가치

| # | 질문 | 목적 |
|---|------|------|
| N1 | "이 문제가 완전히 해결된다면, 팀의 하루가 어떻게 달라질까요?" | 비전 그리기 |
| N2 | "이 시간이 절약된다면 어디에 재투자하시겠어요?" | 가치 확인 |
| N3 | "이 성과를 경영진에게 보고하신다면, 어떤 반응이실 것 같나요?" | EB 가치 확인 |
| N4 | "이 문제를 해결하는 것이 [Name]님 개인적으로도 중요한가요?" | Champion 동기 |

**미팅 마무리 (5분)**:
```
"오늘 말씀 정리하면:
- 현재 [current state 요약]
- 핵심 과제는 [pain 1, 2]
- 이를 해결하면 [expected impact]

맞으시죠?

다음 단계로 [demo / 기술 검토 / 제안서]를 준비해드리면 좋겠는데,
1. 이런 솔루션에 대한 예산이 이미 잡혀 있나요?
2. 최종 결정은 누가 하시나요?
3. 언제까지 결정하셔야 하는 타임라인이 있으신가요?"
```

#### Demo Script Framework

**Pre-Demo Checklist**:
- [ ] Discovery에서 파악한 Pain 1-3개 정리
- [ ] 고객의 용어/표현으로 시나리오 구성 (우리 용어가 아닌)
- [ ] 각 기능이 고객 Pain에 어떻게 연결되는지 한 문장으로 설명 가능한가?
- [ ] 참석자 확인 — 새 참석자 있으면 Discovery 질문 추가
- [ ] Demo 환경 사전 테스트

**Demo 구조**: [3분] 컨텍스트 재확인 → [20분] Pain 중심 시연 (Pain별 Before/After) → [10분] 질문 & 반응 → [5분] Next Steps

#### QBR Agenda 템플릿

```
"오늘 QBR에서는 세 가지를 다루겠습니다:
1. 지난 분기 성과 리뷰와 합의한 KPI 달성 현황
2. 앞으로 더 가치를 높일 수 있는 방법
3. 다음 분기 함께 달성할 목표"
```

| 섹션 | 핵심 질문 |
|------|----------|
| 성과 | "합의했던 [KPI]에서 어느 정도 달성 되셨나요?" |
| 가치 | "[Our product] 없이 이 업무를 한다면 어떤 차이가 있을까요?" |
| 불만 | "개선되었으면 하는 부분이 있다면요?" |
| Adoption | "[Feature X]는 아직 많이 활용하지 않으시는 것 같은데, 이유가 있으시나요?" |
| Expansion | "다음 분기에 [new capability]를 시도해볼 의향이 있으신가요?" |

#### Agent Pre/Post-Call 자동화

**Pre-Call Briefing (Agent 자동 생성)**:
1. Account snapshot (산업, 규모, Tier, Health Score)
2. Contact profile (직급, 관심사, 최근 LinkedIn 활동)
3. Engagement history (이전 터치 이력, 마지막 대화 요약)
4. Recommended talking points (trigger event, peer reference)
5. MEDDICC gap → 이번 콜에서 채워야 할 정보
6. Suggested questions (gap 기반 2-3개)

**Post-Call Processing (Agent 자동 실행)**:
1. 트랜스크립트에서 MEDDICC 요소별 정보 추출
2. CRM Activity 기록 (요약, 다음 스텝, 감정 분석)
3. MEDDICC 필드 업데이트 초안 생성
4. Next best action 추천
5. Follow-up 이메일 초안 생성 (콜 내용 기반)
→ AE가 확인 + 승인하면 CRM 반영

### 4.4 Email Templates & Cadence

#### 설계 원칙

| # | 원칙 | 세부 |
|---|------|------|
| 1 | **125 단어 이내** | 모바일 퍼스트. 스크롤 없이 읽을 수 있어야 함 |
| 2 | **CTA 1개** | 한 이메일에 하나의 행동만 요청 |
| 3 | **Subject line** | 소문자, 3-5단어, 낚시 없음 |
| 4 | **개인화** | T1=100% 커스텀, T2=산업+역할, T3=머지필드 기반 |
| 5 | **발송 시간** | 화-목, 오전 7:30-8:30 또는 오후 5:00-6:00 (현지 시간) |

#### 14일 Outbound Cadence 풀 타임라인

| Day | 채널 | 목적 | 핵심 요소 |
|-----|------|------|----------|
| 1 | **Email #1** | Trigger-based 접근 | 트리거 이벤트 + Pain + 동종업계 사례 |
| 3 | LinkedIn | Connection + Value Add | 프로필 리서치 기반 개인화 |
| 5 | **Email #2** | 인사이트 공유 | 업계 통계 + 문제 비용 정량화 |
| 7 | Phone #1 | 직접 대화 시도 | 30초 스크립트 + voicemail |
| 9 | **Email #3** | Social Proof | 동종 업계 성공 사례 + 정량적 성과 |
| 10 | Phone #2 | 재시도 | 이전 이메일 참조 |
| 12 | **Email #4** | Break-up | 마지막 가치 제공 + 존중하며 문 열어두기 |
| 14 | Email #5 (조건부) | Re-engagement | engagement signal 있을 때만 발송 |

#### 핵심 이메일 템플릿 3종

**Email #1: Trigger-Based Cold Open** — Subject: `[trigger event]에 관해`
```
[First Name]님, 안녕하세요.

[Their Company]가 최근 [trigger event: Series B 완료 / 영업팀 20명 채용 중]하신 것 봤습니다.

이 단계의 [industry] 기업들이 자주 겪는 문제가
[specific problem: 파이프라인 가시성 부족 / CRM 데이터 정확도 하락]인데요.

혹시 이 부분이 현재 과제로 느껴지시나요?

[Your Name]
```

**Email #2: Value-Add Insight** — Subject: `[industry] 벤치마크 하나`
```
[First Name]님,

[industry]에서 최근 흥미로운 데이터를 봤습니다:

[Insight: "MEDDICC를 체계적으로 적용하는 팀은 win rate가 38%입니다" /
"영업 rep이 CRM 업데이트에 주당 평균 4.5시간을 쓰고 있습니다"]

[Their Company] 규모에서 이 차이는
[quantified impact: 연간 $X의 매출 차이]를 만듭니다.

관심 있으시면 10분 대화로 더 자세히 공유드리겠습니다.

[Your Name]
```

**Email #4: Breakup** — Subject: `마지막 연락`
```
[First Name]님,

몇 번 연락드렸는데 바쁘신 것 같습니다. 더 이상 메일 보내지 않겠습니다.

하나만 남기면, [resource: 가이드/벤치마크 리포트]가
[relevant benefit]에 도움 되실 수 있을 것 같습니다: [link]

타이밍이 맞을 때 이 메일에 답해주시면 됩니다.

[Your Name]
```

#### CS 이메일 2종

**Health Check (Usage 하락 감지)** — Subject: `[Their Company] 활용 현황 체크인`
```
[First Name]님,

최근 [our product] 사용 패턴을 보니 [지난 달 대비 로그인 빈도가 줄어든 것 같습니다].

혹시 팀에서 어려운 점이 있거나, 도움이 필요한 부분이 있으신가요?

15분 체크인 콜로 해결 방법을 함께 찾아보면 좋겠습니다: [Calendar link]

[CS Name]
```

**Renewal 시작 (D-90)** — Subject: `갱신 관련 안내`
```
[First Name]님,

계약이 [renewal date]에 갱신 시점을 맞이합니다.

지난 [contract period] 동안의 성과를 정리하면:
• [Achievement 1]
• [Achievement 2]

갱신 조건과 다음 기간의 계획에 대해 미팅을 잡으면 좋겠습니다.

[CS Name] + [AE Name]
```

#### Agent 개인화 변수 매핑

| 변수 | 소스 | Trigger → Problem Mapping |
|------|------|--------------------------|
| `[trigger event]` | News/Enrichment API | 자금 조달 → 빠른 성장에 프로세스 미달 |
| `[specific problem]` | Trigger → Problem table | 영업팀 채용 → 온보딩, 프로세스 표준화 |
| `[peer company]` | Internal case study DB | 새 제품 출시 → 새 시장 진입, ICP 재정의 |
| `[specific metric]` | Internal case study DB | 경영진 교체 → 새 전략 도입, quick win |
| `[quantified impact]` | Agent 계산 | M&A → 시스템 통합, 프로세스 통일 |

### 4.5 Objection Handling

#### 원칙

1. **반박하지 않는다.** 먼저 인정하고, 질문으로 진짜 이유를 파악한다.
2. **질문이 답보다 먼저.** 처방 전에 진단한다.
3. **침묵은 무기다.** 대응 후 멈추고, 상대방이 소화할 시간을 준다.
4. **모든 반론을 극복할 필요는 없다.** 일부는 진짜 disqualifier다.
5. **고객 이야기가 논리보다 강하다.** "[고객 A]의 경우"가 "저희 생각에는"보다 효과적이다.

#### Objection Category Tree

```
반론
├── 가격/예산 (Price/Budget)
│   ├── "너무 비쌉니다"
│   └── "예산이 없습니다"
├── 경쟁/대안 (Competition)
│   ├── "이미 [경쟁사] 쓰고 있습니다"
│   ├── "내부 개발하겠습니다"
│   └── "계약이 남아있습니다"
├── 타이밍/우선순위 (Timing)
│   ├── "지금은 아닙니다"
│   └── "생각해 보겠습니다"
├── 권한/프로세스 (Authority)
│   └── "상사 확인이 필요합니다"
├── 제품/기능 (Product)
│   ├── "기능 X가 없네요"
│   └── "도입이 복잡할 것 같아요"
└── 회피 (Brush-off)
    └── "자료 보내주세요"
```

#### 핵심 5대 반론 상세

**1. "너무 비쌉니다"** — 대응 프레임: Isolate → Quantify → Reframe

진단 질문: "가격 자체가 부담이신 건가요, 아니면 투자 대비 가치가 불확실하신 건가요?"

| 상황 | 대응 |
|------|------|
| 가치 불확실 | "[problem]이 월 [X]시간, 연 [$Y] 비용이라고 하셨는데, 저희 투자금은 그 fraction입니다" |
| 예산 미확보 | "ROI가 명확하면 예산 확보할 수 있는 프로세스가 있으신가요? 비즈니스 케이스를 함께 만들어드립니다" |
| 경쟁사 대비 | "총소유비용(TCO)으로 비교해보시면 다른 결론이 나올 수 있습니다" |

**절대 하지 말 것**: 즉시 할인 제안. (가격 저항 ≠ 할인 요청)

**2. "이미 [경쟁사]를 쓰고 있습니다"**

```
"이해합니다. [경쟁사]는 [acknowledged strength]에 강한 솔루션이죠.

저희 고객 중 [경쟁사]에서 전환하신 분들이 말씀하시는 건,
[specific gap: 확장성 / 통합 / 사용성]에서 차이를 느꼈다는 거예요.

혹시 [known weakness area]는 현재 어떻게 처리하고 계신가요?"
```

**핵심**: 경쟁사를 비난하지 않는다. 차이점을 질문으로 탐색한다.

**3. "생각해 보겠습니다"**

진단: "타이밍 문제인가요, 아니면 제가 충분히 설명 못 드린 부분이 있는 건가요?"

| 진짜 이유 | 대응 |
|----------|------|
| 타이밍 (진짜) | "언제쯤 다시 논의하면 좋을까요?" |
| 내부 설득 필요 | "Executive summary를 만들어드릴까요?" |
| 숨겨진 반론 | "진행을 망설이시게 하는 가장 큰 이유가 무엇인가요?" |
| 거절 (정중한) | "3개월 뒤에 체크인 드려도 괜찮을까요?" |

**4. "상사 확인이 필요합니다"** — Champion Coaching 대응

```
"물론이죠. 제가 도움드릴 수 있는 부분이 있습니다:

1. Executive Summary 1장으로 핵심을 정리해드릴까요?
2. 혹시 그 분과 직접 짧은 미팅을 잡을 수 있을까요?
3. 가장 강조하면 좋을 포인트가 [ROI 수치, peer reference]입니다."
```

**5. "내부 개발하겠습니다"** — TCO 프레임 대응

```
"내부 개발은 확실히 완전한 통제권을 갖는 장점이 있죠.

보통 고객사에서 비교하실 때 간과되는 부분이 있는데:
1. 개발 시간: 보통 6-12개월 vs 저희는 [X주] 내 라이브
2. 유지보수: 전담 인력 [N명] × 연봉 vs 저희 구독료
3. 기회비용: 엔지니어링 팀이 코어 제품 대신 이걸 만드는 비용

'만들 수 있느냐'가 아니라 '만드는 것이 최선의 자원 배분이냐'가 질문입니다."
```

#### Quick Reference Table (콜 중 참조용)

| 반론 | 즉석 대응 | 후속 질문 |
|------|----------|----------|
| "너무 비쌉니다" | "가격과 가치 중 어디에 걱정이신 건지요?" | "현재 이 문제의 비용을 금액으로 환산하면?" |
| "이미 다른 걸 씁니다" | "[경쟁사]로 [specific area]는 어떻게 해결하고 계신가요?" | "[known weakness]에 대해서는 만족하시나요?" |
| "생각해 보겠습니다" | "내부에서 추가로 확인하셔야 하는 점이 있으신가요?" | "이번 주 내로 확인 후 연락 주시면?" |
| "상사 확인이 필요해요" | "그 분이 가장 궁금해하실 포인트는 무엇일까요?" | "Executive Summary를 준비해드릴까요?" |
| "내부 개발하겠습니다" | "내부 개발의 총 비용(인력, 시간, 유지보수)을 산출해보셨나요?" | "코어 제품 개발에 집중하는 대신 이걸 아웃소싱하면?" |
| "기능 X가 없네요" | "그 기능으로 달성하려는 구체적인 결과가 무엇인가요?" | "그 기능 없이 현재 고객들이 어떻게 해결하는지 보여드릴까요?" |
| "도입이 복잡할 것 같아요" | "보통 [X주] 안에 라이브하고 있습니다" | "6개월 뒤에도 현재 방식으로 하시는 것과 비교하면요?" |
| "자료 보내주세요" | "어떤 내용이 가장 도움 되실까요?" | "[Problem]이 현재 실제로 해결해야 할 과제인가요?" |
| "계약이 남았어요" | "갱신 시기가 언제이신가요?" | "3-6개월 전에 비교 평가하시면 협상력이 올라가실 텐데요" |

#### Agent 연동: 반론 패턴 분석

Agent가 분기별 CRM Activity + Call transcript에서 반론 데이터를 집계:
1. 반론 유형별 빈도 (Top 5)
2. 반론 → 극복 → 진행 성공률 (유형별)
3. Rep별 반론 대응 성공률 비교
4. 새로운 반론 패턴 감지
5. Playbook 업데이트 제안 → Win/Loss Analysis (Play 05)에 피드

### 4.6 Competitive Battle Card

#### 핵심 원칙

1. **경쟁사를 비난하지 않는다.** 차이점을 질문으로 탐색하고, 고객이 스스로 판단하게 한다.
2. **FUD를 퍼뜨리지 않는다.** 사실 기반으로만 비교한다.
3. **우리 가치를 먼저 확립한다.** 경쟁사 공격이 아닌 우리 강점 중심으로 대화한다.
4. **고객의 관점에서 비교한다.** 기능 나열이 아닌 비즈니스 성과 기준으로 포지셔닝한다.
5. **분기별 Win/Loss Analysis(Play 05) 결과로 업데이트한다.**

#### 경쟁 유형 분류

| 유형 | 위험도 | 대응 전략 |
|------|--------|---------|
| **Direct Competitor** | 높음 | 차별점(DC alignment) 강조, Killer Questions |
| **Indirect Competitor** | 중간 | 접근법의 우위 논증 |
| **Do Nothing** | **매우 높음 (Loss 37%)** | Cost of Inaction + SPIN Implication |
| **Internal Build** | 높음 | TCO + Time-to-Value + Opportunity Cost |

> **통계**: Win/Loss 분석에서 가장 큰 Loss 원인은 경쟁사가 아닌 **"Do Nothing" (37%)**이다.

#### Battle Card 10-섹션 템플릿

경쟁사별로 다음 10개 섹션을 작성한다:

| # | 섹션 | 핵심 내용 |
|---|------|----------|
| 1 | Competitor Overview | 기본 정보, 포지셔닝, 타겟 시장, SWOT |
| 2 | Feature Comparison | 고객 관점 비즈니스 성과 기준 비교 (★★★/★★☆/★☆☆) |
| 3 | Pricing Comparison | 가격 구조, TCO 3년 비교, 숨겨진 비용 |
| 4 | Win/Loss Track Record | 분기별 전적, Win/Loss Reason Top 5 |
| 5 | **Killer Questions** | 경쟁사 약점 노출하는 탐색 질문 (7개) |
| 6 | **Landmine Questions** | 평가 기준을 우리에게 유리하게 설정하는 질문 (5개) |
| 7 | Positioning Statements | "When they say X, we say Y" (ACE 모델) |
| 8 | Customer Stories | Before → Trigger → After 구조 전환 사례 |
| 9 | "Do Nothing" Battle Card | Cost of Inaction Framework |
| 10 | "Internal Build" Battle Card | Build vs Buy TCO Framework |

#### Killer Questions vs Landmine Questions

| 구분 | Killer Question | Landmine Question |
|------|----------------|-------------------|
| **타이밍** | 경쟁사가 이미 언급된 후 | 경쟁사 언급 전 또는 초기 |
| **목적** | 경쟁사 약점을 직접 노출 | 평가 기준을 우리에게 유리하게 설정 |
| **방식** | 질문 → 약점 확인 → 우리 강점 연결 | 씨앗만 심고, 고객이 스스로 발견 |
| **MEDDICC** | Competition (C) 직접 | Decision Criteria (DC) shaping |

**Killer Question 예시**: "MEDDICC나 deal qualification 프로세스를 시스템에서 직접 추적하고 계신가요?"
→ 경쟁사가 MEDDICC 네이티브 미지원이면 약점 노출

**Landmine Question 예시**: "벤더 평가하실 때 '멀티 CRM 환경에서의 네이티브 통합'도 기준에 포함하고 계신가요?"
→ 고객이 이 기준을 추가하면 경쟁사 자동 탈락

#### ACE 포지셔닝 모델

모든 Positioning Statement는 ACE 구조를 따른다:

```
A — Acknowledge (인정): "맞습니다, [경쟁사]는 [their claim]에 강합니다."
C — Counter (전환):     "다만 [customer's situation]에서 중요한 건 [our strength]입니다."
E — Evidence (증거):    "[Customer X]가 [competitor]에서 전환 후 [quantified result]를 달성했습니다."
```

**절대 하지 말 것**: "그건 사실이 아닙니다" 또는 "그들은 거짓말하고 있습니다."

#### "Do Nothing" 대응: Cost of Inaction Framework

```
Cost of Inaction 계산:

1. DIRECT COSTS (직접 비용)
   • 인건비 낭비: [X hours/week] × [hourly rate] × 52 = $[Annual]
   • 매출 손실: [Lost deals/quarter] × [avg deal size] × 4 = $[Annual]

2. OPPORTUNITY COSTS (기회 비용)
   • 추가 매출, 시장 선점, 인재 유지 효과

3. COMPOUNDING EFFECT (복리 효과)
   • "매일 $[daily cost]씩 낭비하고 계신 셈입니다"

총 비행동 비용 (3년): $[XXX,XXX]
vs. 우리 솔루션 3년 투자: $[XX,XXX] → ROI: [X]배
```

#### Agent Battle Card 연동

| 기능 | 설명 |
|------|------|
| **Pre-call Briefing** | 미팅 전 경쟁사 Battle Card 자동 요약 + Killer Questions + 관련 고객 사례 |
| **Real-time Call Support** | 콜 중 경쟁사 언급 감지 → 추천 대응 화면 표시 + 관련 데이터 즉시 제공 |
| **Win/Loss Feedback Loop** | 분기별 Win Rate 변화 감지 → Battle Card 자동 업데이트 트리거 |
| **CRM 연동** | `MEDDICC_Competitor__c` 기반 어떤 Battle Card를 제공할지 결정 |

### 4.7 Pricing & Discount Matrix

#### 3-Tier 가격 구조 (Good / Better / Best)

| 패키지 | 포지셔닝 | 대상 | Users | Support SLA |
|--------|----------|------|-------|-------------|
| **Good** (Starter) | 핵심 기능만. 진입 장벽 최소화 | SMB, 초기 도입 | 최대 10 | 이메일 (48hr) |
| **Better** (Professional) | 핵심 + 분석 + 통합. 가장 많이 팔림 | Mid-market, Growth | 최대 50 | 이메일+채팅 (24hr) |
| **Best** (Enterprise) | 전체 기능 + 전담 지원 + SLA + 커스텀 | Enterprise, T1 | 무제한 | 전담 CSM+전화 (4hr) |

> **Anchor Rule**: 항상 Better 패키지를 기본으로 제시. Good은 "최소한", Best는 "최적"으로 프레이밍.

#### Discount Authority Matrix

| Discount Range | Approver | SLA | 필수 문서 |
|---------------|----------|-----|----------|
| **0-10%** | AE 자체 승인 | 즉시 | CRM Deal Note에 할인 사유 기록 |
| **11-20%** | Sales Manager | **4시간** | 서면 정당화 + 경쟁 상황 컨텍스트 |
| **21-30%** | VP Sales | **24시간** | Business Case + P&L 영향 분석 |
| **30%+** | C-Level (예외적) | **48시간** | Executive Approval Form + 이사회 수준 정당화 |

#### Discount Approval Decision Tree

```
할인 요청 발생
│
├── 할인율 ≤ 10%?
│   ├── YES → AE 자체 승인 → CRM 기록 → 완료
│   └── NO ↓
│
├── 할인율 ≤ 20%?
│   ├── YES → Sales Manager 에스컬레이션
│   │         ├── 승인 → CRM 기록 → 완료
│   │         └── 반려 → 대안 협상 지시
│   └── NO ↓
│
├── 할인율 ≤ 30%?
│   ├── YES → VP Sales 에스컬레이션
│   │         ├── 승인 → CRM 기록 → 완료
│   │         └── 반려 → 대안 패키지/조건 협상
│   └── NO ↓
│
└── 할인율 > 30%
    └── C-Level 에스컬레이션 (극히 예외적)
```

#### 할인 적절/부적절 기준

**Acceptable Triggers**:

| Trigger | 최대 추가 할인 | 조건 |
|---------|-------------|------|
| 경쟁 압박 | +10% | 경쟁사 제안서 또는 구체적 증거 |
| Multi-year 약정 | 2년 +5%, 3년 +10%, 4년+ +15% | 최소 24개월 약정 |
| Strategic Account (T1) | +5% | 포트폴리오 차원 전략적 가치 |
| 대량 라이선스 | 26-50: 5%, 51-100: 8%, 101-250: 12% | Volume 티어별 |
| 레퍼런스 합의 | +5% | 공식 사례 발표 + 로고 사용 동의 |
| 분기 마감 가속 | +5% | 당 분기 내 계약 서명 확정 시 |

**Red Flags (부적절한 할인)**:

| 상황 | 대신 할 일 |
|------|-----------|
| 가치 입증 없이 가격부터 논의 | Discovery 재실행, Gap Selling 적용 |
| 영업 초기 단계 (S1-S3) | "최종 조건은 범위 확정 후 논의" |
| Champion 없이 가격 양보 | Champion 확보 후 가격 논의 |
| 이미 Win 가능성 높은 딜 | 할인 없이 클로징 진행 |

#### 7 Guard Rails

| Guard Rail | 규칙 | Agent 검증 |
|-----------|------|-----------|
| Maximum Discount Cap | 어떤 경우에도 **40% 초과 불가** | `Discount_Pct > 40` → 자동 차단 |
| Minimum ACV Floor | 패키지별 최소 ACV 하한선 | `ACV < Floor` → 경고 |
| Discount Frequency | 동일 계정에 연 2회 이상 추가 할인 불가 | Account history 체크 |
| Margin Floor | 총 마진율 [X]% 이하 할인 금지 | P&L 시뮬레이션 자동 실행 |
| 할인 + Free Months 중복 금지 | 동시 제공 불가 | 복합 할인 감지 시 경고 |
| 갱신 시 할인 확대 금지 | 이전 대비 확대 시 VP Sales 승인 | 자동 에스컬레이션 |
| 승인 전 Stage 진행 차단 | 11%+ 할인은 승인 전 진행 불가 | CRM Stage gate |

#### Multi-year & Volume Discount

**Multi-year**:

| 계약 기간 | 추가 할인 | 총 가능 할인 (AE 권한 내) |
|-----------|----------|--------------------------|
| 12개월 (기본) | 0% | 0-10% |
| 24개월 | +5% | 5-15% |
| 36개월 | +10% | 10-20% |
| 48개월+ | +15% (VP Sales 승인) | 15-25% |

> Multi-year 할인은 Standard Discount Authority와 **별도 누적**. 예: AE 자체 5% + Multi-year 5% = 총 10%는 AE 권한 내.

**Volume**:

| 사용자 수 | Volume Discount |
|----------|----------------|
| 1-25 | 0% |
| 26-50 | 5% |
| 51-100 | 8% |
| 101-250 | 12% |
| 251-500 | 15% (Manager 승인) |
| 500+ | Custom (VP + Deal Desk) |

#### Negotiation Playbook 핵심

**5대 원칙**:
1. 절대 먼저 양보하지 않는다
2. 할인은 교환이다 (기간, 범위, 결제 조건과 맞교환)
3. 가치 먼저, 가격은 나중에
4. 침묵은 무기다 — 가격 제시 후 먼저 말하지 않는다
5. "최종 제안"은 한 번만 사용

**Trade-Off Menu** (할인 대신 제안할 것):

| 고객 요구 | AE 역제안 |
|----------|---------|
| "10% 깎아주세요" | "24개월 약정 시 동일 할인 가능합니다" |
| "가격이 너무 높아요" | "Better 대신 Good + Analytics Add-on 조합은?" |
| "경쟁사는 더 싸요" | "연간 선결제 시 추가 3% 할인 가능합니다" |
| "더 내려야 결재 받아요" | "이번 분기 내 서명 시 [X]% 추가 가능합니다" |
| "할인 더 필요합니다" | "공식 레퍼런스 사례 동의 시 추가 5% 가능" |

**피해야 할 협상 트랩**:

| 트랩 | 대응 |
|------|------|
| Flinch (과장 반응) | 침묵. 반응하지 않는다. 가격 근거 재설명 |
| Nibbling (추가 요구) | "이 조건은 이미 최종 합의된 범위입니다" |
| Good cop / Bad cop | Bad cop의 구체적 우려에 집중, 감정 무시 |
| Budget bluff | "그 예산으로 가능한 범위를 구성해드리겠습니다" → 축소 패키지 |
| Deadline pressure | "급한 결정보다 맞는 결정이 중요합니다" |

### 4.8 Sales Onboarding Curriculum

#### 30/60/90 Day 구조

```
     Phase 1: LEARN              Phase 2: EXECUTE            Phase 3: OWN
     (Day 1-30)                  (Day 31-60)                 (Day 61-90)
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│ - 제품/시장 이해     │    │ - T3 계정 실전 배정  │    │ - 독립 계정 운영     │
│ - 7-Stage Canon     │───▶│ - 지도하 콜/이메일   │───▶│ - T2 Co-pilot 시작  │
│ - MEDDICC/SPIN/Gap  │    │ - 파이프라인 구축    │    │ - 딜 진행 (S1-S3)   │
│ - 롤플레이 & 인증   │    │ - Agent Co-pilot    │    │ - 성과 목표 달성     │
│ - Shadow 10+ calls  │    │ - 매일 Debrief      │    │ - 360 피드백        │
└─────────────────────┘    └─────────────────────┘    └─────────────────────┘
      Manager 1:1 (주3회)        Manager 1:1 (주2회)        Manager 1:1 (주1회)
      Buddy (매일)               Buddy (주3회)              Buddy (주1회)
```

#### Phase별 Graduation Criteria

**30-Day (Phase 1 → Phase 2)** — 10개 중 8개 Pass:

| # | Criteria | Threshold |
|---|----------|-----------|
| 1 | Product Knowledge Test | >80% (50문항) |
| 2 | Cold Call Role-Play | Rubric 평균 2.5+ |
| 3 | Discovery Call Role-Play | Rubric 평균 2.5+ |
| 4 | Objection Handling Role-Play | 3개 반론 중 2개 성공 |
| 5 | CRM Data Entry Accuracy | >90% (5개 mock 딜) |
| 6 | Shadow Calls | 10회 이상 (Discovery 5+, Demo 2+, Cold 3+) |
| 7 | MEDDICC Comprehension | 7요소 설명 + 샘플 딜 분석 제출 |
| 8 | Agent Usage Proficiency | Pre-call brief + Post-call draft 검토 |
| 9 | 7-Stage Canon Comprehension | 각 Stage 설명 + 본인 역할 연결 |
| 10 | Buddy/Manager Assessment | "Phase 2 진행 준비됨" 동의 |

**60-Day (Phase 2 → Phase 3)** — 10개 중 7개 Pass:

| # | Criteria | Threshold |
|---|----------|-----------|
| 1 | Activity Volume | 주간 목표의 50%+ (최근 2주 평균) |
| 2 | Meetings Booked | 3회 이상 |
| 3 | First SQL Generated | 1개 이상 S2+ Opportunity |
| 4 | MEDDICC Field Completion | 활성 Opp 70%+ 입력 |
| 5 | CRM Hygiene | 24시간 내 Activity 기록률 80%+ |
| 6 | Call Quality Score | Manager 리뷰 평균 3.0+/5.0 |
| 7 | Email Sequence Performance | Open rate >30%, Reply rate >5% |
| 8 | Agent Workflow Adoption | Pre-call/Post-call 활용률 80%+ |
| 9 | Pipeline Value | $[X] 이상 (역할별 설정) |
| 10 | Manager Behavioral Assessment | 5개 행동 지표 중 4개 Demonstrated |

**90-Day (온보딩 졸업)** — 10개 중 8개 Pass:

| # | Criteria | Threshold |
|---|----------|-----------|
| 1 | Activity Volume | 정규 목표의 80%+ |
| 2 | Pipeline Generated | $[X] 이상 |
| 3 | Deals Won or SQLs | 1건 CW 또는 3건+ SQL (S2+) |
| 4 | MEDDICC Compliance | 80%+ 필드 완성 |
| 5 | CRM Hygiene | Activity 90%+, 필수 필드 85%+ |
| 6 | Call Quality | Manager 리뷰 평균 3.5+/5.0 |
| 7 | Agent Workflow Proficiency | 전체 Agent 워크플로우 독립 운영 |
| 8 | Peer/360 Feedback | 종합 평가 4.0+/5.0 |
| 9 | Deal Strategy Presentation | 1개 딜 전략 팀 앞 발표 |
| 10 | Win Rate (early indicator) | Meeting→SQL 전환율이 팀 평균 50%+ |

#### Activity Ramp Schedule

| 주차 | 일일 콜 | 일일 이메일 | 주간 미팅 | 전체 목표 대비 |
|------|--------|-----------|---------|--------------|
| Week 5 | 10-15 | 15-20 | 1 | 25% |
| Week 6 | 15-20 | 20-30 | 1-2 | 35% |
| Week 7 | 20-25 | 30-40 | 2-3 | 45% |
| Week 8 | 25-30 | 40-50 | 2-3 | 55% |
| Week 9 | 30-35 | 50-55 | 3 | 65% |
| Week 10 | 35-40 | 55-60 | 3-4 | 75% |
| Week 11 | 40-45 | 60+ | 4-5 | 85% |
| Week 12 | 45+ | 60+ | 5+ | 90%+ |

#### Role-Play Rubric

| 평가 항목 | 1 (미흡) | 2 (기본) | 3 (양호) | 4 (우수) |
|----------|---------|---------|---------|---------|
| **오프닝** | 스크립트 의존 | 기본 흐름, 긴장감 | 자연스러운 진행 | 자신감 있고 상대 편안 |
| **질문 품질** | 닫힌 질문 위주 | SPIN 시도, 전환 어색 | SPIN 흐름, Implication 도달 | Need-payoff까지 자연스러움 |
| **경청** | 답변 중 끼어듦 | 기본 경청, 후속 부족 | 답변 기반 후속 질문 | 적극 경청 + 깊은 후속 |
| **반론 대응** | 방어적/즉시 반박 | 인정하나 전환 어색 | 인정→질문→리프레임 | 자연스러운 대응 + 사례 |
| **다음 단계** | Next step 없음 | 모호한 제안 | 구체적 일정/행동 합의 | Mutual action plan |

**인증 기준**: 전 항목 평균 2.5+ & 항목별 최소 2점

#### Role-Specific Tracks

| Track | Phase 1 Focus | Phase 2 Focus | Phase 3 Focus |
|-------|---------------|---------------|---------------|
| **SDR** | Cold call 숙달, ICP 판별 | T3 outbound 시퀀스 독립 운영 | 독립 미팅 세팅 + AE 핸드오프 |
| **AE** | MEDDICC + SPIN + Gap Selling | Discovery & Demo 실전 (지도하) | S1→S3 독립 진행, 제안서 초안 |
| **CS/AM** | Health Score 모델, QBR 구조 | 첫 고객 미팅, Health check 이메일 | 독립 QBR, Expansion 기회 식별 |

#### Manager Onboarding Checklist (핵심 항목)

- Pre-Boarding: CRM/이메일/Agent 접근 설정, Buddy 배정, Shadow call 스케줄
- Phase 1: 제품 교육, Canon/MEDDICC/SPIN 교육, 롤플레이 인증, Shadow 10회
- Phase 2: T3 계정 배정, 첫 실전 콜, Daily debrief, 첫 SQL 생성
- Phase 3: 독립 운영, 80%+ 활동량, Deal Strategy 발표, 360 리뷰

### 4.9 7개 Play 상세

> 모든 Play는 **5-블록 구조**를 준수: Input → Process → Output → Metric → Tool/Agent. 이 구조가 Agent System Prompt로 직접 변환된다.

#### Play 01: New Logo Outbound (T2/T3)

**목적**: 신규 SQL 생성 — Canon Stage 2→3→4

| 항목 | 내용 |
|------|------|
| **Trigger** | Target Account List 배포, intent signal (자금 조달, 채용, 제품 출시), 이벤트 참석자 |
| **SQL 기준** | ICP Fit ≥50 + Manager급 접촉 + Pain 확인 + 미팅 확보 |

**프로세스**:
1. Pre-sequence Research (D0): 뉴스, LinkedIn, 개인화 포인트 추출
2. 14일 Multi-channel Cadence: Email #1 (trigger) → LinkedIn → Call → Email #2 (insight) → Email #3 (social proof) → Email #4 (breakup)
3. Response Handling: Positive → AE 핸드오프, No response → 90일 큐
4. AE Handoff: 계정 컨텍스트 + Pain 가설 + Engagement 이력

| 메트릭 | 목표 |
|--------|------|
| Meetings Booked | 12-18/month (SDR) |
| SQL Generated | 8-12/month |
| Show Rate | >80% |
| SQL-to-Opp | >60% |

**Tier별 자동화**: T2 — Agent 초안 → SDR 편집/발송. T3 — Agent 자동 발송, 사람은 응답만 처리.

---

#### Play 02: Strategic Account Expansion (T1)

**목적**: T1 White-Space 공략 — Canon Stage 4→5→6

| 항목 | 내용 |
|------|------|
| **Trigger** | QBR 주기 (30일 전), Usage 30%+ 급증, 신규 부서 접촉, NPS 개선, 갱신 D-180 |
| **산출물** | White-space Map + QBR Deck + Expansion Opp + Updated Account Plan |

**프로세스**:
1. White-Space Analysis: Agent가 제품 카탈로그 vs 현재 계약 자동 매핑, AE 검증
2. Stakeholder Mapping: Champion, 새 부서장, EB, 사용자, Blocker 식별
3. Value Story 구축: 성과 지표 + 미활용 기능 + Expansion 가치 + Peer 벤치마크
4. QBR 실행 (45분): Partnership 리뷰(10분) → 활용 분석(10분) → 성장 기회(15분) → 다음 분기 계획(10분)
5. Expansion Opp 생성 + Multi-thread (Land & Expand, Cross-sell, Upsell)

| 메트릭 | 목표 |
|--------|------|
| Expansion Revenue | YoY 20%+ |
| White-space Conversion | >30% |
| NRR | >120% |
| Active Contacts per T1 | ≥5 |

**자동화**: Human-led. Agent는 데이터 수집, White-space 분석, QBR 초안, Stakeholder 변화 감지 보조.

---

#### Play 03: Renewal Rescue

**목적**: 갱신 리스크 계정 구출 — Canon Stage 6→5

| 항목 | 내용 |
|------|------|
| **Trigger** | Health Score Red (<50) → 즉시, Yellow (<60) → 7일 내, NPS ≤6, Usage 30%+ 하락, Champion 퇴사, P1 티켓 5+/월 |
| **SLA** | Red → 48시간 내 개입, Yellow → 7일 내 개입 |

**프로세스**:
1. Risk Assessment: Agent가 Health Score, 하락 요인, 추천 액션 포함 리스크 리포트 자동 생성
2. Root Cause Diagnosis: 제품 품질 / 도입 미흡 / 가치 미실현 / 관계 약화 / 경쟁 위협 / 조직 변화
3. Save Plan: Red → Executive Save (war room → 진단 → 임원 미팅 → 구출 플랜), Yellow → Proactive Intervention
4. Save Actions: 가치 재강화, 사용법 워크숍, 기술 이슈 해결, Champion 재구축, 가격 유연성 (VP 승인)
5. 결과 평가: Health 회복 → 정상 운영, 정체 → 재검토, Churn → Win/Loss Analysis 투입

| 메트릭 | 목표 |
|--------|------|
| Save Rate | >70% |
| GRR | >90% |
| Health Recovery Rate | >60% |
| Logo Retention | >95% |

**자동화**: Agent가 Health 일일 계산, 트리거 감지, 리스크 리포트 생성, LinkedIn Champion 퇴사 모니터링. 전략 실행은 사람.

---

#### Play 04: CS-Driven Upsell

**목적**: CS 감지 확장 signal → AE 핸드오프 — Canon Stage 4→5→6

| 항목 | 내용 |
|------|------|
| **Trigger** | Usage 30%+ 급증, 용량 80%+ 도달, NPS 9-10, 자발적 Reference 제안, 미구매 기능 Support 요청 |
| **핸드오프 기준** | Health Score ≥70 + 명확한 비즈니스 니즈 + 의사결정 경로 확인 |

**프로세스**:
1. Signal Detection: Agent 일일 스캔 → Strong/Moderate/Weak 분류 → CS 알림
2. CS Qualification Call: 비즈니스 니즈, 예상 성과, 타임라인, Decision maker, Budget 확인
3. CS → AE Handoff: Agent가 구조화된 핸드오프 문서 생성 (확장 유형, 신호, 고객 니즈, 딜 규모)
4. Joint CS-AE Strategy Meeting: 컨텍스트 이전, 역할 분담
5. Expansion Pipeline Progression: AE가 Stage 4 Canon에 따라 진행, CS는 관계 유지

| 메트릭 | 목표 |
|--------|------|
| Signal-to-Qualified | >30% |
| Handoff-to-Win | >50% |
| Signal→Handoff 소요 | <14일 |
| NRR Impact | +10pp |

---

#### Play 05: Win/Loss Analysis

**목적**: 승패 패턴 → Playbook 업데이트 — Canon Stage 7 (전체 피드백)

| 항목 | 내용 |
|------|------|
| **Trigger** | Per-deal: Closed Won/Lost 즉시. Quarterly: 분기 종료 후 2주 |
| **산출물** | 딜별 Debrief Sheet + 분기 Aggregate Report + Playbook 업데이트 |

**프로세스**:
1. Per-deal Debrief (3-5일 내): Agent가 MEDDICC 점수, Call 핵심 순간, Loss Reason 포함 Debrief Sheet 자동 생성
2. Buyer Interview (상위 20% ACV 딜 선별): Win 6문항 / Loss 6문항 구조화된 인터뷰
3. Quarterly Aggregate: Agent 자동 생성 — Win/Loss 분포 (Tier/소스/경쟁사별), MEDDICC 상관 분석, Sales Cycle 분석
4. Insight → Action: Playbook 업데이트, Agent Prompt 수정, 프로세스 개선, 교육 반영

| 메트릭 | 목표 |
|--------|------|
| Debrief Completion Rate | >90% |
| Buyer Interview Rate | >50% (상위 ACV) |
| Insight-to-Action Rate | >70% |
| Win Rate 개선 추세 | 분기별 추적 |

---

#### Play 06: Inbound Lead Handling

**목적**: 인바운드 5분 내 응대 → SQL — Canon Stage 3→4

| 항목 | 내용 |
|------|------|
| **Trigger** | 웹 폼, 콘텐츠 다운로드, 이벤트 등록, 채팅, 추천, Trial 가입 |
| **SLA** | P1/P2 (Demo, Pricing): <5분, P3: <2시간 |

**프로세스**:
1. Instant Capture & Enrichment (0-2분): 폼 파싱, Enrichment API, LinkedIn 매치, CRM 중복 체크, ICP Fit 즉시 계산
2. Lead Scoring & Routing (2-5분): Composite Score = ICP Fit + Source Priority + Engagement + Intent → 라운드 로빈 (territory/workload), 3분 미응답 시 fallback
3. Speed-to-Lead Response: 소스별 대응 — Demo 요청: AE 직접 콜 5분 + 캘린더 / Trial: SDR 전화 + 셋업 도움 / 추천: SDR이 추천인 이름 언급
4. Qualification (Day 1-3): BANT + MEDDICC, SQL/MQL/Disqualify 분류
5. Non-SQL Nurture: 페르소나별 시퀀스 배정, 90일 재활용 규칙

| 메트릭 | 목표 |
|--------|------|
| Speed to Lead | <5분 (P1/P2) |
| 5-min Response Rate | >80% |
| Lead-to-SQL Conversion | 15-25% (Demo 30-50%) |
| SQL-to-Opp | >60% |
| Enrichment Coverage | >90% |

**Tier별 자동화**: T2 — Agent enrichment + 초안, SDR 검토. T3 — Agent가 채팅 포함 풀 사이클 처리, SDR은 요약만 검토.

---

#### Play 07: Partner Channel Sales

**목적**: 파트너 협업 파이프라인 — Canon Stage 3→4→5→6

| 항목 | 내용 |
|------|------|
| **Trigger** | 파트너 온보딩 완료, 파트너 리드 제출, Deal registration, Co-marketing 이벤트 |
| **파트너 유형** | Referral, Reseller, Technology, SI (System Integrator) |

**프로세스**:
1. Partner Onboarding (D1-30): CRM 등록 (Type=Partner), Enablement kit 자동 발송, Certification 트래킹 (14-30일), 첫 Joint Planning 세션
2. Deal Registration: 파트너가 필수 정보 제출 → Agent 자동 검증 (CRM 충돌, ICP Fit, Certification, 중복) → 자동 승인 or Partner Manager 에스컬레이션
3. Co-selling: Joint Account Planning (Agent가 Overlap 분석 자동 생성), Partner-assisted Demo
4. Lead Handling SLA: Referral 4시간, Reseller 24시간, Feedback 72시간마다, 첫 미팅 7일 내
5. Commission: Closed Won 시 자동 계산 (Referral 10-15%, Reseller 20-35%, Tech 5-10%, SI 10-15%)

| 메트릭 | 목표 |
|--------|------|
| Partner-sourced Pipeline | >25% |
| Partner Win Rate | >35% |
| Revenue from Partners | >20% |
| Active Partner Rate | >60% |
| Time-to-First-Deal (신규) | <90일 |
| Commission Accuracy | >99% |

**Tier별 자동화**: Referral — T3 AI-led (자동 리드 처리). Reseller/Tech — T2 Co-pilot (검증 + 라우팅). SI — T1 Human-led.

---

## 5. Agent 아키텍처

### BCG 5-Agent 모델 개요

BCG의 "How AI Agents Will Transform B2B Sales" 논문에서 제시된 5-Agent 모델을 본 프로젝트에 맞게 adapted. Orchestration Agent가 중앙에서 라우팅하고, 5개 전문 Agent가 각 도메인을 담당한다.

### Agent 상호작용 다이어그램

```
                    ┌─────────────────────┐
                    │  Orchestration Agent │
                    │  (Router & Planner)  │
                    └─────────┬───────────┘
                              │
          ┌───────────┬───────┼───────┬────────────┐
          ▼           ▼       ▼       ▼            ▼
    ┌───────────┐ ┌────────┐ ┌─────┐ ┌──────┐ ┌────────┐
    │   Lead    │ │ Qual   │ │Deal │ │  CS  │ │  Ops   │
    │Generation │ │ Agent  │ │Agent│ │Agent │ │Analyst │
    └─────┬─────┘ └───┬────┘ └──┬──┘ └──┬───┘ └───┬────┘
          │           │         │       │         │
          └─────┬─────┘         │       │         │
                │               │       │         │
          ┌─────▼───────────────▼───────▼─────────▼────┐
          │                                              │
          │         CRM (Single Source of Truth)          │
          │      + Playbook RAG (pgvector)               │
          │                                              │
          └──────────────────────────────────────────────┘
```

**데이터 흐름**:
- 모든 Agent는 CRM을 통해 읽기/쓰기 (shadow DB 금지)
- Playbook RAG를 참조하여 방법론 기반 판단
- Orchestration Agent가 task를 라우팅하고, 결과를 수집

### 각 Agent 역할 상세

| Agent | 역할 | Input | Output | 자율성 수준 |
|-------|------|-------|--------|-----------|
| **Orchestration** | 태스크 라우팅, 워크플로우 규칙 적용, 핸드오프 조정, 우선순위 관리 | CRM event, schedule trigger, user request | 태스크 할당, 핸드오프 실행, 에스컬레이션 | Assisted → Autonomous |
| **Lead Generation** | 시장 스캐닝, 리드 enrichment, ICP 3축 스코어링, 아웃바운드 시퀀스 초안 | Target Account List, 외부 데이터 소스 | Enriched Account, ICP Score, 이메일 초안 | High (데이터 중심) |
| **Qualification** | 콜 트랜스크립트 MEDDICC 추출, 딜 스코어링, stage gate 검증, next-best-action | Call transcript, CRM Opportunity | MEDDICC 필드, 딜 스코어, 추천 액션 | Medium (사람 검증) |
| **Deal Conversion** | 제안서 초안, 가격 최적화, 할인 검증, 계약 검토, 온보딩 핸드오프 | Qualified Opportunity, 가격 정책 | 제안서 draft, 가격 시나리오, 핸드오프 문서 | Medium (승인 게이트) |
| **Customer Success** | Health Score 산출, 이탈 리스크 감지, expansion signal, QBR 자료, 갱신 예측 | Usage data, Support tickets, NPS | Health Score, 리스크 알림, QBR 보고서 | High (트리거 기반) |
| **Ops Analyst** | 파이프라인 리포트, 예측, Win/Loss 분석, 이상 감지 | CRM 전체 데이터 | 주간/월간 리포트, 예측, 패턴 인사이트 | High (읽기 전용) |

### Tier별 자동화 수준 매트릭스

| 활동 | T1 Strategic | T2 Core | T3 Long-tail |
|------|-------------|---------|-------------|
| Account Research | Agent 작성, 사람 검토 | Agent 자동 | Agent 자동 |
| Outbound Email | 사람 작성 | Agent 초안 → 사람 발송 | Agent 자동 발송 |
| Discovery Call 준비 | Agent briefing 자료 | Agent briefing | Agent briefing |
| MEDDICC 업데이트 | Agent 추출 → 사람 검토 | Agent 추출 → 사람 승인 | Agent 자동 업데이트 |
| 제안서 작성 | 사람 작성, Agent 데이터 | Agent 초안 → 사람 편집 | Agent 자동 (표준 제안) |
| QBR 자료 | Agent 초안 → 사람 커스터마이징 | Agent 자동 생성 | 해당 없음 |
| 리포트/예측 | Agent 자동 | Agent 자동 | Agent 자동 |

---

## 6. CRM 데이터 모델

### 5개 Core Object

```
┌──────────┐       ┌──────────┐       ┌──────────────┐
│ Account  │──1:N──│ Contact  │       │  Opportunity │
│          │       │          │──N:1──│              │
│ ICP Score│       │ Role     │       │  MEDDICC 7   │
│ Tier     │       │ Engage   │       │  Stage       │
│ Health   │       │ Level    │       │  Win/Loss    │
└────┬─────┘       └──────────┘       └──────┬───────┘
     │                                        │
     │         ┌──────────┐                   │
     └──1:N──▶│ Activity  │◀──N:1─────────────┘
              │          │
              │ Type     │
              │ Outcome  │
              └──────────┘
                    │
              ┌─────▼────┐
              │  Case/   │
              │  Ticket  │
              └──────────┘
```

### 주요 커스텀 필드

**Account Object**:

| 필드 | API Name | 타입 | 설명 |
|------|----------|------|------|
| ICP Score | `ICP_Score__c` | Number(0-160) | ICP 3축 종합 점수 |
| Account Tier | `Account_Tier__c` | Picklist(T1/T2/T3) | 계정 등급 |
| Health Score | `Health_Score__c` | Number(0-100) | 고객 건강도 (CS) |
| Annual Revenue | `Annual_Revenue__c` | Currency | 연매출 |
| Tech Stack | `Tech_Stack__c` | Multi-Select | 사용 기술 스택 |
| Last Enrichment Date | `Last_Enrichment__c` | DateTime | 마지막 enrichment 시점 |

**Opportunity Object — MEDDICC 필드**:

| MEDDICC | API Name | 타입 | Agent 자동화 |
|---------|----------|------|------------|
| Metrics | `Metrics__c` | Long Text | 콜 트랜스크립트에서 자동 추출 |
| Economic Buyer | `Economic_Buyer__c` | Lookup(Contact) | 조직도 기반 추천 |
| Decision Criteria | `Decision_Criteria__c` | Long Text | 대화 분석 자동 추출 |
| Decision Process | `Decision_Process__c` | Long Text | 발견 시 자동 기록 |
| Identified Pain | `Identified_Pain__c` | Long Text | Gap Selling 프레임 자동 분류 |
| Champion | `Champion_Name__c` | Lookup(Contact) | 행동 패턴 기반 후보 추천 |
| Competition | `Competitor__c` | Multi-Select | 언급 감지 자동 태깅 |
| MEDDICC Score | `MEDDICC_Score__c` | Number(0-21) | 7요소 합산 자동 계산 |

### Dashboard 5종

| # | Dashboard | 주요 위젯 | 주기 |
|---|-----------|---------|------|
| 1 | **Pipeline Health** | 파이프라인 금액, Stage 분포, Coverage Ratio, Aging | 실시간 |
| 2 | **Sales Velocity** | Win Rate, Cycle Length, ACV, Velocity Index | 주간 |
| 3 | **Activity Metrics** | Activity-to-Opp ratio, 채널별 효율, Rep별 활동량 | 주간 |
| 4 | **Forecast Accuracy** | Commit vs Actual, 카테고리별 정확도, 월별 추이 | 월간 |
| 5 | **CS & Retention** | GRR/NRR, Health Score 분포, Churn Risk, Expansion Pipeline | 월간 |

### 데이터 품질 규칙

| 규칙 | 적용 대상 | 동작 |
|------|---------|------|
| Stage 전환 시 MEDDICC 최소 점수 | Opportunity | 미달 시 전환 차단 + Agent 알림 |
| 필수 필드 미입력 시 경고 | Account, Contact | 생성 후 48시간 내 미입력 시 Manager 알림 |
| 90일 이상 미접촉 계정 | Account | 자동 플래그 + re-engagement 시퀀스 트리거 |
| Win/Loss 사유 미입력 | Closed Won/Lost Opp | 72시간 내 미입력 시 에스컬레이션 |

---

## 7. 기술 스택 & PoC

### 7.1 기술 스택 비교 결정

#### Workflow Engine 비교

| 기준 | n8n | Zapier | Make |
|------|-----|--------|------|
| Self-Hosting | **O (핵심 장점)** | X | X |
| AI Agent Node | **O (내장)** | AI by Zapier (제한적) | X |
| CRM 연동 | 400+ 노드 | 7,000+ 앱 | 1,800+ 앱 |
| 가격 (Self-hosted) | **$0** | $20-600/mo | $9-300/mo |
| 코드 노드 | JS + Python | 코드 제한적 | JS |
| PE Portfolio 배포 | **Docker 복제** | 계정별 과금 | 계정별 과금 |

**선정**: **n8n (self-hosted)** — Self-hosting으로 비용 $0, AI Agent node 내장, Docker로 portfolio 배포 가능.

#### Agent Framework 비교

| 기준 | CrewAI | LangChain/LangGraph | AutoGen | OpenAI Assistants | Claude SDK |
|------|--------|---------------------|---------|-------------------|------------|
| Multi-Agent | **Native (핵심)** | LangGraph로 가능 | Native (대화) | 수동 구현 | SDK로 가능 |
| BCG 5-Agent 매핑 | **1:1 개념 매핑** | Graph 설계 필요 | 대화 패턴 | 미지원 | 수동 설계 |
| Setup 용이성 | **높음** | 낮음 | 낮음 | 매우 높음 | 중간 |
| LLM 자유도 | 모든 LLM | 모든 LLM | Azure 중심 | GPT only | Claude only |
| 가중 합계 | **4.02** | 4.03 | 2.79 | 2.89 | 3.66 |

**선정**: **CrewAI** (Production) — BCG 5-Agent 모델의 role-based 구조와 1:1 매핑. Hierarchical process로 Orchestration Agent 구현.

#### 최종 기술 스택 결정

| 레이어 | PoC | Production | 선정 근거 |
|--------|-----|-----------|----------|
| Workflow | n8n (self-hosted) | n8n (유지) | Self-hosting, AI node, CRM 내장, 무료 |
| Agent Framework | n8n AI Agent node | CrewAI | BCG 5-Agent 1:1 매핑, role-based |
| LLM | Claude API (Sonnet) | Claude Sonnet + Haiku | Reasoning 품질, 200K context, Haiku for T3 비용 |
| Vector DB | Supabase pgvector | PostgreSQL pgvector | CRM 데이터 동거, ACID, self-hosting |
| Monitoring | Helicone (free) | Langfuse (self-hosted) | 오픈소스, portfolio 배포 가능 |
| API Server | — | FastAPI (CrewAI 래퍼) | n8n ↔ CrewAI 연동 |

### 7.2 PoC 3종 요약

#### 인프라 구성

```
┌──────────────────────────────────────────────────────┐
│                 Docker Compose                        │
│                                                       │
│   ┌─────────────────┐    ┌──────────────────────┐    │
│   │  n8n (port 5678) │    │ PostgreSQL + pgvector │    │
│   │  Workflow Runtime│    │    (port 5432)        │    │
│   └────────┬────────┘    └──────────┬───────────┘    │
│            │                        │                  │
│            ▼                        ▼                  │
│   ┌─────────────┐          ┌──────────────┐          │
│   │  Claude API  │          │  4 DB Tables  │          │
│   │  (External)  │          │  - playbook   │          │
│   └─────────────┘          │    _chunks    │          │
│                             │  - meddicc    │          │
│   ┌─────────────┐          │    _extracts  │          │
│   │    Slack     │          │  - agent_exec │          │
│   │  (Optional)  │          │  - lead_enrich│          │
│   └─────────────┘          └──────────────┘          │
└──────────────────────────────────────────────────────┘
```

#### PoC 상세

| | PoC #1: Post-Call CRM Updater | PoC #2: Weekly Ops Report | PoC #3: Lead Enrichment |
|---|---|---|---|
| **트리거** | Webhook (콜 트랜스크립트) | Schedule (매주 월 08:00 KST) | Webhook (신규 계정) |
| **Agent** | Qualification Agent | Ops Analyst Agent | Lead Generation Agent |
| **프로세스** | 트랜스크립트 → MEDDICC 7요소 추출 → 점수 산출 → CRM 업데이트 draft | DB 파이프라인 쿼리 → 트렌드 분석 → 마크다운 리포트 생성 | 계정 데이터 수집 → ICP 3축 스코어링 → Tier 분류 → 추천 액션 |
| **산출물** | MEDDICC 필드 + 점수 + next action | 파이프라인 리포트 (Slack/Email) | ICP Score + Tier + enrichment 데이터 |
| **비용/실행** | ~$0.02 (3K input + 2K output) | ~$0.04 (5K input + 3K output) | ~$0.02 (2K input + 2K output) |
| **검증 포인트** | MEDDICC 추출 정확도, CRM 필드 매핑 | 리포트 품질, 인사이트 유용성 | ICP 스코어 정확도, enrichment 커버리지 |

---

## 8. 산업 벤치마크 & 사례

### KPI 벤치마크 주요 수치

| 메트릭 | 업계 평균 | 상위 25% | 프로젝트 목표 | 평가 |
|--------|---------|---------|-------------|------|
| Win Rate (Overall) | 20-25% | 30-35% | >30% | Realistic |
| Win Rate (Enterprise) | 15-20% | 25%+ | — | — |
| Sales Cycle (Mid-Market) | 60-90일 | 45-60일 | <90일 | Realistic |
| ACV (Mid-Market B2B) | $25K-$75K | $75K+ | — | — |
| Pipeline Coverage | 3-4x | 4-5x | 3-5x | Realistic |
| Gross Retention Rate | 85-90% | >93% | >90% | Stretch |
| Net Revenue Retention | 100-110% | 120%+ | >110% | Realistic |
| Forecast Accuracy | 70-80% | 85%+ | >85% | Stretch |
| MEDDICC Adoption (6mo) | 40-50% | 70%+ | >80% | Ambitious |
| Rep Admin Time Saved (AI) | 5-8 hrs/wk | 10+ hrs/wk | 10+ hrs/wk | Ambitious |

**프로젝트 KPI 평가 요약**: 48% Realistic, 36% Stretch, 16% Ambitious

### AI Sales Agent 성공 사례

| 기업 | AI 적용 범위 | 핵심 성과 |
|------|------------|----------|
| **Ramp** | AI SDR "Ramp Rep" | 파이프라인 40% 자동 생성, SDR 효율 3x 향상 |
| **Deel** | AI Lead Scoring + Routing | Win Rate 25→35%, Speed-to-Lead 4hr→15min |
| **Snowflake** | AI-assisted MEDDICC | CRM 데이터 완성도 45→85%, 예측 정확도 +20% |
| **ZoomInfo** | AI-powered Enrichment | Enrichment 정확도 95%+, 리서치 시간 60% 감소 |
| **Vista Equity** | Portfolio 공통 AI 영업 | 포트폴리오 전체 Win Rate 5pp 개선 |
| **Rippling** | AI Meeting Prep + Follow-up | 미팅 전환율 30% 개선, Follow-up 시간 75% 감소 |
| **HubSpot** | Breeze AI (자체 AI) | 리드 스코어링 정확도 40% 향상 |

### 실패 사례 교훈

| 실패 유형 | 원인 | 교훈 | 본 프로젝트 대응 |
|----------|------|------|----------------|
| AI SDR 응답률 급락 | 개인화 부족, 스팸 감지 | Tier별 자동화 수준 차별화 | T1 수동, T2 Co-pilot, T3 AI-led |
| CRM 데이터 오염 | AI가 잘못된 데이터 자동 입력 | Human-in-the-loop 필수 | 모든 CRM 쓰기에 검증 단계 |
| PE 강제 도입 실패 | 현장 저항, 교육 부재 | "시간 절약" Agent부터 시작 | Post-Call Updater (PoC #1)로 시작 |
| 블랙박스 예측 | 예측 근거 불투명 | 투명한 reasoning chain | Claude Extended Thinking 활용 |
| 브랜드 톤 불일치 | AI 생성 문체가 회사와 안 맞음 | Playbook 기반 톤 가이드 | Playbook RAG로 일관된 톤 유지 |

### 시장 규모

AI Sales Agent 시장 규모: **$5.6B** (2024), 연 성장률 30%+ 전망.
주요 벤더: Salesforce Einstein, HubSpot Breeze, Gong, Clari, ZoomInfo, Salesloft, 11x.ai, Artisan AI 등.

---

## 9. 로드맵 & Next Steps

### 현재 완료 상태

| Phase | 상태 | 산출물 |
|-------|------|--------|
| Phase 1: Foundation | ✅ 완료 | Sales Canon, ICP Framework, Tier Model, KPI Set |
| Phase 2: Playbook | ✅ 완료 | 9개 Playbook 문서, 7개 Play, Call Scripts, Email Templates, MEDDICC Guide |
| Phase 3: CRM | ✅ 설계 완료 | CRM Schema, 5 Dashboard 설계, Data Quality Rules, API Mapping |
| Phase 4: Agent PoC | ⬜ 스캐폴딩 | PoC 3종 코드, Docker 환경, 시스템 프롬프트, 테스트 데이터 |
| Phase 5: Scale | ⬜ 미착수 | — |

### 다음 작업 (선행 조건별)

| 순서 | 작업 | 선행 조건 | 예상 기간 |
|------|------|----------|----------|
| 1 | **PoC #1 실행** (Post-Call CRM Updater) | OpenAI/Claude API 키 + Docker | 1-2주 |
| 2 | 파일럿 포트폴리오사 선정 | PE Ops VP 의사결정 | 의사결정 대기 |
| 3 | ICP 기준값 실제 데이터 검증 | 고객 데이터 접근 | 1주 |
| 4 | CRM 인스턴스 접근 + 필드 매핑 | CRM admin 권한 | 2-3주 |
| 5 | PoC #2-3 빌드 | PoC #1 검증 완료 | 2-3주 |
| 6 | Playbook RAG 벡터화 | pgvector 구축 (Docker에 포함) | 1주 |
| 7 | CrewAI Production 전환 | PoC 전체 검증 완료 | 4-8주 |

### 리스크 & 의존성

| 리스크 | 영향도 | 완화 전략 |
|--------|--------|---------|
| Playbook 없이 Agent 빌드 | Agent 환각, 비일관 출력 | Phase 1-2를 Phase 4의 hard prerequisite로 설정 (완료) |
| CRM 데이터 품질 저하 | Agent 읽기/쓰기 부정확 | Phase 3에서 필드 거버넌스 강제 (설계 완료) |
| MEDDICC 도입 피로 (6개월 내 40-50% 이탈) | 파이프라인 진행 중단 | Agent가 지속적 nudge + compliance 알림 제공 |
| T1 계정 과자동화 | 전략적 관계 손상 | Tier 기반 자율성 규칙 엄격 적용 |
| Rep AI 저항 | 낮은 도입률 | "시간 절약" Agent부터 시작, "대체" 아닌 "보조" 포지셔닝 |
| LLM 비용 폭증 | 예산 초과 | Helicone/Langfuse 모니터링, Haiku(T3) 활용, 프롬프트 최적화 |

### 의존성

- **CRM 접근**: Salesforce 또는 HubSpot Admin API 권한
- **콜 녹음**: Gong, Chorus 등 트랜스크립트 소스
- **Sales Leadership Buy-in**: Playbook 표준화 + 프로세스 변경 승인
- **LLM API**: Anthropic Claude 또는 OpenAI API 키
- **인프라**: n8n self-hosting 서버 (또는 클라우드 인스턴스)

---

## 부록

### A. 디렉토리 구조

```
salesagent/
├── CLAUDE.md                          # 프로젝트 가이드
├── agent.md                           # Agent 아키텍처 정의
├── scope.md                           # 프로젝트 범위 & 로드맵
├── todo.md                            # 작업 목록
├── report.md                          # 이 보고서
├── report.html                        # 이 보고서 (HTML 버전)
│
├── agent/                             # Agent별 상세 프롬프트
│   ├── 01_qualification_agent.md
│   ├── 02_orchestration_agent.md
│   ├── 03_lead_generation_agent.md
│   ├── 04_deal_conversion_agent.md
│   └── 05_customer_success_agent.md
│
├── crm/
│   └── schema.md                      # CRM 데이터 모델
│
├── poc/                               # PoC 스캐폴딩
│   ├── README.md
│   ├── docker-compose.yml
│   ├── .env.example
│   ├── workflows/                     # n8n 워크플로우 3종
│   ├── prompts/                       # 시스템 프롬프트 3종
│   ├── scripts/                       # 셋업 & 테스트 스크립트
│   └── fixtures/                      # 테스트 데이터
│
├── playbook/                          # 영업 Playbook
│   ├── 00_sales_process_canon.md      # 7-Stage Canon
│   ├── 01_icp_and_scoring.md          # ICP & 스코어링
│   ├── 02_meddicc_guide.md            # MEDDICC 가이드
│   ├── 03_call_scripts.md             # 콜 스크립트
│   ├── 04_email_templates.md          # 이메일 템플릿
│   ├── 05_objection_handling.md       # 반론 대응
│   ├── 06_competitive_battle_card.md  # 경쟁 Battle Card
│   ├── 07_pricing_discount_matrix.md  # 가격 & 할인
│   ├── 08_sales_onboarding_curriculum.md  # 온보딩
│   └── plays/                         # 7개 Play
│       ├── play_01 ~ play_07
│
└── research/                          # 산업 리서치
    ├── 01_kpi_benchmarks.md
    ├── 02_ai_sales_agent_cases.md
    └── 03_tech_stack_comparison.md
```

### B. 문서 목록 & 분량

| 문서 | 파일 | 예상 분량 |
|------|------|----------|
| Sales Process Canon | `playbook/00_sales_process_canon.md` | ~350줄 |
| ICP & Scoring | `playbook/01_icp_and_scoring.md` | ~350줄 |
| MEDDICC Guide | `playbook/02_meddicc_guide.md` | ~450줄 |
| Call Scripts | `playbook/03_call_scripts.md` | ~500줄 |
| Email Templates | `playbook/04_email_templates.md` | ~600줄 |
| Objection Handling | `playbook/05_objection_handling.md` | ~500줄 |
| Competitive Battle Card | `playbook/06_competitive_battle_card.md` | ~550줄 |
| Pricing & Discount | `playbook/07_pricing_discount_matrix.md` | ~450줄 |
| Sales Onboarding | `playbook/08_sales_onboarding_curriculum.md` | ~400줄 |
| 7 Plays | `playbook/plays/play_01~07` | 각 ~250줄 |
| Agent Architecture | `agent.md` | ~150줄 |
| 5 Agent Specs | `agent/01~05` | 각 ~300줄 |
| CRM Schema | `crm/schema.md` | ~500줄 |
| KPI Benchmarks | `research/01_kpi_benchmarks.md` | ~500줄 |
| AI Sales Cases | `research/02_ai_sales_agent_cases.md` | ~600줄 |
| Tech Stack Comparison | `research/03_tech_stack_comparison.md` | ~1,400줄 |
| Project Scope | `scope.md` | ~175줄 |

**전체**: 약 30개 문서, 총 ~10,000줄

### C. 용어집

| 용어 | 설명 |
|------|------|
| **ACV** | Annual Contract Value. 연간 계약 금액 |
| **AE** | Account Executive. 영업 담당자 |
| **Battle Card** | 경쟁사 대비 포지셔닝 정보를 정리한 1-page 가이드 |
| **Canon** | 포트폴리오 공통 영업 프로세스 표준 (7단계) |
| **CAC** | Customer Acquisition Cost. 고객 획득 비용 |
| **Champion** | 고객사 내부에서 우리 솔루션을 옹호하는 핵심 인물 |
| **Co-pilot** | Agent가 초안을 작성하고 사람이 검토/승인하는 협업 모드 |
| **CRM** | Customer Relationship Management. Salesforce, HubSpot 등 |
| **CrewAI** | Role-based multi-agent framework (Production 선정) |
| **EB** | Economic Buyer. 최종 예산 결정권자 |
| **Enrichment** | 외부 데이터를 수집하여 계정/리드 정보를 보강하는 프로세스 |
| **Gap Selling** | Current State → Future State → Gap 프레임워크 (Keenan) |
| **GRR** | Gross Revenue Retention. 총 매출 유지율 (확장 제외) |
| **Health Score** | 고객 건강도 지수 (0-100, Usage/Support/Engagement 기반) |
| **ICP** | Ideal Customer Profile. 이상적 고객 프로필 (3축 스코어링) |
| **Langfuse** | 오픈소스 LLM 모니터링 도구 (Production 선정) |
| **MEDDICC** | Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion, Competition. 딜 적격성 프레임워크 |
| **MCP** | Model Context Protocol. Anthropic의 외부 도구 연결 표준 |
| **n8n** | Self-hosted workflow automation 플랫폼 (PoC + Production) |
| **NRR** | Net Revenue Retention. 순 매출 유지율 (확장 포함) |
| **pgvector** | PostgreSQL 벡터 검색 extension (Vector DB 선정) |
| **Play** | 특정 상황에 대한 실행 가이드 (Input→Process→Output→Metric→Tool/Agent) |
| **QBR** | Quarterly Business Review. 분기별 비즈니스 리뷰 |
| **RAG** | Retrieval-Augmented Generation. 벡터 검색 기반 LLM 컨텍스트 주입 |
| **SDR** | Sales Development Representative. 리드 발굴 담당자 |
| **SPIN** | Situation-Problem-Implication-Need payoff. 질문 기반 영업 프레임워크 |
| **SQL** | Sales Qualified Lead. 영업 적격 리드 |
| **T1/T2/T3** | Account Tier. Strategic(사람 주도) / Core(Co-pilot) / Long-tail(AI 주도) |
| **TCO** | Total Cost of Ownership. 총 소유 비용 |

---

*이 보고서는 2026-03-09 기준으로 작성되었으며, 프로젝트 진행에 따라 업데이트됩니다.*
