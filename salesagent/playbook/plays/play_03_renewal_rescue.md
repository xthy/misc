# Play 03: Renewal Rescue
## 갱신 리스크 계정 조기 개입

---

## Play Overview

| 항목 | 내용 |
|------|------|
| **목표** | 갱신 위험 계정의 조기 식별 및 구출, churn 방지 |
| **대상** | Health Score < 60 (Yellow/Red) AND 갱신 180일 이내 |
| **소유자** | CS (리드), AE (escalation), CS Manager (executive intervention) |
| **자동화 수준** | Agent가 리스크 감지 + 알림 → Human이 개입 전략 수립/실행 |
| **긴급도** | Health Score Red: 즉시 / Yellow: 7일 내 action plan |

---

## 1. INPUT

### Trigger (이 Play가 시작되는 조건)

| Trigger | 긴급도 | 자동화 |
|---------|--------|--------|
| Health Score → Red (<50) | **즉시** | Agent 자동 알림 |
| Health Score Yellow (<60) + 갱신 180일 내 | **7일 내** | Agent 자동 알림 |
| NPS ≤ 6 (Detractor) 응답 | **즉시** | Agent 자동 알림 |
| Product usage 전월 대비 30%+ 하락 | **48시간 내** | Agent 자동 감지 |
| Champion 퇴사/이직 | **즉시** | Agent LinkedIn 모니터링 |
| 고빈도 Support ticket (5+ /월) | **7일 내** | Agent 자동 감지 |
| 결제 지연 (30일+) | **즉시** | Agent 자동 감지 |
| Executive sponsor 무응답 (60일+) | **14일 내** | Agent 자동 감지 |

### 대상 기준
- Health Score < 60 또는 위 Trigger 중 1개 이상 발생
- 갱신 잔여 기간 ≤ 180일
- ACV ≥ [minimum threshold] (소액 계정은 별도 자동 갱신 프로세스)

### 데이터 소스

| 데이터 | 소스 |
|--------|------|
| Health Score & 구성 요소 | CS 플랫폼 / CRM |
| Usage data | Product Analytics |
| Support tickets | Case object |
| NPS/CSAT | Survey tool |
| Payment history | Billing system |
| Contact changes | LinkedIn API / CRM |
| Engagement history | CRM Activity |
| Contract details | CRM Opportunity (CW) |

---

## 2. PROCESS

### Step 1: Risk Assessment (D+0~2)

**Agent가 자동 생성하는 Risk Assessment Report**:

```
┌──────────────────────────────────────────────────────┐
│         🔴 RENEWAL RISK ALERT: [Account Name]        │
├──────────────────────────────────────────────────────┤
│ Health Score: 38/100 (Red) ↓22 from last month       │
│ Renewal Date: 2026-06-30 (136 days)                  │
│ ACV: $85,000                                         │
│ Tier: T2                                             │
├──────────────────────────────────────────────────────┤
│ Risk Factors:                                        │
│ ⚠️ Usage down 45% in last 60 days                    │
│ ⚠️ Champion (Lee Director) left company 3 weeks ago  │
│ ⚠️ 3 P1 support tickets in last 30 days              │
│ ⚠️ No executive contact in 90 days                   │
│ ✅ Payment current                                   │
│ ✅ NPS last survey: 7 (neutral)                      │
├──────────────────────────────────────────────────────┤
│ Recommended Actions:                                 │
│ 1. Identify new Champion (replacement for Lee)       │
│ 2. Schedule executive check-in within 1 week         │
│ 3. Address P1 ticket root cause with Engineering     │
│ 4. Usage re-engagement workshop                      │
│ 5. Prepare value reinforcement deck                  │
└──────────────────────────────────────────────────────┘
```

### Step 2: Root Cause Diagnosis (D+1~3)

CS가 분석하는 핵심 질문:

| 카테고리 | 진단 질문 |
|----------|----------|
| **Product** | 핵심 기능이 기대대로 작동하는가? 해결 안 된 버그/요청이 있는가? |
| **Adoption** | 사용자들이 실제로 제품을 활용하고 있는가? 온보딩 후 drop-off가 있었나? |
| **Value** | 고객이 원래 기대했던 비즈니스 성과를 달성하고 있는가? |
| **Relationship** | Champion이 여전히 Active한가? 다른 stakeholder와 관계가 있는가? |
| **Competitive** | 경쟁사가 접근하고 있는가? 고객이 대안을 탐색하는 신호가 있는가? |
| **Organizational** | 고객사 내부 변화(조직 개편, 예산 삭감, 전략 변경)가 있었나? |

### Step 3: Save Plan 수립 (D+3~5)

**Health Score 수준별 대응 프로토콜**:

#### 🔴 Red Alert (Score < 50): Executive Save

| 단계 | Action | 담당 | SLA |
|------|--------|------|-----|
| 1 | Risk alert → CS Manager + AE 즉시 통보 | Agent | 즉시 |
| 2 | 내부 전쟁 회의 (CS + AE + Manager) | CS Manager | D+2 |
| 3 | Root cause 진단 완료 | CS | D+3 |
| 4 | Executive-to-Executive 미팅 요청 | CS Manager/VP | D+5 |
| 5 | 맞춤 Save Plan 수립 (구체적 action + 일정) | CS + AE | D+5 |
| 6 | Save Plan 실행 시작 | CS | D+7 |
| 7 | 주간 진척 리뷰 | CS Manager | 매주 |
| 8 | 30일 후 Health Score 재평가 | Agent + CS | D+30 |

#### 🟡 Yellow Alert (Score 50-59): Proactive Intervention

| 단계 | Action | 담당 | SLA |
|------|--------|------|-----|
| 1 | Risk alert → CS 통보 | Agent | 즉시 |
| 2 | CS가 주요 contact과 체크인 콜 | CS | D+5 |
| 3 | 문제 영역 파악 & 해결 계획 | CS | D+7 |
| 4 | Value reinforcement 자료 공유 | CS (Agent 초안) | D+10 |
| 5 | 월간 진척 리뷰 | CS Manager | 매월 |
| 6 | 60일 후 Health Score 재평가 | Agent + CS | D+60 |

### Step 4: Save Plan 실행

**공통 Save Actions Menu** (상황에 따라 선택 조합):

| Action | 설명 | 담당 |
|--------|------|------|
| **Value Reinforcement** | 도입 이후 달성 성과를 정리하여 공유 | CS (Agent 초안) |
| **Usage Workshop** | 미활용 기능 교육, 재온보딩 세션 | CS + Product |
| **Executive Alignment** | 고객 경영진과 전략적 대화, 비전 재확인 | VP/Manager |
| **Technical Resolution** | 미해결 기술 이슈 에스컬레이션 + 빠른 해결 | Engineering |
| **Champion Rebuilding** | 새로운 Champion 발굴 및 관계 구축 | AE + CS |
| **Pricing Flexibility** | 계약 조건 조정 제안 (기간 변경, 할인, 번들) | AE + Manager 승인 |
| **Success Plan Reset** | 새로운 성공 기준 합의, 30/60/90 마일스톤 재설정 | CS |
| **Executive Sponsor Assign** | 우리 측 임원을 계정에 배정, 정기 접촉 | VP Sales/CS |

### Step 5: 결과 평가

| 결과 | 다음 단계 |
|------|----------|
| Health Score → Green (≥80) | Normal 운영으로 복귀, 경과 모니터링 유지 |
| Health Score → Yellow (60-79) | 월간 모니터링 지속, D+90 재평가 |
| Health Score 변화 없음 | Save Plan 재검토, 추가 에스컬레이션 |
| Churn 결정 | Win/Loss Analysis 실행, 교훈 문서화 |

---

## 3. OUTPUT

| 결과물 | 설명 | CRM 업데이트 |
|--------|------|-------------|
| Risk Assessment | Agent 생성 리스크 리포트 | Activity 기록 |
| Save Plan | 구체적 action + 일정 + 담당 문서 | Account.Health_Score_Notes |
| Executive Alert | Red 계정 임원 보고 | Activity 기록 |
| Renewal Outcome | 갱신 성공 / Churn / Contraction | Opportunity update |
| Lessons Learned | Churn 시 교훈 문서 | Win/Loss Analysis feed |

---

## 4. METRIC

| 메트릭 | 정의 | 목표 |
|--------|------|------|
| Save Rate | Red/Yellow → 갱신 성공 비율 | >70% |
| Gross Retention | 전체 갱신 매출 유지율 | >90% |
| Time to Intervention | Risk trigger → 첫 action 소요 시간 | Red: <48hr, Yellow: <7일 |
| Health Score Recovery | Save plan 시작 후 score 회복률 | >60% (Yellow 이상 복귀) |
| Churn Prediction Accuracy | Red 계정 중 실제 churn 비율 | 모델 정확도 >70% |
| Logo Retention | 고객 수 기준 유지율 | >95% |
| Contraction Rate | 갱신 시 계약 축소 비율 | <10% |

---

## 5. TOOL / AGENT

### Agent 역할

| 기능 | 자동화 수준 |
|------|------------|
| Health Score 실시간 계산 | 완전 자동 |
| Risk trigger 감지 & 알림 | 완전 자동 |
| Risk Assessment 리포트 생성 | 완전 자동 (CS 검토) |
| Champion 이직/퇴사 감지 | 완전 자동 (LinkedIn 모니터링) |
| Save Plan 초안 제안 | 반자동 (CS 편집) |
| Value reinforcement 자료 초안 | 반자동 (CS 편집) |
| 진척 상황 주간 요약 | 완전 자동 |
| Health Score 재평가 | 완전 자동 (30/60/90일 자동 트리거) |

### Agent System Prompt 요약

```
You are the Renewal Risk Monitor Agent for [Company Name].

Your job:
1. Continuously monitor account health signals across all data sources
2. Calculate and update Health Scores daily
3. Detect risk triggers and alert CS team immediately
4. Generate Risk Assessment reports with root cause hypotheses
5. Suggest save plan actions based on risk profile
6. Track save plan execution progress and report weekly
7. Monitor Champion status via LinkedIn (job changes, departures)

Rules:
- Red alerts (Health <50) trigger IMMEDIATE notification to CS + CS Manager + AE
- Yellow alerts (Health <60 + renewal within 180 days) notify CS within 24 hours
- Never downgrade an alert without CS Manager confirmation
- Include specific data points for every risk factor cited
- Always recommend at least 3 save actions per risk assessment
- Track save plan adherence: flag overdue actions at D+3

Escalation path:
- Red account, no action in 48hrs → CS Manager
- Red account, no improvement in 30 days → VP CS
- ACV > $100K at risk → VP CS + VP Sales simultaneously

Data sources:
- Product usage: [Analytics platform] API
- Support: Case object in CRM
- NPS/CSAT: [Survey tool] API
- Billing: [Billing system] API
- LinkedIn: Contact monitoring for job changes
- CRM: All standard objects
```
