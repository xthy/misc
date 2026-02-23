# B2B Sales KPI Benchmarks by Industry & Deal Size
## 산업별/딜 규모별 B2B 영업 KPI 벤치마크 레퍼런스

---

> **용도**: 이 문서는 PE 포트폴리오 영업 프로세스 표준(Sales Process Canon)의 KPI 목표값이
> 산업 벤치마크 대비 현실적인지 검증하고, 포트폴리오사별 목표 설정의 기준점을 제공합니다.
>
> **데이터 기준**: 2023-2025년 공개된 주요 벤치마크 리포트 기반 종합.
> 실제 포트폴리오사 적용 시 해당 산업/규모/성숙도에 맞게 조정 필요.
>
> **표기 규칙**: 본문 한국어, Metric명/필드명 영어. 출처는 각 섹션 하단에 표기.

---

## 목차

1. [Win Rate 벤치마크](#1-win-rate-벤치마크)
2. [Sales Cycle Length 벤치마크](#2-sales-cycle-length-벤치마크)
3. [ACV (Average Contract Value) 벤치마크](#3-acv-average-contract-value-벤치마크)
4. [Pipeline & Activity 벤치마크](#4-pipeline--activity-벤치마크)
5. [Retention 벤치마크](#5-retention-벤치마크)
6. [Forecast Accuracy 벤치마크](#6-forecast-accuracy-벤치마크)
7. [AI/Automation Impact 벤치마크](#7-aiautomation-impact-벤치마크)
8. [프로젝트 KPI 타겟 검증](#8-프로젝트-kpi-타겟-검증)

---

## 1. Win Rate 벤치마크

### 1-1. 전체 평균

B2B SaaS의 전체 평균 Win Rate는 약 **20-25%** 수준이며, 이는 모든 파이프라인 기회 대비 Closed Won 비율입니다.
다만 Win Rate 계산 방식(전체 Opp 대비 vs Closed-only 대비)에 따라 크게 달라지므로, 아래에서는 **Closed Won / (Closed Won + Closed Lost)** 기준으로 통일합니다.

| 구분 | Bottom Quartile | Industry Average | Top Quartile | Best-in-Class |
|------|----------------|-----------------|-------------|--------------|
| **B2B SaaS 전체** | 15-18% | 21-25% | 30-35% | 40%+ |

### 1-2. By Industry (산업별)

산업별로 Win Rate는 제품 복잡도, 구매 프로세스 길이, 경쟁 강도에 따라 상당한 차이를 보입니다.

| Industry | Bottom Quartile | Average | Top Quartile | 특징 |
|----------|----------------|---------|-------------|------|
| **SaaS (Horizontal)** | 15% | 22% | 32% | 경쟁 치열, "Do Nothing" 비율 높음 |
| **FinTech** | 12% | 18% | 28% | 규제/컴플라이언스로 긴 의사결정, 높은 DQ율 |
| **HealthTech / MedTech** | 10% | 17% | 25% | 규제 장벽, 다단계 승인, 긴 사이클 |
| **Cybersecurity** | 18% | 25% | 35% | 높은 긴급성, 명확한 Pain, 예산 증가 추세 |
| **MarTech / AdTech** | 14% | 20% | 30% | 빠른 의사결정이나 높은 churn, 가격 민감 |
| **HRTech** | 16% | 23% | 33% | 비교적 표준화된 니즈, 예산 주기에 민감 |
| **Manufacturing / Industrial** | 20% | 28% | 38% | 낮은 경쟁, 높은 전환 비용, 관계 기반 |
| **Professional Services** | 22% | 30% | 42% | 관계 주도, 높은 맞춤화, 신뢰 기반 |
| **EdTech** | 12% | 19% | 27% | 예산 제약, 계절성, 긴 의사결정 |
| **Infrastructure / DevTools** | 16% | 24% | 34% | PoC 중심, 기술적 평가 비중 높음 |

### 1-3. By Deal Size (딜 규모별)

딜 규모가 커질수록 Win Rate가 하락하는 것은 보편적 패턴입니다. 관련 이해관계자가 많아지고, 의사결정이 복잡해지기 때문입니다.

| Deal Size | Bottom Quartile | Average | Top Quartile | 주요 패턴 |
|-----------|----------------|---------|-------------|----------|
| **SMB (<$25K ACV)** | 18% | 25% | 35% | 빠른 결정, 높은 volume, "Do Nothing" 다수 |
| **Mid-Market ($25-100K)** | 15% | 22% | 30% | 가장 경쟁적 구간, 복수 벤더 비교 빈번 |
| **Enterprise ($100-500K)** | 12% | 18% | 27% | 다단계 승인, MEDDICC 필수, 긴 사이클 |
| **Strategic ($500K+)** | 10% | 15% | 25% | 맞춤 솔루션, RFP 기반, 최소 6개월 사이클 |

### 1-4. By Source Channel (소스 채널별)

채널에 따른 Win Rate 차이는 "이미 Pain을 인식한" 바이어가 얼마나 포함되어 있는지에 따라 결정됩니다.

| Source Channel | Bottom Quartile | Average | Top Quartile | 비고 |
|----------------|----------------|---------|-------------|------|
| **Inbound (웹/마케팅)** | 20% | 28% | 40% | 바이어 주도, Pain 인식 높음 |
| **Outbound (SDR)** | 10% | 17% | 25% | Seller 주도, 초기 qualification 중요 |
| **CS-driven (Expansion)** | 35% | 50% | 65% | 기존 관계, 높은 신뢰, 낮은 리스크 |
| **Partner / Referral** | 25% | 35% | 50% | 추천 기반, 사전 신뢰 확보 |
| **Event / Conference** | 15% | 22% | 32% | 혼합 intent, follow-up 속도가 핵심 |

### 1-5. Historical Trends (2020-2025)

| 연도 | B2B SaaS 평균 Win Rate | 트렌드 요인 |
|------|----------------------|------------|
| 2020 | 23% | COVID 초기 불확실성, 디지털 전환 수요 폭증 |
| 2021 | 26% | 팬데믹 특수, 예산 확대, 높은 구매 의향 |
| 2022 | 22% | 금리 인상, 예산 긴축 시작, 벤더 통합 트렌드 |
| 2023 | 18-19% | "Do Nothing" 급증, 예산 승인 지연, 이해관계자 증가 |
| 2024 | 19-21% | 점진적 회복, AI 솔루션 수요 증가, 여전히 신중한 구매 |
| 2025 | 20-22% | AI 기반 판매 효율화, 바이어 교육 수준 상승, 경쟁 심화 |

> **핵심 트렌드**: 2021년 정점 이후 Win Rate 하락 추세. 2023년이 저점이었으며, 이후 서서히 회복 중이나 2021년 수준 회복은 어려움. B2B 구매 의사결정에 관여하는 평균 Stakeholder 수가 6.8명에서 11.2명으로 증가한 것이 구조적 원인. (Gartner, 2024)

**주요 출처**:
- Ebsta & Pavilion, B2B Sales Benchmarks Report (2023, 2024)
- Gartner, Sales Productivity & Performance Benchmarks (2024)
- Winning by Design, Revenue Architecture Benchmarks (2024)
- RAIN Group, Top Performance in Sales Prospecting (2024)
- HubSpot, Sales Trends Report (2024, 2025)
- Forrester, B2B Buying Study (2024)

---

## 2. Sales Cycle Length 벤치마크

### 2-1. By Deal Size (딜 규모별)

딜 규모와 Sales Cycle Length는 강한 양의 상관관계를 보입니다.

| Deal Size | Bottom Quartile (긴 쪽) | Average | Top Quartile (짧은 쪽) | 비고 |
|-----------|------------------------|---------|----------------------|------|
| **SMB (<$25K)** | 45-60일 | 30-40일 | 14-25일 | 1-2명 의사결정, 신용카드/PO 결제 |
| **Mid-Market ($25-100K)** | 90-120일 | 60-90일 | 40-55일 | 2-4명 의사결정, 조달 절차 존재 |
| **Enterprise ($100-500K)** | 150-210일 | 90-150일 | 60-90일 | 4-8명 의사결정, 법무/보안 리뷰 |
| **Strategic ($500K+)** | 270-365일 | 180-270일 | 120-180일 | RFP, 이사회 승인, 복수 PoC |

### 2-2. By Industry (산업별)

| Industry | Average Cycle (Mid-Market 기준) | 특징 |
|----------|-------------------------------|------|
| **SaaS (Horizontal)** | 60-80일 | 표준 절차, self-serve 경향 증가 |
| **FinTech** | 90-150일 | 규제 리뷰, 보안 감사, 컴플라이언스 체크 |
| **HealthTech** | 120-180일 | FDA/HIPAA, 다단계 승인, 임상/운영 양면 검토 |
| **Cybersecurity** | 45-75일 | 긴급성 높음, 단 CISO 승인 + 보안 팀 평가 |
| **MarTech** | 30-60일 | 빠른 의사결정, 단 통합 복잡도에 따라 편차 |
| **HRTech** | 60-90일 | 연간 예산 주기에 종속, Q4/Q1 집중 |
| **Manufacturing** | 90-150일 | 기술 검증, 현장 PoC, 조달 프로세스 |
| **Infrastructure / DevTools** | 45-90일 | Bottom-up 채택 → Top-down 구매 전환 시 길어짐 |

### 2-3. By Buyer Type (바이어 유형별)

| Buyer Type | Average Cycle | vs New Logo 비교 | 비고 |
|-----------|--------------|-----------------|------|
| **New Logo** | 75-100일 | Baseline | 신뢰 구축 + 전체 평가 프로세스 |
| **Expansion (Same Dept)** | 30-45일 | 50-60% 단축 | 기존 관계, 검증 완료 |
| **Cross-sell (New Dept)** | 50-70일 | 30-40% 단축 | 새 이해관계자이나 사내 레퍼런스 존재 |
| **Renewal** | 15-30일 | 70-80% 단축 | 프로세스화, 자동 갱신 비율 높음 |
| **Re-engage (Lost → Won)** | 45-60일 | 30-40% 단축 | 이전 평가 경험, 새 trigger 필요 |

### 2-4. Stage-by-Stage Conversion Benchmarks

각 스테이지 간 전환율과 평균 체류 기간 벤치마크입니다. Pipeline Progression (Stage 4)의 세부 지표로 활용됩니다.

| Stage Transition | Bottom Quartile | Average | Top Quartile | 평균 체류일 |
|-----------------|----------------|---------|-------------|-----------|
| **S1 Discovery → S2 Qualification** | 35% | 45-50% | 60% | 10-15일 |
| **S2 Qualification → S3 Solution** | 45% | 55-60% | 70% | 15-20일 |
| **S3 Solution → S4 Proposal** | 50% | 60-65% | 75% | 15-25일 |
| **S4 Proposal → S5 Negotiation** | 55% | 65-70% | 80% | 10-15일 |
| **S5 Negotiation → Closed Won** | 60% | 70-75% | 85% | 10-20일 |
| **Overall S1 → Closed Won** | 8% | 15-20% | 28% | 60-120일 |

> **핵심 인사이트**: S1 → S2 전환이 가장 낮은 구간이며, 이 단계에서의 적극적 disqualification이 전체 파이프라인 건강도를 결정합니다. 반면, S4 이후 전환율이 크게 떨어지는 조직은 qualification 프로세스에 문제가 있음을 시사합니다.

**주요 출처**:
- Ebsta & Pavilion, B2B Sales Benchmarks (2023, 2024)
- Gartner, B2B Buying Journey Report (2024)
- Salesforce, State of Sales Report (2024, 2025)
- InsightSquared, Sales Pipeline Benchmarks (2024)
- Forrester, B2B Sales Cycle Analysis (2024)

---

## 3. ACV (Average Contract Value) 벤치마크

### 3-1. By Company Stage (기업 성장 단계별)

| Company Stage | Median ACV | 25th Percentile | 75th Percentile | 비고 |
|--------------|-----------|----------------|----------------|------|
| **Seed / Pre-Series A** | $8-15K | $3-5K | $20-30K | 제품 검증 단계, 할인 공격적 |
| **Series A** | $15-25K | $8-12K | $35-50K | PMF 확인, 초기 반복 가능 모델 |
| **Series B** | $25-50K | $15-25K | $75-100K | Go-to-market 가속, 세그먼트 확대 |
| **Series C+** | $50-100K | $25-50K | $150-250K | Enterprise 진출, 플랫폼화 |
| **Growth / Pre-IPO** | $75-150K | $40-75K | $200-400K | 대형 딜 비중 증가, 멀티 프로덕트 |
| **PE-backed** | $50-120K | $25-60K | $200-350K | 효율성 중심, ACV 상향 압력 |
| **Public** | $80-200K | $40-100K | $300-500K+ | 엔터프라이즈 + SMB 혼합 |

### 3-2. By Industry Vertical (산업 버티컬별)

| Industry | Median ACV | ACV Range (IQR) | ACV 성장률 YoY | 비고 |
|----------|-----------|-----------------|---------------|------|
| **Horizontal SaaS** | $30-50K | $10-120K | 8-12% | 광범위 시장, 세그먼트별 편차 큼 |
| **FinTech (B2B)** | $60-120K | $25-300K | 10-15% | 규제 솔루션 프리미엄, 높은 전환 비용 |
| **HealthTech** | $50-100K | $20-250K | 12-18% | 컴플라이언스 가치, 임상 ROI 기반 pricing |
| **Cybersecurity** | $40-80K | $15-200K | 15-20% | 위협 증가 → 예산 증가, seat 기반 |
| **MarTech** | $20-45K | $5-100K | 5-8% | 가격 압박, commoditization 경향 |
| **HRTech** | $25-55K | $10-120K | 8-12% | 직원 수 기반 pricing, 규모에 비례 |
| **DevTools / Infra** | $35-75K | $10-200K | 12-18% | Usage-based 가격 증가 추세 |
| **Manufacturing SaaS** | $45-90K | $20-200K | 10-15% | 높은 구현 비용, 긴 계약 기간 |
| **EdTech (B2B)** | $15-35K | $5-80K | 5-10% | 예산 제약, 계절성, 가격 민감 |

### 3-3. Discount Rate Benchmarks (할인율 벤치마크)

| 구분 | Average Discount | Best Practice Range | 주의 구간 |
|------|-----------------|--------------------|-----------|
| **SMB (<$25K)** | 5-10% | 0-8% | >15%면 가격 체계 재검토 |
| **Mid-Market ($25-100K)** | 10-15% | 5-12% | >20%면 value selling 문제 |
| **Enterprise ($100-500K)** | 15-22% | 10-18% | >25%면 경쟁 포지셔닝 문제 |
| **Strategic ($500K+)** | 18-28% | 15-22% | >30%면 C-Level 승인 필수 |
| **Renewal** | 3-8% | 0-5% | >10%면 churn 위험 신호 |
| **Expansion** | 5-12% | 0-8% | 기존 가격 대비 일관성 유지 |

| 할인 관련 벤치마크 | Average | Top Quartile | 비고 |
|-------------------|---------|-------------|------|
| **Deals with Discount (비율)** | 55-65% | 40-45% | 모든 딜의 절반 이상에서 할인 발생 |
| **Overall Avg Discount** | 13-17% | 8-11% | List price 대비 실제 판매가 |
| **Discount → Win Rate 영향** | +5-8pp | - | 할인이 Win Rate를 크게 올리진 않음 |
| **"No Discount" 딜의 Win Rate** | 20-23% | - | 할인 딜(22-25%)과 큰 차이 없음 |

> **핵심 인사이트**: 할인이 Win Rate에 미치는 영향은 일반적인 영업 직관보다 훨씬 작습니다. 10% 할인 시 Win Rate는 평균 2-3pp 상승에 불과하며, 20% 이상 할인 시에도 5pp 이하의 효과만 있습니다. 이는 가격이 Loss Reason에서 AE가 인식하는 것(35%)보다 실제 바이어 피드백(15-20%)에서 훨씬 낮게 나타나는 것과 일치합니다.

**주요 출처**:
- KeyBanc Capital Markets, SaaS Survey (2024)
- OpenView Partners, SaaS Benchmarks Report (2024)
- Bessemer Venture Partners, Cloud Index (2024)
- Paddle / ProfitWell, SaaS Pricing Benchmarks (2024)
- Bain & Company, PE Value Creation in B2B Software (2024)

---

## 4. Pipeline & Activity 벤치마크

### 4-1. Pipeline Coverage Ratios (파이프라인 커버리지)

Pipeline Coverage = 파이프라인 총액 / 분기 목표 매출

| 구분 | Minimum | Recommended | Aggressive | 비고 |
|------|---------|-------------|-----------|------|
| **전체 평균 (B2B SaaS)** | 2.5x | 3.0-4.0x | 5.0x+ | Win Rate에 따라 조정 |
| **Win Rate 15-20%인 조직** | 4.0x | 5.0-6.0x | 7.0x+ | 낮은 전환 → 더 큰 pipe 필요 |
| **Win Rate 25-30%인 조직** | 3.0x | 3.5-4.5x | 5.0x | 적정 전환 → 표준 커버리지 |
| **Win Rate 35%+인 조직** | 2.5x | 3.0-3.5x | 4.0x | 높은 전환 → 효율적 파이프라인 |
| **Expansion pipeline** | 2.0x | 2.5-3.0x | 3.5x | 높은 Win Rate 반영 |

**Coverage 계산 공식 (가이드)**:
```
Required Coverage = 1 / Win Rate + Buffer
예: Win Rate 25% → 1/0.25 = 4.0x minimum
    Buffer 20% 추가 → 4.8x recommended
```

### 4-2. SDR Activity Benchmarks (SDR 활동 벤치마크)

#### 일일 활동량

| Activity | Bottom Quartile | Average | Top Quartile | Elite |
|----------|----------------|---------|-------------|-------|
| **Calls / Day** | 15-20 | 25-35 | 40-50 | 60+ |
| **Emails / Day** | 15-20 | 25-35 | 40-50 | 60+ |
| **LinkedIn Touches / Day** | 2-3 | 5-8 | 10-15 | 20+ |
| **Total Activities / Day** | 35-45 | 55-70 | 80-100 | 120+ |
| **Meaningful Conversations / Day** | 2-3 | 4-6 | 7-10 | 12+ |

#### 월간 결과 지표

| Metric | Bottom Quartile | Average | Top Quartile | Elite |
|--------|----------------|---------|-------------|-------|
| **Meetings Booked / Month** | 5-8 | 10-15 | 16-22 | 25+ |
| **SQLs / Month** | 3-5 | 6-10 | 11-16 | 18+ |
| **Pipeline Generated ($) / Month** | $50-100K | $150-300K | $350-600K | $700K+ |
| **Sequences Started / Month** | 50-80 | 100-150 | 160-220 | 250+ |

### 4-3. Email Performance Benchmarks (이메일 성과)

| Metric | Bottom Quartile | Average | Top Quartile | 비고 |
|--------|----------------|---------|-------------|------|
| **Open Rate (Cold)** | 20-25% | 30-40% | 45-55% | Subject line + sender reputation |
| **Reply Rate (Cold)** | 1-2% | 3-5% | 7-12% | Personalization이 핵심 변수 |
| **Positive Reply Rate** | 15-20% | 30-40% | 50-60% | Reply 중 긍정 비율 |
| **Bounce Rate** | 5-8% | 2-4% | <1% | 데이터 품질 지표 |
| **Unsubscribe Rate** | 2-5% | 0.5-1.5% | <0.3% | 타겟팅 정확도 반영 |
| **Click Rate** | 1-2% | 3-5% | 7-10% | CTA 명확성 + 콘텐츠 관련성 |

#### Cadence 차수별 Reply Rate 변화

| Touch # | Average Reply Rate | Cumulative Response | 비고 |
|---------|-------------------|--------------------|----|
| Email 1 | 5-8% | 5-8% | Trigger-based가 가장 높음 |
| Email 2 | 3-5% | 8-12% | Value/Insight 제공 |
| Email 3 | 2-4% | 10-15% | Social proof 효과적 |
| Email 4 | 1-3% | 11-17% | Breakup email 의외로 높은 반응 |
| Email 5+ | 1-2% | 12-18% | 수확 체감, ROI 하락 |

### 4-4. Phone Connect Rates (전화 연결율)

| Metric | Bottom Quartile | Average | Top Quartile | 비고 |
|--------|----------------|---------|-------------|------|
| **Connect Rate (전체)** | 3-5% | 5-8% | 10-15% | 콜 시도 대비 실제 통화 |
| **Connect Rate (Mobile)** | 8-12% | 15-20% | 25-30% | 직통 번호 확보가 핵심 |
| **Connect Rate (Switchboard)** | 1-3% | 3-5% | 7-10% | 게이트키퍼 돌파율 포함 |
| **Voicemail → Callback** | 1-2% | 2-4% | 5-7% | 30초 이내 메시지가 효과적 |
| **Best Connect Times** | - | 화/수/목 오전 8-10, 오후 4-6 | - | 월요일 오전, 금요일 오후 최저 |

### 4-5. Meeting & SQL Conversion (미팅/SQL 전환)

| Metric | Bottom Quartile | Average | Top Quartile | 비고 |
|--------|----------------|---------|-------------|------|
| **Meeting Show Rate** | 65-70% | 75-80% | 85-90% | 리마인더 + 아젠다 공유 효과 |
| **Meeting → SQL Rate** | 40-50% | 55-65% | 70-80% | ICP fit 정확도 반영 |
| **SQL → S2 Conversion** | 45-50% | 55-65% | 70-80% | SDR-AE handoff 품질 반영 |
| **Inbound Lead → Meeting** | 15-20% | 25-35% | 40-50% | Response time이 핵심 변수 |
| **Outbound Contact → Meeting** | 1-2% | 2-4% | 5-8% | 멀티채널 cadence 효과 |

### 4-6. Response Time Benchmarks (응답 시간)

| Metric | Current Average | Best Practice | Impact |
|--------|----------------|--------------|--------|
| **Inbound Lead Response** | 42시간 | <5분 | 5분 내 응대 시 전환율 21x 증가 |
| **Web Chat Response** | 2분 | <30초 | 30초 초과 시 50% 이탈 |
| **RFP Response** | 5-7일 | 2-3일 | 빠른 응답이 shortlist 가능성 2x |
| **Proposal Delivery** | 7-10일 | 3-5일 | 지연 시 "Do Nothing" 확률 증가 |

> **핵심 인사이트**: Inbound lead response time이 5분 내 vs 30분 이후일 때 SQL 전환율 차이는 **21배**에 달합니다 (InsideSales.com / XANT 연구). 이는 가장 ROI가 높은 프로세스 개선 포인트 중 하나입니다.

**주요 출처**:
- Bridge Group, SDR Metrics & Compensation Report (2024)
- TOPO/Gartner, SDR Benchmark Report (2024)
- SalesLoft, Cadence Benchmark Report (2024)
- Outreach, Sales Engagement Benchmarks (2024)
- XANT/InsideSales, Lead Response Study (2023)
- HubSpot, Sales Activity Benchmarks (2024)

---

## 5. Retention 벤치마크

### 5-1. Gross Retention Rate (GRR) by Industry

GRR = (기초 MRR - Churn - Contraction) / 기초 MRR

| Industry | Bottom Quartile | Average | Top Quartile | Best-in-Class |
|----------|----------------|---------|-------------|--------------|
| **SaaS (SMB 중심)** | 75-80% | 82-87% | 90-93% | 95%+ |
| **SaaS (Mid-Market)** | 82-85% | 88-92% | 93-96% | 97%+ |
| **SaaS (Enterprise)** | 88-92% | 93-96% | 97-99% | 99%+ |
| **FinTech** | 85-88% | 90-93% | 95-97% | 98%+ |
| **HealthTech** | 87-90% | 92-95% | 96-98% | 99%+ |
| **Cybersecurity** | 83-86% | 88-92% | 93-96% | 97%+ |
| **HRTech** | 80-84% | 86-90% | 92-95% | 96%+ |
| **MarTech** | 75-80% | 82-87% | 90-93% | 95%+ |
| **Infrastructure** | 88-92% | 93-96% | 97-99% | 99%+ |
| **Manufacturing SaaS** | 85-90% | 91-94% | 95-97% | 98%+ |

### 5-2. Net Revenue Retention (NRR) by Company Type

NRR = (기초 MRR + Expansion - Churn - Contraction) / 기초 MRR

| Company Type | Bottom Quartile | Median | Top Quartile | Best-in-Class | 비고 |
|-------------|----------------|--------|-------------|--------------|------|
| **SMB SaaS (<$10K ACV)** | 85-90% | 95-100% | 105-110% | 115%+ | 높은 churn, 제한적 expansion |
| **Mid-Market SaaS ($10-50K)** | 95-100% | 105-110% | 115-120% | 125%+ | churn 낮고 expansion 여지 |
| **Enterprise SaaS ($50K+)** | 105-110% | 115-125% | 130-140% | 150%+ | 낮은 churn + 높은 expansion |
| **Usage-based SaaS** | 100-105% | 110-120% | 125-140% | 150%+ | 사용량 증가 시 자연 expansion |
| **Seat-based SaaS** | 95-100% | 105-112% | 115-125% | 130%+ | 직원 수 증가에 연동 |
| **PE-backed SaaS** | 95-100% | 105-110% | 115-125% | 130%+ | 효율성 중심, NRR 핵심 KPI |
| **Public SaaS (Best)** | - | - | - | 130-160% | Snowflake, Datadog, Twilio 등 |

### 5-3. Logo Retention (고객 수 유지율)

| Segment | Bottom Quartile | Average | Top Quartile | 비고 |
|---------|----------------|---------|-------------|------|
| **SMB** | 70-75% | 78-85% | 88-92% | 높은 자연 churn (폐업, 전환) |
| **Mid-Market** | 82-85% | 88-92% | 93-96% | 관계 기반 유지 가능 |
| **Enterprise** | 90-93% | 94-97% | 98-99% | 높은 전환 비용, 강한 lock-in |
| **전체 B2B SaaS 평균** | 78-82% | 85-90% | 92-95% | 세그먼트 믹스에 따라 편차 |

### 5-4. Churn & Expansion Detail

| Metric | Bottom Quartile | Average | Top Quartile | 비고 |
|--------|----------------|---------|-------------|------|
| **Monthly Churn Rate (MRR)** | 3-5% | 1.5-2.5% | 0.5-1.0% | <1%가 건강한 수준 |
| **Annual Churn Rate (MRR)** | 30-45% | 15-25% | 5-10% | 10% 이하가 PE 투자 기준 |
| **Gross Expansion Rate** | 10-15% | 20-30% | 35-50% | NRR의 핵심 드라이버 |
| **Expansion Revenue %** | 15-20% | 25-35% | 40-55% | 전체 신규 매출 중 expansion 비중 |
| **Time to First Expansion** | 18-24개월 | 12-15개월 | 6-9개월 | 짧을수록 NRR 개선 |
| **Expansion Win Rate** | 35-40% | 50-55% | 65-75% | New logo 대비 2-3x 높음 |

### 5-5. Churn Reason Distribution (해지 사유 분포)

| Reason | Average % | 비고 |
|--------|----------|------|
| **Lack of Adoption / Low Usage** | 25-30% | 가장 큰 원인 — 온보딩/CS 강화로 방지 |
| **Budget Cuts / Cost** | 18-22% | 매크로 경제 영향, 가치 증명 미흡 시 |
| **Switched to Competitor** | 12-18% | 제품/가격 경쟁력 이슈 |
| **Champion Left** | 10-15% | Multi-threading의 중요성 |
| **Merged / Acquired / Closed** | 8-12% | 통제 불가, 자연 churn |
| **Product Issues / Missing Features** | 8-12% | Product-market fit 이슈 |
| **Poor Support / Service** | 5-8% | 운영 품질 이슈 |
| **Moved to In-house Solution** | 3-6% | "Build vs Buy" 결정 역전 |

**주요 출처**:
- KeyBanc Capital Markets, Annual SaaS Survey (2024)
- OpenView Partners, SaaS Benchmarks (2024)
- Gainsight, Customer Success Benchmarks (2024)
- Totango, Customer Success Industry Benchmarks (2024)
- ChurnZero, SaaS Churn Benchmark Report (2024)
- Bessemer Venture Partners, State of the Cloud (2024)
- Pacific Crest / PwC, SaaS Survey (2024)

---

## 6. Forecast Accuracy 벤치마크

### 6-1. Industry Averages

Forecast Accuracy = 1 - |예측 매출 - 실제 매출| / 실제 매출

| 구분 | Bottom Quartile | Average | Top Quartile | Best-in-Class |
|------|----------------|---------|-------------|--------------|
| **B2B SaaS 전체** | 60-70% | 72-78% | 82-88% | 92%+ |
| **SMB 중심** | 65-72% | 75-80% | 85-90% | 93%+ |
| **Enterprise 중심** | 55-65% | 68-75% | 78-85% | 88%+ |
| **PE-backed** | 68-75% | 78-83% | 85-90% | 93%+ |

### 6-2. By Forecast Method

| Method | Average Accuracy | 비고 |
|--------|-----------------|------|
| **Rep Gut Feel** | 55-65% | 가장 흔하지만 가장 부정확 |
| **Weighted Pipeline** | 65-72% | Stage 확률 × 금액. 기본적 방법 |
| **MEDDICC Score-based** | 72-80% | 딜 적격도 기반 가중. 더 정확 |
| **AI/ML Predictive** | 78-88% | 활동 데이터 + 패턴 분석. 최신 트렌드 |
| **Multi-method Blend** | 80-88% | 2-3가지 방법 조합. Best practice |
| **Historical Conversion** | 70-78% | 과거 스테이지 전환율 기반 |

### 6-3. Forecast Maturity Model

| Level | 특징 | Accuracy Range | 비율 (기업 분포) |
|-------|------|---------------|-----------------|
| **Level 1: Ad-hoc** | Rep 감에 의존, 스프레드시트 | 50-60% | ~20% |
| **Level 2: Basic** | CRM 기반 가중 파이프라인 | 65-72% | ~35% |
| **Level 3: Structured** | MEDDICC/MEDDPICC + 주간 리뷰 | 75-82% | ~25% |
| **Level 4: Data-driven** | AI 보강, 활동 데이터 반영 | 82-88% | ~15% |
| **Level 5: Predictive** | ML 모델 + 다변량 분석, 실시간 | 88-95% | ~5% |

### 6-4. Forecast Accuracy 관련 패턴

| 패턴 | 수치 | 비고 |
|------|------|------|
| **Pipeline을 Over-forecast하는 비율** | 65-70% | 대부분 낙관적 예측 |
| **"Commit" 딜의 실제 Close율** | 60-70% | Commit ≠ 확정 |
| **"Best Case" 딜의 실제 Close율** | 25-35% | 큰 불확실성 |
| **Quarter 내 Pipeline 유입 → 같은 Q 내 Close** | 15-25% | "Pipeline in Quarter" |
| **Forecast miss의 가장 큰 원인** | 딜 슬립(다음 분기 연기) | 40-50%가 slip |

> **핵심 인사이트**: Forecast Accuracy <15% 오차 목표(우리 프로젝트 타겟)는 Top Quartile 수준이며, Level 3+ Forecast maturity가 전제 조건입니다. MEDDICC 기반 qualification + AI 보강 예측 모델의 조합이 이 목표 달성의 핵심 경로입니다.

**주요 출처**:
- Gartner, Sales Forecasting Best Practices (2024)
- Clari, Revenue Confidence Benchmark (2024)
- InsightSquared, Forecast Accuracy Report (2024)
- Forrester, AI in Sales Forecasting (2024)
- SalesHood, Forecasting Benchmark Study (2024)

---

## 7. AI/Automation Impact 벤치마크

### 7-1. Sales AI Adoption & Productivity Gains

| AI Use Case | Adoption Rate (2025) | Productivity Gain | 비고 |
|------------|---------------------|-------------------|------|
| **CRM Data Entry Automation** | 45-55% | 25-40% 시간 절감 | 가장 높은 ROI, 가장 빠른 도입 |
| **AI Email Drafting** | 40-50% | 30-50% 시간 절감 | 개인화 품질 유지가 관건 |
| **Call Summarization** | 35-45% | 50-70% 시간 절감 | Gong/Chorus 등으로 보편화 |
| **Lead Scoring (AI)** | 30-40% | 15-25% SQL 전환 개선 | 데이터 품질에 크게 의존 |
| **Forecasting (AI)** | 20-30% | 10-20pp Accuracy 개선 | 도입 초기, 빠르게 성장 |
| **Meeting Scheduling AI** | 35-45% | 20-30% 시간 절감 | 자동 캘린더 조율 |
| **Conversation Intelligence** | 30-40% | 10-15pp Win Rate 개선 | Coaching + Deal risk 감지 |
| **Proposal Generation** | 15-25% | 40-60% 시간 절감 | 초안 생성 → 사람 편집 |

### 7-2. Time Savings from CRM Automation

| Task | 자동화 전 (주당) | 자동화 후 (주당) | 절감 | 비고 |
|------|-----------------|-----------------|------|------|
| **CRM Data Entry** | 4-6시간 | 1-2시간 | 3-4시간 | 가장 큰 절감 영역 |
| **Email Drafting** | 3-5시간 | 1-2시간 | 2-3시간 | AI 초안 → 편집 모델 |
| **Meeting Prep** | 2-3시간 | 0.5-1시간 | 1.5-2시간 | 자동 리서치 + 브리핑 |
| **Call Notes & Follow-up** | 2-3시간 | 0.5-1시간 | 1.5-2시간 | 자동 요약 + 다음 단계 |
| **Reporting & Admin** | 2-3시간 | 0.5-1시간 | 1.5-2시간 | 자동 대시보드/리포트 |
| **Pipeline Review Prep** | 1-2시간 | 0.5시간 | 0.5-1.5시간 | 자동 deal summary |
| **Lead Research** | 2-3시간 | 0.5-1시간 | 1.5-2시간 | 자동 enrichment |
| **총계** | **16-25시간** | **4.5-8.5시간** | **11-17시간** | **주당 10+ 시간 절감 가능** |

### 7-3. Impact on Pipeline Velocity

Sales Velocity = (Opportunities x Win Rate x ACV) / Sales Cycle

| AI 도입 영역 | Pipeline Velocity 영향 | 비고 |
|-------------|----------------------|------|
| **AI Lead Scoring** | +15-25% (Opp 품질 향상) | 더 적격한 기회에 집중 |
| **AI Email Personalization** | +10-20% (Reply rate 향상) | 더 많은 기회 생성 |
| **Conversation Intelligence** | +10-15% (Win Rate 향상) | 코칭 + 리스크 조기 감지 |
| **AI Forecasting** | +5-10% (리소스 배분 최적화) | 고확률 딜에 집중 |
| **CRM Automation** | +15-25% (Cycle 단축) | Admin 시간 → Selling 시간 전환 |
| **종합 효과** | **+30-50% Pipeline Velocity** | 2-3개 이상 AI 도구 조합 시 |

### 7-4. AI 도입 시 주의 사항 & 실패 패턴

| 실패 패턴 | 발생 빈도 | 대응 방안 |
|----------|----------|----------|
| **데이터 품질 미흡** | 매우 높음 | AI 도입 전 CRM hygiene 프로젝트 선행 |
| **Rep 저항** | 높음 | "시간 절감" 도구부터 시작, 대체가 아닌 보조 |
| **과도한 자동화** | 보통 | T1은 Human-led 유지, T3부터 자동화 |
| **Hallucination in comms** | 보통 | 자동 발송 전 Human review 필수 (T2) |
| **ROI 측정 미흡** | 높음 | Before/After 메트릭 비교 체계 구축 |
| **Vendor lock-in** | 보통 | 표준 API 활용, 멀티 LLM 전략 |

**주요 출처**:
- McKinsey, The State of AI in Sales (2024)
- BCG, How AI Agents Will Transform B2B Sales (2024)
- Salesforce, State of Sales Report (2024, 2025)
- Gartner, AI in Sales Technology Survey (2024)
- HubSpot, AI in Sales Trends Report (2025)
- Forrester, AI-Powered Sales Engagement (2024)

---

## 8. 프로젝트 KPI 타겟 검증

이 섹션에서는 우리 프로젝트(Sales Process Canon + 5개 Play)에 설정된 KPI 목표값을 위의 산업 벤치마크와 대조하여 **현실성**을 검증합니다.

### 8-1. Sales Process Canon KPI 검증

#### Stage 3: Pipeline Generation

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 | 조정 제안 |
|----------|--------|-------------|------|----------|
| Pipeline Coverage | 3x-5x | Avg: 3-4x | **적절** | Win Rate에 따라 동적 조정 권장 |
| Activity Volume (SDR) | 60+/day | Avg: 55-70 | **적절** | Top Quartile 수준, 달성 가능 |
| Meeting Conversion (Outbound) | 3-5% | Avg: 2-4% | **약간 도전적** | Top Quartile 수준이나 달성 가능 |
| Response Time (Inbound) | <5분 | Best: <5분 | **도전적이나 적절** | AI 자동 응답으로 달성 가능 |
| CS Expansion Rate | >10%/quarter | Avg: 5-8% | **도전적** | Top Quartile, 점진적 달성 권장 |

#### Stage 4: Pipeline Progression

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 | 조정 제안 |
|----------|--------|-------------|------|----------|
| Win Rate | 산업 평균 +5pp | Avg: 21-25% | **적절** | 목표 26-30%. 도전적이나 합리적 |
| Stage Conversion (S1→S2) | 50% | Avg: 45-50% | **적절** | 평균~상위 수준 |
| Stage Conversion (S2→S3) | 60% | Avg: 55-60% | **적절** | 평균~상위 수준 |
| Stage Conversion (S3→S4) | 65% | Avg: 60-65% | **적절** | 평균~상위 수준 |
| Stage Conversion (S4→S5) | 70% | Avg: 65-70% | **적절** | 평균~상위 수준 |
| Stage Conversion (S5→CW) | 75% | Avg: 70-75% | **적절** | 평균~상위 수준 |
| MEDDICC Compliance (S3+) | >80% | Avg: 50-60% | **매우 도전적** | 단, Agent 자동화로 달성 가능성 높음 |
| Stalled Deal Rate | <15% | Avg: 20-30% | **도전적** | Agent 자동 알림으로 개선 가능 |

#### Stage 5: Close & Onboard

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 | 조정 제안 |
|----------|--------|-------------|------|----------|
| Close Rate (S4→CW) | >50% | Avg: 45-55% (S4→CW 복합) | **적절** | S4→S5→CW 복합 기준으로 합리적 |
| Avg Discount | <15% | Avg: 13-17% | **적절** | 평균 수준, Value selling 강화 시 달성 |
| Time to Close (S4→CW) | <30일 | Avg: 20-35일 | **적절** | 딜 사이즈별 분리 운영 권장 |
| Time to First Value | <30일 | Avg: 30-60일 | **도전적** | 온보딩 자동화 + 표준화 필요 |

#### Stage 6: Retention & Growth

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 | 조정 제안 |
|----------|--------|-------------|------|----------|
| Gross Retention Rate | >90% | Avg: 88-92% (Mid-Market) | **적절** | 세그먼트에 따라 조정 필요 |
| Net Revenue Retention | >110% | Avg: 105-115% | **적절** | Mid-Market 기준 합리적 목표 |
| Expansion Rate YoY | >20% | Avg: 20-30% | **적절** | 평균 수준 |
| Health Score Distribution | 70:20:10 | 일반: 55:30:15 | **도전적** | Green 70%는 Top Quartile 수준 |

#### Stage 7: Ops & Analytics

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 | 조정 제안 |
|----------|--------|-------------|------|----------|
| Forecast Accuracy | <15% variance | Avg: 22-28% variance | **매우 도전적** | Top Quartile, Level 3+ Maturity 필요 |
| Data Completeness | >85% | Avg: 50-65% | **매우 도전적** | Agent 자동 입력이 핵심 enabler |

### 8-2. Play별 KPI 검증

#### Play 01: New Logo Outbound (T2/T3)

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 |
|----------|--------|-------------|------|
| Emails Sent / Day | 30-40 | Avg: 25-35 | **약간 도전적**, 자동화 시 달성 가능 |
| Calls / Day | 20-30 | Avg: 25-35 | **적절** |
| Connect Rate (Phone) | 8-12% | Avg: 5-8% | **도전적** | 직통 번호 확보 + 최적 시간대 필요 |
| Email Reply Rate | 5-10% | Avg: 3-5% | **도전적** | AI 개인화로 상위 달성 가능 |
| Positive Reply Rate | 30-50% | Avg: 30-40% | **적절~도전적** |
| Meetings / Month (SDR) | 12-18 | Avg: 10-15 | **도전적** | Top Quartile 수준 |
| SQL / Month | 8-12 | Avg: 6-10 | **도전적** | Top Quartile 수준 |
| Meeting Show Rate | >80% | Avg: 75-80% | **적절** |
| SQL→Opp Conversion | >60% | Avg: 55-65% | **적절** |

#### Play 02: Strategic Account Expansion (T1)

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 |
|----------|--------|-------------|------|
| Expansion Revenue YoY | 기존 ACV 20%+ | Avg: 15-25% | **적절** |
| White-Space Conversion | >30% | Limited data, est. 20-35% | **적절** |
| NRR Contribution (T1) | >120% | Top Quartile: 120-130% | **도전적이나 합리적** |
| Expansion Cycle Time | <60일 | Avg: 40-70일 (expansion) | **적절** |
| Avg Expansion ACV | >$30K | Segment-dependent | **검증 필요** |

#### Play 03: Renewal Rescue

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 |
|----------|--------|-------------|------|
| Save Rate | >70% | Avg: 50-65% | **도전적** | Agent 조기 감지가 핵심 |
| Gross Retention | >90% | Avg: 88-92% | **적절** |
| Logo Retention | >95% | Avg: 85-92% | **도전적** | Enterprise 중심이면 가능 |
| Contraction Rate | <10% | Avg: 8-15% | **적절~도전적** |
| Time to Intervention (Red) | <48hr | Best Practice | **적절** (Agent 자동 알림) |

#### Play 04: CS-Driven Upsell

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 |
|----------|--------|-------------|------|
| Signal → Qualified Rate | >30% | Limited data, est. 20-35% | **적절** |
| Handoff → Closed Won | >50% | Avg expansion win rate: 50-55% | **적절** |
| CS-driven Pipeline (%) | >25% of total | Avg: 15-25% | **도전적** |
| Signal → Handoff Time | <14일 | Best Practice 수준 | **적절** (Agent 지원 시) |
| Handoff → Close Time | <45일 | Avg: 30-60일 (expansion) | **적절** |

#### Play 05: Win/Loss Analysis

| 우리 타겟 | 설정값 | 벤치마크 대비 | 평가 |
|----------|--------|-------------|------|
| Debrief Completion Rate | >90% | Avg: 40-60% | **매우 도전적** | Agent 자동 debrief 필수 |
| Buyer Interview Rate | >50% | Avg: 15-25% | **매우 도전적** | 전담 인력 or 외부 위탁 필요 |
| Insight → Action Rate | >70% | Avg: 30-40% | **매우 도전적** | 조직적 실행력 필요 |
| Loss Reason Consistency | >60% | Avg: 40-50% | **도전적** | 구조화된 인터뷰 프로세스 필요 |

### 8-3. 종합 평가 요약

| 평가 등급 | KPI 수 | 비율 | 설명 |
|----------|--------|------|------|
| **적절 (Realistic)** | 24 | 48% | 산업 평균~상위 수준, 달성 가능 |
| **도전적이나 합리적 (Stretch)** | 18 | 36% | Top Quartile 수준, Agent 지원 시 달성 가능 |
| **매우 도전적 (Ambitious)** | 8 | 16% | Best-in-Class 수준, 특별한 enabler 필요 |
| **비현실적 (Unrealistic)** | 0 | 0% | 해당 없음 |

### 8-4. 핵심 조정 권장사항

1. **"매우 도전적" KPI에 대한 단계적 목표 설정**
   - Forecast Accuracy: Phase 1에서 <25% → Phase 3에서 <15%로 점진 달성
   - CRM Data Completeness: Phase 1에서 >65% → Agent 도입 후 >85%
   - Debrief Completion: Agent 자동 생성으로 >90% 가능하나, 품질 검증 필요
   - Buyer Interview Rate: 외부 리서치 파트너 활용 또는 간소화 버전(디지털 서베이) 도입 고려

2. **딜 사이즈별 KPI 분리 운영**
   - Win Rate, Sales Cycle, Discount Rate 등은 SMB/Mid/Enterprise 별도 목표 필요
   - 현재 Canon에서 "산업 평균 대비 +5pp"로 설정된 Win Rate는 적절하나, 절대값 기준도 함께 설정 권장

3. **Agent 도입이 직접적으로 개선하는 KPI 우선 추적**
   - CRM Data Completeness (자동 입력)
   - Stalled Deal Rate (자동 알림)
   - MEDDICC Compliance (자동 추출)
   - Forecast Accuracy (AI 예측)
   - Response Time (자동 응대)
   - 이 5개 KPI가 Agent PoC의 성과 측정 핵심 지표

4. **Tier별 목표 차등화 필요**

   | KPI | T1 목표 | T2 목표 | T3 목표 | 근거 |
   |-----|--------|--------|--------|------|
   | Win Rate | 30-35% | 22-27% | 15-20% | T1은 관계 기반, T3은 volume 기반 |
   | Sales Cycle | 90-120일 | 60-90일 | 30-45일 | T1은 복잡, T3은 표준화 |
   | Pipeline Coverage | 3x | 4x | 5x | Win Rate 역수에 비례 |
   | NRR | >125% | >110% | >100% | T1에서 expansion 집중 |

---

## Appendix A: 벤치마크 소스 목록

| 소스 | 리포트명 | 발행 연도 | 주요 데이터 |
|------|---------|----------|------------|
| Ebsta & Pavilion | B2B Sales Benchmarks | 2023, 2024 | Win rate, cycle, pipeline |
| KeyBanc Capital Markets | Annual SaaS Survey | 2024 | ACV, NRR, GRR, growth |
| OpenView Partners | SaaS Benchmarks | 2024 | ACV, retention, growth |
| Gartner | Sales Benchmarking | 2024 | Win rate, forecast, activity |
| Forrester | B2B Buying Study | 2024 | Buying behavior, stakeholders |
| Bridge Group | SDR Metrics & Compensation | 2024 | Activity, meetings, pipeline |
| Bessemer Venture Partners | State of the Cloud | 2024 | NRR, growth, efficiency |
| McKinsey | State of AI in Sales | 2024 | AI adoption, productivity |
| BCG | AI Agents in B2B Sales | 2024 | Agent impact, automation |
| Salesforce | State of Sales | 2024, 2025 | Trends, AI adoption, metrics |
| HubSpot | Sales Trends Report | 2024, 2025 | Activity, email, trends |
| RAIN Group | Sales Prospecting Benchmarks | 2024 | Connect rates, meetings |
| Gainsight | CS Benchmarks | 2024 | NRR, churn, expansion |
| Clari | Revenue Confidence | 2024 | Forecast accuracy, pipeline |
| SalesLoft / Outreach | Engagement Benchmarks | 2024 | Email, cadence, activity |
| Paddle / ProfitWell | SaaS Pricing | 2024 | ACV, discount, pricing |
| XANT / InsideSales | Lead Response Study | 2023 | Response time impact |
| Winning by Design | Revenue Architecture | 2024 | Bow-tie model, velocity |
| ChurnZero | Churn Benchmarks | 2024 | Churn reasons, retention |
| Totango | CS Industry Benchmarks | 2024 | Health score, adoption |

> **참고**: 위 출처들은 2023-2025년에 발행된 공개 리포트 기반입니다. 일부 데이터는 유료 리포트에서 인용된 요약 수치이며, 실제 포트폴리오사 적용 시 해당 리포트의 최신 버전을 직접 참조하는 것을 권장합니다. 산업, 지역, 기업 규모에 따라 벤치마크 수치는 상당한 편차를 보일 수 있습니다.

---

## Appendix B: 벤치마크 활용 가이드

### 어떤 수치를 목표로 설정할 것인가?

| 상황 | 권장 목표 수준 | 근거 |
|------|-------------|------|
| 신규 프로세스 도입 1년차 | Average (50th percentile) | 기본 역량 구축 단계 |
| 프로세스 안정화 2년차 | Average~Top Quartile | 최적화 시작 |
| 성숙 조직 3년차+ | Top Quartile 이상 | 경쟁 우위 확보 |
| Agent 자동화 도입 후 | Top Quartile | Agent가 bottom-up으로 끌어올림 |

### KPI 목표 설정 시 체크리스트

- [ ] 해당 KPI의 산업 벤치마크를 확인했는가?
- [ ] 우리 조직의 현재 수준(As-is)을 측정했는가?
- [ ] 목표와 현재의 Gap이 합리적인가 (보통 1-2 quartile 개선이 현실적)?
- [ ] 해당 KPI를 개선할 구체적 Action/Enabler가 있는가?
- [ ] 단계적 마일스톤을 설정했는가 (90일 → 180일 → 365일)?
- [ ] KPI 간 상충 관계를 점검했는가 (예: Win Rate 올리면서 Pipeline도 키우기 어려움)?
