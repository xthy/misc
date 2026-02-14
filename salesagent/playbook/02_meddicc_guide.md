# MEDDICC Qualification Guide
## 딜 적격성 검증 프레임워크

---

## Overview

MEDDICC는 Enterprise B2B 딜의 qualification 업계 표준입니다. 7개 요소를 체계적으로 검증하여 "이 딜이 이길 수 있는가?"를 판단합니다.

**핵심 원칙**: MEDDICC는 한 번 채우는 체크리스트가 아니라, 딜이 진행되면서 **지속적으로 깊어지는 이해**입니다.

> ⚠️ MEDDICC 교육 후 6개월 내 40-50%의 준수율 하락이 일반적입니다. AI Agent의 지속적 nudge가 필수적입니다.

---

## MEDDICC 7 Elements

### M — Metrics (측정 지표)

**정의**: 고객이 우리 솔루션 도입으로 기대하는 **구체적이고 정량화된 비즈니스 성과**

**왜 중요한가**: Metrics가 없으면 고객 내부에서 투자 정당성을 입증할 수 없고, 경쟁사와의 차별화도 추상적이 됩니다.

#### Discovery 질문

| 단계 | 질문 |
|------|------|
| 초기 | "이 프로젝트의 성공을 어떤 수치로 측정하실 계획인가요?" |
| 심화 | "현재 그 지표의 수준은 어느 정도이고, 목표치는 얼마인가요?" |
| 심화 | "그 개선이 연간 매출/비용에 미치는 영향을 금액으로 환산하면 어느 정도일까요?" |
| 검증 | "이 ROI 분석을 경영진에게 공유하셨을 때 반응은 어떠셨나요?" |
| 확장 | "비슷한 규모의 다른 회사가 [X% 개선/Y원 절감]을 달성했는데, 이 수준이 의미 있으시겠어요?" |

#### CRM 필드

| 필드명 | 타입 | 예시 값 |
|--------|------|--------|
| `Metrics_Primary` | Text | "응답 시간 40% 단축" |
| `Metrics_Business_Impact` | Currency | $500,000 annual saving |
| `Metrics_Validated` | Picklist | Not Discussed / Stated / Quantified / Validated by EB |

#### Scoring Rubric

| 점수 | 기준 |
|------|------|
| 0 | Metrics 논의되지 않음 |
| 1 | 고객이 정성적으로 언급 ("더 빠르게", "효율적으로") |
| 2 | 구체적 수치 제시됨 ("30% 개선", "$200K 절감") |
| 3 | ROI 분석 완료 및 Economic Buyer가 검증 |

---

### E — Economic Buyer (경제적 의사결정자)

**정의**: 예산 승인 권한과 구매 결정의 최종 권한을 가진 사람

**왜 중요한가**: EB를 파악하지 못하면, Champion이 내부에서 대변해야 하고 우리가 통제할 수 없는 변수가 증가합니다.

#### Discovery 질문

| 단계 | 질문 |
|------|------|
| 초기 | "이번 투자의 최종 승인은 누가 하시나요?" |
| 심화 | "그 분이 이번 프로젝트에 대해 어느 정도 알고 계신가요?" |
| 심화 | "그 분의 올해 핵심 우선순위 3가지는 무엇인가요?" |
| 전략 | "그 분과 직접 미팅할 기회가 있을까요? 저희가 준비한 ROI 분석을 공유드리고 싶습니다" |
| 검증 | "EB가 이 프로젝트에 공개적으로 지지를 표명하셨나요?" |

#### CRM 필드

| 필드명 | 타입 | 예시 값 |
|--------|------|--------|
| `Economic_Buyer_Name` | Lookup(Contact) | Kim VP, Finance |
| `Economic_Buyer_Title` | Text | VP of Finance |
| `EB_Access_Level` | Picklist | Not Identified / Identified / Engaged / Supportive |
| `EB_Priorities` | Text Area | "FY26 cost reduction, digital transformation" |

#### Scoring Rubric

| 점수 | 기준 |
|------|------|
| 0 | EB 미식별 |
| 1 | EB 이름/직급 파악 |
| 2 | EB와 1회 이상 접촉, 우선순위 파악 |
| 3 | EB가 프로젝트를 공개적으로 지지, 예산 확보 확인 |

---

### D — Decision Criteria (의사결정 기준)

**정의**: 고객이 벤더/솔루션을 평가하는 **구체적인 기준 목록**

**왜 중요한가**: Decision Criteria를 모르면 우리 강점이 아닌 곳에서 경쟁하게 됩니다. 알면 기준 자체를 우리에게 유리하게 영향을 줄 수 있습니다.

#### Discovery 질문

| 단계 | 질문 |
|------|------|
| 초기 | "벤더 선정 시 가장 중요한 3가지 기준은 무엇인가요?" |
| 심화 | "그 기준들 중 가장 가중치가 높은 것은? 협상 불가능한 기준이 있나요?" |
| 영향 | "보안 인증이나 통합 용이성도 중요한 기준이 되시는지요?" (우리 강점 방향 유도) |
| 검증 | "이 평가 기준표를 공유해주실 수 있으신가요?" |
| 확인 | "저희가 이해한 기준을 정리해보면 [A, B, C]인데, 맞으시죠?" |

#### CRM 필드

| 필드명 | 타입 | 예시 값 |
|--------|------|--------|
| `Decision_Criteria` | Text Area | "1. ROI within 12mo, 2. API integration, 3. SOC2 cert" |
| `DC_Alignment` | Picklist | Unknown / Partially Aligned / Fully Aligned / We Shaped It |

#### Scoring Rubric

| 점수 | 기준 |
|------|------|
| 0 | Decision Criteria 미파악 |
| 1 | 일부 기준 언급됨 |
| 2 | 전체 기준 목록 파악, 우리 솔루션과의 alignment 분석 완료 |
| 3 | 기준을 우리에게 유리하게 영향/설정, 경쟁사 대비 우위 확인 |

---

### D — Decision Process (의사결정 프로세스)

**정의**: 고객 내부에서 구매 결정이 이루어지는 **단계, 관여자, 일정**

**왜 중요한가**: Process를 모르면 "갑자기 법무 검토 2개월"같은 surprise가 발생하고 forecast가 무너집니다.

#### Discovery 질문

| 단계 | 질문 |
|------|------|
| 초기 | "내부 구매 승인 프로세스는 어떻게 되나요? 어떤 단계를 거치시나요?" |
| 심화 | "각 단계에서 얼마나 시간이 걸리시나요?" |
| 심화 | "법무 검토나 조달 프로세스가 별도로 있나요?" |
| 심화 | "비슷한 규모의 구매를 최근에 하신 적 있으시면, 그때 프로세스가 어땠나요?" |
| 확인 | "그러면 [A단계 → B단계 → C단계]로 진행되고, 총 X주 정도 소요된다고 이해하면 될까요?" |

#### CRM 필드

| 필드명 | 타입 | 예시 값 |
|--------|------|--------|
| `Decision_Process` | Text Area | "Tech eval → Procurement → Legal → CFO sign-off" |
| `Decision_Timeline` | Date | 2026-06-30 |
| `Decision_Process_Stage` | Picklist | Unknown / Mapped / On Track / Delayed |
| `Paper_Process` | Text | "Procurement requires 3 competitive bids" |

#### Scoring Rubric

| 점수 | 기준 |
|------|------|
| 0 | 프로세스 미파악 |
| 1 | 대략적 프로세스 파악 ("몇 주 걸릴 거예요") |
| 2 | 전체 단계, 관여자, 예상 일정이 문서화됨 |
| 3 | 각 단계별 일정 확인, Paper process 파악, 우리가 일정에 영향력 행사 |

---

### I — Identify Pain (핵심 과제 식별)

**정의**: 고객이 현재 겪고 있는 **비즈니스 과제**와 그것이 야기하는 **영향**

**왜 중요한가**: Pain이 없으면 구매 동기가 없습니다. Pain의 크기가 가격 저항을 결정합니다.

#### Gap Selling 프레임워크 적용

```
┌─────────────────┐              ┌─────────────────┐
│  Current State  │──── GAP ────▶│  Future State   │
│  (고객의 현재)   │              │  (고객이 원하는) │
│                 │              │                 │
│ - 현재 프로세스  │              │ - 원하는 프로세스 │
│ - 현재 성과 수치 │              │ - 목표 성과 수치 │
│ - 현재 환경/도구 │              │ - 필요한 역량    │
│ - 감정적 영향    │              │ - 기대 감정      │
└─────────────────┘              └─────────────────┘
         ▲                                ▲
     우리가 파악                      우리가 연결
     해야 하는 것                     해야 하는 것
```

#### Discovery 질문 (SPIN + Gap Selling 결합)

| 유형 | 질문 |
|------|------|
| **Situation** | "현재 이 업무를 어떤 방식으로 처리하고 계신가요?" |
| **Situation** | "이 프로세스에 몇 명이 관여하고, 얼마나 시간이 걸리나요?" |
| **Problem** | "그 과정에서 가장 불편하거나 비효율적인 부분은 무엇인가요?" |
| **Problem** | "이 문제가 얼마나 자주 발생하나요?" |
| **Implication** | "이 문제가 해결되지 않으면 향후 6-12개월간 어떤 영향이 예상되시나요?" |
| **Implication** | "이 문제가 다른 팀이나 부서에도 영향을 미치나요?" |
| **Need-payoff** | "만약 이 프로세스가 [X]로 개선된다면, 팀에 어떤 변화가 생길까요?" |
| **Gap** | "현재 상태와 원하시는 상태 사이의 가장 큰 차이는 무엇인가요?" |

#### CRM 필드

| 필드명 | 타입 | 예시 값 |
|--------|------|--------|
| `Pain_Primary` | Text Area | "Manual data entry causing 20hrs/week waste per rep" |
| `Pain_Impact` | Text Area | "Losing deals due to slow response, rep frustration" |
| `Pain_Severity` | Picklist | Low / Medium / High / Critical |
| `Current_State` | Text Area | "Excel-based tracking, no automation" |
| `Future_State` | Text Area | "Automated pipeline with real-time visibility" |

#### Scoring Rubric

| 점수 | 기준 |
|------|------|
| 0 | Pain 미파악 |
| 1 | 표면적 문제 언급 ("더 나은 도구가 필요해요") |
| 2 | 구체적 Pain + 비즈니스 임팩트 정량화 |
| 3 | 다수 stakeholder가 Pain에 공감, EB 수준에서 해결 우선순위로 인정 |

---

### C — Champion (내부 옹호자)

**정의**: 우리 솔루션의 도입을 내부에서 적극적으로 밀어주는 사람

**Champion의 3가지 조건** (모두 충족해야 함):
1. **Power**: 의사결정에 영향력이 있다
2. **Access**: EB에게 접근 가능하다
3. **Vested Interest**: 이 프로젝트의 성공이 자신의 이익과 연결된다

#### Discovery 질문

| 단계 | 질문 |
|------|------|
| 식별 | "내부에서 이 프로젝트를 가장 강력히 지지하는 분은 누구인가요?" |
| 검증-Power | "그 분이 이 결정에 어떤 영향력을 행사할 수 있나요?" |
| 검증-Access | "그 분이 [EB 이름]에게 직접 보고하거나 미팅을 잡을 수 있나요?" |
| 검증-Interest | "이 프로젝트가 성공하면 그 분의 역할/성과에 어떤 영향이 있나요?" |
| 코칭 | "다음 내부 미팅에서 어떤 포인트를 강조하면 좋을까요? 제가 자료를 준비해드릴게요" |
| 테스트 | "저희 미팅 전에 내부에서 사전 논의를 해주실 수 있으신가요?" |

#### CRM 필드

| 필드명 | 타입 | 예시 값 |
|--------|------|--------|
| `Champion_Name` | Lookup(Contact) | Lee Director, IT |
| `Champion_Power` | Picklist | Low / Medium / High |
| `Champion_Access_to_EB` | Picklist | None / Indirect / Direct |
| `Champion_Vested_Interest` | Text | "Project success = promotion candidate" |
| `Champion_Status` | Picklist | None / Potential / Confirmed / Active |

#### Scoring Rubric

| 점수 | 기준 |
|------|------|
| 0 | Champion 없음 |
| 1 | 관심 있는 담당자 있으나 3조건 미충족 |
| 2 | Power + Access 확인, 우리를 위해 일부 내부 활동 수행 |
| 3 | 3조건 모두 충족, EB에게 적극 대변, 경쟁 정보 공유, 내부 장애물 제거 |

---

### C — Competition (경쟁)

**정의**: 이 딜에서 우리가 경쟁하는 **대안** (경쟁사, 내부 개발, 현상 유지 포함)

**왜 중요한가**: 가장 큰 경쟁은 종종 "아무것도 안 하는 것(Do Nothing)"입니다.

#### 경쟁 유형

| 유형 | 설명 | 대응 전략 |
|------|------|----------|
| **Direct Competitor** | 같은 카테고리 경쟁사 | 차별점(DC alignment) 강조 |
| **Indirect Competitor** | 다른 방식으로 같은 문제 해결 | 접근법의 우위 논증 |
| **Internal Build** | 고객이 자체 개발 검토 | TCO, 시간, 유지보수 비용 비교 |
| **Do Nothing** | 현상 유지 | Pain의 Implication 강화 (SPIN의 I) |

#### Discovery 질문

| 단계 | 질문 |
|------|------|
| 초기 | "현재 다른 솔루션이나 벤더를 검토 중이신가요?" |
| 심화 | "이전에 비슷한 솔루션을 도입한 적이 있으시다면, 어떤 점이 부족했나요?" |
| 포지셔닝 | "저희와 [경쟁사]를 비교하실 때, 어떤 차이가 가장 중요하게 느껴지시나요?" |
| 방어 | "내부 개발도 고려하고 계신가요?" |
| 테스트 | "현재 시점에서 어떤 옵션이 가장 유력해 보이시나요?" |

#### CRM 필드

| 필드명 | 타입 | 예시 값 |
|--------|------|--------|
| `Competitor_Primary` | Picklist | CompetitorA / CompetitorB / Internal Build / Do Nothing |
| `Competitor_Secondary` | Picklist | (same options) |
| `Competitive_Position` | Picklist | Losing / Even / Winning / Sole Source |
| `Competitor_Strengths` | Text Area | "Lower price, existing relationship" |
| `Our_Differentiators` | Text Area | "Better integration, proven ROI, faster deploy" |

#### Scoring Rubric

| 점수 | 기준 |
|------|------|
| 0 | 경쟁 상황 미파악 |
| 1 | 경쟁사 존재 인지하나 상세 미파악 |
| 2 | 경쟁사 식별, 강/약점 분석, DC 대비 포지셔닝 완료 |
| 3 | 경쟁 우위 확보, Champion이 우리를 지지, DC를 우리 유리하게 설정 |

---

## MEDDICC Composite Score

| 요소 | 최대 점수 | 가중치 |
|------|----------|--------|
| Metrics | 3 | 15% |
| Economic Buyer | 3 | 20% |
| Decision Criteria | 3 | 10% |
| Decision Process | 3 | 10% |
| Identify Pain | 3 | 20% |
| Champion | 3 | 20% |
| Competition | 3 | 5% |
| **Total** | **21** | **100%** |

### Weighted Score 계산

```
MEDDICC Score = (M×0.15 + E×0.20 + DC×0.10 + DP×0.10 + I×0.20 + C_champ×0.20 + C_comp×0.05) × 100 / 3
```

### Score → Action Mapping

| Score 구간 | 해석 | Action |
|-----------|------|--------|
| 80-100 | **Strong**: 이길 가능성 높음 | Accelerate, resource 집중 |
| 60-79 | **Developing**: 진행 중, gap 존재 | 미충족 요소에 집중 |
| 40-59 | **Weak**: 리스크 높음 | Gap 30일 내 해소 or disqualify 검토 |
| 0-39 | **Critical**: 이기기 어려움 | Disqualify 또는 전략 전면 재검토 |

---

## Stage별 MEDDICC 최소 기준

| Opp Stage | 필수 Score 기준 |
|-----------|----------------|
| S1 Discovery | I ≥ 1 (Pain 초기 확인) |
| S2 Qualification | M ≥ 1, I ≥ 2, C(champ) ≥ 1 |
| S3 Solution Design | M ≥ 2, E ≥ 1, DC ≥ 2, I ≥ 2, C(champ) ≥ 2 |
| S4 Proposal | 모든 요소 ≥ 2, E ≥ 2 |
| S5 Negotiation | 모든 요소 ≥ 2, DP ≥ 2, E ≥ 2 |
| S6 Verbal Commit | Composite Score ≥ 80 |

---

## Agent Role: MEDDICC Automation

### 자동화 범위

| 기능 | 설명 |
|------|------|
| **필드 완성도 체크** | Stage 대비 MEDDICC 필수 기준 미달 시 자동 알림 |
| **콜 후 자동 추출** | 트랜스크립트에서 MEDDICC 요소별 정보 추출, 필드 업데이트 초안 |
| **코칭 피드백** | "이 딜은 Champion Score가 1인데, S3으로 진행하려면 2 이상 필요합니다. Champion 검증 미팅을 추천합니다" |
| **주간 딜 리뷰 요약** | 모든 활성 Opportunity의 MEDDICC 상태 요약 + 리스크 딜 하이라이트 |
| **Win/Loss 패턴** | 과거 CW/CL 딜의 MEDDICC 점수 패턴 분석 → 예측 정확도 향상 |

### Agent Prompt (MEDDICC Extraction)

```
Analyze the following call transcript and extract information for each MEDDICC element.

For each element (Metrics, Economic Buyer, Decision Criteria, Decision Process,
Identify Pain, Champion, Competition):
1. Quote the relevant statement from the transcript
2. Assess the current score (0-3) based on the scoring rubric
3. Identify what information is still missing
4. Suggest a specific next question to ask in the follow-up

Format your response as a structured update ready for CRM field entry.
Flag any score changes from the previous assessment.
```
