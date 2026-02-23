# B2B Sales Agent — TODO
**Updated**: 2026-02-14

---

## 데이터 없이 지금 할 수 있는 것

### Priority A: Agent Prompt 구체화 ✅ 완료
현재 각 Play에 "Agent System Prompt 요약"만 있음. 실제 작동 가능한 수준으로 상세화.

- [x] **Orchestration Agent 전체 프롬프트 작성** — 라우팅 룰, 에스컬레이션 조건, Agent 간 핸드오프 로직 → `agent/02_orchestration_agent.md` (990줄)
- [x] **Lead Generation Agent 전체 프롬프트 작성** — 데이터 수집 절차, ICP 스코어링 로직, 출력 포맷 → `agent/03_lead_generation_agent.md` (1,223줄)
- [x] **Qualification Agent 전체 프롬프트 작성** — MEDDICC 추출 로직, few-shot 예시, CRM 업데이트 포맷 → `agent/01_qualification_agent.md` (1,501줄)
- [x] **Deal Conversion Agent 전체 프롬프트 작성** — 제안서 초안 룰, 가격 가이드라인, 승인 플로우 → `agent/04_deal_conversion_agent.md` (1,416줄)
- [x] **Customer Success Agent 전체 프롬프트 작성** — Health Score 계산 로직, 알림 조건, expansion signal 룰 → `agent/05_customer_success_agent.md` (1,298줄)

### Priority B: 추가 Playbook 문서 ✅ 완료

- [x] **Play 06: Inbound Lead Handling** → `playbook/plays/play_06_inbound_lead_handling.md` (675줄)
- [x] **Play 07: Partner Channel Sales** → `playbook/plays/play_07_partner_channel_sales.md` (466줄)
- [x] **Competitive Battle Card 템플릿** → `playbook/06_competitive_battle_card.md` (992줄)
- [x] **Pricing & Discount Matrix** → `playbook/07_pricing_discount_matrix.md`
- [x] **Sales Onboarding Curriculum** → `playbook/08_sales_onboarding_curriculum.md`

### Priority C: 리서치 & 벤치마크 ✅ 완료

- [x] **산업별 영업 KPI 벤치마크 조사** → `research/01_kpi_benchmarks.md`
- [x] **AI Sales Agent 사례 조사** → `research/02_ai_sales_agent_cases.md`
- [x] **n8n vs Zapier vs LangChain 비교** → `research/03_tech_stack_comparison.md`

### 교차검증 (Cross-Validation) ✅ 완료
- [x] Phase 1: Agent 5개 + Battle Card + Play 06 검증 → 2 CRITICAL + 7 HIGH 수정 완료
- [x] Phase 2: Play 07 + Pricing Matrix + Onboarding + Research 검증 → 3 CRITICAL + 8 HIGH 발견, 수정 완료
  - CRITICAL: Discount SLA 통일 (4h/24h/48h), Auto-renewal 60일 통일, Payment Terms Net 45 추가
  - HIGH: CRM schema에 34개 신규 필드 추가 (Partner 17 + Pricing 17)
  - HIGH: Deal Conversion Agent — Anchoring 전략 + Strategic tier 명확화
- [x] Phase 3: 잔여 HIGH/MEDIUM 이슈 4건 수정 완료
  - HIGH-5: Orchestration Agent에 PARTNER_CHANNEL 이벤트 카테고리 추가 (7개 이벤트 + partner_ae_handoff)
  - HIGH-7: Deal Conversion Agent 번들 할인율 → Pricing Matrix 기준(8-20%)으로 정렬
  - HIGH-8: Pricing Matrix에 48개월+ 계약 할인 tier 추가 (+15%, VP Sales 승인 필수)
  - MEDIUM-4: Orchestration Agent ESCALATION 2 임계값 수정 (>20% → >10%, 4단계 승인 체계 정렬)

### Agent PoC 스캐폴딩 ✅ 완료 (3종)
- [x] **PoC #1: Post-Call CRM Updater** → `poc/workflows/post_call_crm_updater.json`
  - Webhook → Claude MEDDICC 추출 → DB 저장 → Slack 알림
  - 시스템 프롬프트: `poc/prompts/meddicc_extractor.md`
  - 테스트 데이터: 한국어 Discovery Call 트랜스크립트
- [x] **PoC #2: Weekly Ops Report** → `poc/workflows/weekly_ops_report.json`
  - Schedule (매주 월 08:00) → SQL 파이프라인 조회 → Claude 분석 → Slack 리포트
  - 시스템 프롬프트: `poc/prompts/weekly_ops_report.md`
  - 테스트 데이터: 18 deals, 6 stages, Win/Loss, Forecast
- [x] **PoC #3: Lead Enrichment & ICP Scoring** → `poc/workflows/lead_enrichment_scorer.json`
  - Webhook → Claude Enrichment + ICP 3축 스코어링 → DB 저장 → Slack (Hot/Warm만)
  - 시스템 프롬프트: `poc/prompts/lead_enrichment_scorer.md`
  - 테스트 데이터: CloudMetrics Inc. (Series B, 부분 데이터)
- [x] **공통 인프라**
  - Docker Compose (n8n + pgvector), `.env.example`, `poc/README.md`
  - DB 스키마 4 tables: playbook_chunks, meddicc_extractions, lead_enrichment_log, agent_executions
  - Setup/Test 스크립트 (setup.sh, test_webhook.sh, test_ops_report.sh, test_lead_enrich.sh)

### 최종 검증 (Final Validation) ✅ 완료
- [x] Phase 4: 전체 문서 최종 교차검증 → 2 HIGH + 2 MEDIUM 발견, 수정 완료
  - HIGH-1: Health Score 초기값 통일 → 80 (Deal Conversion Agent CRM Field Dependencies 100→80)
  - HIGH-2: 연간 가격 인상률 → 3-7% (Deal Conversion Agent 3-5% → 3-7%, default 5%)
  - MEDIUM-1: Deal Conversion Agent Payment Terms 확장 (Net 90, Upfront 추가 + 단계별 surcharge)
  - MEDIUM-1(수정): MEDDICC Guide에 CRM API 필드 매핑 테이블 추가 (11개 필드)
  - LOW-1(수정): Orchestration Agent 에스컬레이션 테이블에 응답 SLA vs 에스컬레이션 타임아웃 구분 명시
  - 12개 영역 PASS 확인 (할인 매트릭스, MEDDICC 공식, ICP 스코어링, CRM 필드, 이벤트 분류 등)

### RAG 벡터화 준비 ✅ 완료
- [x] **Playbook RAG 인제스트 스크립트** → `poc/scripts/ingest_playbook_rag.py`
  - 25개 문서 → 878 chunks (avg 727 chars, ~160K tokens)
  - Dry-run 모드 (DB 없이 청킹 검증 가능)
  - OpenAI text-embedding-3-small (1536 dim) 지원
  - `python3 poc/scripts/ingest_playbook_rag.py --dry-run` 으로 테스트

---

## 데이터 확보 후 할 것

- [ ] OpenAI API 키 → `poc/.env` 설정 → PoC #1 실행
- [ ] 파일럿 포트폴리오사 선정 → ICP 기준값 실데이터로 교체
- [ ] CRM 인스턴스 접근 → schema.md 기반 필드 실제 구축
- [ ] 콜 녹음/트랜스크립트 확보 → PoC 프롬프트 튜닝
- [x] ~~PoC #2 (Weekly Ops Report) + PoC #3 (Lead Enrichment) 빌드~~ — 스캐폴딩 완료
- [ ] Playbook 문서들 벡터 DB에 임베딩 → `python3 poc/scripts/ingest_playbook_rag.py` (스크립트 준비 완료, API 키 필요)
- [ ] Dashboard 5종 실제 구축

---

## 다음 추천 작업 순서

```
1. OpenAI API 키 → PoC 3종 실행 및 검증 (cd poc && ./scripts/setup.sh)
2. 파일럿 포트폴리오사 선정 (PE Ops VP)
3. CRM 인스턴스 접근 + 필드 매핑
4. Playbook RAG 벡터화 + Dashboard 구축
```
