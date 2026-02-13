# Minerva Agent 실행 설계 (v1)

## 1) 이번 목표
- `agend.md`의 사업 정의를 그대로 실무 구현으로 바로 연결
- 입력 데이터가 오기 전 웹 앱의 데이터 파이프라인 뼈대를 확정
- 포맷이 바뀌어도 유지보수 가능한 모듈 구조를 먼저 고정
- 코드-테스트 동시작성 원칙 적용
- 환경 이동(로컬 → 컨테이너/운영) 대비 원칙
  - DB URL, Redis URL, 스토리지 경로, 외부 API 엔드포인트, 배치 batch size, feature flag는 하드코딩 금지
  - 설정은 `.env`/`pydantic Settings`/런타임 설정으로만 주입
  - 포트/호스트/타임아웃/로그 레벨도 env로만 제어
  - 경로는 앱 기준 상대경로+환경변수 조합으로 관리(절대 경로 하드코딩 금지)
  - 테스트에서도 같은 규칙 적용: fixture는 test env 설정을 사용해 격리

## 2) 권장 기술 스택 (MVP)
- Frontend: Next.js + TypeScript + Tailwind + TanStack Query
- Backend: FastAPI (Python)
- DB: PostgreSQL 15+
- Background Job: FastAPI BackgroundTasks + DB 기반 간이 큐
- Object Store: 로컬 파일시스템(필요 시 Docker에서 바인드 볼륨)
- Auth: 회사/포트폴리오 권한 기준 JWT 기반
- 확장(후속): Redis/Celery, S3호환 스토리지(선택)

## 3) PostgreSQL 추천 결론
- 이유
  - 정합성(외래키/트랜잭션) 요구가 강한 B2B 계정 데이터에 적합
  - JSONB + 관계형 모델 동시 사용 가능
  - 유사 문자열/중복 처리 성능을 위한 인덱스 확장(Trigram) 지원
- 추천 기본 확장
  - `uuid-ossp` 또는 `pgcrypto`
  - `pg_trgm` + `btree_gin`
- 초기 운영 가이드
  - 인덱스: `domain`, `account_id`, `segment_id`, `updated_at` 중심
  - 감사성: 모든 업데이트는 변경 이력 트리거로 감사 로그 기록

## 4) 핵심 스키마(초안)
- `portfolio_company`
- `company_need_profile`
- `import_batch`
- `account_raw`
- `account_clean`
- `account_profile_map`(회사명/도메인/주소 정규화)
- `segment_definition`
- `segment_assignment`
- `scoring_rule_set`
- `account_score`
- `export_request`
- `export_file`
- `audit_event`

운영 정책
- 입력은 원본을 `account_raw`에 영구 보관
- 정제 결과는 `account_clean`에 버전으로 기록
- 스코어 계산은 `account_score` 스냅샷 단위
- 모든 배치 작업은 `import_batch`와 연결된 감사 로그 존재

## 5) 파이프라인 설계 (데이터 흐름)
1) 파일 업로드
- 포맷 확인(CSV/XLSX), 행 수/컬럼 수/인코딩 체크
2) 매핑 단계
- 필수 컬럼: company_name, country/region, industry
- 선택 컬럼: revenue, employee_count, website, domain, address, contact_name, contact_email, created_at
3) 정합성 검증
- 필수 컬럼 누락 시 업로드 블록
- 이메일, 도메인, 전화번호 정규화
4) 정제 단계
- 쓰레기값 제거(길이/패턴/휴면 키워드)
- 중복 후보 탐지(회사명 유사도 + 도메인 + 주소)
- 충돌 정책: overwrite, keep_existing, keep_latest 3-way
5) 세그먼트 할당
- Segment 규칙(rule_set) 우선 적용
6) 스코어 계산
- needs_weighted_score
- urgency_score
- match_score
- 최종 가중치 산출
7) Export 생성
- 요청 포맷별 템플릿으로 변환
- 결과물 메타 저장 후 다운로드 URL 생성

## 6) 스코어링 v1 기본 공식
- 기본 점수 = `industry_fit * 0.4 + region_match * 0.2 + growth_signal * 0.15 + data_quality * 0.1 + engagement_signal * 0.15`
- `industry_fit`: 포트폴리오 프로필과 산업 매칭
- `region_match`: 지역/국가 우선순위 매칭
- `growth_signal`: 매출/인력 추세 가용 시 반영
- `data_quality`: 필수필드 완성도, 형식 정합성
- `engagement_signal`: 기존 활동 데이터 연동 시 사용
- 출력값은 0~100, 추천 액션 레이어를 함께 저장(`hot/warm/cold`)

## 7) 유닛 테스트 정책 (엄수)
- Ingestion
  - csv/xlsx 파서 정상/오류 케이스
  - 필드 타입 변환(날짜, 숫자, 전화번호)
- Cleaning
  - 쓰레기값 필터링 규칙 경계값
  - 중복 후보 탐지 일치율 임계치
- Segmentation
- Scoring
  - 각 규칙별/가중치별 기대값
- Export
  - 템플릿 매핑 누락/순번 보존
- API
  - 계약 테스트(요청/응답 JSON 스키마)
- 최소 커버리지: 핵심 비즈니스 로직 80% 이상
- 테스트 위치: `tests/unit`, `tests/integration`

## 8) 폴더 구조 제안
- `api/`: FastAPI 앱 엔트리
- `api/services/ingestion.py`
- `api/services/cleaning.py`
- `api/services/segmentation.py`
- `api/services/scoring.py`
- `api/services/export.py`
- `api/models/`: SQLAlchemy 모델
- `api/schemas/`: Pydantic DTO
- `api/workers/`: 배치 작업 실행
- `web/`: Next.js pages/components
- `web/components/data/`: 업로드/맵핑/검증/스코어 뷰
- `web/components/exports/`: export 생성/요청/이력
- `tests/`: 핵심 규칙별 단위 테스트

## 9) 실행 순서(다음 커밋부터 바로)
1) `agend.md`를 바탕으로 `agent.md` 요구사항 freeze
2) FastAPI 엔드포인트 스켈레톤 + Ingestion DTO + 테스트
3) DB 마이그레이션 v1 생성 + 모델 테스트
4) 정제/스코어링 rule engine 추가 + 계약 테스트
5) Next.js 업로드 화면 + 정합성 결과 뷰
6) Export API + 다운로드 흐름
7) CI에 테스트 게이트 추가

## 10) 데이터가 도착했을 때 바로 할 일
- `raw_data_profile.md` 생성: 컬럼 목록, 타입, 샘플
- `agent.md`의 "필드 매핑" 파트를 실제 파일 기준으로 교체
- `segment_definition` 규칙값 고정
- `scoring_rule_set` v1 가중치 확정
- 포트폴리오별 export 템플릿 YAML 등록

## 11) git 운영
- 브랜치: `develop` 단일 feature 흐름
- 작업 단위 커밋: 문서/스키마/API/프론트 각 1개씩 분리
- 완료 후 `develop` → `main` 병합

### Architecture 상세 연동
- 실행 상세와 분리한 전체 시스템 아키텍처는 `Minerva/architecture.md`를 참조한다.
