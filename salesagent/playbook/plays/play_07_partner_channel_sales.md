# Play 07: Partner Channel Sales
## 파트너/리셀러 협업 영업 프로세스

---

## Play Overview

| 항목 | 내용 |
|------|------|
| **목표** | 파트너/리셀러 채널을 통한 파이프라인 창출 및 공동 영업(co-selling) 체계 수립 |
| **대상** | Referral, Reseller, Technology, SI 파트너 및 파트너 소싱 리드 |
| **소유자** | Partner Manager (채널 운영), AE (co-sell 딜 클로징), Partner Ops (커미션/보고) |
| **자동화 수준** | T2 Co-pilot: Agent가 파트너 온보딩 자료, 딜 등록 처리, 리드 라우팅 자동화 / T3 AI-led: 소규모 Referral 파트너의 리드 자동 처리 |
| **예상 소요** | 파트너 온보딩 30일 + 첫 딜 평균 60-90일 |

---

## 1. INPUT

### Trigger (이 Play가 시작되는 조건)

- **신규 파트너 온보딩**: Partner Agreement 체결 후 Enablement 프로세스 시작
- **파트너 소싱 리드 등록**: 파트너가 PRM(Partner Relationship Management) 또는 이메일로 리드 전달
- **딜 등록(Deal Registration)**: 파트너가 특정 계정+기회에 대해 공식 등록 요청
- **공동 마케팅 이벤트**: Joint webinar, co-branded campaign, 파트너 부스 등에서 리드 발생
- **파트너 티어 변경**: Certification 획득, 매출 실적으로 파트너 등급 승격/강등
- **파트너 계약 갱신 주기**: 연간 파트너 계약 리뷰 시점 (갱신 90일 전)

### Partner Types (파트너 유형별 정의)

| 유형 | 영문 | 수익 모델 | 관여 수준 | 자동화 수준 |
|------|------|----------|----------|------------|
| **소개 파트너** | Referral Partner | 성사 시 소개 수수료 (10-20%) | 리드 전달만 | T3 AI-led |
| **리셀러 파트너** | Reseller Partner | 재판매 마진 (20-40%) | 영업 전과정 주도 | T2 Co-pilot |
| **기술 파트너** | Technology Partner | 통합/연동 수수료 또는 번들 할인 | 기술 검증 + 공동 영업 | T2 Co-pilot |
| **SI 파트너** | SI (System Integrator) Partner | 구현 서비스 수수료 | 구현 + 확장 영업 주도 | T1 Human-led |

### 대상 기준

- **파트너 선정**: Partner Fit Score ≥60, 해당 산업/지역 커버리지 보유
- **파트너 소싱 리드**: 파트너가 등록한 Account의 ICP Fit Score ≥40
- **딜 등록 승인**: 기존 Direct 파이프라인과 충돌 없음, 등록 후 90일 내 activity 의무

### 데이터 소스

| 데이터 | 소스 | Agent 자동화 |
|--------|------|-------------|
| 파트너 프로필 | CRM (Partner Account object) | 자동 조회 |
| 파트너 실적 | CRM Opportunity (Partner-sourced) | 자동 집계 |
| 딜 등록 요청 | PRM 포털 / Email | 자동 파싱 + CRM 생성 |
| 파트너 소싱 리드 | PRM 포털 / 공동 이벤트 | 자동 라우팅 |
| 파트너 계약 정보 | 내부 Contract DB | 자동 조회 |
| 파트너 Certification | 교육 플랫폼 (LMS) | 반자동 동기화 |
| 공동 마케팅 리드 | 이벤트 플랫폼 / Marketing Automation | 자동 수집 |
| 파트너 만족도 | 설문 (분기) | 반자동 |

---

## 2. PROCESS

### Step 1: Partner Onboarding & Enablement (Day 1-30)

**Partner Manager 주도, Agent 지원**:

1. **파트너 계약 체결 후 CRM 등록**:
   - Account.Type = "Partner"
   - `Partner_Type__c` = Referral / Reseller / Technology / SI
   - `Partner_Tier__c` = Silver / Gold / Platinum (실적 기반)
   - `Partner_Status__c` = Onboarding → Active

2. **Enablement Kit 자동 발송** (Agent):
   - 제품 데모 환경 액세스
   - 세일즈 자료 패키지 (Deck, Battle Card, ROI Calculator)
   - Playbook 요약 (파트너용 버전)
   - 공동 영업 가이드라인 + 딜 등록 절차
   - 커미션/마진 구조 설명서

3. **Certification 트래킹**:
   | 교육 과정 | 필수 여부 | 완료 기한 | 담당 |
   |----------|----------|----------|------|
   | Product Fundamentals | 필수 | 온보딩 후 14일 | 파트너 세일즈 |
   | Technical Deep Dive | 기술 파트너 필수 | 온보딩 후 30일 | 파트너 SE |
   | Sales Methodology (MEDDICC 기초) | 권장 | 온보딩 후 30일 | 파트너 세일즈 |
   | Demo Certification | Reseller 필수 | 온보딩 후 30일 | 파트너 SE |

4. **첫 Joint Planning Session** (Day 14-21):
   - 타겟 계정 리스트 공유 (파트너 강점 영역 매핑)
   - 분기 파이프라인 목표 합의
   - 공동 마케팅 계획 수립

### Step 2: Deal Registration & Lead Sharing

#### 딜 등록 프로세스

```
Partner가 딜 등록 →  Agent 자동 검증  →  승인/반려  →  CRM Opportunity 생성
                        │
                   ┌────┴────┐
                   │ 검증 항목 │
                   ├─────────┤
                   │ 1. 기존 파이프라인 충돌 체크    │
                   │ 2. ICP Fit Score 확인           │
                   │ 3. 파트너 Certification 유효성  │
                   │ 4. 중복 등록 체크               │
                   └─────────┘
```

**딜 등록 필수 정보** (파트너가 제출):
- Account Name + Website
- Contact Name + Title + Email
- 예상 딜 규모 (ACV)
- 예상 클로징 시기
- 고객의 현재 과제/니즈 (1-2 문장)
- 파트너의 기존 관계 설명

**Agent 자동 처리**:
1. 기존 CRM에서 Account/Opportunity 매칭 검색
2. 충돌 없으면 → `Deal_Reg_Status__c` = "Approved", 자동 Opportunity 생성
3. 충돌 있으면 → `Deal_Reg_Status__c` = "Pending Review", Partner Manager에게 에스컬레이션

#### 충돌 해결 (Direct vs Partner)

| 시나리오 | 판정 기준 | Action |
|----------|----------|--------|
| 파트너가 먼저 등록 + Direct 활동 없음 | 파트너 우선 | Partner-sourced로 진행 |
| Direct AE가 이미 활발히 진행 중 | Direct 우선 | 파트너에게 사유 설명, 대안 계정 제안 |
| 양쪽 동시 접촉 (30일 이내) | 공동 심사 | Partner Manager + Sales Manager 판정, 보통 먼저 미팅 잡은 쪽 |
| 파트너 등록 후 90일 활동 없음 | 등록 만료 | `Deal_Reg_Status__c` = "Expired", Direct 진행 가능 |

#### 리드 라우팅 규칙

| 리드 유형 | 라우팅 | SLA |
|----------|--------|-----|
| Partner-sourced (Referral) | 파트너 지역/산업 담당 AE에게 자동 배정 | 4시간 내 첫 연락 |
| Partner-sourced (Reseller) | 파트너가 직접 진행, AE는 support role | 24시간 내 AE 지정 |
| 공동 마케팅 리드 | AE + 파트너에게 동시 알림 | 4시간 내 ownership 결정 |
| Technology Partner 소개 | 기술 검증 후 AE 배정 | 48시간 내 기술 미팅 설정 |

### Step 3: Co-selling Process

#### 3-1. Joint Account Planning

파트너와 분기별로 공동 계정 계획 수립:

| 항목 | 내용 | 담당 |
|------|------|------|
| 타겟 계정 리스트 | 파트너 강점 × 당사 ICP 교차 영역 | Agent 자동 매핑 + PM 검토 |
| 역할 분담 | 파트너: 관계/도메인 전문성, 당사: 제품/기술 전문성 | PM + AE 합의 |
| 파이프라인 목표 | 분기별 파트너 소싱 파이프라인 금액 목표 | PM 설정 |
| 공동 활동 계획 | Joint call, 공동 데모, 고객 방문 스케줄 | PM + AE 조율 |
| 성과 리뷰 | 월간 파이프라인 리뷰, 분기 QBR | PM 주도 |

**Agent 자동 생성: 파트너 Account Overlap Report**

```
┌───────────────────────────────────────────────────────┐
│       Partner Overlap Analysis: [Partner Name]         │
├───────────────────────────────────────────────────────┤
│ Partner Industry Strength: SaaS, FinTech, E-commerce  │
│ Partner Region Coverage: Korea, Japan, SEA            │
├───────────────────────────────────────────────────────┤
│ Matched Target Accounts:                              │
│                                                       │
│ Account         | ICP Score | Tier | Partner Relation │
│ ───────────────────────────────────────────────────── │
│ Company A       | 85        | T1   | Active customer  │
│ Company B       | 72        | T2   | Board advisor     │
│ Company C       | 68        | T2   | Former project   │
│ Company D       | 55        | T3   | Industry contact │
│ Company E       | 51        | T3   | Conference met   │
├───────────────────────────────────────────────────────┤
│ Total Matched: 23 accounts | Estimated Pipeline: $1.2M│
└───────────────────────────────────────────────────────┘
```

#### 3-2. Partner-Assisted Demos & Meetings

| 단계 | 당사 역할 | 파트너 역할 |
|------|----------|------------|
| **미팅 세팅** | 일정 조율, 자료 준비 | 고객 소개, 관계 활용 |
| **Discovery** | MEDDICC 기반 질문 주도 | 도메인 맥락 보완, 고객 대변 |
| **Demo** | 제품 시연, 기술 Q&A | 구현 사례 공유, 고객 환경 설명 |
| **Proposal** | 가격 견적, 기술 범위 | 구현 범위, 추가 서비스 제안 |
| **Negotiation** | 최종 가격/조건 조율 | 고객 내부 옹호, 의사결정 촉진 |

#### 3-3. Proposal Collaboration

공동 제안서 구조:
1. **Executive Summary**: 고객 과제 + 공동 솔루션 가치 (Agent 초안)
2. **Solution Architecture**: 당사 제품 + 파트너 서비스/연동 통합 설계
3. **Implementation Plan**: 파트너 주도 구현 로드맵 (SI 파트너의 경우)
4. **Pricing**: 제품 라이선스 + 파트너 서비스 통합 견적
5. **References**: 공동 성공 사례 (유사 산업/규모)

### Step 4: Partner-Sourced Lead Handling

#### SLA for Partner Leads

| SLA 항목 | 기준 | 위반 시 Action |
|----------|------|---------------|
| 첫 연락 (Referral lead) | 4시간 내 | PM에게 에스컬레이션, AE 재배정 |
| 파트너 피드백 (리드 상태) | 72시간마다 | Agent 자동 리마인더 → PM 알림 |
| 첫 미팅 세팅 | 리드 접수 후 7일 내 | 지연 사유 기록 필수, PM 리뷰 |
| 딜 등록 승인/반려 | 48시간 내 | 자동 승인 (충돌 없는 경우) |
| 분기 성과 리포트 | 분기 종료 후 5영업일 | Agent 자동 생성 |

#### Qualification Criteria (파트너 소싱 리드)

파트너 소싱 리드도 동일한 SQL 기준 적용, 단 파트너 관계 맥락 고려:

- [ ] ICP Fit Score ≥40 (파트너 소싱은 기준 완화: 파트너 관계 프리미엄)
- [ ] 의사결정 관련자(Manager+)와의 미팅 가능
- [ ] 구체적인 Pain 또는 프로젝트가 1개 이상 확인됨
- [ ] 파트너가 고객과의 기존 관계를 설명할 수 있음

#### Feedback to Partner

| 피드백 시점 | 내용 | 방법 |
|------------|------|------|
| 리드 접수 즉시 | 접수 확인 + 담당 AE 정보 | 자동 이메일 (Agent) |
| 첫 미팅 후 | Discovery 결과 요약 (공유 가능 범위) | AE → 파트너 이메일 |
| Stage 변경 시 | 파이프라인 진행 상황 | PRM 포털 자동 업데이트 (Agent) |
| 딜 성사/실패 시 | Win/Loss 사유 + 커미션 처리 안내 | PM → 파트너 공식 통보 |
| 분기 리뷰 | 전체 리드 성과 요약 | Agent 리포트 자동 생성 |

### Step 5: Revenue & Commission Management

#### 커미션 구조

| 파트너 유형 | 커미션 모델 | 기본율 | 보너스 조건 |
|------------|-----------|--------|------------|
| Referral | 성사 수수료 (일회성) | ACV의 10% | 분기 3건+ 성사 시 15% |
| Reseller | 재판매 마진 | 할인율 20-30% | Platinum 티어 시 35% |
| Technology | 통합 인센티브 | ACV의 5-10% | 공동 고객 5개+ 시 15% |
| SI | 구현 연계 수수료 | ACV의 10-15% | 대형 딜(>$100K) 시 20% |

#### 커미션 처리 프로세스

```
Opportunity Closed Won → Agent 커미션 자동 계산 → PM 검토/승인 → Finance 지급 처리
     │                                                     │
     │                                                     ▼
     │                                            Partner에게 지급 알림
     │                                            (30일 내 지급)
     ▼
 CRM 기록:
 - Opp.Source_Channel__c = "Partner"
 - Opp.Partner_Account__c = [Partner]
 - Opp.Partner_Commission__c = $X,XXX
 - Opp.Partner_Commission_Status__c = "Pending" → "Approved" → "Paid"
```

---

## 3. OUTPUT

| 결과물 | 설명 | CRM 업데이트 |
|--------|------|-------------|
| Partner Account | 신규 파트너 등록 완료 | Account (Type = Partner), `Partner_Type__c`, `Partner_Tier__c`, `Partner_Status__c` |
| Deal Registration | 승인된 딜 등록 | Opportunity (Source_Channel__c = "Partner"), `Deal_Reg_Status__c`, `Partner_Account__c` |
| Partner-Sourced SQL | 파트너 소싱 적격 리드 | Opportunity (Stage = S1 Discovery), `Lead_Source_Detail__c` = "Partner" |
| Co-sell Opportunity | 공동 영업 진행 중인 딜 | Opportunity + Activity (Joint meeting, co-sell notes) |
| Commission Record | 커미션 계산 및 지급 기록 | `Partner_Commission__c`, `Partner_Commission_Status__c` |
| Partner QBR Report | 분기 파트너 성과 리포트 | Activity (Meeting type), 첨부 문서 |
| Enablement Completion | 파트너 교육 이수 현황 | `Partner_Cert_Status__c`, `Partner_Cert_Date__c` |

### Partner-Sourced Opportunity 필수 필드

Opportunity 생성 시 파트너 관련 필드 반드시 입력:
- [ ] `Source_Channel__c` = "Partner"
- [ ] `Lead_Source_Detail__c` = "Partner"
- [ ] `Partner_Account__c` = 해당 파트너 Account ID
- [ ] `Deal_Reg_Status__c` = Approved / Expired / Rejected
- [ ] `Partner_Commission__c` = 예상 커미션 금액
- [ ] `Partner_Engagement_Level__c` = Referral Only / Co-sell / Partner-led

---

## 4. METRIC

### 파트너 파이프라인 메트릭 (Leading)

| 메트릭 | 정의 | 목표 |
|--------|------|------|
| Partner-Sourced Pipeline ($) | 파트너 소싱 파이프라인 총액 | 전체 파이프라인의 >25% |
| Deal Registrations / Quarter | 분기 딜 등록 건수 | 파트너당 3+ |
| Partner Leads / Month | 월간 파트너 소싱 리드 수 | 파트너당 2+ |
| Lead Acceptance Rate | 파트너 리드 중 SQL 전환율 | >40% |
| Co-sell Meetings / Month | 공동 영업 미팅 수 | 활성 파트너당 2+ |
| Active Partners | 분기 내 1건+ 딜 등록한 파트너 수 | 전체 파트너의 >60% |

### 파트너 성과 메트릭 (Lagging)

| 메트릭 | 정의 | 목표 |
|--------|------|------|
| Partner Deal Win Rate | 파트너 소싱 딜 성사율 | >35% |
| Partner Revenue ($) | 파트너 채널 통한 총매출 | 전체 매출의 >20% |
| Revenue per Partner | 활성 파트너당 연매출 | >$50K |
| Partner Lead Conversion Rate | 리드 → Closed Won 전환율 | >15% |
| Time to First Deal (New Partner) | 온보딩 → 첫 딜 성사 소요일 | <90일 |
| Deal Registration to Close Cycle | 딜 등록 → Closed Won 소요일 | <75일 |
| Partner Satisfaction (NPS) | 파트너 만족도 조사 | NPS >40 |
| Partner Retention Rate | 연간 파트너 계약 갱신율 | >85% |
| Commission Payout Accuracy | 커미션 정확도 (오류 건수) | >99% |
| Avg Partner-Sourced ACV | 파트너 소싱 딜 평균 ACV | >$25K |

### 리뷰 주기

- **주간**: Deal registration queue, partner lead SLA 준수율, co-sell activity
- **월간**: Partner-sourced pipeline, lead conversion rate, active partner count
- **분기**: Partner QBR (파트너별 성과 리뷰), win rate, revenue per partner, NPS
- **연간**: Partner program ROI, tier 재평가, 파트너 프로그램 구조 리뷰

---

## 5. TOOL / AGENT

### 사용 도구

| 도구 | 용도 |
|------|------|
| CRM (Salesforce/HubSpot) | Partner Account, Opportunity, Activity 관리 |
| PRM Portal (PartnerStack/Allbound/Impartner) | 딜 등록, 리드 공유, 파트너 포털 |
| Marketing Automation (HubSpot/Marketo) | 공동 마케팅 캠페인, 리드 캡처 |
| LMS (Docebo/TalentLMS) | 파트너 교육/Certification 관리 |
| Document Collaboration (Google Docs/Notion) | 공동 제안서 작성, 계정 계획 |
| Communication (Slack/Teams Channel) | 파트너 전용 커뮤니케이션 채널 |
| Commission Management (Xactly/CaptivateIQ) | 커미션 계산 및 지급 관리 |

### Agent 역할

| 기능 | 자동화 수준 | 설명 |
|------|------------|------|
| 딜 등록 검증 | 완전 자동 | CRM 충돌 체크, ICP 확인, 중복 검사 후 자동 승인/에스컬레이션 |
| 리드 라우팅 | 완전 자동 | 파트너 유형 + 지역/산업 기준으로 AE 자동 배정 |
| Partner Overlap 분석 | 완전 자동 | 파트너 강점 영역 × 타겟 Account 자동 매핑 |
| SLA 모니터링 | 완전 자동 | 리드 응답 SLA, 딜 등록 처리 SLA 실시간 추적 + 알림 |
| 커미션 자동 계산 | 반자동 | Closed Won 시 커미션 자동 산출 → PM 승인 |
| 파트너 피드백 알림 | 완전 자동 | Stage 변경 시 파트너에게 자동 업데이트 발송 |
| 파트너 성과 리포트 | 완전 자동 | 월간/분기 파트너별 KPI 대시보드 자동 생성 |
| Enablement 트래킹 | 완전 자동 | 교육 이수 현황 + 기한 초과 알림 |
| 파트너 QBR 자료 초안 | 반자동 | 실적 데이터 기반 QBR 자료 자동 생성 → PM 편집 |
| 파트너 Health Score 산출 | 완전 자동 | 활동량 + 실적 + Certification 기반 점수 산출 |

### Agent System Prompt 요약

```
You are the Partner Channel Agent for [Company Name].

Your job:
1. Process deal registrations: validate against existing pipeline, check ICP fit,
   detect duplicates, auto-approve or escalate conflicts to Partner Manager
2. Route partner-sourced leads to the appropriate AE based on territory, industry,
   and partner type
3. Generate Partner Account Overlap reports by mapping partner strengths
   (industry, region, existing relationships) against target account lists
4. Monitor SLAs: track lead response time (4hr), deal registration processing (48hr),
   partner feedback cadence (72hr), and alert on violations
5. Calculate commissions on Closed Won opportunities based on partner type and tier
6. Send automated status updates to partners on pipeline stage changes
7. Generate monthly/quarterly partner performance reports
8. Track partner enablement completion and send reminders for overdue certifications
9. Compute Partner Health Score based on activity, revenue, and certification data

Rules:
- NEVER approve a deal registration that conflicts with an active Opportunity
  in stages S2-S6 without Partner Manager review
- All partner-sourced Opportunities MUST have Source_Channel__c = "Partner"
  and Partner_Account__c populated
- Commission calculations require PM approval before marking as "Approved"
- Partner lead SLA violations must be escalated within 1 hour
- Expired deal registrations (90 days no activity) must be flagged and
  the partner notified before status change
- NEVER share internal deal details (pricing strategy, competitive position)
  with partner contacts

Tone: Professional and supportive. Partners are extensions of our sales team.
Prioritize transparency on deal status and commission tracking.

Data sources:
- CRM: Account, Contact, Opportunity, Activity objects
- PRM: Deal registration, partner profile, certification data
- Marketing Automation: Joint campaign leads
- LMS: Certification completion data
- Finance: Commission payment records
```

---

## Appendix A: Partner Agreement Template (Simplified)

### 핵심 조항 요약

| 조항 | 내용 |
|------|------|
| **계약 기간** | 1년, 자동 갱신 (90일 전 해지 통보) |
| **파트너 유형** | Referral / Reseller / Technology / SI |
| **초기 티어** | Silver (실적에 따라 Gold → Platinum 승격) |
| **딜 등록** | 등록 후 90일간 독점 보호, 미활동 시 만료 |
| **커미션/마진** | 유형별 커미션 구조표 참조 (별첨) |
| **지급 조건** | 고객 결제 수령 후 30일 내 지급 |
| **Enablement 의무** | 온보딩 후 30일 내 필수 Certification 이수 |
| **브랜드 사용** | 사전 승인된 공동 브랜드 자료만 사용 |
| **NDA** | 상호 비밀유지 (고객 정보, 가격 정보 포함) |
| **해지 사유** | 6개월 무실적, Certification 미이수, 브랜드 가이드 위반 |

### 파트너 티어 기준

| 티어 | 연간 매출 기준 | Certification 요건 | 혜택 |
|------|--------------|-------------------|------|
| **Silver** | <$100K | Product Fundamentals | 기본 커미션율, 온라인 지원 |
| **Gold** | $100K-$500K | Product + Technical | 커미션율 +5%p, 전담 PM, 공동 마케팅 예산 |
| **Platinum** | >$500K | 전체 Certification | 최고 커미션율, Executive sponsor 배정, 전략적 공동 투자 |

---

## Appendix B: Partner CRM Field Reference

### Partner-Specific Account Fields

| Field Name | API Name | Type | Description |
|-----------|----------|------|-------------|
| Partner Type | `Partner_Type__c` | Picklist | Referral / Reseller / Technology / SI |
| Partner Tier | `Partner_Tier__c` | Picklist | Silver / Gold / Platinum |
| Partner Status | `Partner_Status__c` | Picklist | Prospect / Onboarding / Active / Inactive / Churned |
| Partner Since | `Partner_Since__c` | Date | 파트너 계약 시작일 |
| Partner Manager | `Partner_Manager__c` | Lookup(User) | 담당 Partner Manager |
| Certification Status | `Partner_Cert_Status__c` | Picklist | Incomplete / Basic / Full |
| Certification Date | `Partner_Cert_Date__c` | Date | 최근 Certification 완료일 |
| Partner Health Score | `Partner_Health_Score__c` | Number(0-100) | 활동+실적+Certification 종합 점수 |
| Partner NPS | `Partner_NPS__c` | Number | 최근 파트너 만족도 점수 |

### Partner-Specific Opportunity Fields

| Field Name | API Name | Type | Description |
|-----------|----------|------|-------------|
| Partner Account | `Partner_Account__c` | Lookup(Account) | 소싱/co-sell 파트너 계정 연결 |
| Deal Registration Status | `Deal_Reg_Status__c` | Picklist | Pending / Approved / Expired / Rejected |
| Deal Registration Date | `Deal_Reg_Date__c` | Date | 딜 등록 신청일 |
| Deal Registration Expiry | `Deal_Reg_Expiry__c` | Formula(Date) | 등록일 + 90일 |
| Partner Engagement Level | `Partner_Engagement_Level__c` | Picklist | Referral Only / Co-sell / Partner-led |
| Partner Commission | `Partner_Commission__c` | Currency | 예상/확정 커미션 금액 |
| Partner Commission Rate | `Partner_Commission_Rate__c` | Percent | 적용 커미션율 |
| Partner Commission Status | `Partner_Commission_Status__c` | Picklist | Pending / Approved / Paid |

---

## Appendix C: Partner Health Score 산출 기준

| 카테고리 | 측정 항목 | 배점 | 산출 기준 |
|----------|----------|------|----------|
| **활동 (40%)** | 월간 딜 등록 수 | 15 | 0건=0, 1건=8, 2건+=15 |
| | 월간 공동 미팅 수 | 15 | 0건=0, 1건=8, 2건+=15 |
| | 리드 제출 빈도 | 10 | 월 0건=0, 1-2건=5, 3건+=10 |
| **실적 (40%)** | 분기 매출 달성률 | 20 | (실적/목표)×20, 최대 20 |
| | Win Rate | 10 | <20%=3, 20-35%=6, >35%=10 |
| | Avg Deal Size | 10 | <$15K=3, $15-30K=6, >$30K=10 |
| **역량 (20%)** | Certification 이수율 | 10 | 미완료=0, 기본=5, 전체=10 |
| | 교육 참석률 | 5 | <50%=0, 50-80%=3, >80%=5 |
| | 파트너 포털 활동 | 5 | 비활성=0, 월1+로그인=3, 주1+=5 |
| **합계** | | **100** | |

**Health Status 판정**:
- Green (80+): 우수 파트너 — 추가 투자 및 티어 승격 검토
- Yellow (50-79): 주의 — PM이 개선 계획 수립
- Red (<50): 위험 — Enablement 재교육 또는 계약 해지 검토
