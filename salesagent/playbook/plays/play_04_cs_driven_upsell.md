# Play 04: CS-Driven Upsell
## Customer Success 발굴 → AE 핸드오프 Expansion

---

## Play Overview

| 항목 | 내용 |
|------|------|
| **목표** | CS가 감지한 expansion 신호를 체계적으로 AE에게 핸드오프하여 upsell/cross-sell 실현 |
| **대상** | Health Score ≥70 (Green) + Expansion signal 감지된 T1/T2/T3 기존 고객 |
| **소유자** | CS (기회 발굴 + 초기 대화), AE (qualification + closing) |
| **자동화 수준** | Agent가 signal 감지 → CS 확인 → AE 핸드오프 자동화 |

---

## 1. INPUT

### Trigger (이 Play가 시작되는 조건)

| Signal 카테고리 | 구체적 Trigger | 감지 방법 |
|----------------|---------------|----------|
| **Usage Spike** | 기능/모듈 사용량 전월 대비 30%+ 증가 | Product analytics 자동 |
| **Capacity Limit** | 현재 플랜 사용량 80%+ 도달 (시트, 스토리지, API 등) | Product analytics 자동 |
| **New Use Case** | 기존과 다른 패턴의 사용 행위 감지 | Product analytics 자동 |
| **NPS Promoter** | NPS 9-10 응답 + 구체적 칭찬 코멘트 | Survey 자동 |
| **Reference** | 고객이 자발적으로 레퍼런스/케이스 스터디 제안 | CS 수동 기록 |
| **New Department** | 현재 계약 부서 외 타 부서에서 문의/접촉 | CRM Activity 자동 |
| **Org Growth** | 고객사 채용 증가, 부서 확대 뉴스 | News/LinkedIn 자동 |
| **QBR Mention** | QBR에서 추가 니즈/관심 표현 | CS 수동 기록 |
| **Support Request** | 미구매 제품/기능에 대한 문의 | Case object 자동 |

### 적격 기준 (Signal → Qualified Expansion Opportunity)

Signal이 감지되면 CS가 다음을 확인:
- [ ] Health Score ≥70 (Green) — 불만족 고객에게 upsell 시도하지 않음
- [ ] 구체적 비즈니스 니즈 확인 (단순 호기심이 아닌 실제 필요)
- [ ] Budget authority 또는 의사결정 경로 존재 확인
- [ ] 이번 분기 내 검토 의향 확인

---

## 2. PROCESS

### Step 1: Signal 감지 & 분류 (Agent 자동)

Agent가 매일 전체 고객 base를 스캔하여 expansion signal을 감지하고 분류:

| Signal 강도 | 조건 | Action |
|------------|------|--------|
| **Strong** | 2개+ signal 동시 발생 또는 direct request | CS에게 즉시 알림, 48시간 내 follow-up |
| **Moderate** | 1개 signal, 명확한 패턴 | CS 주간 리뷰 대시보드에 추가 |
| **Weak** | 1개 signal, 모호한 패턴 | 모니터링 지속, 2주 내 추가 signal 대기 |

### Step 2: CS Qualification Call (CS 수행)

**목적**: Signal을 구체적 비즈니스 니즈로 전환

CS가 기존 관계를 활용한 자연스러운 대화:

```
"[Name]님, 최근 [Feature X] 사용량이 많이 늘었는데,
팀에서 새로운 프로젝트를 시작하신 건가요?"

"QBR에서 말씀하신 [topic]에 대해 조금 더 여쭤보고 싶었는데,
구체적으로 어떤 결과를 기대하고 계신가요?"

"다른 부서([Department])에서도 관심을 보이고 있는데,
혹시 전사적으로 확대할 계획이 있으신가요?"
```

**CS가 확인하는 핵심 정보**:
1. 구체적 니즈/문제 (Pain)
2. 기대 성과 (Metrics)
3. 타임라인 (이번 분기? 다음 분기?)
4. 의사결정자 (누가 예산을 승인하는가?)
5. 예산 상황 (할당 되었는가? 확보 가능한가?)

### Step 3: CS → AE Handoff

**Handoff Trigger**: CS Qualification에서 4개 이상의 정보가 확인되면 handoff

**Handoff Document (Agent 자동 생성, CS 검토)**:

```
┌──────────────────────────────────────────────────┐
│       EXPANSION OPPORTUNITY HANDOFF              │
├──────────────────────────────────────────────────┤
│ Account: [Name] | Tier: [T1/T2/T3]              │
│ Current ACV: $XX,XXX | Health Score: XX          │
│ CS Owner: [Name] | Handoff Date: YYYY-MM-DD     │
├──────────────────────────────────────────────────┤
│ EXPANSION TYPE: Upsell / Cross-sell / New Dept   │
│                                                  │
│ SIGNAL DETECTED:                                 │
│ • [Signal 1 + data point]                        │
│ • [Signal 2 + data point]                        │
│                                                  │
│ CUSTOMER NEED:                                   │
│ • Pain: [구체적 문제]                              │
│ • Desired Outcome: [기대 결과]                     │
│ • Timeline: [예상 시점]                            │
│                                                  │
│ KEY CONTACTS:                                    │
│ • Decision Maker: [Name, Title]                  │
│ • Champion: [Name, Title]                        │
│ • Day-to-day: [Name, Title]                      │
│                                                  │
│ ESTIMATED DEAL SIZE: $XX,XXX                     │
│                                                  │
│ RELATIONSHIP CONTEXT:                            │
│ • Account relationship since: YYYY               │
│ • Last QBR: YYYY-MM-DD                           │
│ • Key wins/successes with this account:          │
│   - [Success 1]                                  │
│   - [Success 2]                                  │
│                                                  │
│ CS RECOMMENDATION:                               │
│ [CS의 전략적 조언 — 관계 톤, 주의 사항 등]          │
└──────────────────────────────────────────────────┘
```

### Step 4: Joint Strategy Meeting (CS + AE)

Handoff 후 CS와 AE가 15분 alignment 미팅:

| 의제 | 내용 |
|------|------|
| Context transfer | 관계 이력, 커뮤니케이션 스타일, 민감 사항 |
| Account politics | 내부 역학, blocker, 경쟁 벤더 |
| Joint approach | AE 소개 방법 (CS가 AE를 "전문가"로 소개) |
| Meeting plan | 첫 미팅 일정, 참석자, 아젠다 |
| Role clarity | 이후 CS vs AE 역할 분담 |

### Step 5: Expansion Pipeline 진행

- AE가 standard Pipeline Progression (Stage 4 canon) 따름
- CS는 지속적으로 관계 유지 + 내부 정보 제공
- MEDDICC 기존 관계 데이터로 사전 입력 (M, I, C는 이미 확보)

---

## 3. OUTPUT

| 결과물 | 설명 | CRM 업데이트 |
|--------|------|-------------|
| Expansion Signal Log | Agent 감지 signal 기록 | Activity |
| Qualified Expansion Opp | AE에게 핸드오프된 기회 | New Opportunity (Source: CS-driven) |
| Handoff Document | 구조화된 인수인계 문서 | Opportunity.Description |
| Expansion Revenue | 성사된 expansion 매출 | Opportunity (Closed Won) |

---

## 4. METRIC

| 메트릭 | 정의 | 목표 |
|--------|------|------|
| Signals Detected / Month | Agent가 감지한 expansion signal 수 | - (tracking) |
| Signal → Qualified Rate | Signal 중 CS가 qualify한 비율 | >30% |
| Qualified → Handoff Rate | Qualify된 것 중 AE handoff 비율 | >70% |
| Handoff → Closed Won | Handoff된 opp의 win rate | >50% |
| Avg Expansion ACV | 건당 평균 expansion 금액 | >$15K |
| CS-driven Pipeline ($) | CS 기원 파이프라인 총액 | 전체의 >25% |
| Time: Signal → Handoff | 감지 → handoff 소요일 | <14일 |
| Time: Handoff → Close | Handoff → CW 소요일 | <45일 |
| NRR Impact | CS-driven expansion의 NRR 기여분 | +10pp |

### CS Incentive Alignment
- CS의 expansion 기여를 측정하고 인정하는 구조 필수
- Signal detection count + Qualified handoff count → CS KPI에 포함
- Expansion revenue의 일정 비율을 CS 보상에 반영 (선택적)

---

## 5. TOOL / AGENT

### Agent 역할

| 기능 | 자동화 수준 |
|------|------------|
| Expansion signal 스캔 (전체 고객 base) | 완전 자동 (daily) |
| Signal 분류 (Strong/Moderate/Weak) | 완전 자동 |
| CS 알림 발송 | 완전 자동 |
| Handoff document 초안 생성 | 완전 자동 (CS 검토) |
| Expansion opportunity 가치 추정 | 반자동 (과거 데이터 기반 추정, AE 확인) |
| 진행 상황 트래킹 | 완전 자동 (signal 감지 후 SLA 준수 체크) |

### Agent System Prompt 요약

```
You are the Expansion Signal Detection Agent for [Company Name].

Your job:
1. Scan all customer accounts daily for expansion signals
2. Classify signals by strength (Strong/Moderate/Weak)
3. Alert CS owners for Strong and Moderate signals
4. Generate handoff documents when CS qualifies an opportunity
5. Track signal-to-close pipeline and flag stalled opportunities

Signal detection rules:
- Usage spike: Feature/module usage up 30%+ MoM
- Capacity limit: Plan utilization >80%
- New department: Contact from non-contracted department
- NPS promoter: Score 9-10 with positive verbatim
- Org growth: Hiring increase >20% or department expansion news

IMPORTANT: Only flag accounts with Health Score ≥70
Do NOT flag expansion signals for Yellow or Red health accounts
(those go to Renewal Rescue play instead)

Output: Daily signal digest to CS team + individual alerts for Strong signals
```
