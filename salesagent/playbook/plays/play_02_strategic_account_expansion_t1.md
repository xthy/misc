# Play 02: Strategic Account Expansion (T1)
## 기존 T1 계정의 White-Space 공략

---

## Play Overview

| 항목 | 내용 |
|------|------|
| **목표** | T1 기존 고객 계정 내 미판매 영역 발굴 및 매출 확대 |
| **대상** | Tier T1 Strategic Account, Health Score ≥ 60 (Yellow 이상) |
| **소유자** | AE (전략), CS (인사이트 제공), AM (실행) |
| **자동화 수준** | Human-led + Agent Assist (데이터 수집, 자료 생성, 기회 식별) |
| **예상 소요** | 지속적 (분기 QBR 사이클에 연동) |

---

## 1. INPUT

### Trigger (이 Play가 시작되는 조건)
- **QBR 사이클**: 분기별 QBR 30일 전 자동 시작
- **Usage Spike**: 특정 기능/모듈 사용량 전분기 대비 30%+ 증가
- **New Department Contact**: 기존 사용 부서 외 새 부서에서 접촉 발생
- **NPS/CSAT 상승**: NPS 8+ 또는 CSAT 만족 이상 응답
- **Contract Milestone**: 갱신 180일 전 (expansion과 renewal 동시 논의 기회)
- **조직 변화**: 새 예산 배정, 경영진 교체, 부서 신설
- **Agent 감지**: White-space 분석에서 미판매 제품/서비스 영역 발견

### 대상 기준
- Account Tier = T1
- Health Score ≥ 60 (Red 계정은 Renewal Rescue play로 이동)
- 현재 계약 금액 대비 White-space potential ≥ 50%
- Champion이 Active 상태

### 데이터 소스

| 데이터 | 소스 | Agent 자동화 |
|--------|------|-------------|
| 현재 계약 범위 | CRM Opportunity (CW records) | 자동 조회 |
| 제품/서비스 카탈로그 | 내부 Product DB | 자동 매핑 |
| 사용량 데이터 | Product Analytics | 자동 수집 |
| 조직도 | CRM Contact + LinkedIn | 반자동 |
| QBR 히스토리 | CRM Activity / Document store | 자동 조회 |
| 고객 성과 지표 | CS 플랫폼 / CRM | 자동 수집 |
| 산업 트렌드 | News / Research | 자동 수집 |

---

## 2. PROCESS

### Step 1: White-Space Analysis (QBR D-30)

**Agent가 자동 생성하는 White-Space Map**:

```
┌─────────────────────────────────────────────────┐
│           [Account Name] White-Space Map         │
├─────────────┬───────────┬───────────────────────┤
│ Product/    │ Current   │ Expansion             │
│ Service     │ Status    │ Opportunity            │
├─────────────┼───────────┼───────────────────────┤
│ Product A   │ ✅ Active  │ Usage at 40% capacity │
│ Product B   │ ✅ Active  │ New module available  │
│ Product C   │ ❌ None   │ HIGH: Dept X needs it │
│ Service 1   │ ✅ Active  │ Upgrade tier possible │
│ Service 2   │ ❌ None   │ MED: Adjacent use case│
│ Service 3   │ ❌ None   │ LOW: No signal yet    │
├─────────────┴───────────┴───────────────────────┤
│ Current ACV: $120K | White-Space Potential: $80K │
└─────────────────────────────────────────────────┘
```

**AE가 검토/보완하는 항목**:
- 각 White-space 영역의 실현 가능성 평가
- Champion과의 사전 대화에서 확인된 신규 니즈
- 정치적 요소 (부서 간 예산 경쟁, 의사결정 경로 차이)

### Step 2: Stakeholder Mapping (QBR D-25)

| 대상 | 파악 항목 | 방법 |
|------|----------|------|
| **기존 Champion** | 현재 만족도, expansion에 대한 의향, 내부 영향력 변화 | 1:1 미팅 |
| **New Department Head** | 니즈, 예산, 의사결정 구조 | Champion 소개 또는 Cold approach |
| **Economic Buyer** | 전사 우선순위 변화, 예산 상황 | Executive Sponsor 미팅 |
| **End Users** | 추가 기능 요구, 불만 사항, 활용도 | CS를 통한 피드백 수집 |
| **Potential Blockers** | 반대 의견, 경쟁 벤더 지지자 | 관계 매핑, 간접 정보 |

### Step 3: Value Story 구성 (QBR D-20)

**Agent가 초안 생성, AE가 편집**:

1. **성과 리뷰**: 도입 이후 달성한 Metrics (ROI, 효율성, 성과)
   - "도입 6개월 후 [Metric A] 35% 개선, [Metric B] $200K 절감"

2. **미활용 가치**: 현재 사용하지 않는 기능/역량
   - "Product A의 [Advanced Feature]를 활용하면 추가로 [X] 가능"

3. **Expansion Value Proposition**: White-space 영역별 맞춤 가치 제안
   - "[Dept X]에서 Product C를 도입하면 [specific outcome]"

4. **Peer Benchmark**: 동종 업계 유사 규모 고객 대비 활용도
   - "같은 산업의 T1 고객 평균 대비 [Feature Y] 활용도가 30% 낮음"

### Step 4: QBR 실행

**QBR Agenda (Agent가 초안 생성)**:

```
1. [10분] 파트너십 성과 리뷰
   - 합의된 KPI 달성 현황
   - 주요 성공 사례 & 학습

2. [10분] 활용도 분석 & 최적화 추천
   - 현재 사용 패턴
   - 미활용 기능 활성화 제안
   - 활용도 향상 로드맵

3. [15분] 전략적 성장 기회
   - White-space 영역 제안 (1-2개 핵심)
   - Peer benchmark & 산업 트렌드
   - ROI 시뮬레이션

4. [10분] 다음 분기 계획
   - 상호 합의 목표
   - Action items & 담당자
   - 다음 미팅 일정

5. [5분] Executive Alignment
   - 전사 우선순위와의 연계
   - Executive sponsor 피드백
```

### Step 5: Expansion Opportunity 생성

QBR 또는 ongoing 대화에서 구체적 expansion 기회가 확인되면:

1. CRM에 새 Opportunity 생성 (Source = "CS-driven Expansion")
2. Stage = S2 Qualification (이미 관계가 있으므로 S1 skip 가능)
3. MEDDICC 요소 기존 관계 기반으로 사전 입력
4. 별도의 Pipeline Progression (Play 없이 Stage 4 canon 따름)

### Step 6: Multi-Thread Expansion

| 전략 | 실행 방법 |
|------|----------|
| **Land & Expand** | 한 부서 성공 → 동일 제품 타 부서 확산 |
| **Cross-sell** | 현재 제품과 보완적인 다른 제품/서비스 제안 |
| **Upsell** | 현재 티어 → 상위 티어 업그레이드 (기능, 용량, SLA) |
| **Platform Play** | 개별 제품 → 통합 플랫폼 전환 (번들 할인) |

---

## 3. OUTPUT

| 결과물 | 설명 | CRM 업데이트 |
|--------|------|-------------|
| White-Space Map | 계정별 expansion 기회 매핑 | Account.White_Space__c 갱신 |
| QBR Deck | 성과 리뷰 + expansion 제안 자료 | Activity 기록 (Meeting) |
| Expansion Opportunity | 구체적 expansion 기회 | New Opportunity (Source: CS-driven) |
| Account Plan Update | 12개월 계획 갱신 | Account Plan 문서 업데이트 |
| Stakeholder Map Update | 신규 관계자 추가, 역할 변화 반영 | Contact.MEDDICC_Role 갱신 |

---

## 4. METRIC

| 메트릭 | 정의 | 목표 |
|--------|------|------|
| Expansion Revenue | T1 계정 expansion 매출 | 기존 ACV의 20%+ YoY |
| White-Space Conversion | 식별된 기회 → 실제 expansion 전환율 | >30% |
| QBR Execution Rate | T1 계정 분기 QBR 실행 비율 | 100% |
| Multi-Thread Depth | T1 계정당 Active contact 수 | ≥5명 |
| NRR Contribution | T1 계정의 NRR 기여 | >120% |
| Expansion Cycle Time | Expansion opp → Closed Won 소요일 | <60일 (기존 관계 leverage) |
| Avg Expansion ACV | 건당 평균 expansion 금액 | >$30K |

---

## 5. TOOL / AGENT

### Agent 역할 (T1 = Human-led이므로 보조 역할)

| 기능 | Agent 수행 | AE/CS 수행 |
|------|-----------|-----------|
| White-space 분석 | 제품 카탈로그 × 현재 계약 자동 매핑 | 실현 가능성 평가, 우선순위 결정 |
| 사용량 트렌드 분석 | 자동 데이터 수집 + 이상치 감지 | 전략적 해석 |
| QBR 자료 초안 | 성과 데이터 + 활용도 + 벤치마크 자동 생성 | 스토리라인 편집, 전략적 제안 추가 |
| Stakeholder 변화 감지 | LinkedIn/뉴스 모니터링, 이직/승진 자동 감지 | 관계 전략 수립, 직접 소통 |
| Expansion signal 감지 | Usage spike, 새 부서 접촉 등 자동 알림 | 기회 평가, 접근 전략 결정 |
| Account Plan 갱신 | 데이터 기반 섹션 자동 업데이트 | 전략적 판단, Action plan 결정 |

### Agent System Prompt 요약

```
You are the Strategic Account Intelligence Agent for T1 accounts at [Company Name].

Your job:
1. Monitor T1 account health, usage, and engagement continuously
2. Generate white-space analysis by mapping current contract vs full product catalog
3. Detect expansion signals: usage spikes, new department contacts, NPS improvements
4. Prepare QBR materials: performance review, usage analytics, peer benchmarks
5. Track stakeholder changes: job changes, new hires, departures via LinkedIn/news
6. Suggest expansion opportunities with estimated deal size and recommended approach

Rules:
- NEVER send outbound messages to T1 contacts without AE approval
- All recommendations must include supporting data points
- Flag any Health Score decline immediately (don't wait for QBR)
- QBR materials must be ready 7 days before scheduled QBR date
- Always recommend multi-threading opportunities when <3 active contacts exist

Output format: Structured account intelligence brief, updated weekly
```
