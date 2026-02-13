# Minerva Agenda (v0.1)

## 1) 프로젝트 정의
Minerva는 Affinity Equity Partners(AEP) 포트폴리오 회사들의 B2B Account 데이터를 수집/정제/재가공하고, 고객 세그먼트별로 분류한 뒤 Insight 및 영업 가능성(Scoring)까지 산출해 영업/개발 의사결정을 지원하는 프로젝트다.

## 2) 현재 목표(이슈 우선순위)
1. 포트폴리오 회사별 Account 입력 데이터 Import → AEP DB 적재
2. 정합성/클렌징 규칙 기반 데이터 정제
3. AEP가 만든 ‘고객 군 Seg’ 기준 분류
4. 계정별 적합도/영업 가능성(Scoring) 산출
5. 계정별 Needs(각 사별 요구) 기반 Export
6. 이후 실제 영업 오퍼레이션(태스크/팔로우업/활동 로그)까지 확장 가능한 웹 브라우저 UI 구성

## 3) 아키텍처 제안(우선순위 높은 버전)
- Frontend
  - React/Next.js + TypeScript + Tailwind (또는 MUI)로 대시보드/업로드/매핑/리뷰 UI 구현
  - 핵심 뷰
    - Data Ingestion: 파일 업로드/필드 매핑/중복 처리 규칙(Overwrite/Skip) 선택
    - Data Quality: 중복/누락/무의미값 표시 + 사전 정의 규칙 기반 수정/삭제
    - Segmentation/Insight: 세그먼트 분포, 히트맵, 우선순위 Top 계정
    - Scoring: 고객 적합도/영업성공 확률/Next Action
    - Export Center: 회사별 포맷/규칙으로 파일 Export
- Backend
  - FastAPI (또는 NestJS) 기반의 모듈형 API
  - 핵심 모듈
    - Ingestion Service: 파일 파서, 어댑터, 스키마 매핑, 배치 적재
    - Data Quality Service: 정규화/규칙 엔진/클렌징
    - Segmentation Service: 규칙+학습 기반 분류(초기엔 규칙 기반 우선)
    - Scoring Service: feature 계산 + 모델 파이프라인(초기엔 규칙/가중치 기반)
    - Export Service: 포맷별 템플릿 변환
- 배치 처리
  - 대량 데이터는 비동기 작업 큐(Sidekiq/Celery-like, 또는 큐 라이브러리)로 처리해 UI 블로킹 제거

## 4) 데이터 모델(1차 버전)
- 원본 Raw 단계
  - `import_batch`(원본 파일/시트/업로드 메타)
  - `account_raw`(원본 필드/원본 값 보존, 정합성 검사 이력 추적)
- 정제/정규화 단계
  - `account_master`(정제 후의 중심 엔티티)
  - `account_alias`(회사명/도메인/주소 정규화 매핑)
- 분류/점수 단계
  - `segment`(AEP Segment 정의)
  - `account_segment`(계정별 세그먼트 소속 + 근거 점수)
  - `account_scoring`(필요적합도, 영업가능성, 근거/요인 설명)
- Needs/출력 단계
  - `portfolio_company`(회사별 메타)
  - `company_need_profile`(각 회사의 타깃, 금지 조건, 우선 규칙)
  - `account_export_log`(누가 언제 어떤 형식으로 Export 했는지 감사 로그)

## 5) DB 추천
사용자 질문: PostgreSQL 추천 여부
- 결론: PostgreSQL 사용을 추천한다.
  - 이유: 관계형 스키마가 명확(고객-세그먼트-점수-이력), JSON 필드도 일부 지원, 트랜잭션/무결성, 확장성, 분석 쿼리 성능 적당
  - 추가 플러그인 고려
    - `uuid-ossp` 또는 `pgcrypto`(ID)
    - `pg_trgm`/`fuzzystrmatch`(회사명/도메인 매칭 개선)
    - `pgvector`(후속에 임베딩 기반 유사도 검색이 필요할 때)
- 초기 운영 시 초기 설정 기준
  - `postgres:15` 이상, 연결 풀링(Pooling), JSONB + 인덱스 기반 하이브리드 스키마, 이력은 감사를 위해 `created_at/updated_at/version` 필수
- 대안 검토
  - 단일 사용자/소규모 PoC: Supabase(Postgres)도 고려 가능(운영 편의성)
  - 분석 지연이 매우 크면 ClickHouse/BigQuery 연동을 2nd tier로 고려

## 6) 입력 데이터 받기 전, 웹 앱 구성에서 꼭 정해야 할 항목
- 공통
  - 기본 키(예: company_domain, 등록 이메일, 전화번호, 주소) 우선순위 및 충돌 규칙
  - 중복 처리 방식(Overwrite vs Keep Existing)
  - “쓰레기 데이터” 판정 규칙(빈도/길이/정규식/금지값)
- 세그먼트
  - Segment 기준이 정적 규칙인지, 점수 임계치 기반인지
  - Segment 변경 이력 관리 정책
- Scoring
  - 현재는 규칙 기반으로 시작(예: 산업 적합성 40, 지역성 20, 매출/직원 20, 수요 신호 20)
  - 필요할 때 ML 기반 모델로 레이어 전환
- Export
  - 회사별 필수 필드 목록 vs 선택 필드 목록
  - 파일 포맷 우선순위(CSV/Excel/API)
  - 감사 로그/수정 이력 노출 범위

## 7) “테스트를 작성하며 개발” 정책
- 모든 신규 코드에 대해 최소 1:1 유닛 테스트 작성
- 테스트 구분
  - 파서/매핑 규칙/클렌징 규칙: 단위 테스트(주요 경계값 포함)
  - 세그먼트·스코어링 함수: 계산 검증 테스트
  - API 레이어: 계약 테스트(입출력 스키마)
- CI 권장
  - PR/merge 전 테스트 게이트
  - 마이그레이션은 테스트 DB에서 실행 검증

## 8) 브랜치/버전 관리 제안
- `develop` 브랜치에서 작업 진행
- 기능 단위로 커밋(작게, 메시지 명확하게)
- 완료 후 `develop` → `main` 병합
- 현재 저장소는 기본 브랜치가 `master`이므로, 먼저 `develop` 브랜치 생성 후 진행 권장

## 9) 다음 단계(사용자 데이터 수령 후)
- 업로드 템플릿 정의(필드 매핑표)
- 데이터 품질 규칙(클렌징 룰) 확정
- Segmentation/Scoring v1 룰북 정의
- 포트폴리오별 Needs 카드 정의
- Export 템플릿 확정

---

### 요청 주신 입력 데이터가 오면 바로 다음 문서를 같이 갱신
- `raw_data_profile.md`(컬럼/타입/예시)
- `mapping_plan.md`(컬럼 매핑 및 규칙)
- `scoring_rules.md`(가중치/임계치)

### 실행 상세 설계
- `agent.md`에서 v1 실행 우선순위, 스키마 초안, 스코어링 공식, 유닛 테스트 정책을 이어서 정리함.

### Architecture 상세
- 시스템 아키텍처(컴포넌트/파이프라인/보안/배포)는 `Minerva/architecture.md`로 상세 정리됨.
