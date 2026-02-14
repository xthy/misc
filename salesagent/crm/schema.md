# CRM Data Model Standard
## Salesforce / HubSpot Schema for B2B Sales Agent

---

## Design Principles

1. **Playbook 1:1 매핑**: CRM 필드와 Stage 정의가 Playbook과 정확히 일치
2. **Agent 읽기/쓰기 가능**: 모든 필드는 API로 접근 가능하며, Agent가 자동 업데이트할 수 있는 구조
3. **분석 가능**: Win/Loss reason, Source, Competitor 등 Agent 학습용 태그 체계 포함
4. **최소주의**: 꼭 필요한 필드만 — 필드가 많을수록 데이터 품질 하락

---

## Object Model Overview

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Account    │◀───▶│   Contact    │     │   Activity   │
│              │     │              │     │              │
│ ICP Score    │     │ Role (MEDDICC)│    │ Type         │
│ Tier         │     │ Engagement   │     │ Outcome      │
│ Health Score │     │ Last Touch   │     │ Next Step    │
└──────┬───────┘     └──────┬───────┘     └──────────────┘
       │                    │                     ▲
       │                    │                     │
       ▼                    ▼                     │
┌──────────────┐     ┌──────────────┐            │
│ Opportunity  │◀───▶│  Opp-Contact │            │
│              │     │  Junction    │            │
│ Stage        │     │ Role in Deal │            │
│ MEDDICC (7)  │     └──────────────┘            │
│ Win/Loss     │                                 │
│ Competitor   │─────────────────────────────────┘
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Case /    │
│   Ticket     │
│              │
│ Category     │
│ Resolution   │
│ Escalation   │
└──────────────┘
```

---

## Account Object

### Standard Fields

| Field Name | API Name | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| Account Name | `Name` | Text | Yes | 회사명 |
| Industry | `Industry` | Picklist | Yes | 산업 분류 |
| Sub-Industry | `Sub_Industry__c` | Picklist | No | 세부 산업 |
| Employee Count | `NumberOfEmployees` | Number | Yes | 직원 수 |
| Annual Revenue | `AnnualRevenue` | Currency | Yes | 연매출 |
| Website | `Website` | URL | Yes | 웹사이트 |
| HQ Location | `BillingCountry` / `BillingState` | Text | Yes | 본사 위치 |
| Founded Year | `Founded_Year__c` | Number | No | 설립 연도 |

### Custom Fields (Agent Required)

| Field Name | API Name | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| **ICP Fit Score** | `ICP_Fit_Score__c` | Number(0-100) | Yes | Firmographic + Technographic + Needs 합산 |
| **Intent Score** | `Intent_Score__c` | Number(0-30) | Yes | 구매 의도 신호 점수 |
| **Engagement Score** | `Engagement_Score__c` | Number(0-30) | Yes | 상호작용 점수 |
| **Total Account Score** | `Total_Account_Score__c` | Formula | Auto | Fit + Intent + Engagement |
| **Account Tier** | `Tier__c` | Picklist | Yes | T1 Strategic / T2 Core / T3 Long-tail |
| **Health Score** | `Health_Score__c` | Number(0-100) | Yes | 기존 고객 건강도 (신규: null) |
| **Health Status** | `Health_Status__c` | Formula | Auto | Green(80+) / Yellow(50-79) / Red(<50) |
| Tech Stack | `Tech_Stack__c` | Multi-select Picklist | No | 사용 기술 목록 |
| Current Vendor | `Current_Vendor__c` | Text | No | 현재 경쟁 벤더 |
| Contract Expiry | `Contract_Expiry__c` | Date | No | 기존 벤더 계약 만기일 |
| Last Scored Date | `Last_Scored_Date__c` | DateTime | Auto | 마지막 스코어링 시점 |
| Score Change Flag | `Score_Change_Flag__c` | Text | Auto | 점수 변동 사유 |
| White Space | `White_Space__c` | Text Area | No | 미판매 제품/서비스 영역 |
| Account Owner | `OwnerId` | Lookup(User) | Yes | 담당 AE/AM |

### Picklist Values

**Industry**:
```
SaaS / FinTech / HealthTech / Manufacturing / Retail /
E-commerce / Logistics / Education / Media / Professional Services / Other
```

**Tier**:
```
T1 Strategic / T2 Core / T3 Long-tail
```

---

## Contact Object

### Standard Fields

| Field Name | API Name | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| Name | `FirstName`, `LastName` | Text | Yes | 이름 |
| Title | `Title` | Text | Yes | 직급/직함 |
| Email | `Email` | Email | Yes | 이메일 |
| Phone | `Phone` | Phone | No | 전화번호 |
| Department | `Department` | Text | No | 부서 |
| LinkedIn URL | `LinkedIn_URL__c` | URL | No | LinkedIn 프로필 |

### Custom Fields (Agent Required)

| Field Name | API Name | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| **MEDDICC Role** | `MEDDICC_Role__c` | Multi-select Picklist | Yes | EB / Champion / Influencer / Blocker / End User / Coach |
| **Engagement Level** | `Engagement_Level__c` | Picklist | Yes | Cold / Warm / Engaged / Active / Champion |
| **Last Touch Date** | `Last_Touch_Date__c` | Date | Auto | 마지막 접촉 일자 |
| **Last Touch Type** | `Last_Touch_Type__c` | Picklist | Auto | Email / Call / Meeting / LinkedIn / Event |
| Persona | `Persona__c` | Picklist | No | Technical / Business / Executive |
| Preferred Channel | `Preferred_Channel__c` | Picklist | No | Email / Phone / LinkedIn |
| Communication Notes | `Comm_Notes__c` | Text Area | No | 커뮤니케이션 스타일, 선호 사항 |

### Picklist Values

**MEDDICC Role**:
```
Economic Buyer / Champion / Influencer / Blocker / End User / Coach / Unknown
```

**Engagement Level**:
```
Cold (접촉 없음) / Warm (응답 있음) / Engaged (미팅 참석) /
Active (정기적 소통) / Champion (내부 옹호)
```

---

## Opportunity Object

### Standard Fields

| Field Name | API Name | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| Opportunity Name | `Name` | Text | Yes | 기회명 |
| Account | `AccountId` | Lookup | Yes | 관련 계정 |
| Amount | `Amount` | Currency | Yes | 딜 금액 |
| Close Date | `CloseDate` | Date | Yes | 예상 마감일 |
| Stage | `StageName` | Picklist | Yes | 현재 단계 |
| Probability | `Probability` | Percent | Auto | Stage별 자동 설정 |
| Owner | `OwnerId` | Lookup(User) | Yes | 담당 AE |

### Stage Definition (Playbook Canon 연동)

| Stage | API Value | Probability | Description |
|-------|-----------|-------------|-------------|
| S1 Discovery | `S1_Discovery` | 10% | 첫 미팅 완료, Pain 초기 확인 |
| S2 Qualification | `S2_Qualification` | 20% | MEDDICC M, I, Champion 확인 |
| S3 Solution Design | `S3_Solution_Design` | 40% | Demo/PoC 완료, DC 합의 |
| S4 Proposal | `S4_Proposal` | 60% | 제안서 제출, EB 확인 |
| S5 Negotiation | `S5_Negotiation` | 80% | 가격/조건 협상, DP 확인 |
| S6 Verbal Commit | `S6_Verbal_Commit` | 90% | 구두 합의, 계약서 검토 |
| Closed Won | `Closed_Won` | 100% | 계약 체결 |
| Closed Lost | `Closed_Lost` | 0% | 패배 |

### MEDDICC Custom Fields

| Field Name | API Name | Type | Description |
|-----------|----------|------|-------------|
| **Metrics - Primary** | `MEDDICC_Metrics__c` | Text Area | 고객 기대 KPI |
| **Metrics - Business Impact** | `MEDDICC_Metrics_Impact__c` | Currency | ROI 금액 |
| **Metrics - Score** | `MEDDICC_M_Score__c` | Picklist(0-3) | 검증 수준 |
| **Economic Buyer** | `MEDDICC_EB__c` | Lookup(Contact) | EB 연결 |
| **EB Access Level** | `MEDDICC_EB_Access__c` | Picklist | Not Identified / Identified / Engaged / Supportive |
| **EB Score** | `MEDDICC_E_Score__c` | Picklist(0-3) | 접근 수준 |
| **Decision Criteria** | `MEDDICC_DC__c` | Text Area | 평가 기준 |
| **DC Alignment** | `MEDDICC_DC_Align__c` | Picklist | Unknown / Partial / Full / We Shaped |
| **DC Score** | `MEDDICC_DC_Score__c` | Picklist(0-3) | alignment 수준 |
| **Decision Process** | `MEDDICC_DP__c` | Text Area | 의사결정 단계 |
| **Decision Timeline** | `MEDDICC_DP_Date__c` | Date | 예상 결정일 |
| **DP Score** | `MEDDICC_DP_Score__c` | Picklist(0-3) | 프로세스 파악 수준 |
| **Pain - Primary** | `MEDDICC_Pain__c` | Text Area | 핵심 과제 |
| **Pain Severity** | `MEDDICC_Pain_Severity__c` | Picklist | Low / Medium / High / Critical |
| **Pain Score** | `MEDDICC_I_Score__c` | Picklist(0-3) | Pain 깊이 |
| **Champion** | `MEDDICC_Champion__c` | Lookup(Contact) | Champion 연결 |
| **Champion Status** | `MEDDICC_Champ_Status__c` | Picklist | None / Potential / Confirmed / Active |
| **Champion Score** | `MEDDICC_C_Score__c` | Picklist(0-3) | Champion 강도 |
| **Competitor Primary** | `MEDDICC_Competitor__c` | Picklist | 주요 경쟁사 |
| **Competitive Position** | `MEDDICC_Comp_Position__c` | Picklist | Losing / Even / Winning / Sole Source |
| **Competition Score** | `MEDDICC_Comp_Score__c` | Picklist(0-3) | 경쟁 우위 수준 |
| **MEDDICC Total** | `MEDDICC_Total__c` | Formula(Number) | Weighted composite score |

### Additional Opportunity Fields

| Field Name | API Name | Type | Description |
|-----------|----------|------|-------------|
| **Source Channel** | `Source_Channel__c` | Picklist | Outbound / Inbound / CS-driven / Partner / Event |
| **Win/Loss Reason (Primary)** | `Win_Loss_Reason_1__c` | Picklist | 주요 승/패 사유 |
| **Win/Loss Reason (Secondary)** | `Win_Loss_Reason_2__c` | Picklist | 보조 사유 |
| **Loss Detail** | `Loss_Detail__c` | Text Area | 패배 상세 설명 |
| **Next Step** | `Next_Step__c` | Text Area | 다음 액션 (Agent 자동 제안) |
| **Next Step Date** | `Next_Step_Date__c` | Date | 다음 액션 예정일 |
| **Days in Stage** | `Days_in_Stage__c` | Formula | 현재 Stage 체류 일수 |
| **Stalled Flag** | `Stalled__c` | Formula(Boolean) | Days_in_Stage > 30 |
| **ACV** | `ACV__c` | Currency | 연간 계약 가치 |
| **Contract Term** | `Contract_Term__c` | Number(months) | 계약 기간 |
| **Discount %** | `Discount_Pct__c` | Percent | 적용 할인율 |
| **Forecast Category** | `Forecast_Category__c` | Picklist | Pipeline / Best Case / Commit / Closed |

### Win/Loss Reason Picklist

**Win Reasons**:
```
Better Product Fit / Superior Integration / Price/Value /
Stronger Relationship / Faster Implementation / Better Support/SLA /
Reference Customers / Sole Source
```

**Loss Reasons**:
```
Price Too High / Competitor Chosen / No Budget / No Decision (Do Nothing) /
Timing Not Right / Missing Feature / Internal Build /
Lost Champion / Relationship with Competitor / Compliance/Security Gap
```

---

## Activity Object

| Field Name | API Name | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| Activity Type | `Type__c` | Picklist | Yes | Call / Email / Meeting / LinkedIn / Event / Demo |
| Subject | `Subject` | Text | Yes | 활동 제목 |
| Related Account | `AccountId` | Lookup | Yes | 관련 계정 |
| Related Opportunity | `OpportunityId` | Lookup | If exists | 관련 기회 |
| Related Contact | `WhoId` | Lookup | Yes | 대상 인물 |
| Date/Time | `ActivityDate` | DateTime | Yes | 활동 일시 |
| Duration (min) | `Duration__c` | Number | For calls/meetings | 소요 시간 |
| Outcome | `Outcome__c` | Picklist | Yes | Connected / Voicemail / No Answer / Meeting Held / Rescheduled |
| Summary | `Description` | Text Area | Yes | 활동 요약 (Agent 자동 생성 가능) |
| Next Step | `Next_Step__c` | Text Area | Yes | 다음 액션 |
| Sentiment | `Sentiment__c` | Picklist | No | Positive / Neutral / Negative (Agent 판단) |
| MEDDICC Updated | `MEDDICC_Updated__c` | Boolean | No | 이 활동으로 MEDDICC 필드 갱신 여부 |
| Source | `Activity_Source__c` | Picklist | Auto | Manual / Agent-Generated / Auto-Logged |

---

## Case / Ticket Object (CS 연계)

| Field Name | API Name | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| Case Number | `CaseNumber` | Auto | Auto | 케이스 번호 |
| Account | `AccountId` | Lookup | Yes | 관련 계정 |
| Contact | `ContactId` | Lookup | Yes | 요청자 |
| Category | `Category__c` | Picklist | Yes | Bug / Feature Request / How-to / Billing / Escalation |
| Priority | `Priority` | Picklist | Yes | Low / Medium / High / Critical |
| Status | `Status` | Picklist | Yes | New / In Progress / Waiting / Resolved / Closed |
| Resolution Time (hrs) | `Resolution_Time__c` | Number | Auto | 접수 → 해결 시간 |
| Escalation Level | `Escalation_Level__c` | Picklist | No | None / L1 / L2 / L3 / Executive |
| Satisfaction Score | `CSAT__c` | Number(1-5) | No | 고객 만족도 |

---

## Dashboards & Reports

### Dashboard 1: Pipeline Health (주간 리뷰)

| Component | Chart Type | Data |
|-----------|-----------|------|
| Pipeline by Stage | Stacked Bar | Opp Amount by Stage |
| Pipeline Coverage | Gauge | Pipeline ÷ Quota |
| New Opps This Week | KPI | Count of new Opps |
| Stalled Deals | Table | Opps where Stalled__c = true |
| MEDDICC Compliance | Bar | Avg MEDDICC scores by Stage |
| Top 10 Deals | Table | Highest Amount Opps with Stage, Score |

### Dashboard 2: Sales Performance (월간)

| Component | Chart Type | Data |
|-----------|-----------|------|
| Win Rate (by Tier) | Bar | CW ÷ (CW+CL) grouped by Tier |
| Sales Cycle (by Tier) | Bar | Avg days to close by Tier |
| ACV Trend | Line | Monthly average ACV |
| Sales Velocity | KPI | (Opps × WR × ACV) ÷ Cycle |
| Rep Leaderboard | Table | Rep, Quota, Attainment, Win Rate |
| Stage Conversion Funnel | Funnel | Conversion between stages |

### Dashboard 3: Activity & Efficiency (주간)

| Component | Chart Type | Data |
|-----------|-----------|------|
| Activities by Type | Pie | Call / Email / Meeting / LinkedIn |
| Activities per Rep | Bar | Activity count by Owner |
| Activity to Opp Ratio | KPI | Activities ÷ New Opps |
| Response Time | KPI | Avg lead response time |
| Meetings Booked | Line | Weekly meeting trend |
| Cadence Completion | Bar | % of sequences completed |

### Dashboard 4: Customer Health (월간)

| Component | Chart Type | Data |
|-----------|-----------|------|
| Health Distribution | Donut | Green / Yellow / Red accounts |
| At-Risk Accounts | Table | Accounts where Health_Status = Red |
| NRR | KPI | Net Revenue Retention |
| Renewal Pipeline | Table | Renewals due in 90 days |
| Expansion Pipeline | Bar | Expansion Opps by Source |
| Support Ticket Trend | Line | Case volume by month |

### Dashboard 5: Forecast (분기)

| Component | Chart Type | Data |
|-----------|-----------|------|
| Forecast vs Actual | Bar | Commit vs Closed by month |
| Forecast Category Breakdown | Stacked Bar | Pipeline / Best Case / Commit |
| Weighted Pipeline | KPI | Sum(Amount × Probability) |
| Forecast Accuracy (Historical) | Line | Quarterly accuracy trend |
| Upside/Downside | Table | Deals that could swing forecast |

---

## Data Hygiene Rules (Validation & Automation)

### Required Field Rules

| Trigger | Validation |
|---------|-----------|
| Stage → S2 | MEDDICC_I_Score ≥ 1, MEDDICC_M_Score ≥ 1 |
| Stage → S3 | MEDDICC_EB ≠ null, MEDDICC_DC ≠ empty |
| Stage → S4 | Amount > 0, MEDDICC_Total ≥ 40 |
| Stage → Closed Lost | Win_Loss_Reason_1 ≠ null, Loss_Detail ≠ empty |
| Stage → Closed Won | Discount reviewed, Contract_Term filled |

### Auto-Update Rules (Agent-driven)

| Trigger | Action |
|---------|--------|
| Activity logged with Contact | Update Contact.Last_Touch_Date |
| No Activity on Opp in 30 days | Set Stalled__c = true, alert Owner |
| Health Score drops below 50 | Alert CS Manager, create follow-up Task |
| Renewal within 90 days | Create Renewal Opportunity, alert CS + AE |
| Champion Contact leaves company | Alert AE, flag opportunity risk |

---

## API Integration Points (Agent에게 필요한 endpoints)

| Operation | Salesforce API | HubSpot API |
|-----------|---------------|-------------|
| Read Account | `GET /sobjects/Account/{id}` | `GET /crm/v3/objects/companies/{id}` |
| Update Account | `PATCH /sobjects/Account/{id}` | `PATCH /crm/v3/objects/companies/{id}` |
| Read Opportunity | `GET /sobjects/Opportunity/{id}` | `GET /crm/v3/objects/deals/{id}` |
| Update Opportunity | `PATCH /sobjects/Opportunity/{id}` | `PATCH /crm/v3/objects/deals/{id}` |
| Create Activity | `POST /sobjects/Task` | `POST /crm/v3/objects/tasks` |
| SOQL Query | `GET /query?q=SELECT...` | `POST /crm/v3/objects/search` |
| Bulk Read | `POST /composite/batch` | `POST /crm/v3/objects/batch/read` |
| Webhooks (triggers) | Platform Events / Change Data Capture | Webhooks API |
