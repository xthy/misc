# B2B Sales Agent — TODO
**Updated**: 2026-02-14

---

## 데이터 없이 지금 할 수 있는 것

### Priority A: Agent Prompt 구체화
현재 각 Play에 "Agent System Prompt 요약"만 있음. 실제 작동 가능한 수준으로 상세화.

- [ ] **Orchestration Agent 전체 프롬프트 작성** — 라우팅 룰, 에스컬레이션 조건, Agent 간 핸드오프 로직
- [ ] **Lead Generation Agent 전체 프롬프트 작성** — 데이터 수집 절차, ICP 스코어링 로직, 출력 포맷
- [ ] **Qualification Agent 전체 프롬프트 작성** — MEDDICC 추출 로직, few-shot 예시, CRM 업데이트 포맷
- [ ] **Deal Conversion Agent 전체 프롬프트 작성** — 제안서 초안 룰, 가격 가이드라인, 승인 플로우
- [ ] **Customer Success Agent 전체 프롬프트 작성** — Health Score 계산 로직, 알림 조건, expansion signal 룰

### Priority B: 추가 Playbook 문서
현재 5개 Play 외에 커버되지 않은 시나리오.

- [ ] **Play 06: Inbound Lead Handling** — 웹사이트/이벤트 리드 즉시 응대 프로세스
- [ ] **Play 07: Partner Channel Sales** — 파트너/리셀러 협업 영업 프로세스
- [ ] **Competitive Battle Card 템플릿** — 경쟁사별 강/약점, 포지셔닝, killer question
- [ ] **Pricing & Discount Matrix** — 할인 승인 체계, 번들 규칙, 가격 에스컬레이션
- [ ] **Sales Onboarding Curriculum** — 신규 Rep 30/60/90일 교육 과정

### Priority C: 리서치 & 벤치마크
Playbook의 목표 수치를 산업 데이터로 보강.

- [ ] **산업별 영업 KPI 벤치마크 조사** — Win rate, Sales cycle, ACV by industry/deal size
- [ ] **AI Sales Agent 사례 조사** — 실제 도입 기업 사례, 성과 데이터, 실패 사례
- [ ] **n8n vs Zapier vs LangChain 비교** — Agent PoC 기술스택 최종 선정을 위한 비교 분석

---

## 데이터 확보 후 할 것

- [ ] 파일럿 포트폴리오사 선정 → ICP 기준값 실데이터로 교체
- [ ] CRM 인스턴스 접근 → schema.md 기반 필드 실제 구축
- [ ] 콜 녹음/트랜스크립트 확보 → Agent PoC #1 (Post-Call Updater) 빌드
- [ ] Playbook 문서들 벡터 DB에 임베딩 (RAG)
- [ ] Dashboard 5종 실제 구축

---

## 내일 추천 작업 순서

```
1. Agent Prompt 구체화 (Priority A)
   → 코드 단계 진입 시 바로 쓸 수 있는 수준으로
   → Qualification Agent (MEDDICC 추출)부터 시작 추천 — 가장 구조화되어 있어서 작성하기 좋음

2. Competitive Battle Card 템플릿
   → 실제 경쟁사 없이도 구조와 예시를 만들어둘 수 있음

3. Play 06: Inbound Lead Handling
   → Outbound (Play 01)과 짝이 되는 Play, 파이프라인 생성의 나머지 절반
```
