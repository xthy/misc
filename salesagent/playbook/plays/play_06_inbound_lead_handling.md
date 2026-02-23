# Play 06: Inbound Lead Handling
## 웹사이트/이벤트 리드 즉시 응대 프로세스

---

## Play Overview

| 항목 | 내용 |
|------|------|
| **목표** | 인바운드 리드를 5분 내 응대하여 SQL로 전환, 소스별 최적 응대 프로세스 실행 |
| **대상** | 웹사이트, 이벤트, 콘텐츠, 레퍼럴 등 모든 인바운드 채널의 리드 |
| **소유자** | SDR (초기 응대/적격성 검증), AE (미팅 이후 인수) |
| **자동화 수준** | T2: Co-pilot (Agent 즉시 enrichment + 초안, SDR 검토/발송), T3: AI-led (Agent 자동 응대 + 라우팅, 적격만 SDR 전달) |
| **핵심 SLA** | 5분 이내 첫 응대 (업무시간 내), 15분 이내 (업무시간 외 — 자동 응답) |

> **Play 01과의 관계**: Play 01(New Logo Outbound)이 우리가 먼저 타겟을 찾아가는 **공격** 프로세스라면, Play 06은 리드가 먼저 찾아오는 **수비→역공** 프로세스입니다. Outbound는 14일 시퀀스로 관심을 만들지만, Inbound는 이미 존재하는 관심을 놓치지 않는 것이 핵심입니다. **Speed-to-lead가 전환율의 #1 결정 요인**입니다.

---

## 1. INPUT

### Trigger (이 Play가 시작되는 조건)

| # | Trigger | 설명 |
|---|---------|------|
| 1 | Website form submission | Contact Us, Pricing 문의, Demo 요청 |
| 2 | Content download | 백서, 케이스 스터디, ROI 계산기, 가이드 |
| 3 | Event/Webinar 등록 또는 참석 | 웨비나 참석, 오프라인 이벤트 방문, 부스 스캔 |
| 4 | Chat widget inquiry | 웹사이트 실시간 채팅으로 문의 |
| 5 | Referral | 기존 고객, 파트너, 네트워크 추천 |
| 6 | Free trial / PoC signup | 셀프서브 트라이얼 또는 PoC 요청 |

### Lead Source Classification & Priority

| Source Type | Priority | Response SLA | Routing | 전환율 벤치마크 |
|-------------|----------|-------------|---------|---------------|
| **Demo Request** | P1 Critical | 5분 | AE 즉시 배정 (Fit A/B), SDR (Fit C) | 30-50% → SQL |
| **Pricing Page + Contact Us** | P1 Critical | 5분 | SDR → AE 핸드오프 | 20-35% → SQL |
| **Free Trial / PoC Signup** | P1 Critical | 5분 | SDR + SE 배정 | 25-40% → SQL |
| **Referral** | P2 High | 15분 | 추천인의 Account Owner 또는 SDR | 40-60% → SQL |
| **Chat Inquiry** | P2 High | 실시간 | T3: Agent 실시간 응답, T1/T2: SDR 인계 | 10-20% → SQL |
| **Webinar/Event 참석** | P3 Medium | 2시간 | SDR 시퀀스 배정 | 5-15% → SQL |
| **Content Download** | P3 Medium | 2시간 | 자동 nurture → SDR (engagement 기반) | 3-8% → SQL |
| **Webinar/Event 등록 (미참석)** | P4 Low | 24시간 | 자동 nurture 시퀀스 | 1-3% → SQL |

### 대상 기준

- **필수**: 유효한 연락처 정보 (이메일 + 이름 + 회사명)
- **즉시 스코어링**: 리드 인입 시 ICP Fit Score 자동 계산
- **중복 확인**: CRM 기존 Account/Contact와 매칭 체크
- **제외**: 경쟁사 이메일 도메인, 개인 이메일(gmail/yahoo 등 — B2B 기준), 명백한 스팸

### 데이터 소스

| 데이터 | 소스 | Agent 자동화 |
|--------|------|-------------|
| 리드 기본 정보 (이름, 이메일, 회사) | Form submission / Chat log / Event platform | 자동 수집 |
| 회사 정보 (산업, 규모, 매출, 지역) | Enrichment API (Clearbit/ZoomInfo/Apollo) | 자동 보강 |
| 기술스택 | BuiltWith / Wappalyzer / Enrichment | 자동 수집 |
| CRM 기존 기록 | CRM (Account, Contact, Opportunity) | 자동 조회 (중복 확인) |
| 웹사이트 행동 데이터 | Web analytics (방문 페이지, 체류 시간, 방문 횟수) | 자동 수집 |
| 폼 제출 상세 (메시지, 관심 제품) | Form data fields | 자동 파싱 |
| Intent 신호 | Bombora / G2 / TrustRadius | 자동 수집 |
| 소셜 프로필 | LinkedIn (enrichment 경유) | 반자동 |

---

## 2. PROCESS

### Step 1: Instant Lead Capture & Enrichment (0-2분)

리드 인입과 동시에 Agent가 자동 실행하는 초기 처리:

**1-1. 데이터 수집 & 보강**
- 폼 데이터 파싱: 이름, 이메일, 회사명, 직급, 메시지 내용
- Enrichment API 호출: 회사 규모, 산업, 매출, 기술스택, 자금 조달 현황
- LinkedIn 프로필 매칭 (가능한 경우): 직급 확인, 의사결정 영향력 판단
- 웹사이트 행동 데이터 연결: 방문 페이지, 체류 시간, 재방문 여부

**1-2. CRM 중복 확인 (De-duplication)**

| 매칭 결과 | Action |
|----------|--------|
| 기존 Account + Contact 존재 | 기존 레코드에 Activity 추가, Account Owner에게 즉시 알림 |
| 기존 Account 있으나 Contact 신규 | Contact 생성, Account Owner + SDR에게 알림 |
| 기존 Contact (다른 Account) | 이직 가능성 확인, 신규 Account 생성 검토 |
| 완전 신규 | Account + Contact 생성, ICP Score 계산 후 라우팅 |

**1-3. ICP Fit Score 즉시 산출**
- Firmographic (40%): 산업, 직원 수, 연매출, 지역, 성장률
- Technographic (30%): CRM, 기술 성숙도, 현재 솔루션
- Needs-based (30%): 폼 메시지 분석, 관심 영역 추론
- Fit 등급 산출: A(80-100), B(60-79), C(50-59), D(<50)

### Step 2: Lead Scoring & Routing (2-5분)

**2-1. 복합 점수 산출**

| 점수 구성 | 가중치 | 산출 방법 |
|----------|--------|----------|
| ICP Fit Score | 기본 (0-100) | Enrichment 기반 자동 계산 |
| Source Priority Score | 가산 (0-20) | Demo: +20, Contact Us: +15, Referral: +18, Trial: +15, Chat: +10, Event: +8, Content: +5 |
| Engagement Score | 가산 (0-30) | 웹 방문 빈도, 페이지 뷰, 이전 이메일 오픈/클릭 |
| Intent Score | 가산 (0-30) | 외부 intent 신호 (Bombora/G2) |

**2-2. 라우팅 규칙**

| 조건 | 라우팅 | 응대 방식 |
|------|--------|----------|
| Fit A + Demo/Trial/Contact Us | AE 즉시 배정 | AE 직접 전화 (5분 내) + 캘린더 링크 발송 |
| Fit A/B + Demo/Trial | SDR → AE 핸드오프 | SDR 즉시 전화 (5분 내) + 미팅 세팅 |
| Fit A/B + Content/Event | SDR 시퀀스 배정 | 맞춤 follow-up 이메일 (2시간 내) + 콜 |
| Fit B/C + Demo/Contact Us | SDR 시퀀스 배정 | SDR 전화 (1시간 내) + 적격성 확인 |
| Fit C + Content/Event | 자동 Nurture 시퀀스 | Agent 자동 이메일 시퀀스 |
| Fit D | 자동 Disqualify | Thank you 이메일 + 리소스 링크 (자동) |

**2-3. Round-Robin 배정 규칙**
- Territory 기반: 리드의 지역/산업에 따라 담당 SDR/AE 배정
- Workload 균형: 당일 배정 건수 + 미처리 건수 기반 밸런싱
- Specialty 매칭: 산업/제품 전문성 기반 우선 배정
- Fallback: 배정 후 3분 내 미확인 → 다음 순서 SDR에게 재배정

### Step 3: Speed-to-Lead Response (5분 이내)

> **핵심 원칙**: 인바운드 리드의 전환율은 5분 내 응대 시 10분 내 대비 4배, 30분 내 대비 21배 높습니다 (InsideSales.com 연구). 첫 응답 속도가 곧 전환율입니다.

**소스별 응대 전략**:

#### Demo Request / Pricing / Contact Us (P1)

| 단계 | Action | 담당 | SLA |
|------|--------|------|-----|
| 즉시 | 확인 이메일 자동 발송 (캘린더 링크 포함) | Agent | 0분 (자동) |
| 1-5분 | SDR/AE 전화 시도 | SDR/AE | 5분 내 |
| 전화 연결 시 | 감사 인사 → 요청 확인 → 간단 적격성 → 미팅 제안 | SDR/AE | - |
| 부재 시 | 보이스메일(30초) + 개인화 이메일 + SMS(선택) | SDR | 10분 내 |
| Day 1 | 2차 전화 시도 | SDR | 당일 |
| Day 2 | 3차 전화 시도 + 가치 제공 이메일 | SDR | - |

#### Free Trial / PoC Signup (P1)

| 단계 | Action | 담당 | SLA |
|------|--------|------|-----|
| 즉시 | 환영 이메일 + 시작 가이드 자동 발송 | Agent | 0분 (자동) |
| 1-5분 | SDR 전화: "설정 도움이 필요하신지?" | SDR | 5분 내 |
| Day 1 | 온보딩 체크인 이메일 | Agent/SDR | 24시간 |
| Day 3 | 활용도 체크 + 미팅 제안 | SDR | - |
| Day 7 | Trial 중간 점검 콜 | SDR/AE | - |
| Day 14 | Trial 종료 전 전환 미팅 제안 | AE | - |

#### Referral (P2)

| 단계 | Action | 담당 | SLA |
|------|--------|------|-----|
| 즉시 | 추천인에게 감사 알림 (자동 또는 수동) | Agent/SDR | 0분 |
| 5-15분 | 리드에게 전화: 추천인 언급하며 접근 | SDR/AE | 15분 내 |
| 부재 시 | 추천인 이름 포함 개인화 이메일 | SDR | 30분 내 |
| Day 1-2 | 미팅 세팅 시도 | SDR | - |

#### Chat Inquiry (P2)

| 단계 | Action | 담당 | SLA |
|------|--------|------|-----|
| 실시간 | T3: Agent 실시간 채팅 응대 | Agent | 즉시 |
| 실시간 | T1/T2: SDR로 라이브 핸드오프 | SDR | 30초 내 |
| 채팅 중 | 적격성 판단 → 미팅 제안 또는 리소스 제공 | SDR/Agent | - |
| 채팅 후 | 대화 요약 CRM 기록, follow-up 이메일 | Agent | 10분 내 |

#### Event/Webinar 참석 (P3)

| 단계 | Action | 담당 | SLA |
|------|--------|------|-----|
| 이벤트 후 | 참석 감사 이메일 + 세션 자료 + 관련 콘텐츠 | Agent | 2시간 내 |
| Day 1 | Fit A/B 리드에게 SDR 전화 시도 | SDR | 24시간 |
| Day 2-3 | 개인화 follow-up 이메일 (세션 내용 언급) | SDR/Agent | - |
| Day 5-7 | 2차 전화 + 미팅 제안 | SDR | - |

#### Content Download (P3)

| 단계 | Action | 담당 | SLA |
|------|--------|------|-----|
| 즉시 | Thank you 이메일 + 다운로드 링크 + 관련 콘텐츠 추천 | Agent | 0분 (자동) |
| Day 1-2 | Fit A/B: SDR 전화 (콘텐츠 주제 연결 가치 제안) | SDR | - |
| Day 3-5 | 추가 콘텐츠 시리즈 이메일 (자동) | Agent | - |
| Day 7+ | Engagement 기반 판단: 추가 interaction → SDR escalation | Agent | - |

### Step 4: Lead Qualification (Day 1-3)

첫 미팅/통화에서의 적격성 검증:

**4-1. 초기 BANT + MEDDICC 확인**

| 요소 | 확인 질문 | CRM 필드 |
|------|----------|----------|
| **Budget** | "이번 프로젝트에 예산이 배정되어 있나요?" | `Budget_Status__c` |
| **Authority** | "도입 결정은 어떤 프로세스로 이루어지나요?" | `MEDDICC_DP__c` |
| **Need** | "지금 이 솔루션을 찾게 된 계기가 무엇인가요?" | `MEDDICC_Pain__c` |
| **Timeline** | "언제까지 도입을 원하시나요?" | `MEDDICC_DP_Date__c` |
| **Metrics** | "성공을 어떤 수치로 측정하실 계획인가요?" | `MEDDICC_Metrics__c` |
| **Champion** | "내부에서 이 프로젝트를 가장 지지하는 분은?" | `MEDDICC_Champion__c` |

**4-2. 리드 분류 판정**

| 판정 | 기준 | Action |
|------|------|--------|
| **SQL** | Fit A/B + BANT 2개 이상 충족 + 구체적 Pain 확인 | Opportunity 생성 (S1 Discovery), AE 핸드오프 |
| **MQL (Nurture)** | Fit A/B + 관심 있으나 타이밍/예산 미확보 | Nurture 시퀀스 배정, 재접촉 일정 설정 |
| **Disqualify** | Fit C/D + Pain 불명확 + 구매 의향 없음 | DQ 사유 기록, Thank you 이메일, 리소스 제공 |

**4-3. SQL Handoff → AE**

미팅이 SQL로 인정되려면:
- [ ] ICP Fit Score >=50인 계정
- [ ] 의사결정 관련자 (Manager+)와의 미팅
- [ ] 구체적인 Pain 또는 관심사가 1개 이상 확인됨
- [ ] 미팅 일시 확정 (캘린더 초대 수락)
- [ ] Inbound Source 기록 (`Source_Channel__c` = "Inbound")

AE에게 전달하는 필수 정보:
1. **Lead Source & Context**: 어떤 채널로 인입했고, 폼에 무엇을 적었는지
2. **Account Context**: 산업, 규모, 기술스택, ICP Score
3. **Contact Info**: 이름, 직급, LinkedIn, 선호 커뮤니케이션
4. **Pain / Interest**: 인바운드 동기, SDR이 파악한 초기 Pain
5. **Engagement History**: 웹 행동, 콘텐츠 다운로드 이력, 이전 접촉 기록
6. **Meeting Agenda**: 합의된 미팅 목적과 기대사항

### Step 5: Non-SQL Lead Nurturing

적격 미달이지만 잠재력 있는 리드의 장기 육성 프로세스:

**5-1. Nurture 시퀀스 배정 기준**

| Persona / Interest | 시퀀스 | 주기 | 기간 |
|-------------------|--------|------|------|
| Technical Buyer + 제품 관심 | Technical Education 시퀀스 | 주 1회 | 8주 |
| Business Buyer + ROI 관심 | Business Value 시퀀스 | 격주 | 12주 |
| Executive + 전략 관심 | Executive Insight 시퀀스 | 월 1회 | 6개월 |
| 일반 관심 (콘텐츠 다운로드) | General Awareness 시퀀스 | 격주 | 8주 |

**5-2. Re-engagement Trigger (Nurture → Active)**

| 신호 | Action | 라우팅 |
|------|--------|--------|
| 이메일 3회 이상 오픈 (7일 내) | SDR 전화 시도 | SDR 자동 배정 |
| 웹사이트 Pricing 페이지 방문 | SDR 즉시 알림 + 전화 | SDR 긴급 알림 |
| 새 콘텐츠 다운로드 | 맞춤 follow-up 이메일 | Agent → SDR |
| 웨비나 재등록 | SDR 사전 접촉 | SDR 배정 |
| 동일 회사 다른 담당자 인바운드 | Multi-threading 기회 알림 | SDR + Account Owner |

**5-3. Lead Recycling**

| 상태 | Recycling 규칙 | 재진입 조건 |
|------|---------------|-----------|
| Nurture 시퀀스 완료, 무응답 | 90일 쿨다운 후 Watch 풀로 이동 | 새 intent 신호 또는 engagement 발생 |
| Disqualified (타이밍) | 6개월 후 재스코어링 | Score 변동 또는 trigger event 발생 |
| Disqualified (Fit 미달) | 연간 재스코어링 | 기업 변화(성장, M&A)로 Fit 개선 |

---

## 3. OUTPUT

| 결과물 | 설명 | CRM 업데이트 |
|--------|------|-------------|
| **SQL** | 적격 미팅이 세팅된 기회 | Opportunity 생성 (S1 Discovery), `Source_Channel__c` = "Inbound", `Lead_Source_Detail__c` = 소스 유형 |
| **Nurture Lead** | 관심 있으나 즉시 전환 불가 | `Contact.Engagement_Level__c` = "Warm", Nurture Sequence 배정, Follow-up Date 설정 |
| **Disqualified** | ICP 미달 또는 명확한 부적격 | `Contact.Engagement_Level__c` = "Cold", DQ Reason 기록, `Disqualify_Reason__c` 입력 |
| **Existing Account Alert** | 기존 고객/진행 중 opp의 추가 접촉 | Account Owner에게 알림, Activity 기록, Opp에 연결 |
| **Handoff Doc** | AE에게 전달되는 미팅 브리핑 | Activity 기록 + `Opp.Description`에 Inbound 컨텍스트 요약 |
| **Enriched Account** | Agent가 보강한 계정 데이터 | `ICP_Fit_Score__c`, `Tech_Stack__c`, `Intent_Score__c` 업데이트 |

### CRM 필수 기록 항목

| 필드 | API Name | 값 예시 |
|------|----------|--------|
| Lead Source | `Source_Channel__c` | Inbound |
| Source Detail | `Lead_Source_Detail__c` | Demo Request / Content Download / Webinar / Referral / Chat / Trial |
| First Response Time | `First_Response_Time__c` | 3분 (DateTime 차이 계산) |
| Inbound Form Data | `Inbound_Form_Data__c` | 폼 제출 원문 (Text Area) |
| Referring URL | `Referring_URL__c` | 유입 페이지 URL |
| Referrer Name | `Referrer_Name__c` | 추천인 이름 (Referral인 경우) |

---

## 4. METRIC

### 활동 메트릭 (Leading)

| 메트릭 | 정의 | 목표 | 측정 주기 |
|--------|------|------|----------|
| **Speed to Lead** | 리드 인입 → 첫 응대 (전화/이메일) 시간 | <5분 (P1/P2), <2시간 (P3) | 일간 |
| **5-Min Response Rate** | 5분 내 응대된 P1/P2 리드 비율 | >80% | 일간 |
| **Contact Attempt Rate** | 인입 리드 중 전화 시도된 비율 (P1/P2) | >95% | 일간 |
| **Contact Rate** | 전화 시도 → 실제 통화 연결 비율 | 30-50% | 주간 |
| **Enrichment Coverage** | 자동 enrichment 완료된 리드 비율 | >90% | 주간 |
| **Routing Accuracy** | 올바른 담당자에게 배정된 비율 | >95% | 주간 |
| **Auto-Response Rate** | 자동 확인 이메일이 즉시 발송된 비율 | 100% | 일간 |

### 결과 메트릭 (Lagging)

| 메트릭 | 정의 | 목표 | 측정 주기 |
|--------|------|------|----------|
| **Inbound SQL / Month** | 인바운드 소스 월간 SQL 수 | 목표 대비 100% | 월간 |
| **Inbound-to-SQL Conversion** | 인바운드 리드 → SQL 전환율 | 전체: 15-25%, Demo: 30-50% | 월간 |
| **SQL-to-Opp Conversion** | SQL → S2 이상 진행 비율 | >60% | 월간 |
| **Pipeline Generated ($)** | 인바운드 기여 파이프라인 금액 | ACV x SQL 수 | 월간 |
| **Win Rate (by Source)** | 소스별 최종 수주율 | Inbound > Outbound 평균 | 분기 |
| **Avg Deal Size (Inbound)** | 인바운드 기원 딜 평균 ACV | 벤치마크 대비 추적 | 분기 |
| **CAC (Inbound)** | 인바운드 채널 고객 획득 비용 | Outbound CAC 대비 <60% | 분기 |
| **Nurture-to-SQL Conversion** | Nurture 시퀀스 → SQL 전환율 | 5-10% | 분기 |

### 소스별 전환 추적 매트릭스

| Source Type | Lead → Contact Rate | Contact → Meeting Rate | Meeting → SQL Rate | SQL → CW Rate |
|-------------|-------------------|----------------------|-------------------|---------------|
| Demo Request | 90%+ | 60-70% | 70-80% | 추적 |
| Pricing / Contact Us | 80%+ | 40-50% | 60-70% | 추적 |
| Free Trial | 70%+ | 30-40% | 50-60% | 추적 |
| Referral | 85%+ | 60-70% | 70-80% | 추적 |
| Chat | 60%+ | 25-35% | 50-60% | 추적 |
| Event/Webinar | 40%+ | 15-25% | 40-50% | 추적 |
| Content Download | 20%+ | 10-15% | 30-40% | 추적 |

### 리뷰 주기

- **일간**: Speed to lead, 5-min response rate, P1/P2 미처리 건
- **주간**: Contact rate, conversion by source, routing accuracy, SDR 생산성
- **월간**: SQL count, pipeline $, conversion rates, source mix 분석
- **분기**: Win rate by source, CAC by channel, nurture 효과, 소스별 ROI

---

## 5. TOOL / AGENT

### 사용 도구

| 도구 | 용도 |
|------|------|
| CRM (Salesforce/HubSpot) | Account/Contact/Opportunity/Activity 관리, 라우팅 룰 |
| Marketing Automation (HubSpot/Marketo/Pardot) | 폼 처리, 자동 이메일, 리드 스코어링, Nurture 시퀀스 |
| Enrichment (Clearbit/ZoomInfo/Apollo) | 즉시 회사/연락처 정보 보강 |
| Chat (Intercom/Drift/HubSpot Chat) | 웹사이트 실시간 채팅, Agent 연동 |
| Calendar (Calendly/HubSpot Meetings) | 미팅 링크 자동 삽입, 라운드로빈 배정 |
| Dialer (Aircall/RingCentral) | 즉시 전화 응대, 녹음, 보이스메일 드롭 |
| Web Analytics (GA4/Mixpanel) | 웹 행동 추적, 페이지 방문 이력 |
| Event Platform (Zoom Webinar/Hopin) | 웨비나/이벤트 참석 데이터 |

### Agent 역할

| Agent 기능 | T2 (Co-pilot) | T3 (AI-led) |
|-----------|--------------|-------------|
| Lead Enrichment | Agent 자동 완료 → SDR 확인 | Agent 자동 완료 |
| ICP Scoring | Agent 자동 계산 → SDR 검토 | Agent 자동 계산 |
| 중복 확인 & 라우팅 | Agent 추천 → SDR 확인 후 배정 | Agent 자동 배정 |
| 초기 응대 이메일 | Agent 초안 → SDR 편집/발송 | Agent 자동 발송 |
| Chat 응대 | Agent 초안 → SDR 실시간 수정 발송 | Agent 자동 응대 (복잡한 건만 SDR 인계) |
| 전화 사전 준비 자료 | Agent 생성 → SDR 검토 후 통화 | Agent 생성 → SDR 검토 후 통화 |
| 응답/행동 분류 | Agent 분류 → SDR 확인 | Agent 자동 분류 |
| Nurture 시퀀스 배정 | Agent 추천 → SDR 승인 | Agent 자동 배정 |
| CRM Activity 기록 | Agent 자동 | Agent 자동 |
| Re-engagement 알림 | Agent 감지 → SDR 알림 | Agent 감지 → SDR 알림 |
| 성과 리포트 | Agent 주간 리포트 생성 | Agent 주간 리포트 생성 |

### Agent System Prompt 요약

```
You are the Inbound Lead Handler Agent for [Company Name].

Your job:
1. Capture and enrich every inbound lead within 60 seconds of submission
2. Calculate ICP Fit Score using firmographic, technographic, and needs-based data
3. Check for duplicate accounts/contacts in CRM before creating new records
4. Classify lead priority (P1-P4) based on source type and Fit Score
5. Route leads to the correct SDR/AE based on territory, workload, and specialty
6. Generate personalized auto-response emails referencing the lead's specific inquiry
7. For T3 accounts: handle full response cycle including chat, email, and nurture
8. For T2 accounts: draft responses for SDR review and provide call prep briefs
9. Monitor lead engagement signals and trigger re-engagement workflows
10. Log all activities to CRM with proper source attribution

Rules:
- NEVER let a P1/P2 lead go unresponded for more than 5 minutes during business hours
- Auto-send confirmation email within 60 seconds of any form submission
- If a lead matches an existing account with an active opportunity, alert the Account Owner immediately
- Always include a calendar booking link in demo request responses
- Never auto-send outbound messages to contacts who have opted out
- Escalate any lead mentioning a competitor's name or an active evaluation to SDR/AE immediately
- If lead is from a referral, always mention the referrer's name in the first response
- For chat: if the conversation requires pricing, contract, or legal discussion, hand off to human immediately
- Log First_Response_Time__c for every inbound lead without exception

Disqualification criteria (auto-DQ with thank you email):
- Personal email domain (gmail, yahoo, hotmail) for B2B — flag for review, do not hard reject
- Competitor email domain — log and alert Sales Ops
- Incomplete form data (no company name) — request additional info
- ICP Fit Score < 30 — auto-DQ, provide resource link

Tone: Responsive, helpful, professional. Acknowledge their specific request/question.
Match their language (Korean or English based on form submission language).
Show urgency without being pushy. Lead with value, not product pitch.

Data sources:
- CRM: Account, Contact, Opportunity, Activity objects
- Forms: Marketing automation form submissions
- Enrichment: [Clearbit/ZoomInfo/Apollo] API
- Web: [Analytics platform] for behavior tracking
- Chat: [Intercom/Drift] webhook events
- Events: [Zoom Webinar/Hopin] attendee data
- Intent: [Bombora/G2] API (if available)
```

---

## Appendix A: Response Templates

### A-1. Demo Request Auto-Response

**Subject**: `데모 요청 감사합니다`

```
[First Name]님, 안녕하세요.

[Our Company] 데모를 요청해주셔서 감사합니다.

[inquiry detail: 관심 영역 / 메시지 내용 요약]에 대해
맞춤으로 보여드릴 수 있도록 준비하겠습니다.

아래 링크로 편한 시간을 잡아주시면
담당 [SDR/AE Name]이 맞춤 데모를 진행해드리겠습니다:

[Calendar booking link]

미팅 전에 혹시 특별히 보고 싶은 기능이나
해결하고 싶은 과제가 있으시면 알려주세요.

곧 뵙겠습니다,
[SDR/AE Name]
[Title] | [Our Company]
[Phone] | [Email]
```

**Agent 개인화 포인트**:
- `[inquiry detail]` → 폼 메시지에서 관심 영역 자동 추출
- `[SDR/AE Name]` → 라우팅 결과에 따라 자동 삽입
- `[Calendar booking link]` → 배정된 담당자의 캘린더 링크

---

### A-2. Pricing / Contact Us Auto-Response

**Subject**: `문의 주셔서 감사합니다`

```
[First Name]님, 안녕하세요.

[Our Company]에 문의해주셔서 감사합니다.

말씀해주신 [inquiry summary]에 대해
담당자가 곧 연락드리겠습니다.

빠른 상담을 원하시면 아래 링크로 미팅을 잡아주세요:
[Calendar booking link]

또는 이 메일에 추가 정보를 알려주시면
더 맞춤화된 답변을 준비하겠습니다.

감사합니다,
[SDR Name]
[Title] | [Our Company]
```

---

### A-3. Content Download Follow-up

**Subject**: `[content title] 도움이 되셨기를`

```
[First Name]님, 안녕하세요.

[content title] 다운로드 감사합니다.

이 자료와 함께 보시면 좋은 콘텐츠를 추천드립니다:
• [Related content 1]: [link]
• [Related content 2]: [link]

혹시 [content topic]과 관련해서
[Their Company]에서 현재 겪고 계신 과제가 있으시다면,
10분 정도 대화로 도움을 드릴 수 있을 것 같습니다.

관심 있으시면 편한 시간을 알려주세요:
[Calendar link]

[SDR Name]
[Title] | [Our Company]
```

**Agent 개인화 포인트**:
- `[content title]` → 다운로드 자료명 자동 삽입
- `[Related content]` → 콘텐츠 유사도 기반 자동 추천 (최대 2개)
- `[content topic]` → 콘텐츠 카테고리에서 문제 가설 매핑

---

### A-4. Event/Webinar Follow-up

**Subject**: `[event name] 참석 감사합니다`

```
[First Name]님, 안녕하세요.

[event name]에 참석해주셔서 감사합니다.
[session title / topic] 세션이 도움이 되셨기를 바랍니다.

세션에서 다룬 [key topic]과 관련해서
추가 자료를 공유드립니다:
• 발표 자료: [link]
• 관련 케이스 스터디: [link]

[Their Company]에서 [key topic]에 대해
더 깊이 논의해보고 싶으시다면,
15분 정도 대화해보면 좋겠습니다.

[Calendar link]

[SDR Name]
[Title] | [Our Company]
```

---

### A-5. Referral Response

**Subject**: `[Referrer Name]님 소개로 연락드립니다`

```
[First Name]님, 안녕하세요.

[Referrer Name]님께서 [Their Company]를 소개해주셨습니다.

[Referrer Name]님과 함께 [referral context: 비슷한 과제를 해결 /
좋은 성과를 달성]한 경험이 있어서,
[Their Company]에서도 도움이 될 수 있을 것 같다고 연결해주셨습니다.

잠깐 통화로 상황을 들어보고
저희가 도움이 될 수 있는지 확인해보면 어떨까요?

편한 시간을 잡아주세요:
[Calendar link]

감사합니다,
[SDR/AE Name]
[Title] | [Our Company]
```

---

### A-6. Chat Follow-up (채팅 후)

**Subject**: `오늘 채팅 후속`

```
[First Name]님, 안녕하세요.

아까 채팅으로 문의해주신 내용 정리해드립니다.

질문하신 내용:
• [Question/Topic 1]
• [Question/Topic 2]

답변 요약:
• [Answer 1]
• [Answer 2]

[추가 확인 필요한 사항]에 대해서는
확인 후 [date]까지 다시 연락드리겠습니다.

더 자세한 논의가 필요하시면 미팅을 잡아주세요:
[Calendar link]

[SDR Name]
[Title] | [Our Company]
```

---

### A-7. Disqualification Thank You

**Subject**: `문의 감사합니다`

```
[First Name]님, 안녕하세요.

[Our Company]에 관심 가져주셔서 감사합니다.

현재 시점에서는 [Their Company]와 저희의 솔루션이
최적의 매칭이 아닐 수 있지만,
아래 자료가 도움이 되실 수 있습니다:

• [Resource 1]: [link]
• [Resource 2]: [link]

향후 상황이 변하시거나 추가 질문이 있으시면
언제든 이 메일로 연락 주세요.

감사합니다,
[Our Company] Team
```

---

## Appendix B: Inbound SDR 전화 스크립트

### B-1. Demo Request 후 Speed Call (5분 내)

```
[전화 연결 시]

"[First Name]님, 안녕하세요. [Our Company]의 [SDR Name]입니다.
방금 데모를 요청해주셔서 바로 전화드렸습니다.

먼저, 시간 괜찮으세요? 2-3분이면 됩니다.

[Yes]

감사합니다. [폼에서 언급한 내용]에 관심을 가져주셨는데,
현재 [problem area]에서 어떤 부분이 가장 과제로 느껴지시나요?

[고객 응답 듣기]

네, 이해했습니다. 저희가 [관련 역량]으로
[유사 기업]에서 [구체적 성과]를 달성한 사례가 있는데요,

맞춤 데모를 통해 [First Name]님 상황에 어떻게 적용할 수 있는지
보여드리면 좋겠습니다.

이번 주 [요일] [시간]에 30분 정도 시간 되시나요?
아니면 다른 편한 시간을 알려주시면 맞추겠습니다.

[미팅 확정 후]

좋습니다. 캘린더 초대 보내드리겠습니다.
미팅 전에 특별히 보고 싶은 기능이 있으시면 알려주세요.

감사합니다, [First Name]님. [날짜]에 뵙겠습니다."
```

### B-2. 부재 시 보이스메일 (30초)

```
"[First Name]님, 안녕하세요. [Our Company]의 [SDR Name]입니다.

방금 [데모 요청 / 문의]해주셔서 감사드리며 바로 전화드렸습니다.

확인 이메일 보내드렸고, 캘린더 링크도 포함되어 있습니다.
편한 시간에 잡아주시거나, 이 번호로 회신 주셔도 됩니다.

감사합니다."
```

---

## Appendix C: Inbound vs Outbound 비교

| 항목 | Play 01 (Outbound) | Play 06 (Inbound) |
|------|-------------------|-------------------|
| **시작점** | 우리가 먼저 접근 | 리드가 먼저 접근 |
| **핵심 목표** | 관심 창출 → 미팅 세팅 | 관심 놓치지 않기 → 즉시 전환 |
| **#1 성공 요인** | 개인화된 메시지 | Speed to lead (5분 SLA) |
| **시퀀스 구조** | 14일 멀티채널 캐던스 | 소스별 차별화된 응대 플로우 |
| **자동화 비중** | 메시지 생성 중심 | 리드 처리 + 라우팅 + 응대 전체 |
| **평균 전환율** | 3-5% (접촉 → 미팅) | 15-25% (리드 → SQL) |
| **SDR 역할** | 리서치 + 아웃리치 실행 | 즉시 응대 + 적격성 검증 |
| **Agent 핵심 역할** | 메시지 개인화, 리서치 | Enrichment, 라우팅, 즉시 응대 |
| **CAC** | 상대적 높음 | 상대적 낮음 |
| **CRM Source** | `Source_Channel__c` = "Outbound" | `Source_Channel__c` = "Inbound" |
