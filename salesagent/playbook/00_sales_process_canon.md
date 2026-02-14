# B2B Sales Process Canon
## 포트폴리오 공통 영업 프로세스 표준

---

## Purpose

이 문서는 PE 포트폴리오 전체에 적용되는 B2B 영업 프로세스의 **공통 뼈대(Canon)**입니다.
각 포트폴리오사는 제품/시장이 다르더라도 이 7단계 구조를 공유하며, 이를 통해:
- Cross-portfolio 벤치마킹이 가능
- 새 투자 후 100일 GTM 턴어라운드 시 즉시 적용 가능
- AI Agent의 동작 기준(workflow rules)이 됨

---

## 7-Stage Workflow

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

---

## Stage 1: Market Strategy (시장 전략)

### 목적
"누구에게, 어떤 방식으로 팔 것인가"의 큰 그림을 확정한다.

### 핵심 활동

| 활동 | 설명 | 담당 |
|------|------|------|
| ICP 정의 | Firmographic + Technographic + Needs-based 3축 기반 이상 고객상 정의 | Sales Leadership + Ops |
| 시장 세분화 | TAM → SAM → SOM 분석, 세그먼트별 우선순위 | Strategy + Ops |
| Territory 설계 | 지리/산업/규모 기준 영업 영역 배분 | Sales Ops |
| Coverage Model | 채널 믹스 결정: Field / Inside / Digital | Sales Leadership |
| Competitive Landscape | 주요 경쟁사 매핑, 포지셔닝 차별점 정의 | Marketing + Sales |

### Stage Entry Criteria
- 제품/서비스가 시장에 출시 가능한 상태
- 최소 10개 이상의 기존 고객 or 파일럿 사례 보유

### Stage Exit Criteria
- ICP 문서 승인 완료
- Territory 배분 완료, 각 rep에게 Target Account List 배포
- Coverage model 확정 (T1/T2/T3 기준)

### KPIs
| 메트릭 | 설명 | 목표 |
|--------|------|------|
| TAM Coverage | 접근 가능한 시장 대비 실제 커버 비율 | >60% |
| ICP Match Rate | 신규 리드 중 ICP 적합 비율 | >40% |
| Territory Balance | rep 간 기회 균형도 (Gini coefficient) | <0.3 |

### Agent Role
- 시장 데이터 자동 수집/갱신 (산업 트렌드, 기업 뉴스, 기술 채택 현황)
- ICP fit 자동 스코어링
- Territory 최적화 시뮬레이션

---

## Stage 2: Account Planning & Scoring (계정 계획 & 스코어링)

### 목적
개별 계정 수준의 전략을 수립하고 자원 배분 우선순위를 결정한다.

### 핵심 활동

| 활동 | 설명 | 담당 |
|------|------|------|
| Account Scoring | ICP 적합도 + 구매 의도 + 참여도 복합 스코어 산출 | Sales Ops + Agent |
| Tier 분류 | 스코어 기반 T1/T2/T3 분류 | Sales Ops |
| Account Plan 작성 | T1/T2 대상 개별 계정 전략 문서 | AE |
| Org Chart Mapping | 의사결정자(EB), Champion, Influencer, Blocker 식별 | AE + SDR |
| White-space Analysis | 미판매 제품/서비스 영역 식별 | AE + CS |

### Account Plan 필수 구성요소
1. **계정 개요**: 사업 모델, 최근 이슈, 전략적 우선순위
2. **조직도 & 의사결정 구조**: EB, Champion, Influencer, Blocker 매핑
3. **White-space 분석**: 현재 사용 vs 미판매 영역
4. **경쟁사 포지션**: 현재 벤더, 계약 만기, 교체 가능성
5. **맞춤 Value Proposition**: 이 계정에 특화된 가치 제안
6. **12개월 Action Plan**: 마일스톤, 핵심 활동, 목표 매출

### Stage Entry Criteria
- ICP 기반 Target Account List 확보
- 계정 기본 데이터(산업, 규모, 기술스택) CRM에 입력 완료

### Stage Exit Criteria
- Account Score 산출 및 Tier 분류 완료
- T1 계정 100%, T2 계정 50% 이상 Account Plan 작성 완료

### KPIs
| 메트릭 | 설명 | 목표 |
|--------|------|------|
| Account Score Coverage | 스코어가 산출된 계정 비율 | 100% |
| Plan Completion Rate | Account Plan 작성 완료율 (T1/T2) | T1: 100%, T2: 50% |
| Scoring Accuracy | Score 상위 20% 계정의 실제 전환율 | >3x 평균 |

### Agent Role
- 계정 데이터 자동 수집 (뉴스, 재무제표, 기술스택, 채용공고)
- Account Score 자동 계산 및 주기적 갱신
- "이 계정의 다음 최선 액션" 추천
- Account Plan 초안 생성

---

## Stage 3: Pipeline Generation (파이프라인 생성)

### 목적
적격 기회(SQL/Opportunity)를 목표 대비 충분한 양으로 생성한다.

### 3개 채널별 활동

#### 3-1. Outbound (SDR-driven)

| 활동 | 설명 |
|------|------|
| Prospecting | Target Account List 기반 의사결정자 식별 |
| Multi-channel Cadence | 이메일 + 콜 + LinkedIn 14일 시퀀스 실행 |
| Lead Enrichment | 연락처, 기술스택, 최근 뉴스 등 정보 보강 |
| Meeting Booking | 적격 미팅 세팅 → AE에게 핸드오프 |

**역할 분리 (Predictable Revenue 모델)**:
- **SDR**: 초기 접촉, 미팅 세팅에 집중
- **AE**: SDR이 세팅한 미팅부터 클로징까지

#### 3-2. Inbound / Field Sales

| 활동 | 설명 |
|------|------|
| Inbound 응대 | 웹사이트/이벤트 통한 리드 즉시 응대 (5분 이내 목표) |
| Field Meeting | T1/T2 대상 대면 미팅, 사전 준비가 성과의 80% |
| Event/Conference | 타겟 이벤트 참석, 현장 리드 확보 |

#### 3-3. CS-driven Expansion

| 활동 | 설명 |
|------|------|
| Health Score Trigger | 사용량 증가, NPS 상승 등 expansion 신호 감지 |
| CS → AE Handoff | CS가 기회 발굴 → AE에게 qualified expansion opp 전달 |
| QBR 기반 발굴 | 분기 리뷰에서 추가 니즈 포착 |

### Stage Entry Criteria
- Target Account List + 담당 배정 완료
- Outbound cadence 시퀀스 및 스크립트 준비 완료

### Stage Exit Criteria
- SQL(Sales Qualified Lead) 기준 충족하는 기회가 CRM에 등록됨
- 파이프라인 커버리지 3x 이상 확보

### KPIs
| 메트릭 | 설명 | 목표 |
|--------|------|------|
| Pipeline Coverage | 파이프라인 총액 ÷ 분기 목표 | 3x~5x |
| SQL/Month | 월간 신규 적격 기회 수 | rep 역량별 설정 |
| Activity Volume | 일일 콜/이메일/LinkedIn 터치 수 | SDR: 60+ activities/day |
| Meeting Conversion | 접촉 → 미팅 전환율 | Outbound: 3-5% |
| Response Time | 인바운드 리드 → 첫 접촉 | <5분 (업무시간 내) |
| CS Expansion Rate | CS 발굴 expansion opp 수 / 전체 관리 계정 | >10%/quarter |

### Agent Role
- 리드 enrichment 자동화 (이메일, 전화번호, 기술스택, 뉴스)
- 시퀀스 메시지 초안 생성 (개인화 포함)
- 콜 후 요약 + CRM 자동 업데이트
- CS health score 기반 expansion signal 자동 감지

---

## Stage 4: Pipeline Progression (파이프라인 진행)

### 목적
기회를 체계적으로 진전시키고, 비적격 기회를 빠르게 걸러낸다.

### 핵심 활동

| 활동 | 설명 | 담당 |
|------|------|------|
| Discovery Call | SPIN/Gap Selling 기반 심층 니즈 파악 | AE |
| MEDDICC Qualification | 7개 요소 체계적 검증 | AE |
| Demo / PoC | 맞춤 시연 또는 기술 검증 | AE + SE |
| Stakeholder Expansion | 다수 의사결정자 관계 구축 | AE |
| Competitive Positioning | 경쟁사 대비 차별점 커뮤니케이션 | AE + Marketing |

### Opportunity Stage 정의 (CRM 표준)

| Stage # | Stage Name | 확률 | 필수 조건 |
|---------|-----------|------|----------|
| S1 | Discovery | 10% | 첫 미팅 완료, Pain 초기 확인 |
| S2 | Qualification | 20% | MEDDICC 중 M, I, C(hampion) 확인 |
| S3 | Solution Design | 40% | Demo/PoC 완료, Decision Criteria 합의 |
| S4 | Proposal | 60% | 제안서 제출, Economic Buyer 확인 |
| S5 | Negotiation | 80% | 가격/조건 협상 중, Decision Process 확인 |
| S6 | Verbal Commit | 90% | 구두 합의, 계약서 검토 중 |
| CW | Closed Won | 100% | 계약 체결 완료 |
| CL | Closed Lost | 0% | 실패 (사유 기록 필수) |

### Stage Entry Criteria
- SQL 기준 충족 기회가 CRM에 등록됨
- AE가 해당 기회에 배정됨

### Stage Exit Criteria
- Closed Won 또는 Closed Lost (사유 기록 포함)

### KPIs
| 메트릭 | 설명 | 목표 |
|--------|------|------|
| Win Rate | Closed Won ÷ Total Closed | 산업 평균 대비 +5pp |
| Sales Cycle | Opp 생성 → Closed Won 평균 일수 | 산업/딜 사이즈별 설정 |
| Stage Conversion | 각 스테이지 간 전환율 | S1→S2: 50%, S2→S3: 60%, S3→S4: 65%, S4→S5: 70%, S5→CW: 75% |
| MEDDICC Compliance | 7개 필드 중 완성 비율 | S3 이후 >80% |
| Stalled Deal Rate | 30일+ 스테이지 변화 없는 기회 비율 | <15% |

### Agent Role
- MEDDICC 필드 완성도 자동 체크 & 누락 알림
- 딜 진행 상태 요약 (주간)
- 리스크 시그널 감지 ("60일째 스테이지 변화 없음", "Champion 접촉 없음")
- Next best action 추천
- 콜 후 MEDDICC 필드 자동 추출 (트랜스크립트 분석)

---

## Stage 5: Close & Onboard (계약 & 온보딩)

### 목적
딜을 성공적으로 마무리하고, 고객이 가치를 빠르게 실현하도록 온보딩한다.

### 핵심 활동

| 활동 | 설명 | 담당 |
|------|------|------|
| Proposal 작성 | 맞춤 제안서 + 가격 패키지 | AE + Sales Ops |
| 가격 협상 | 할인 가이드라인 내 협상, 에스컬레이션 | AE + Sales Manager |
| 계약 체결 | 법무 검토, 최종 서명 | AE + Legal |
| Sales→CS Handoff | 구조화된 인수인계 | AE → CS/AM |
| Kickoff Meeting | 고객과의 프로젝트 킥오프 | CS + AE |
| Onboarding Execution | 30/60/90일 계획 실행 | CS |

### 할인 승인 매트릭스 (예시)

| 할인 범위 | 승인 권한 |
|----------|----------|
| 0-10% | AE 자체 승인 |
| 11-20% | Sales Manager 승인 |
| 21-30% | VP Sales 승인 |
| 30%+ | C-Level 승인 (예외적) |

### Sales → CS Handoff 필수 항목
1. 고객의 핵심 과제 (Pain) 및 기대 성과
2. 합의된 성공 기준 (Metrics)
3. 주요 관계자 매핑 (EB, Champion, Day-to-day contact)
4. 계약 조건 요약 (가격, 기간, SLA)
5. 미해결 이슈 또는 위험 요소
6. 30/60/90일 온보딩 마일스톤 초안

### Stage Entry Criteria
- Opportunity가 S4(Proposal) 이상
- 가격/제안서 초안 준비 완료

### Stage Exit Criteria
- 계약 체결 완료 (CW)
- Handoff 문서 작성 및 CS 인수인계 완료
- 킥오프 미팅 일정 확정

### KPIs
| 메트릭 | 설명 | 목표 |
|--------|------|------|
| Close Rate (S4→CW) | Proposal 이후 계약 전환율 | >50% |
| Avg Discount | 평균 할인율 | <15% |
| Time to Close | S4 → CW 소요 일수 | <30일 |
| Handoff Quality | CS의 인수인계 만족도 (5점 척도) | >4.0 |
| Time to First Value | 계약 → 고객이 첫 가치 실현 | <30일 |

### Agent Role
- 제안서 초안 생성
- 계약서 조항 체크 (누락 항목, 비표준 조건 경보)
- Handoff 문서 자동 생성 (CRM 데이터 기반)
- 온보딩 체크리스트 자동 트래킹 & 리마인더

---

## Stage 6: Retention & Growth (유지 & 성장)

### 목적
고객을 유지하고 계정 내 매출을 확대한다.

### 핵심 활동

| 활동 | 설명 | 담당 |
|------|------|------|
| Adoption Monitoring | 사용량, 기능별 활용도, 로그인 빈도 추적 | CS |
| Health Score 관리 | 복합 지표 기반 계정 건강도 모니터링 | CS + Agent |
| QBR 실행 | 분기별 성과 리뷰, 다음 분기 목표 합의 | CS + AE |
| Renewal 관리 | 갱신 90일 전 프로세스 시작, 리스크 조기 경보 | CS + AE |
| Expansion/Upsell | White-space 기반 추가 제안, 사용량 trigger | AE + CS |

### Health Score 모델

| 구성 요소 | 가중치 | 측정 방법 |
|----------|--------|----------|
| Product Adoption | 30% | DAU/MAU, 기능 사용률, 로그인 빈도 |
| Support Health | 20% | 티켓 빈도, 에스컬레이션 수, 해결 시간 |
| Relationship | 20% | Champion 접촉 빈도, 멀티 스레딩 수준 |
| Customer Sentiment | 15% | NPS, CSAT, 서베이 응답 |
| Financial Health | 15% | 결제 이력, 계약 잔여 기간, 사용량 대비 계약 규모 |

**Health Score 등급**:
- 🟢 **Healthy** (80-100): 정상 운영, expansion 기회 탐색
- 🟡 **At Risk** (50-79): CS 주의 필요, 30일 내 action plan 수립
- 🔴 **Critical** (<50): 즉시 에스컬레이션, executive sponsor 개입

### Renewal Timeline

| D-날 | 활동 |
|------|------|
| D-180 | Renewal forecast에 반영, Health Score 점검 |
| D-90 | Renewal 프로세스 시작, CS + AE 미팅 |
| D-60 | 고객과 renewal 논의, 조건 협상 시작 |
| D-30 | 계약서 발송, 법무 검토 |
| D-0 | 갱신 완료 또는 churn 기록 |

### Stage Entry Criteria
- 계약 체결 및 온보딩 완료
- CS 담당자 배정 완료

### Stage Exit Criteria
- Renewal 완료 또는 Churn 기록
- (Expansion의 경우) 새로운 Opportunity로 Stage 4에 재진입

### KPIs
| 메트릭 | 설명 | 목표 |
|--------|------|------|
| Gross Retention Rate | (기초 MRR - Churn - Contraction) ÷ 기초 MRR | >90% |
| Net Revenue Retention | (기초 MRR + Expansion - Churn - Contraction) ÷ 기초 MRR | >110% |
| Expansion Rate | Expansion MRR ÷ 기초 MRR | >20% YoY |
| Health Score Distribution | Green:Yellow:Red 비율 | 70:20:10 |
| QBR Completion Rate | 분기별 QBR 실행 비율 (T1/T2) | T1: 100%, T2: 75% |

### Agent Role
- Health Score 자동 계산 및 등급 변화 경보
- QBR 자료 초안 생성 (사용량 데이터, 성과 요약, 추천 안건)
- 갱신 리스크 예측 (D-180 시점)
- Expansion 기회 자동 감지 (사용량 증가, 새 부서 접촉 등)

---

## Stage 7: Ops & Analytics (운영 & 분석)

### 목적
전체 영업 엔진의 성과를 측정, 예측, 최적화한다.

### 핵심 활동

| 활동 | 설명 | 담당 |
|------|------|------|
| 주간 Pipeline Review | 파이프라인 건강도, 이상치, forecast 검토 | Sales Manager + Ops |
| 월간 Ops Report | 전체 메트릭 대시보드 리뷰, 트렌드 분석 | Sales Ops |
| 분기 Forecast | Bottom-up + Top-down 예측 조율 | Sales Leadership |
| Win/Loss Analysis | 분기별 패턴 분석, Playbook/Agent 정책 업데이트 | Sales Ops + Enablement |
| Process Optimization | 병목 구간 식별, 프로세스 개선 | Sales Ops |

### Core Metrics Dashboard

| 카테고리 | 메트릭 | 계산 | 리뷰 주기 |
|----------|--------|------|----------|
| **효과성** | Win Rate | CW ÷ (CW + CL) | 월간 |
| | Sales Cycle | Opp 생성 → CW 평균 일수 | 월간 |
| | ACV | 총 계약 금액 ÷ 계약 수 | 월간 |
| **효율성** | Sales Velocity | (Opps × Win Rate × ACV) ÷ Cycle | 월간 |
| | Pipeline Coverage | Pipeline 총액 ÷ 목표 | 주간 |
| | CAC | 총 S&M 비용 ÷ 신규 고객 수 | 분기 |
| **활동** | Activity-to-Opp Ratio | Activities ÷ Opps Created | 주간 |
| | Response Time | 리드 인입 → 첫 접촉 | 일간 |
| **리텐션** | NRR | (기초 + Expansion - Churn - Contraction) ÷ 기초 | 월간 |
| | Gross Retention | (기초 - Churn - Contraction) ÷ 기초 | 월간 |
| **예측** | Forecast Accuracy | 예측 vs 실제 오차율 | 분기 |
| | Stage Conversion | 스테이지 간 전환율 | 월간 |

### 분석 쪼개기 기준 (Dimensions)
모든 메트릭은 아래 기준으로 drill-down 가능해야 함:
- **Tier별**: T1 / T2 / T3
- **채널별**: Outbound / Inbound / CS-driven / Partner
- **Rep별**: 개인 성과 비교
- **산업별**: 산업 세그먼트 비교
- **제품별**: 제품/서비스 라인 비교
- **기간별**: MoM, QoQ, YoY 트렌드

### Stage Entry Criteria
- 데이터가 CRM에 축적됨 (최소 1분기 이상)

### Stage Exit Criteria
- N/A (상시 운영)

### KPIs
| 메트릭 | 설명 | 목표 |
|--------|------|------|
| Forecast Accuracy | 예측 vs 실제 매출 오차 | <15% |
| Data Completeness | CRM 필수 필드 입력률 | >85% |
| Report Delivery | 주간/월간 보고서 정시 발행률 | 100% |
| Insight Actionability | 보고서 기반 실행된 개선 건수 | >2/month |

### Agent Role
- 주간/월간 Ops 보고서 자동 생성
- 파이프라인 이상치 감지 ("이번 주 T2 pipeline 30% 감소")
- Forecast 자동 산출 (가중 파이프라인 기반)
- Win/Loss 패턴 분석 ("경쟁사 X 대비 기술 딜에서 win rate 20%p 낮음")
- 프로세스 병목 식별 ("S2→S3 전환율 하락 중, Discovery 질 문제 의심")

---

## Cross-Stage Rules

### Handoff 규칙
| From | To | Trigger | 필수 전달 항목 |
|------|----|---------|---------------|
| SDR → AE | Stage 3→4 | SQL 기준 충족 | Pain summary, contact info, engagement history |
| AE → CS | Stage 5 | Closed Won | Handoff doc (6 items above) |
| CS → AE | Stage 6→3 | Expansion signal | Health score, usage data, identified opportunity |

### Escalation 규칙
| 상황 | Action | 담당 |
|------|--------|------|
| Deal stuck >30 days | Alert to Sales Manager | Agent → Manager |
| Discount >20% requested | Manager approval required | AE → Manager |
| Health Score → Red | Immediate CS + Manager review | Agent → CS Manager |
| Champion leaves company | Re-qualify opportunity | Agent alert → AE |
| Forecast miss >20% | Executive review | Ops → VP Sales |

### Data Hygiene 규칙
- 모든 Activity는 CRM에 24시간 내 기록
- Opportunity stage 변경 시 MEDDICC 해당 필드 업데이트 필수
- Closed Lost 시 Loss Reason (1차 + 2차) + Competitor 기록 필수
- Contact의 Role, Engagement Level 분기 1회 이상 갱신
