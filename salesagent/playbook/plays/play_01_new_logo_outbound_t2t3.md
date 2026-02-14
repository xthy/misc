# Play 01: New Logo Outbound (T2/T3)
## 콜+이메일+LinkedIn 기반 신규 고객 발굴

---

## Play Overview

| 항목 | 내용 |
|------|------|
| **목표** | T2/T3 타겟 계정에서 신규 SQL(Sales Qualified Lead) 생성 |
| **대상** | ICP Fit Score ≥50, Tier T2 또는 T3 계정의 의사결정 관련 담당자 |
| **소유자** | SDR (실행), AE (미팅 이후 인수) |
| **자동화 수준** | T2: Co-pilot (AI 초안 → 사람 검토), T3: AI-led (자동 실행, 응답만 사람 처리) |
| **예상 소요** | 14일 시퀀스 / 계정당 10-13 터치포인트 |

---

## 1. INPUT

### Trigger (이 Play가 시작되는 조건)
- 신규 Target Account List 배포 (분기 시작)
- Account Score 변동으로 Tier 승격 (Watch → Nurture 이상)
- Intent 신호 감지 (채용공고, 자금 조달, 경쟁사 리뷰 등)
- 이벤트/웨비나 참석자 중 미접촉 계정 발견

### 대상 기준
- **Account**: ICP Fit Score ≥50, Tier = T2 or T3
- **Contact**: Title에 VP, Director, Head of, Manager 포함 (구매 영향력 보유)
- **Persona**: Technical Buyer, Business Buyer, Executive Sponsor 중 최소 2명 타겟

### 데이터 소스
| 데이터 | 소스 | Agent 자동화 |
|--------|------|-------------|
| 계정 기본 정보 | CRM (Account object) | 자동 조회 |
| 연락처 | CRM + Enrichment (Apollo/ZoomInfo) | 자동 보강 |
| 기술스택 | BuiltWith / Wappalyzer | 자동 수집 |
| 최근 뉴스 | Google News / PR wire | 자동 수집 |
| Intent 신호 | Bombora / G2 | 자동 수집 |
| 경쟁사 사용 현황 | Enrichment / 영업 인텔 | 반자동 |

---

## 2. PROCESS

### Step 1: Pre-Sequence Research (Day 0)

**SDR (T2) / Agent (T3) 수행**:

1. Account 배경 조사:
   - 최근 6개월 뉴스/보도자료
   - 최근 채용공고 (관련 직무)
   - 자금 조달 / M&A 이벤트
   - 경영진 변동

2. Contact 리서치:
   - LinkedIn 프로필 확인 (경력, 관심사, 최근 활동)
   - 공통 연결(mutual connection) 확인
   - 최근 발표/기고/인터뷰 확인

3. 개인화 포인트 1-2개 선정:
   - Trigger event (자금 조달, 채용, 제품 출시 등)
   - 공유 경험 (같은 컨퍼런스, mutual connection)
   - 산업 트렌드 연결

### Step 2: 14-Day Multi-Channel Cadence

| Day | Channel | Action | 메시지 테마 |
|-----|---------|--------|------------|
| **1** | Email | Cold Email #1 | **Trigger 기반 관심 유발.** 특정 이벤트/뉴스 언급 + 한 가지 문제 가설 제시. "이 문제가 관심사인지요?" |
| **2** | LinkedIn | 연결 요청 | 개인화된 노트 (300자 이내). 판매 언급 없음. |
| **3** | Phone | 콜 #1 | 패턴 인터럽트 오프닝. 30초 가치 가설. 15분 미팅 요청. 부재 시 30초 보이스메일. |
| **5** | Email | Email #2: 가치 제공 | **인사이트 공유.** 관련 케이스 스터디 수치, 산업 벤치마크, 또는 역발상 관점. 4-6문장. |
| **7** | LinkedIn | 콘텐츠 참여 | 그들의 포스트에 의미 있는 댓글 또는 관련 아티클 공유+태그. |
| **8** | Phone | 콜 #2 | Email #1 또는 #2 언급. 다른 각도 또는 새 정보. |
| **9** | Email | Email #3: 소셜 프루프 | **동종 업계 사례.** "[유사 기업]이 [문제]를 겪다가 [성과]를 달성했습니다." 구체적 수치 1개. |
| **10** | LinkedIn | DM | 짧고 대화체. "혹시 [리소스]가 도움 되실까 해서요. 부담 없이 공유드려요." |
| **11** | Phone | 콜 #3 | 직접적으로: "몇 번 연락드렸는데, [문제]가 현재 팀에서 실제로 다루고 계신 건가요?" |
| **12** | Email | Email #4: 마지막 가치 | **브레이크업.** "더 이상 방해 안 드리겠습니다. 한 가지 유용한 [리소스]만 남깁니다." |
| **14** | Email | Email #5 (선택) | **재참여** (이전 참여 신호 있을 때만). "[X] 확인하신 것 같은데, 10분 대화 가치가 있을까요?" |

### Step 3: Response Handling

| 응답 유형 | Action | SLA |
|----------|--------|-----|
| 긍정 응답 (미팅 수락) | 즉시 캘린더 링크 발송, AE에게 미팅 노트 전달 | 2시간 내 |
| 관심 표명 (질문/정보 요청) | 맞춤 자료 발송, 미팅 제안 | 4시간 내 |
| 타이밍 이슈 ("나중에") | Nurture 시퀀스로 이동, 재접촉 일정 설정 | 24시간 내 |
| 부정 응답 ("관심 없음") | 정중한 감사 + 옵트아웃 기록, 사유 CRM 기록 | 24시간 내 |
| 무응답 (시퀀스 완료) | 90일 재접촉 대기열로 이동 | 자동 |
| Objection 제기 | Objection Handling Guide 참조, 대응 후 미팅 재시도 | 4시간 내 |

### Step 4: Meeting Set → AE Handoff

미팅 세팅 시 SDR이 AE에게 전달하는 필수 정보:

1. **Account Context**: 산업, 규모, 기술스택, 최근 이벤트
2. **Contact Info**: 이름, 직급, LinkedIn, 선호 커뮤니케이션
3. **Pain Hypothesis**: SDR이 파악한 초기 Pain 또는 관심사
4. **Engagement History**: 어떤 메시지에 반응했는지, 대화 내용 요약
5. **Meeting Agenda**: 합의된 미팅 목적과 기대사항

---

## 3. OUTPUT

| 결과물 | 설명 | CRM 업데이트 |
|--------|------|-------------|
| SQL | 적격 미팅이 세팅된 기회 | Opportunity 생성 (S1 Discovery) |
| Nurture Lead | 관심은 있으나 타이밍이 아닌 리드 | Contact.Engagement_Level = "Warm", Follow-up Date 설정 |
| Disqualified | ICP 미달 또는 명확한 무관심 | Contact.Engagement_Level = "Cold", DQ Reason 기록 |
| Handoff Doc | AE에게 전달되는 미팅 브리핑 | Activity 기록 + Opp.Description에 요약 |

### SQL 기준 (Handoff Threshold)
미팅이 SQL로 인정되려면:
- [ ] ICP Fit Score ≥50인 계정
- [ ] 의사결정 관련자(Manager+)와의 미팅
- [ ] 구체적인 Pain 또는 관심사가 1개 이상 확인됨
- [ ] 미팅 일시 확정 (캘린더 초대 수락)

---

## 4. METRIC

### 활동 메트릭 (Leading)

| 메트릭 | 정의 | 목표 (SDR 1인 기준) |
|--------|------|---------------------|
| Daily Activities | 일일 총 터치 수 (콜+이메일+LinkedIn) | 60+ |
| Emails Sent / Day | 일일 발송 이메일 | 30-40 |
| Calls Made / Day | 일일 콜 수 | 20-30 |
| LinkedIn Touches / Day | 일일 LinkedIn 활동 | 5-10 |
| Connect Rate (Phone) | 콜 → 실제 통화 연결 비율 | 8-12% |
| Email Reply Rate | 이메일 → 응답 비율 | 5-10% |
| Positive Reply Rate | 응답 중 긍정 비율 | 30-50% |

### 결과 메트릭 (Lagging)

| 메트릭 | 정의 | 목표 |
|--------|------|------|
| Meetings Booked / Month | 월간 세팅 미팅 수 | 12-18 (SDR 1인) |
| SQL / Month | 미팅 중 적격 기회로 전환된 수 | 8-12 |
| Meeting Show Rate | 예약 미팅 → 실제 참석 비율 | >80% |
| SQL-to-Opp Conversion | SQL → S2 이상 진행 비율 | >60% |
| Pipeline Generated ($) | SDR이 기여한 파이프라인 금액 | ACV × SQL 수 |
| Sequence Completion Rate | 시작된 시퀀스 중 완료된 비율 | >85% |

### 리뷰 주기
- **일간**: Activity volume, connect rate
- **주간**: Meetings booked, reply rate, sequence stats
- **월간**: SQL count, pipeline $, conversion rates
- **분기**: SDR 생산성 벤치마크, 시퀀스 A/B 테스트 결과

---

## 5. TOOL / AGENT

### 사용 도구

| 도구 | 용도 |
|------|------|
| CRM (Salesforce/HubSpot) | Account/Contact/Activity 관리 |
| Sequencer (Apollo/Outreach/Salesloft) | 멀티채널 시퀀스 실행, 자동 스케줄링 |
| Dialer (Aircall/RingCentral) | 콜 실행, 녹음, 보이스메일 드롭 |
| Enrichment (Apollo/ZoomInfo/Clearbit) | 연락처, 기술스택, 기업 정보 보강 |
| LinkedIn Sales Navigator | 의사결정자 탐색, InMail, 소셜 활동 |
| Calendar (Calendly/HubSpot Meetings) | 미팅 링크 발송, 자동 리마인더 |

### Agent 역할

| Agent 기능 | T2 (Co-pilot) | T3 (AI-led) |
|-----------|--------------|-------------|
| Account Research | Agent 수집 → SDR 확인 | Agent 자동 완료 |
| 이메일 초안 작성 | Agent 초안 → SDR 편집/발송 | Agent 작성 + 자동 발송 |
| 개인화 포인트 추출 | Agent 제안 → SDR 선택 | Agent 자동 적용 |
| 콜 사전 준비 자료 | Agent 생성 → SDR 검토 | N/A (T3는 이메일 중심) |
| 응답 분류 | Agent 분류 → SDR 확인 | Agent 자동 분류 + 긍정만 SDR 전달 |
| CRM Activity 기록 | Agent 자동 | Agent 자동 |
| 시퀀스 성과 분석 | Agent 주간 리포트 생성 | Agent 주간 리포트 생성 |

### Agent System Prompt 요약

```
You are the Outbound SDR Agent for [Company Name].

Your job:
1. Research target accounts: collect recent news, funding events, job postings,
   tech stack, and competitive landscape
2. Identify 2-3 decision-maker contacts per account (VP/Director/Head of level)
3. Generate personalized outbound messages following the 14-day cadence template
4. Personalize each message with 1-2 specific trigger points
5. For T3 accounts: execute the sequence automatically
6. For T2 accounts: draft messages for SDR review
7. Classify responses (positive/negative/nurture/objection)
8. Log all activities to CRM with proper tagging

Rules:
- Never send more than 5 emails in a 14-day period to one contact
- Always include an unsubscribe option
- If a contact replies "not interested" or "unsubscribe", immediately stop the sequence
- Escalate any response that mentions a competitor or active evaluation to SDR/AE
- Email length must be under 125 words
- Subject lines must be lowercase, 3-5 words, no clickbait

Tone: Professional but conversational. No jargon. No exclamation marks.
Focus on the prospect's world, not our product.

Data sources:
- CRM: Account, Contact, Activity objects
- Enrichment: [Apollo/ZoomInfo] API
- News: Google News API / RSS feeds
- Intent: [Bombora/G2] API (if available)
```

---

## Appendix: Email Templates

### Email #1: Trigger-Based Open

```
Subject: [trigger event]에 관해

[First Name]님, 안녕하세요.

[Company Name]이 최근 [trigger event: 자금 조달, 채용, 제품 출시 등]하신 것 봤습니다.

비슷한 단계의 [산업] 기업들이 자주 겪는 문제가 [specific problem]인데요.
혹시 [Company Name]에서도 이 부분이 과제로 느껴지시는지 궁금합니다.

관심 있으시다면, 10분 정도 대화 가능하실까요?

[Sender Name]
```

### Email #3: Social Proof

```
Subject: [peer company] 사례

[First Name]님,

[산업]에서 [Peer Company 1]과 [Peer Company 2]도
비슷한 [problem] 문제를 겪고 있었습니다.

[Our Solution]을 도입한 후 [specific metric: "응답 시간 40% 단축",
"파이프라인 30% 증가" 등]을 달성했습니다.

동일한 접근이 [Their Company]에도 적용 가능할 것 같은데,
15분 정도 사례를 공유드려도 될까요?

[Sender Name]
```

### Email #4: Breakup

```
Subject: 마지막 연락

[First Name]님,

몇 번 연락드렸는데 바쁘신 것 같습니다.
더 이상 방해 안 드리겠습니다.

혹시 나중에 [problem area]에 대해 이야기 나누고 싶으시면
이 메일에 답 주시면 됩니다.

하나만 남기면, [useful resource/link]가
[relevant benefit]에 도움 될 수 있을 것 같습니다.

감사합니다,
[Sender Name]
```
