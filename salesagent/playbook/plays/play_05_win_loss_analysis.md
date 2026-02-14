# Play 05: Win/Loss Analysis
## 분기별 패턴 분석 → Playbook & Agent 정책 업데이트

---

## Play Overview

| 항목 | 내용 |
|------|------|
| **목표** | 승/패 패턴을 체계적으로 분석하여 Playbook, Agent prompt, 프로세스를 개선 |
| **대상** | 분기 내 Closed Won + Closed Lost 전체 Opportunity |
| **소유자** | Sales Ops (분석 리드), Product Marketing (인사이트), Enablement (실행) |
| **자동화 수준** | Agent가 데이터 수집/분석 → Human이 인터뷰 + 의사결정 |
| **주기** | 분기 1회 (Deep dive) + 딜별 즉시 (Per-deal debrief) |

---

## 1. INPUT

### Trigger
- **Per-deal**: Opportunity → Closed Won 또는 Closed Lost 전환 시 즉시
- **Quarterly**: 분기 종료 후 2주 내 (데이터 마감 후)

### 데이터 소스

| 데이터 | 소스 | 수집 방법 |
|--------|------|----------|
| Opportunity data | CRM | Agent 자동 추출 |
| Win/Loss reason | CRM (필수 필드) | AE 입력 |
| MEDDICC scores | CRM | Agent 자동 집계 |
| Activity history | CRM | Agent 자동 |
| Call recordings/transcripts | Gong/Chorus | Agent 자동 분석 |
| Buyer interviews | 직접 인터뷰 | Human (Ops/PMM) |
| Competitor intel | CRM + Market research | 반자동 |
| Sales cycle data | CRM (timestamps) | Agent 자동 |
| Deal size / discount data | CRM | Agent 자동 |

---

## 2. PROCESS

### Track A: Per-Deal Debrief (매 딜 종료 직후)

**타이밍**: Closed Won/Lost 후 3-5일 이내
**참석**: AE + Sales Manager (15분)
**Agent가 사전 준비하는 Debrief Sheet**:

```
┌──────────────────────────────────────────────────┐
│           DEAL DEBRIEF: [Opportunity Name]        │
├──────────────────────────────────────────────────┤
│ Result: Won / Lost    │ ACV: $XX,XXX             │
│ Cycle: XX days        │ Stage at Close: SX       │
│ Source: [Channel]     │ Tier: T[X]               │
│ Competitor: [Name]    │ Rep: [Name]              │
├──────────────────────────────────────────────────┤
│ MEDDICC FINAL SCORES:                            │
│ M:X  E:X  DC:X  DP:X  I:X  C:X  Comp:X         │
│ Composite: XX/100                                │
├──────────────────────────────────────────────────┤
│ KEY MOMENTS (Agent extracted from call logs):    │
│ • Discovery call: [핵심 발견]                      │
│ • Demo: [반응]                                     │
│ • Proposal: [피드백]                               │
│ • Final decision: [결정적 요인]                     │
├──────────────────────────────────────────────────┤
│ Win/Loss Reason (AE 기록):                       │
│ Primary: [Reason]                                │
│ Secondary: [Reason]                              │
│ Detail: [Free text]                              │
├──────────────────────────────────────────────────┤
│ DEBRIEF QUESTIONS:                               │
│ 1. 이 딜의 결정적 순간은 언제였나?                   │
│ 2. 다시 한다면 무엇을 다르게 하겠는가?                │
│ 3. MEDDICC 중 가장 약했던 요소는?                   │
│ 4. 경쟁사 대비 우리의 결정적 강점/약점은?             │
│ 5. 다른 rep에게 전달할 학습이 있는가?                │
└──────────────────────────────────────────────────┘
```

### Track B: Buyer Interview (선별적)

**대상**: ACV 상위 20% 딜 + 전략적 학습 가치가 있는 딜
**인터뷰어**: Sales Ops 또는 Product Marketing (담당 AE가 아닌 제3자)
**타이밍**: 결정 후 2-4주 (감정 정리 후, 기억 신선할 때)
**소요**: 15-30분

#### 인터뷰 질문 (Win)

| # | 질문 | 파악 목적 |
|---|------|----------|
| 1 | "구매를 결정하신 가장 큰 이유 한 가지는 무엇인가요?" | Primary win factor |
| 2 | "다른 옵션을 거의 선택하실 뻔한 순간이 있었나요?" | Competitive risk |
| 3 | "저희 영업팀과의 경험은 어떠셨나요?" | Sales execution quality |
| 4 | "제품 시연/PoC에서 가장 인상 깊었던 점은?" | Product differentiation |
| 5 | "내부에서 이 결정을 설득하실 때 어떤 논리를 사용하셨나요?" | Internal value story |
| 6 | "비슷한 결정을 하는 동료에게 어떤 조언을 하시겠어요?" | Messaging insight |

#### 인터뷰 질문 (Loss)

| # | 질문 | 파악 목적 |
|---|------|----------|
| 1 | "[Winner]를 선택하신 가장 큰 이유는 무엇인가요?" | Primary loss factor |
| 2 | "저희가 다르게 했다면 결과가 바뀔 수 있었을까요?" | Actionable feedback |
| 3 | "평가 과정에서 저희에 대해 가장 우려되셨던 점은?" | Perceived weakness |
| 4 | "저희 영업팀과의 경험 중 아쉬웠던 부분이 있으시다면?" | Sales execution gap |
| 5 | "가격이 결정에 얼마나 영향을 미쳤나요?" | Price sensitivity (buyer 관점) |
| 6 | "내부 의사결정 과정에서 가장 논쟁이 된 포인트는?" | Decision dynamics |

### Track C: Quarterly Aggregate Analysis (Agent + Human)

**Agent가 자동 생성하는 분석 보고서**:

#### C-1. Win/Loss 분포

```
Q1 2026 Win/Loss Summary
─────────────────────────────────────
Total Closed: 45 | Won: 18 | Lost: 27
Win Rate: 40%

By Tier:
  T1: 8/12 won (67%) ████████████▓▓▓▓▓▓
  T2: 7/20 won (35%) ████████▒▒▒▒▒▒▒▒▒▒▒▒
  T3: 3/13 won (23%) █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

By Source:
  Outbound: 6/18 (33%)
  Inbound: 8/15 (53%)
  CS-driven: 4/7 (57%)
  Partner: 0/5 (0%)

By Competitor:
  vs CompA: 5/12 (42%)
  vs CompB: 3/8 (38%)
  vs Do Nothing: 2/10 (20%) ← 주의
  vs Internal Build: 2/5 (40%)
```

#### C-2. Loss Reason Analysis

```
Top 5 Loss Reasons (buyer-validated):
─────────────────────────────────────
1. No Decision / Do Nothing (37%) ← 가장 큰 적
2. Competitor Chosen (22%)
3. Price / Budget (18%)
4. Missing Feature (11%)
5. Timing Not Right (7%)

⚠️ Note: AE self-reported "Price" as #1 (35%),
but buyer interviews say it was #3 (18%).
Rep perception ≠ Buyer reality.
```

#### C-3. MEDDICC Correlation Analysis

```
MEDDICC Score at S3 → Win Rate Correlation:
─────────────────────────────────────
Score 0-39: Win Rate 8%
Score 40-59: Win Rate 24%
Score 60-79: Win Rate 52%
Score 80-100: Win Rate 78%

Weakest MEDDICC Elements in Lost Deals:
1. Champion (avg 0.8/3) ← 가장 약한 고리
2. Economic Buyer (avg 1.1/3)
3. Decision Process (avg 1.3/3)
```

#### C-4. Sales Cycle Analysis

```
Avg Cycle by Outcome:
  Won: 52 days
  Lost: 78 days ← 길수록 질 확률 높음

Deals stuck >60 days at any stage:
  Win rate: 12% (vs avg 40%)
  → Action: 60일 stall rule 강화 필요
```

### Track D: Insight → Action 전환

분기 분석 후 반드시 다음 3가지를 업데이트:

| 업데이트 대상 | 인사이트 예시 | 구체적 변경 |
|-------------|-------------|-----------|
| **Playbook** | "Do Nothing이 최대 경쟁자" | Discovery 스크립트에 "Cost of Inaction" 질문 추가 |
| **Agent Prompt** | "Champion score가 가장 약한 요소" | MEDDICC Agent가 S2에서 Champion 검증 더 강하게 push |
| **Process** | "60일+ 딜의 win rate 12%" | 60일 stall 시 자동 disqualify review 트리거 추가 |
| **Training** | "AE가 가격을 loss 이유로 과대평가" | 분기 교육에 buyer interview 결과 공유 |
| **Product** | "Missing Feature 11% of losses" | PM에게 기능 요청 우선순위 데이터 제공 |

---

## 3. OUTPUT

| 결과물 | 소비자 | 주기 |
|--------|--------|------|
| Per-deal Debrief Sheet | AE + Manager | 매 딜 |
| Buyer Interview Summary | Sales Ops, PMM, Product | 선별 딜 |
| Quarterly Win/Loss Report | Leadership, Sales, Product, Marketing | 분기 |
| Playbook Change Log | Sales Enablement | 분기 |
| Agent Prompt Update | Agent Admin / Sales Ops | 분기 |
| Competitive Battle Card Update | AE, SDR | 분기 |

---

## 4. METRIC

| 메트릭 | 정의 | 목표 |
|--------|------|------|
| Debrief Completion Rate | CL/CW 딜 중 debrief 완료 비율 | >90% |
| Buyer Interview Rate | 대상 딜 중 인터뷰 완료 비율 | >50% |
| Insight → Action Rate | 인사이트 중 실제 변경으로 이어진 비율 | >70% |
| Win Rate Trend | 분기별 win rate 변화 추이 | 개선 추세 |
| Loss Reason Consistency | AE 기록 vs Buyer 인터뷰 일치율 | >60% |
| Playbook Updates / Quarter | 분기당 Playbook 변경 건수 | 3-5건 |

---

## 5. TOOL / AGENT

### Agent 역할

| 기능 | 자동화 수준 |
|------|------------|
| Deal Debrief Sheet 자동 생성 | 완전 자동 (CW/CL trigger) |
| Call transcript에서 key moment 추출 | 완전 자동 |
| Win/Loss reason 분포 집계 | 완전 자동 |
| MEDDICC score ↔ win rate 상관 분석 | 완전 자동 |
| Sales cycle 패턴 분석 | 완전 자동 |
| Competitor별 win rate 비교 | 완전 자동 |
| AE 자가보고 vs Buyer 인터뷰 gap 분석 | 반자동 (인터뷰 데이터 수동 입력 필요) |
| Quarterly report 생성 | 완전 자동 (Human 해석 추가) |
| Playbook/Agent 변경 제안 | 반자동 (Agent 제안 → Human 결정) |

### Agent System Prompt 요약

```
You are the Win/Loss Analysis Agent for [Company Name].

Your job:
1. Generate deal debrief sheets when any Opportunity reaches Closed Won or Closed Lost
2. Extract key moments and patterns from call transcripts
3. Aggregate win/loss data quarterly across all dimensions:
   - By tier, source channel, competitor, rep, industry, deal size
4. Correlate MEDDICC scores with outcomes
5. Identify statistically significant patterns and anomalies
6. Compare AE-reported loss reasons with buyer interview data
7. Suggest specific Playbook, process, and Agent prompt changes

Analysis rules:
- Always compare Win vs Loss cohorts on every dimension
- Flag any competitor where win rate drops >10pp QoQ
- Flag any rep whose win rate is >1 std dev below team average
- Flag any MEDDICC element where Lost deals score <1.5 avg
- Compare "Do Nothing" loss rate to competitor losses
- Track deals that were in pipeline >60 days — calculate separate win rate

Report format: Executive summary (1 page) + detailed analysis + recommended actions
Each recommendation must have: Data evidence, Specific change, Expected impact, Owner

Output cadence:
- Per-deal debrief: Within 24 hours of close
- Quarterly report: 2 weeks after quarter end
- Ad-hoc analysis: On request
```
