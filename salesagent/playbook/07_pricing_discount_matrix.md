# Pricing & Discount Matrix
## 가격 정책 및 할인 승인 체계

---

## Purpose

이 문서는 포트폴리오 전체에 적용되는 **가격 구조, 할인 승인 권한, 계약 조건, 번들 규칙**의 표준입니다.
모든 AE, Sales Manager, Deal Desk는 이 매트릭스를 기준으로 가격 협상을 수행하며,
Deal Conversion Agent는 이 규칙을 자동으로 검증하고 위반 시 에스컬레이션을 트리거합니다.

### 이 문서의 위치 (7-Stage Canon 매핑)
- **Stage 4: Pipeline Progression** — S5 Negotiation 단계에서 가격 협상 가이드
- **Stage 5: Close & Onboard** — 제안서 작성, 할인 승인, 계약 체결의 기준
- **Stage 6: Retention & Growth** — 갱신 및 확장 가격 정책

### 관련 문서
| 문서 | 연관 영역 |
|------|----------|
| `00_sales_process_canon.md` | 할인 승인 매트릭스 원본 (Stage 5) |
| `05_objection_handling.md` | "너무 비쌉니다" 반론 대응 |
| `crm/schema.md` | `Discount_Pct__c`, `ACV__c`, `Contract_Term__c` 필드 |
| `agent.md` | Deal Conversion Agent 역할 정의 |

---

## 1. Pricing Model Framework

### 1-1. Standard Pricing Tiers (Good / Better / Best)

모든 포트폴리오사는 3-tier 가격 구조를 기본으로 합니다. 구체적 기능과 가격은 포트폴리오사별로 커스터마이징하되, 구조는 동일합니다.

| 패키지 | 영문명 | 포지셔닝 | 대상 | 가격 범위 |
|--------|--------|----------|------|----------|
| 기본 | **Good** (Starter) | 핵심 기능만. 진입 장벽 최소화 | SMB, 초기 도입 | [$ X] /user/month |
| 표준 | **Better** (Professional) | 핵심 + 분석 + 통합. 가장 많이 팔리는 패키지 | Mid-market, Growth | [$ Y] /user/month |
| 프리미엄 | **Best** (Enterprise) | 전체 기능 + 전담 지원 + SLA + 커스터마이징 | Enterprise, T1 | [$ Z] /user/month |

> **Anchor Rule**: 제안 시 항상 **Better** 패키지를 기본으로 제시. Good은 "최소한", Best는 "최적"으로 프레이밍.

### 1-2. Pricing Model Types

| 과금 모델 | 설명 | 적합한 경우 | 주의사항 |
|-----------|------|------------|----------|
| **Per-User (Named)** | 지정 사용자 수 기반 과금 | 사용자별 가치가 명확한 SaaS | 사용자 증가 시 자동 expansion |
| **Per-Seat (Concurrent)** | 동시 접속자 수 기반 | 사용자 풀이 크지만 동시 사용은 제한적 | 피크 관리 필요 |
| **Usage-Based** | 실제 사용량(API 콜, 트랜잭션, 저장 용량) 기반 | 사용량 변동이 큰 서비스 | 최소 약정(minimum commit) 설정 필수 |
| **Flat-Rate** | 기능/모듈 단위 고정 금액 | 단순한 제품, 예측 가능한 가치 | Expansion 동력이 약할 수 있음 |
| **Hybrid** | Per-User 기본 + Usage 초과분 과금 | 기본 가치 + 성장 연동형 | 청구 복잡도 증가 |

### 1-3. Annual vs Monthly Billing

| 결제 주기 | 가격 수준 | 할인 | 조건 |
|-----------|----------|------|------|
| **Monthly** | 정가 (List Price) | 없음 | 최소 약정 3개월 |
| **Annual** (선결제) | 정가 대비 **15-20% 할인** | 연간 결제 할인 | 12개월 선결제 필수 |
| **Annual** (분기 결제) | 정가 대비 **10% 할인** | 분기 결제 할인 | 12개월 약정, 분기별 청구 |

> **원칙**: Annual 결제를 기본으로 제안. Monthly는 PoC/Trial 이후 전환 시에만 허용.

### 1-4. Pricing by Account Tier

| Account Tier | Pricing Strategy | 가격 유연성 | 협상 주체 | Agent 역할 |
|-------------|-----------------|------------|----------|-----------|
| **T1 Strategic** | Custom pricing, Enterprise Agreement (EA) | 높음 — 맞춤 가격, 볼륨 커밋, 장기 계약 | AE + VP Sales + Deal Desk | 시장 가격 벤치마크 제공, P&L 시뮬레이션 |
| **T2 Core** | Standard pricing + 볼륨 할인 | 중간 — 미리 정의된 할인 테이블 내 | AE + Sales Manager | 할인 범위 자동 검증, 승인 워크플로 트리거 |
| **T3 Long-tail** | Self-serve pricing, 최소 협상 | 낮음 — 정가 또는 연간 결제 할인만 | AE (자체 승인 범위 내) | 자동 견적 생성, 표준 가격 적용 |

---

## 2. Discount Approval Matrix (할인 승인 체계)

### 2-1. Standard Discount Authority

`00_sales_process_canon.md`의 할인 승인 매트릭스를 상세화한 버전입니다.

| Discount Range | Approver | SLA | 필수 문서 | CRM Action |
|---------------|----------|-----|----------|------------|
| **0-10%** | AE 자체 승인 | 즉시 | CRM Deal Note에 할인 사유 기록 | `Discount_Pct__c` 업데이트 |
| **11-20%** | Sales Manager 승인 | **4시간** | 서면 정당화 + 경쟁 상황 컨텍스트 | Manager approval tag in CRM |
| **21-30%** | VP Sales 승인 | **24시간** | Business Case + P&L 영향 분석 | VP approval + deal review meeting |
| **30%+** | C-Level 승인 (예외적) | **48시간** | Executive Approval Form + 이사회 수준 정당화 | C-Level sign-off, Deal Desk review |

### 2-2. Discount Approval Decision Tree

```
할인 요청 발생
│
├── 할인율 ≤ 10%?
│   ├── YES → AE 자체 승인 → CRM 기록 → 완료
│   └── NO ↓
│
├── 할인율 ≤ 20%?
│   ├── YES → Sales Manager에게 에스컬레이션
│   │         ├── 승인 → CRM 기록 → 완료
│   │         └── 반려 → AE에게 대안 협상 지시
│   └── NO ↓
│
├── 할인율 ≤ 30%?
│   ├── YES → VP Sales에게 에스컬레이션
│   │         ├── 승인 → CRM 기록 → 완료
│   │         └── 반려 → 대안 패키지/조건 협상
│   └── NO ↓
│
└── 할인율 > 30%
    └── C-Level 에스컬레이션
          ├── 승인 (극히 예외적) → CRM 기록 + 사후 리뷰
          └── 반려 → Walk-away 또는 구조 변경
```

### 2-3. Discount Triggers & Guidelines

#### 할인이 적절한 경우 (Acceptable Triggers)

| Trigger | 최대 추가 할인 | 조건 |
|---------|-------------|------|
| **경쟁 압박** (Competitive pressure) | +10% | 경쟁사 제안서 또는 구체적 경쟁 증거 필요 |
| **Multi-year 약정** (2년+) | 아래 2-4 참조 | 최소 24개월 약정 계약 |
| **Strategic Account** (T1) | +5% | 포트폴리오 차원의 전략적 가치 입증 |
| **대량 라이선스** (Volume) | 아래 2-5 참조 | 최소 사용자 수 기준 충족 |
| **레퍼런스 합의** (Reference deal) | +5% | 공식 사례 발표 + 로고 사용 동의 |
| **분기 마감 가속** (Quarter-end pull-in) | +5% | 당 분기 내 계약 서명 확정 시에만 |

#### 할인이 부적절한 경우 (Red Flags)

| 상황 | 이유 | 대신 할 일 |
|------|------|-----------|
| 가치 입증 없이 가격부터 논의 | Buyer가 제품 가치를 모른 채 가격만 비교 중 | Discovery 재실행, Gap Selling 프레임 적용 |
| 영업 초기 단계 (S1-S3) | 협상은 S5에서. 이전 할인은 앵커만 낮춤 | "최종 조건은 구체적 범위 확정 후 논의" |
| Champion 없이 가격 양보 | 내부 옹호자 없으면 할인해도 의미 없음 | Champion 확보 후 가격 논의 |
| 작년 할인 갱신 시 동일 적용 요구 | 할인은 시점별 맥락이 다름 | 신규 가치 제안으로 정당화 |
| 이미 Win 가능성 높은 딜 | 불필요한 마진 손실 | 할인 없이 클로징 진행 |

### 2-4. Multi-Year Commitment Discounts

| 계약 기간 | 추가 할인 | 조건 | 총 가능 할인 (AE 권한 내) |
|-----------|----------|------|--------------------------|
| **12개월** (기본) | 0% | 표준 | 0-10% |
| **24개월** | +5% | 전액 선결제 or 분기 결제 | 5-15% |
| **36개월** | +10% | 전액 선결제 or 분기 결제, 연간 가격 조정 조항 포함 | 10-20% |
| **48개월+** | +15% | 전액 선결제, VP Sales 승인 필수, 연간 가격 조정 조항 포함, 조기 해지 조항 필수 | 15-25% |

> **주의**: Multi-year 할인은 Standard Discount Authority와 **별도 누적**. 예: AE가 자체 5% + Multi-year 5% = 총 10%는 AE 권한 내. 자체 10% + Multi-year 5% = 총 15%는 Sales Manager 승인 필요.

### 2-5. Volume-Based Discount Tiers

| 사용자 수 (Per-User 기준) | Volume Discount | 누적 가능 |
|--------------------------|----------------|----------|
| 1-25 users | 0% | - |
| 26-50 users | 5% | Standard + Volume |
| 51-100 users | 8% | Standard + Volume |
| 101-250 users | 12% | Standard + Volume |
| 251-500 users | 15% | Standard + Volume, Manager 승인 |
| 500+ users | Custom | VP Sales + Deal Desk |

### 2-6. Pilot / PoC Pricing Guidelines

| 항목 | 기준 |
|------|------|
| **PoC 기간** | 최대 30일 (예외: 60일, Manager 승인) |
| **PoC 가격** | 정가의 0% (무료) 또는 정가의 50% 중 선택 |
| **무료 PoC 조건** | T1 계정, 또는 ACV [$ X]+ 예상 딜에 한함 |
| **유료 PoC 크레딧** | PoC 비용은 본 계약 체결 시 첫 해 요금에서 차감 |
| **PoC 성공 기준** | 사전 합의된 KPI 달성 여부 (계약 전 문서화 필수) |
| **PoC → 계약 전환 목표** | >60% |

### 2-7. Discount Guard Rails

| Guard Rail | 규칙 | Agent 검증 |
|-----------|------|-----------|
| **Maximum Discount Cap** | 어떤 경우에도 **40% 초과 불가** (C-Level 승인 포함) | `Discount_Pct__c > 40` → 자동 차단 |
| **Minimum ACV Floor** | 패키지별 최소 ACV 하한선: Good [$ A], Better [$ B], Best [$ C] | `ACV__c < Floor` → 경고 |
| **Discount Frequency Limit** | 동일 계정에 연 2회 이상 추가 할인 불가 | Account history 체크 |
| **Margin Floor** | 총 마진율 [X]% 이하로 떨어지는 할인 금지 | P&L 시뮬레이션 자동 실행 |
| **Discount + Free Months 중복 금지** | 할인과 무료 기간을 동시 제공 불가 | 복합 할인 감지 시 경고 |

---

## 3. Bundle Rules

### 3-1. Good-Better-Best Package Composition

| 기능 카테고리 | Good (Starter) | Better (Professional) | Best (Enterprise) |
|-------------|----------------|----------------------|-------------------|
| **Core Features** | [기본 기능 A, B, C] | [기본 + 고급 기능 D, E] | [전체 기능] |
| **Users** | 최대 [10] users | 최대 [50] users | 무제한 |
| **Storage** | [5] GB | [50] GB | [무제한 / 커스텀] |
| **Support** | 이메일 (48hr SLA) | 이메일 + 채팅 (24hr SLA) | 전담 CSM + 전화 (4hr SLA) |
| **Integrations** | 기본 [3]개 | 표준 [10]개 | 무제한 + 커스텀 API |
| **Analytics** | 기본 리포트 | 고급 대시보드 + 내보내기 | 커스텀 BI 연동 |
| **Training** | 셀프서브 (문서/비디오) | 그룹 온보딩 (월 1회) | 전담 트레이닝 + QBR |
| **SLA** | 99.5% uptime | 99.9% uptime | 99.95% uptime + SLA 크레딧 |
| **가격** | [$ X] /user/month | [$ Y] /user/month | [$ Z] /user/month |

### 3-2. Cross-sell / Upsell Path

```
Good (Starter)
  │
  ├── Trigger: 사용자 8명 도달 (80% cap) → Upsell → Better
  ├── Trigger: 고급 기능 3회 이상 문의 → Upsell → Better
  │
  ▼
Better (Professional)
  │
  ├── Trigger: 사용자 40명 도달 (80% cap) → Upsell → Best
  ├── Trigger: 커스텀 통합 요청 → Upsell → Best
  ├── Trigger: SLA 이슈 2회 이상 → Upsell → Best (SLA 개선)
  │
  ▼
Best (Enterprise)
  │
  └── Trigger: 추가 부서/사업부 도입 → Expansion (Volume increase)
  └── Trigger: 신규 제품 라인 → Cross-sell (Add-on)
```

### 3-3. Add-on Pricing

| Add-on | 설명 | 대상 패키지 | 가격 |
|--------|------|------------|------|
| **Advanced Analytics** | BI 연동, 커스텀 대시보드 | Good, Better | [$ P] /month |
| **Premium Support** | SLA 업그레이드, 전담 CSM | Good, Better | [$ Q] /month |
| **API Access** | REST API 무제한 호출 | Good | [$ R] /month |
| **SSO / SAML** | 엔터프라이즈 인증 | Good, Better | [$ S] /month |
| **Data Migration** | 기존 시스템 데이터 이관 | 전체 | [$ T] (일회성) |
| **Custom Training** | 맞춤 교육 프로그램 | 전체 | [$ U] /session |

### 3-4. Bundle Discounts

| Bundle 구성 | 개별 구매 대비 할인 | 조건 |
|-------------|-------------------|------|
| Better + Advanced Analytics | 10% | 연간 결제 시 |
| Better + Premium Support | 8% | 연간 결제 시 |
| Best + 2개 이상 Add-on | 15% | 24개월 이상 약정 |
| 전 제품 풀 패키지 (Best + All Add-ons) | 20% | 36개월 약정, VP Sales 승인 |

> **원칙**: 개별 제품 할인보다 **번들 할인**을 우선 제안. 마진율은 더 높으면서 고객에게는 더 큰 할인처럼 보임.

---

## 4. Contract Terms

### 4-1. Standard Contract Options

| 항목 | 옵션 | 기본값 | 비고 |
|------|------|--------|------|
| **계약 기간** | 12 / 24 / 36 months | **12 months** | 24+ 시 multi-year 할인 적용 |
| **결제 조건** | Net 30 / Net 45 / Net 60 / Net 90 | **Net 30** | Net 45+ 시 surcharge 적용 (Section 4-2 참조) |
| **결제 주기** | 연간 선결제 / 분기 / 월간 | **연간 선결제** | 월간은 PoC 전환 시에만 |
| **자동 갱신** | Yes / No | **Yes** (60일 사전 통지 해지) | 자동 갱신 조항은 표준 |
| **가격 조정** | 연간 [3-7]% 인상 조항 | **연 5%** | 36개월 계약에 필수 포함 |
| **SLA** | Good / Better / Best 패키지별 | 패키지별 상이 | Best는 SLA 크레딧 포함 |

### 4-2. Payment Terms Impact on Pricing

| Payment Term | 가격 영향 | 적용 시 |
|-------------|----------|---------|
| **Net 30** (기본) | 정가 | 표준 |
| **Net 45** | +1% surcharge | Enterprise 고객, 조달 프로세스 표준 |
| **Net 60** | +2% surcharge | 대기업, 조달 프로세스 긴 경우 |
| **Net 90** | +3% surcharge | 공공기관, 특수 조달 |
| **선결제** (Upfront) | -3% 추가 할인 | 현금 흐름 최적화 |

### 4-3. Auto-Renewal Guidelines

| 항목 | 규칙 |
|------|------|
| 기본 설정 | 모든 계약은 자동 갱신이 기본 |
| 통지 기간 | 만기 **60일 전** 서면 통지로 해지 가능 |
| 갱신 시 가격 | `Price_Escalation__c` 조항에 따라 조정 (아래 Section 5 참조) |
| Agent 역할 | 만기 D-90에 자동 알림, 갱신 조건 사전 준비 |

### 4-4. Non-Standard Terms (법무 검토 필요)

| 비표준 조건 | 법무 검토 필요 여부 | 에스컬레이션 |
|------------|-------------------|------------|
| 배상 조항 변경 (Indemnification) | **필수** | Legal + VP Sales |
| 책임 한도 변경 (Liability cap) | **필수** | Legal + CFO |
| 데이터 처리 조항 (DPA 커스터마이징) | **필수** | Legal + Security |
| SLA 크레딧 상향 | 조건부 | Deal Desk |
| 중도 해지 조항 (Early termination) | **필수** | Legal + VP Sales |
| MFN 조항 (Most Favored Nation) | **필수** | Legal + C-Level |
| Escrow 요구 | **필수** | Legal + CTO |
| 감사권 (Audit rights) | 조건부 | Legal |

### 4-5. Contract Risk Assessment

| Risk Level | 기준 | 필요 조치 |
|-----------|------|----------|
| **Low** | 표준 조건, 12개월, 정가 또는 10% 이내 할인 | AE 자체 진행 |
| **Medium** | Multi-year, 20% 이내 할인, 1-2개 비표준 조항 | Manager 리뷰 + Deal Desk |
| **High** | 30%+ 할인, 다수 비표준 조항, MFN/Escrow 요구 | VP Sales + Legal + CFO 리뷰 |
| **Critical** | ACV [$ X]+ 대형 딜, 전략적 의미가 큰 계약 | C-Level + 이사회 보고 |

---

## 5. Price Escalation & Renewal Pricing

### 5-1. Annual Price Increase Guidelines

| 항목 | 기준 |
|------|------|
| **표준 인상률** | 연 **3-7%** (계약서 명시) |
| **기본 인상률** | 연 **5%** (별도 합의 없을 시) |
| **인상 상한** | CPI(소비자물가지수) + 3% 또는 7% 중 낮은 값 |
| **통지** | 갱신 **60일 전** 서면 통지 |
| **인상 면제** | 없음 (Multi-year 계약 시 계약서 내 인상률 고정) |

### 5-2. Renewal Pricing vs New Customer Pricing

| 구분 | 가격 기준 | 할인 정책 |
|------|----------|----------|
| **신규 고객** | 현재 List Price 기준 | Standard Discount Matrix 적용 |
| **갱신 고객** (정상) | 기존 계약가 + 연간 인상률 | 추가 할인 불가 (이미 할인 반영됨) |
| **갱신 고객** (Expansion) | Expansion 분은 현재 List Price, 기존분은 계약가 유지 | Expansion 할인은 Standard Matrix 적용 |
| **갱신 고객** (At-Risk) | 아래 5-4 참조 | 유연하게 대응 (VP Sales 승인 범위) |

### 5-3. Expansion Pricing for Existing Customers

| Expansion 유형 | 가격 기준 | 할인 가이드 |
|---------------|----------|------------|
| **사용자 추가** (Same package) | 기존 계약 단가 적용 | 볼륨 티어 상승 시 전체 단가 재조정 |
| **패키지 업그레이드** (Good → Better) | 업그레이드 패키지 정가, 남은 기간 비례 정산 | 최대 10% (Loyalty discount) |
| **Add-on 추가** | Add-on 정가 | 번들 할인 적용 가능 |
| **신규 부서/사업부** | 별도 계약 또는 마스터 계약 하 추가 | 통합 볼륨으로 할인 재계산 |

### 5-4. At-Risk Account Pricing Flexibility

Health Score가 Red 또는 Yellow인 갱신 대상 계정에 대한 특별 가격 정책.

| Health Status | 허용 조치 | 승인 권한 | 조건 |
|-------------|----------|----------|------|
| **Yellow** (50-79) | 인상률 동결 (0%) | Sales Manager | 개선 계획 합의 필수 |
| **Yellow** (50-79) | 추가 5% 할인 | VP Sales | 12개월 한정, Improvement Plan 문서화 |
| **Red** (<50) | 최대 15% 할인 + 인상 동결 | VP Sales + CS Director | Retention Plan 필수, 6개월 재평가 |
| **Red** (<50) | 계약 축소 (Downgrade) 허용 | Manager | Churn보다 Downgrade 선호 |
| **Churn imminent** | Custom rescue package | C-Level | 케이스별 판단, 최대 6개월 한정 |

> **원칙**: At-risk 할인은 반드시 **개선 계획(Improvement Plan)**과 연동. 할인만 주고 방치하는 것은 금지.

---

## 6. Competitive Pricing Intelligence

### 6-1. Competitive Price Response Framework

| 경쟁 상황 | 대응 전략 | 절대 하지 말 것 |
|----------|----------|---------------|
| 경쟁사가 30%+ 저렴 | Value-based 비교 (TCO, ROI), 차별화 기능 강조 | 즉시 매칭하지 않음 |
| 경쟁사가 10-30% 저렴 | 번들 제안, Multi-year 할인, Add-on 무료 제공 | 기능 축소 제안하지 않음 |
| 경쟁사가 비슷한 가격 | 가치/서비스 차별화에 집중 | 가격 전쟁에 진입하지 않음 |
| "내부 개발" 대안 | TCO 분석 (인건비 + 유지보수 + 기회비용) | 기술 비교에 말리지 않음 |

### 6-2. Price Matching Policy

| 항목 | 정책 |
|------|------|
| **공식 입장** | "저희는 가격 매칭을 하지 않습니다" |
| **이유** | 가격 매칭은 상품화(commoditization) 시그널. 가치 기반 판매 원칙 위배 |
| **대안** | 할인 대신 가치 추가: 무료 온보딩, 추가 교육, 연장 PoC, SLA 업그레이드 |
| **예외** | T1 Strategic 계정의 경우 VP Sales 재량으로 경쟁 대응 가격 제시 가능 |

### 6-3. Value-Based Selling Counters

가격 반론에 대한 Value Framework (05_objection_handling.md 연계):

| 반론 | Value Counter | 정량화 방법 |
|------|-------------|------------|
| "너무 비쌉니다" | Cost of Inaction (아무것도 안 하는 비용) 계산 | 현재 비효율 × 12개월 = 연간 손실액 |
| "경쟁사가 더 싸요" | TCO (총소유비용) 비교 | 라이선스 + 구현 + 운영 + 기회비용 |
| "예산이 없습니다" | ROI Payback 기간 제시 | 투자금 ÷ 월간 절감액 = 회수 개월 수 |
| "가격을 더 내려야 합니다" | Trade-off 제안 (아래 Section 8 참조) | 가격 vs 조건 (기간, 범위, 결제) |

### 6-4. Competitive Intelligence CRM Tracking

| CRM Field | API Name | 용도 |
|-----------|----------|------|
| Primary Competitor | `MEDDICC_Competitor__c` | 이 딜의 주 경쟁사 |
| Competitive Position | `MEDDICC_Comp_Position__c` | Losing / Even / Winning / Sole Source |
| Competitor Price (추정) | `Competitor_Price_Est__c` | 경쟁사 추정 가격 (있을 경우) |
| Competitive Notes | `Competitive_Notes__c` | 경쟁 관련 상세 메모 |

---

## 7. Agent Integration (Deal Conversion Agent 연동)

### 7-1. Deal Conversion Agent의 가격/할인 관련 역할

`agent.md`에 정의된 Deal Conversion Agent는 다음 가격/할인 관련 기능을 수행합니다:

| 기능 | 설명 | Autonomy Level |
|------|------|---------------|
| **할인 자동 검증** | `Discount_Pct__c` 입력 시 승인 권한 자동 매칭 | Autonomous |
| **Guard Rail 시행** | Maximum cap, ACV floor, margin floor 위반 감지 | Autonomous (차단) |
| **승인 워크플로 트리거** | 할인 범위별 적절한 승인자에게 자동 라우팅 | Autonomous |
| **P&L 시뮬레이션** | 할인 적용 시 마진, LTV, CAC payback 자동 계산 | Assisted (데이터 제공) |
| **경쟁 가격 벤치마크** | 유사 딜의 할인율, 경쟁 상황 참조 데이터 제공 | Assisted (참고용) |
| **제안서 가격 섹션 초안** | 패키지, 할인, 조건을 반영한 가격 테이블 생성 | Co-pilot (AE 검토 후 발송) |
| **갱신 가격 자동 계산** | 기존 계약가 + 인상률 + expansion 반영 | Autonomous |

### 7-2. CRM Fields (가격/할인 관련)

| Field | API Name | Type | Description | Agent 접근 |
|-------|----------|------|-------------|-----------|
| Discount % | `Discount_Pct__c` | Percent | 적용 할인율 | Read/Write |
| ACV | `ACV__c` | Currency | 연간 계약 가치 | Read/Write |
| Contract Term | `Contract_Term__c` | Number (months) | 계약 기간 | Read/Write |
| List Price | `List_Price__c` | Currency | 정가 (할인 전) | Read |
| Net Price | `Net_Price__c` | Formula | List Price × (1 - Discount%) | Auto |
| Discount Approver | `Discount_Approver__c` | Lookup(User) | 할인 승인자 | Write |
| Discount Approval Status | `Discount_Approval_Status__c` | Picklist | Pending / Approved / Rejected | Read/Write |
| Discount Justification | `Discount_Justification__c` | Text Area | 할인 사유 상세 | Write |
| Package Tier | `Package_Tier__c` | Picklist | Good / Better / Best | Read/Write |
| Billing Frequency | `Billing_Frequency__c` | Picklist | Monthly / Quarterly / Annual | Read/Write |
| Payment Terms | `Payment_Terms__c` | Picklist | Net30 / Net60 / Net90 / Upfront | Read/Write |
| Price Escalation % | `Price_Escalation_Pct__c` | Percent | 연간 가격 인상률 | Read/Write |
| Multi-Year Discount % | `Multi_Year_Discount_Pct__c` | Percent | Multi-year 추가 할인 | Read/Write |
| Total Effective Discount | `Total_Effective_Discount__c` | Formula | Standard + Multi-Year + Volume | Auto |
| Margin % | `Margin_Pct__c` | Formula | 마진율 | Auto |
| Competitor Price Est | `Competitor_Price_Est__c` | Currency | 경쟁사 추정 가격 | Read/Write |

### 7-3. Automated Discount Validation Rules

Agent가 실시간으로 검증하는 규칙:

```
Rule 1: DISCOUNT_CAP
  IF Discount_Pct__c > 40%
  THEN → BLOCK (할인 등록 차단, AE에게 경고)

Rule 2: APPROVAL_ROUTING
  IF Discount_Pct__c > 10% AND Discount_Approval_Status__c != 'Approved'
  THEN → HOLD (승인 완료 전까지 Stage 진행 차단)

Rule 3: ACV_FLOOR
  IF ACV__c < [Minimum ACV for Package_Tier__c]
  THEN → WARN (AE에게 경고, 진행은 허용)

Rule 4: MARGIN_FLOOR
  IF Margin_Pct__c < [X]%
  THEN → ESCALATE (VP Sales + Deal Desk 자동 알림)

Rule 5: MULTI_DISCOUNT_CHECK
  IF Discount_Pct__c > 0 AND (Free_Months__c > 0 OR Credit_Amount__c > 0)
  THEN → WARN (복합 할인 감지, Manager 확인 필요)

Rule 6: FREQUENCY_CHECK
  IF Account has > 2 discounted deals in trailing 12 months
  THEN → WARN (할인 남용 가능성, Manager 리뷰)

Rule 7: RENEWAL_ESCALATION_CHECK
  IF Is_Renewal__c = true AND Discount_Pct__c > Previous_Discount_Pct__c
  THEN → ESCALATE (갱신 시 할인 확대는 VP Sales 승인 필요)
```

### 7-4. Approval Workflow Automation (n8n 워크플로)

```
Trigger: Discount_Pct__c updated on Opportunity
│
├── Step 1: Validate against Guard Rails (Rules 1-7)
│   ├── BLOCK → Notify AE, revert field
│   └── PASS ↓
│
├── Step 2: Determine Approval Level
│   ├── 0-10% → Auto-approve, log in CRM
│   ├── 11-20% → Route to Sales Manager (Slack/Email)
│   ├── 21-30% → Route to VP Sales (Slack/Email + Calendar hold)
│   └── 30%+ → Route to C-Level (Email + Deal Desk brief)
│
├── Step 3: Approver Action
│   ├── Approved → Update Discount_Approval_Status__c = 'Approved'
│   │             → Log approver + timestamp
│   │             → Notify AE
│   └── Rejected → Update Discount_Approval_Status__c = 'Rejected'
│                 → Log rejection reason
│                 → Notify AE with guidance
│
└── Step 4: Post-Approval
    ├── Update Net_Price__c (auto-calculated)
    ├── Update Forecast (if ACV changed)
    └── Log discount event in Activity history
```

---

## 8. Appendix: Price Negotiation Playbook

AE가 라이브 협상 중 빠르게 참조할 수 있는 치트 시트.

### 8-1. Negotiation Principles

| 원칙 | 설명 |
|------|------|
| **절대 먼저 양보하지 않는다** | 고객이 구체적으로 요청하기 전까지 할인을 먼저 제안하지 않는다 |
| **할인은 교환이다** | "가격을 내리려면 무언가를 받아야 합니다" (기간, 범위, 결제 조건) |
| **가치 먼저, 가격은 나중에** | Discovery에서 확인된 Pain/Gap의 금전적 가치를 먼저 확립 |
| **침묵은 무기다** | 가격 제시 후 먼저 말하지 않는다. 침묵을 견딘다 |
| **최종 제안은 한 번만** | "이것이 저희가 제시할 수 있는 최선입니다"는 한 번만 사용 |

### 8-2. Opening Position → Walk-Away Point

| 구간 | 설명 | 예시 |
|------|------|------|
| **Opening** (List Price) | 정가에서 시작. 앵커링 효과 활용 | "Better 패키지 기준 [$ Y]/user/month입니다" |
| **Target** (5-10% 할인) | 가장 현실적인 합의점. 이 수준에서 클로징이 목표 | "연간 결제 시 [$ Y×0.9]/user/month 가능합니다" |
| **Floor** (15-20% 할인) | Manager 승인 범위 내 최대. 이 이상은 에스컬레이션 | "이 수준은 상급자 승인이 필요합니다" |
| **Walk-Away** (ACV Floor 미달) | 이 이하로는 계약 불가. 마진이 비즈니스를 정당화하지 못함 | "이 조건으로는 진행이 어렵습니다" |

### 8-3. Trade-Off Menu (할인 대신 제안할 것들)

고객이 가격 인하를 요구할 때, **순수 할인 대신 교환 가능한 조건**:

| 고객 요구 | AE 역제안 (Trade-Off) | AE 이점 |
|----------|----------------------|--------|
| "10% 깎아주세요" | "24개월 약정 시 동일 할인 가능합니다" | 장기 계약 확보 |
| "가격이 너무 높아요" | "Better 대신 Good + Analytics Add-on 조합은 어떨까요?" | 패키지 최적화, 마진 보호 |
| "경쟁사는 더 싸요" | "연간 선결제 시 추가 3% 할인 가능합니다" | 현금 흐름 개선 |
| "더 내려야 결재 받아요" | "이번 분기 내 서명 시 [X]% 추가 가능합니다" | 딜 사이클 단축 |
| "예산이 부족해요" | "올해 9개월분만 계약하고, 내년부터 12개월로?" | 올해 예산 내 맞춤 |
| "할인 더 필요합니다" | "공식 레퍼런스 사례 제공에 동의하시면 추가 5% 가능" | 마케팅 자산 확보 |
| "무료 기간을 달라" | "PoC 비용을 본 계약에서 차감하는 구조는 어떨까요?" | 유료 PoC 확보 |

### 8-4. Negotiation Quick Reference Card

| 상황 | 스크립트 |
|------|---------|
| **가격 첫 제시** | "[고객명]의 상황에 맞는 Better 패키지 기준으로, [$ Y]/user/month, 연간 [$ Y×12×users]입니다. 앞서 논의하신 [specific pain]을 해결하기 위한 구성입니다." |
| **할인 요청 시** | "이해합니다. 어느 정도 수준을 기대하시는지요? 저희도 가능한 범위 내에서 조건을 맞춰보겠습니다." |
| **구체적 할인 수치 요구 시** | "말씀하신 수준은 [제가 / 상급자가] 검토가 필요합니다. 대신 [trade-off option]을 제안드리면 동일한 효과가 있을 수 있습니다." |
| **최종 제안** | "종합적으로, [Package] + [Term] + [Discount]% 조건으로 제안드립니다. 이것이 저희가 제시할 수 있는 최선의 조건입니다." |
| **Walk-away** | "안타깝지만, 이 조건으로는 저희 양쪽 모두에게 성공적인 파트너십이 어렵다고 판단됩니다. 향후 상황이 바뀌시면 언제든 연락 주십시오." |

### 8-5. Common Negotiation Traps (피해야 할 함정)

| 함정 | 설명 | 대응 |
|------|------|------|
| **Flinch (과장 반응)** | 고객이 가격 듣고 놀란 척 | 침묵. 반응하지 않는다. 가격의 근거를 재설명 |
| **Nibbling (추가 요구)** | 합의 직전에 "하나만 더" 요구 | "이 조건은 이미 최종 합의된 범위입니다" |
| **Good cop / Bad cop** | 한 명은 우호적, 한 명은 적대적 | Bad cop의 구체적 우려에 집중, 감정 무시 |
| **Budget bluff** | "예산이 [X]밖에 없다" (실제보다 적게 말함) | "그 예산으로 가능한 범위를 구성해드리겠습니다" → 축소 패키지 제안 |
| **Deadline pressure** | "오늘 결정 안 하면 다른 벤더로" | "급한 결정보다 맞는 결정이 중요합니다. 내일까지 최종 제안 드리겠습니다" |

---

## 9. Revision History

| 버전 | 날짜 | 변경 내용 | 작성자 |
|------|------|----------|--------|
| 1.0 | [YYYY-MM-DD] | 초안 작성 | [Author] |

---

## 10. Related CRM Schema Updates

이 문서에서 참조하는 CRM 필드 중 `crm/schema.md`에 아직 없는 신규 필드:

| Field Name | API Name | Type | Object | Description |
|-----------|----------|------|--------|-------------|
| List Price | `List_Price__c` | Currency | Opportunity | 정가 (할인 전) |
| Net Price | `Net_Price__c` | Formula | Opportunity | 할인 후 가격 |
| Discount Approver | `Discount_Approver__c` | Lookup(User) | Opportunity | 할인 승인자 |
| Discount Approval Status | `Discount_Approval_Status__c` | Picklist | Opportunity | Pending / Approved / Rejected |
| Discount Justification | `Discount_Justification__c` | Text Area | Opportunity | 할인 사유 |
| Package Tier | `Package_Tier__c` | Picklist | Opportunity | Good / Better / Best |
| Billing Frequency | `Billing_Frequency__c` | Picklist | Opportunity | Monthly / Quarterly / Annual |
| Payment Terms | `Payment_Terms__c` | Picklist | Opportunity | Net30 / Net60 / Net90 / Upfront |
| Price Escalation % | `Price_Escalation_Pct__c` | Percent | Opportunity | 연간 가격 인상률 |
| Multi-Year Discount % | `Multi_Year_Discount_Pct__c` | Percent | Opportunity | Multi-year 추가 할인 |
| Total Effective Discount | `Total_Effective_Discount__c` | Formula | Opportunity | 종합 실효 할인율 |
| Margin % | `Margin_Pct__c` | Formula | Opportunity | 마진율 |
| Competitor Price Est | `Competitor_Price_Est__c` | Currency | Opportunity | 경쟁사 추정 가격 |
| Free Months | `Free_Months__c` | Number | Opportunity | 무료 제공 월수 |
| Credit Amount | `Credit_Amount__c` | Currency | Opportunity | 크레딧 금액 |
| Is Renewal | `Is_Renewal__c` | Boolean | Opportunity | 갱신 딜 여부 |
| Previous Discount % | `Previous_Discount_Pct__c` | Percent | Opportunity | 이전 계약 할인율 |

> **Action Required**: 이 문서가 승인되면, 위 필드들을 `crm/schema.md`의 Opportunity Object 섹션에 추가해야 합니다.
