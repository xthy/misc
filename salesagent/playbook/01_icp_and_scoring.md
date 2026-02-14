# ICP & Account Scoring Framework

---

## 1. Ideal Customer Profile (ICP) 정의

ICP는 "우리 솔루션에서 가장 큰 가치를 얻고, 우리에게 가장 높은 수익을 가져다주는 고객의 특성"을 체계적으로 정의한 것입니다.

### 3축 ICP 프레임워크

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

### Firmographic Criteria (40%)

| 속성 | Ideal (5점) | Good (3점) | Poor (1점) |
|------|------------|-----------|-----------|
| **산업** | [Primary verticals: SaaS, FinTech, HealthTech] | [Adjacent: Manufacturing, Retail] | [Misfit: Government, Non-profit] |
| **직원 수** | 200-2,000 (Mid-Market sweet spot) | 50-199 or 2,001-10,000 | <50 or >10,000 |
| **연매출** | $20M-$500M | $5M-$19M or $501M-$2B | <$5M or >$2B |
| **지역** | [Primary markets] | [Secondary markets] | [No-go regions] |
| **성장률** | >20% YoY | 10-20% YoY | <10% or declining |
| **자금 조달** | Series B-D or PE-backed | Series A or Public | Pre-seed/Seed |

### Technographic Criteria (30%)

| 속성 | Ideal (5점) | Good (3점) | Poor (1점) |
|------|------------|-----------|-----------|
| **CRM** | Salesforce | HubSpot, Dynamics | None or custom |
| **기술 성숙도** | Cloud-native, API-first | Hybrid (cloud + on-prem) | Legacy on-prem only |
| **현재 솔루션** | Competitor X or manual process | Partial solution in place | Committed to competitor Y (3yr lock-in) |
| **통합 필요** | 표준 API 통합 가능 | 커스텀 통합 필요 | 통합 불가능 |
| **보안 요구** | Standard (SOC2 충분) | Enhanced (HIPAA 등) | Government-level (FedRAMP) |

### Needs-based Criteria (30%)

| 속성 | Ideal (5점) | Good (3점) | Poor (1점) |
|------|------------|-----------|-----------|
| **핵심 Pain** | 우리 솔루션이 직접 해결하는 문제 보유 | 관련 문제 인식하나 우선순위 낮음 | 문제 인식 없음 |
| **Budget** | 예산 확보됨 또는 확보 진행 중 | 예산 미확보이나 ROI case로 가능 | 예산 없음, ROI 불명확 |
| **Timeline** | 6개월 내 도입 의향 | 6-12개월 내 | 12개월+ 또는 미정 |
| **의사결정 복잡도** | 단일 부서 결정 | 2-3개 부서 합의 | 전사 위원회 승인 필요 |
| **Champion 존재** | 내부 옹호자 확인됨 | 관심 있는 담당자 있음 | 접점 없음 |

> **커스터마이징 가이드**: 위 기준의 구체적 값(산업명, 직원 수 구간, 기술스택 등)은 각 포트폴리오사의 실제 고객 데이터로 교체해야 합니다. 현재는 B2B SaaS Mid-Market 기준 best practice 값입니다.

---

## 2. Account Scoring Model

### Scoring 접근법: Tiered Weighted Model

가장 투명하고 실행 가능한 접근법으로, 먼저 **Fit Score**(적합도)로 거르고, 통과한 계정에 **Intent + Engagement Score**를 더합니다.

```
                     ┌─────────────────┐
                     │  All Accounts   │
                     └────────┬────────┘
                              │
                    ┌─────────▼─────────┐
                    │  Fit Score (ICP)  │  Firmographic + Technographic + Needs
                    │  Threshold: ≥50  │
                    └─────────┬─────────┘
                              │ Pass
                    ┌─────────▼─────────┐
                    │  Intent Score     │  구매 의도 신호
                    │  (0-30점)         │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │  Engagement Score │  우리와의 상호작용
                    │  (0-30점)         │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │  Total Score      │  Fit + Intent + Engagement
                    │  (0-160)          │
                    └───────────────────┘
```

### Fit Score 계산 (0-100)

ICP 3축 × 각 기준별 1-5점 × 가중치

| 축 | 기준 수 | 각 기준 최대 | 축 가중치 | 축 최대 점수 |
|----|--------|------------|----------|-------------|
| Firmographic | 6개 | 5점 | 40% | 40점 |
| Technographic | 5개 | 5점 | 30% | 30점 |
| Needs-based | 5개 | 5점 | 30% | 30점 |
| **합계** | | | | **100점** |

**계산 공식**:
```
Fit Score = (Firmo 합계/30 × 40) + (Techno 합계/25 × 30) + (Needs 합계/25 × 30)
```

**Fit 등급**:
- A-Fit (80-100): ICP에 매우 적합
- B-Fit (60-79): 적합하나 일부 gap
- C-Fit (50-59): 최소 기준 충족
- D-Fit (<50): **제외** — 추가 스코어링하지 않음

### Intent Score (0-30)

구매 의도를 나타내는 외부/내부 신호:

| 신호 | 점수 | 소스 |
|------|------|------|
| 관련 키워드 검색 (intent data) | +5 | Bombora, G2, TrustRadius |
| 경쟁사 리뷰/비교 페이지 방문 | +5 | Intent data provider |
| 관련 직무 채용공고 게시 | +4 | LinkedIn, Indeed |
| 자금 조달/인수 이벤트 | +4 | Crunchbase, PitchBook |
| 기존 벤더 계약 만기 근접 | +5 | 영업 인텔 |
| 산업 규제 변화로 솔루션 필요 | +3 | 뉴스, 규제 모니터링 |
| 경영진 교체 (관련 직급) | +4 | LinkedIn, 뉴스 |

### Engagement Score (0-30)

우리와의 실제 상호작용:

| 신호 | 점수 | 소스 |
|------|------|------|
| 웹사이트 방문 (3회+ /월) | +3 | Web analytics |
| 콘텐츠 다운로드 | +4 | Marketing automation |
| 웨비나/이벤트 참석 | +5 | Event platform |
| 이메일 응답 | +5 | CRM / Sequencer |
| 미팅 참석 | +8 | CRM |
| 데모/PoC 요청 | +10 | CRM |
| 복수 부서 접촉 (Multi-threading) | +5 | CRM |

### Total Score & Action

| Total Score 구간 | 등급 | Action |
|-----------------|------|--------|
| 120-160 | **Hot** | 즉시 AE 배정, T1 대우, 24시간 내 접촉 |
| 90-119 | **Warm** | SDR 우선 시퀀스, 1주 내 접촉 |
| 60-89 | **Nurture** | 자동 nurture 시퀀스, 월간 터치 |
| 50-59 | **Watch** | 마케팅 리드 풀, 분기 모니터링 |
| <50 | **Excluded** | Fit 미달, 추적 중단 |

---

## 3. Account Tiering Model

Fit Score와 Account Value(매출 잠재력)를 결합하여 3개 Tier로 분류합니다.

### Tier 분류 기준

| Tier | 기준 | 계정 수 비중 | 매출 비중 (목표) |
|------|------|-------------|----------------|
| **T1 Strategic** | Fit A + ACV > $100K (또는 상위 20%) | ~10-15% | ~50-60% |
| **T2 Core** | Fit A/B + ACV $25K-$100K | ~20-30% | ~25-35% |
| **T3 Long-tail** | Fit B/C + ACV < $25K | ~55-70% | ~10-20% |

### Tier별 Coverage Model

| 구분 | T1 Strategic | T2 Core | T3 Long-tail |
|------|-------------|---------|-------------|
| **Ownership** | Named AE (1:10-20) | Pooled AE (1:50-80) | Agent-led / Pooled SDR (1:200+) |
| **Interaction** | Human-led | Co-pilot (AI draft, human review) | AI-led (human escalation only) |
| **Meeting Frequency** | Monthly+ (대면 포함) | Quarterly | On-demand |
| **Account Plan** | 필수 (상세) | 필수 (간략) | 자동 생성 |
| **QBR** | 분기 (대면) | 반기 (원격) | 없음 (자동 보고서) |
| **Outbound Cadence** | 맞춤 (100% 개인화) | 반자동 (50% 개인화) | 자동 (템플릿 기반, AI 개인화) |
| **Response SLA** | 4시간 이내 | 24시간 이내 | 48시간 이내 |

### Tier 변동 규칙

| 변동 | Trigger | 프로세스 |
|------|---------|---------|
| T3 → T2 승격 | 사용량 급증, 대형 expansion 기회 발견 | Agent 알림 → Manager 승인 |
| T2 → T1 승격 | ACV $100K+ 달성, 전략적 중요성 확인 | 분기 리뷰에서 결정 |
| T1 → T2 강등 | 매출 감소, engagement 하락, churn 리스크 | 분기 리뷰에서 결정 |
| T2 → T3 강등 | Health Score Red 지속, 축소 계약 | Agent 알림 → Manager 확인 |

---

## 4. Scoring Automation (Agent Spec)

### Auto-Scoring Trigger

| Trigger | Action | 주기 |
|---------|--------|------|
| 신규 계정 CRM 등록 | Fit Score 자동 계산 | Real-time |
| Intent data 업데이트 | Intent Score 재계산 | Weekly |
| 웹/이메일/미팅 활동 | Engagement Score 갱신 | Daily |
| Account Score 등급 변화 | Tier 재분류 추천 + 알림 | Daily |
| 분기 시작 | 전체 계정 Full Rescore | Quarterly |

### Agent System Prompt 요약 (Account Scoring)

```
You are the Account Scoring Agent for [Company Name].

Your job:
1. Collect account data from CRM, enrichment sources, and intent providers
2. Calculate Fit Score (ICP 3-axis), Intent Score, and Engagement Score
3. Classify accounts into Tiers (T1/T2/T3) based on scoring rules
4. Flag tier changes and score anomalies for human review
5. Recommend next-best-action based on score profile

Rules:
- Never promote an account to T1 without human approval
- Flag any account with Fit Score drop >20 points in 30 days
- Re-score all accounts on the 1st of each quarter
- Log all score changes with reasoning in CRM Activity

Data sources:
- CRM: Account, Contact, Opportunity, Activity objects
- Enrichment: [Clearbit/ZoomInfo/Apollo] for firmographic + technographic
- Intent: [Bombora/G2] for intent signals
- Web: [Analytics platform] for engagement tracking
```

---

## 5. Implementation Checklist

- [ ] ICP 기준값을 실제 고객 데이터로 검증 (Top 20 고객 분석)
- [ ] Scoring 가중치를 과거 win/loss 데이터로 백테스트
- [ ] CRM에 Score 필드 추가 (Account: ICP_Score, Intent_Score, Engagement_Score, Total_Score, Tier)
- [ ] Enrichment 도구 연동 (최소 1개: Clearbit, ZoomInfo, Apollo 등)
- [ ] Intent data 소스 연결 (선택: Bombora, G2 등)
- [ ] Auto-scoring 로직 Agent에 구현 (n8n workflow 또는 CRM automation)
- [ ] 분기별 Rescore + Tier 리뷰 프로세스 캘린더 등록
- [ ] Scoring 결과 Dashboard 구축 (Tier별 분포, 점수 변동 추이)
