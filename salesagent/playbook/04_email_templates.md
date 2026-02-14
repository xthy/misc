# Email Templates & Cadence Library

---

## 설계 원칙

1. **125 단어 이내**: 모바일 퍼스트. 스크롤 없이 읽을 수 있어야 함
2. **CTA 1개**: 한 이메일에 하나의 행동만 요청
3. **Subject line**: 소문자, 3-5단어, 낚시 없음
4. **개인화**: T1=100% 커스텀, T2=산업+역할 개인화, T3=머지필드 기반
5. **발송 시간**: 화-목, 오전 7:30-8:30 또는 오후 5:00-6:00 (수신자 현지 시간)
6. **회신 처리**: 모든 회신(부정적 포함)에 2시간 내 사람이 응답

---

## 1. Outbound Prospecting Cadence (14일)

### Email #1: Trigger-Based Cold Open (Day 1)

**목적**: 첫 접촉. 관심 유발, 판매하지 않음.

**Subject**: `[trigger event]에 관해`

```
[First Name]님, 안녕하세요.

[Their Company]가 최근 [trigger event: Series B 완료 / 영업팀 20명 채용 중 /
새 제품 라인 출시]하신 것 봤습니다.

이 단계의 [industry] 기업들이 자주 겪는 문제가
[specific problem: 파이프라인 가시성 부족 / 영업 프로세스 표준화 어려움 /
CRM 데이터 정확도 하락]인데요.

혹시 이 부분이 현재 과제로 느껴지시나요?

[Your Name]
[Title] | [Company]
```

**Agent 개인화 포인트**:
- `[trigger event]` → Agent가 뉴스/채용공고/Crunchbase에서 자동 추출
- `[specific problem]` → Trigger type에 따라 매핑된 문제 가설 선택

---

### Email #2: Value-Add Insight (Day 5)

**목적**: 가치 제공. 우리가 도메인 전문가임을 보여줌.

**Subject**: `[industry] 벤치마크 하나`

```
[First Name]님,

[industry]에서 최근 흥미로운 데이터를 봤습니다:

[Insight: "B2B SaaS 영업팀의 평균 win rate는 22%인데,
MEDDICC를 체계적으로 적용하는 팀은 38%입니다" /
"영업 rep이 CRM 업데이트에 주당 평균 4.5시간을 쓰고 있습니다"]

[Their Company] 규모에서 이 차이는
[quantified impact: 연간 $X의 매출 차이 / 영업 생산성 30% 차이]를 만듭니다.

관심 있으시면 10분 대화로 더 자세히 공유드리겠습니다.

[Your Name]
```

---

### Email #3: Social Proof (Day 9)

**목적**: 동종 업계 성공 사례로 신뢰 구축.

**Subject**: `[peer company] 사례`

```
[First Name]님,

[Their Industry]에서 [Peer Company 1]과 [Peer Company 2]도
비슷한 과제를 겪고 있었습니다.

[Our Solution]을 도입한 후:
• [Metric 1]: [구체적 수치, 예: 파이프라인 30% 증가]
• [Metric 2]: [구체적 수치, 예: 영업 사이클 20일 단축]

[Their Company]에서도 비슷한 결과가 가능할 것 같은데,
15분 정도 사례를 공유드려도 될까요?

[Your Name]
```

---

### Email #4: Breakup / Last Value (Day 12)

**목적**: 마지막 가치 제공. 존중하며 문 열어두기.

**Subject**: `마지막 연락`

```
[First Name]님,

몇 번 연락드렸는데 바쁘신 것 같습니다.
더 이상 메일 보내지 않겠습니다.

하나만 남기면, [resource: 가이드/벤치마크 리포트/체크리스트]가
[relevant benefit]에 도움 되실 수 있을 것 같습니다:
[link or attachment]

타이밍이 맞을 때 이 메일에 답해주시면 됩니다.

[Your Name]
```

---

### Email #5: Re-engagement (Day 14, 선택)

**조건**: 이전 이메일 오픈/클릭/LinkedIn 프로필 방문 등 engagement signal이 있을 때만

**Subject**: `짧은 질문`

```
[First Name]님,

[our resource/email] 확인해주신 것 같아 다시 연락드립니다.

[Problem area]에 대해 10분 대화,
해볼 만한 가치가 있으실까요?

[Your Name]
```

---

## 2. Meeting Confirmation & Follow-up

### 미팅 확정 후 확인 메일

**Subject**: `[Date] 미팅 확인`

```
[First Name]님, 미팅 잡아주셔서 감사합니다.

일시: [Date, Time]
방식: [Zoom link / 장소]
소요: 30분

미팅에서 다룰 내용:
1. [Their Company]의 현재 [area] 상황
2. [specific problem]에 대한 접근 방법
3. 맞으면 다음 단계 논의

혹시 사전에 궁금한 점이나 미팅 전 공유하실 내용이 있으시면 알려주세요.

[Your Name]
```

### Discovery Call 후 Follow-up

**Subject**: `오늘 미팅 정리`

```
[First Name]님, 오늘 시간 내주셔서 감사합니다.

대화 핵심을 정리하면:

현재 상황:
• [Current state summary]
• [Key pain point 1]
• [Key pain point 2]

기대 결과:
• [Desired outcome 1]
• [Desired outcome 2]

다음 단계:
• 저희: [our action, 예: demo 환경 준비] — [date]까지
• [Name]님: [their action, 예: 팀원 미팅 참석 확인] — [date]까지

다음 미팅: [Date, Time]

빠트린 부분이나 수정할 내용 있으시면 말씀해주세요.

[Your Name]
```

### Demo 후 Follow-up

**Subject**: `데모 후속 + [요청 자료]`

```
[First Name]님,

오늘 데모에서 보여드린 내용 중
[feature/capability]에 관심을 많이 보여주셨는데,
관련해서 [case study / ROI calculator / technical spec]를 첨부합니다.

말씀하신 [specific question/concern]에 대해서는
[answer or "내부 확인 후 [date]까지 답변드리겠습니다"].

다음 단계로 [PoC / 제안서 / executive briefing]을
[proposed date]에 진행하면 어떨까요?

[Your Name]
```

---

## 3. Proposal & Negotiation Stage

### Proposal 발송

**Subject**: `[Their Company] x [Our Company] 제안서`

```
[First Name]님,

논의 내용을 바탕으로 제안서를 준비했습니다.

핵심 요약:
• 범위: [scope summary]
• 투자: [price summary]
• 기대 ROI: [ROI summary]
• 시작 가능 시점: [timeline]

첨부 제안서를 검토하시고,
[date]에 30분 리뷰 미팅을 잡으면 어떨까요?

질문이나 수정이 필요한 부분은 미리 알려주시면
미팅 전에 반영하겠습니다.

[Your Name]
```

### Negotiation Follow-up (가격 반론 후)

**Subject**: `가격 관련 정리`

```
[First Name]님,

말씀하신 예산 고려사항을 반영해봤습니다.

[Option A]: [adjusted scope/price]
[Option B]: [alternative structure]

두 옵션 모두 [core value proposition]은 유지하면서
[their concern: 초기 투자 부담 / 연간 예산 제약]을 고려했습니다.

[Name]님 팀에서 어떤 구조가 더 맞으시는지
[date]에 10분만 통화로 정리하면 좋겠습니다.

[Your Name]
```

---

## 4. Customer Success Emails

### Onboarding Kickoff

**Subject**: `[Their Company] 온보딩 시작합니다`

```
[First Name]님, [Our Company] CS팀의 [CS Name]입니다.

[Their Company]를 모시게 되어 기쁩니다.
앞으로 제가 성공적인 도입과 활용을 함께 지원하겠습니다.

30/60/90일 온보딩 계획을 준비했습니다:
[Link to onboarding plan]

킥오프 미팅: [Date, Time, Link]

아젠다:
1. 팀 소개 및 역할 확인
2. 성공 기준 및 KPI 합의
3. 기술 셋업 일정
4. Q&A

미팅 전에 기대하시는 점이나 우선순위가 있으시면 알려주세요.

[CS Name]
```

### Health Check (Usage 하락 감지)

**Subject**: `[Their Company] 활용 현황 체크인`

```
[First Name]님,

최근 [our product] 사용 패턴을 보니
[specific observation: 지난 달 대비 로그인 빈도가 줄어든 것 같습니다 /
Feature X 사용이 중단된 것 같습니다].

혹시 팀에서 어려운 점이 있거나, 도움이 필요한 부분이 있으신가요?

15분 체크인 콜로 해결 방법을 함께 찾아보면 좋겠습니다:
[Calendar link]

아니면 이 메일에 상황을 알려주셔도 됩니다.

[CS Name]
```

### QBR 초대

**Subject**: `Q[X] 분기 리뷰`

```
[First Name]님,

Q[X] 분기 리뷰를 안내드립니다.

일시: [Date, Time]
소요: 45분

아젠다:
1. 지난 분기 성과 리뷰 (KPI 달성 현황)
2. 활용도 분석 & 최적화 제안
3. 다음 분기 목표 설정
4. Q&A

사전 준비 자료를 [date]까지 공유드리겠습니다.
[Name]님 쪽에서도 팀의 피드백이나 논의하고 싶은 안건이 있으시면
미리 알려주세요.

추가로 참석이 필요한 분이 계시면 말씀해주세요.

[CS Name]
```

### Renewal 시작 (D-90)

**Subject**: `갱신 관련 안내`

```
[First Name]님,

[Their Company]의 [Our Product] 계약이
[renewal date]에 갱신 시점을 맞이합니다.

지난 [contract period] 동안의 성과를 정리하면:
• [Achievement 1]
• [Achievement 2]
• [Achievement 3]

갱신 조건과 다음 기간의 계획에 대해
[date]에 미팅을 잡으면 좋겠습니다.

특별히 논의하고 싶은 사항이 있으시면 미리 알려주세요.

[CS Name] + [AE Name]
```

---

## 5. Agent 개인화 변수 가이드

### 자동 머지 필드

| 변수 | 소스 | 예시 |
|------|------|------|
| `[First Name]` | CRM Contact | "민수" |
| `[Their Company]` | CRM Account | "ABC Corp" |
| `[Industry]` | CRM Account.Industry | "FinTech" |
| `[Title]` | CRM Contact.Title | "VP of Sales" |
| `[trigger event]` | News/Enrichment API | "Series B $30M 완료" |
| `[peer company]` | Internal case study DB | "DEF Inc" |
| `[specific metric]` | Internal case study DB | "파이프라인 30% 증가" |
| `[specific problem]` | Trigger → Problem mapping | "영업 데이터 가시성 부족" |

### Trigger → Problem Mapping Table

| Trigger Type | Problem Hypothesis |
|-------------|-------------------|
| 자금 조달 | 빠른 성장에 프로세스가 못 따라가는 문제 |
| 영업팀 채용 | 온보딩 시간, 프로세스 표준화, 생산성 ramp-up |
| 새 제품 출시 | 새 시장 진입, ICP 재정의, 파이프라인 구축 |
| 경영진 교체 | 새 전략/체계 도입 니즈, quick win 필요 |
| M&A | 시스템 통합, 조직 재편, 프로세스 통일 |
| 경쟁사 뉴스 | 시장 경쟁 심화, 차별화 니즈 |
| 실적 발표 | 성장/하락에 따른 전략 변화 |
