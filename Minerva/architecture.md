# Minerva Architecture (v1)

## 0. MacBook Air self-host 기준(권장)
- 목표: 로컬 단일 장비에서 부팅만 하면 동작, 오픈소스, 유료 서비스 의존 최소화
- 권장 스택
  - PostgreSQL (로컬 설치 또는 Docker)
  - FastAPI (API + 간단한 백그라운드 작업)
  - Next.js (또는 Vite + React) 웹 UI
  - 로컬 파일시스템 업로드/Export 저장소
  - Python venv/uv + 단일 프로세스 개발
- 제외 항목(v1)
  - Redis, RQ/Celery, 분산 워커
  - S3/클라우드 오브젝트 스토리지
  - 별도 모니터링 스택
- 처리 방식
  - 작은 배치는 동기 처리 또는 비동기 background task로 즉시 응답
  - 큰 배치는 job queue를 DB에 간이 적재한 뒤 폴링으로 상태 조회
- 확장 전환
  - 필요 시 Redis+RQ, MinIO, 모니터링(로그/메트릭)을 단계적으로 추가

## 1. 한 줄 설계 목표
`Minerva`는 포트폴리오 B2B Account 데이터를 안정적으로 수집·정제·세분화·점수화하고, 포트폴리오 회사별 니즈에 맞춰 Export까지 자동화하는 플랫폼이다.

## 2. 시스템 경계
- Web UI (Next.js)
- API/서비스 (FastAPI)
- DB (PostgreSQL)
- 로컬 파일시스템 스토리지 (임시/영구 업로드/Export 파일)
- 인증/권한 (JWT + RBAC)

## 3. 논리 아키텍처
```mermaid
flowchart LR
  U[사용자/운영자] --> UI[Next.js Browser UI]
  UI --> API[FastAPI API]
  API --> UP[Upload Service]
  UP --> FS[Local File Storage]
  UP --> RB[Raw Data Ingestion + Parse]
  RB --> RDB[(PostgreSQL)]

  API --> W[Background Task (FastAPI)

  W --> CLEAN[Cleaning Service]
  W --> SEG[Segmentation Service]
  W --> SCORE[Scoring Service]
  W --> EXP[Export Service]

  CLEAN --> RDB
  SEG --> RDB
  SCORE --> RDB
  EXP --> FS
  EXP --> API

  API --> AUD[Audit & Event Log]
  AUD --> RDB
```

## 4. 데이터 파이프라인
- Stage 0 (Ingest)
  - 파일 업로드 후 raw 파일을 로컬 저장소에 보관 + `import_batch` 레코드 생성
  - 파일 메타: 포맷, 행 수, 업로더, 대상 포트폴리오
- Stage 1 (Parse/Normalize)
  - XLSX/CSV를 canonical row로 변환
  - 컬럼 자동 추론 + 사용자 매핑 템플릿 적용
- Stage 2 (Validation)
  - 필수값, 타입, 범주, 정규식 검증
  - 실패 행은 reason과 함께 리포트
- Stage 3 (Cleaning)
  - 쓰레기값 제거/보정
  - 중복 탐지(Exact + 유사도), 충돌 처리(Overwrite / Keep Latest / Skip)
- Stage 4 (Enrichment & Segment)
  - 회사명 정규화, 도메인 추출, 주소 정규화
  - Segment Rule 적용 + 근거 로그 저장
- Stage 5 (Scoring)
  - 규칙 가중치 기반 score 계산 + explainability 저장
  - 우선순위 큐(테이블 단위) 반영
- Stage 6 (Export)
  - 포트폴리오별 템플릿으로 필터링/정렬/포맷팅
  - 생성 파일 hash와 파라미터 포함해 저장

## 5. 핵심 컴포넌트 책임
- API Gateway
  - 인증, 권한, 요청 검증, 트랜잭션/오류 핸들링
- Ingestion Service
  - 파일 업로드, 파싱, 배치 생성
- Cleaning Service
  - 규칙 엔진, 클렌징 룰 버전 관리
- Segmentation Service
  - 규칙 기반 분류, 후속 ML 인터페이스(확장용)
- Scoring Service
  - 수치형 스코어 및 `hot/warm/cold` 산출
- Export Service
  - 템플릿 렌더링/포맷 변환/다운로드 URL 발급
- Audit Service
  - 이벤트 로그, 사용자 활동 이력 저장

## 6. 이벤트/오류 처리
- 동시성 제어: 업로드 배치 단위 락 + idempotent job key
- 실패 정책: 재시도 3회 + 오류 테이블에 DLQ 대체 저장
- 상태 모델: `PENDING/RUNNING/VALIDATING/CLEANING/SCORING/EXPORT/DONE/FAILED`
- 트랜잭션 경계: `account_raw` insert + `import_batch` 상태 전환을 단일 흐름으로 관리

## 7. 보안/권한
- 회사/포트폴리오 단위 데이터 격리: `portfolio_company_id` 기반 정책
- 감사: 수정·삭제·Export은 actor/시간/사유 기록
- 비밀값은 환경변수(`.env`) 또는 Vault 대체로 로컬 키 관리
- 업로드 파일 정책 및 업로드 크기 제한

## 8. 성능/스케일 (로컬 기준)
- 행 10만 이하: 단일 인스턴스 동작 가능
- 대량 업로드 시 chunk 단위 처리(예: 5k~20k)
- 동기 미리보기 + 전체 비동기 검증 분리
- Postgres 인덱스 우선순위
  - `(portfolio_company_id, domain)`
  - `(segment_id, score_bucket)`
  - `(account_status, created_at)`

## 9. 배포 아키텍처(초기)
- 추천: Docker Compose(개발/테스트), 이후 `uvicorn + next dev/build` 단일 머신 실행
- 서비스 구성
  - web:3000
  - api:8000
  - postgres:5432
- 단일 repo에서 시작 후 확장 시 모듈 분리

## 10. CI/CD 및 테스트 전략
- Pipeline
  - lint + unit test + migration test + 간단한 API 계약 테스트
- 문서-코드 동기화
  - architecture/agent/agend 변경 시 PR 템플릿에서 동기화 체크
- 배포 전 점검
  - 업로드 샘플 3종: 정상/누락컬럼/중복 데이터
  - export 샘플 2종: CSV/Excel

## 11. 단계적 확장
- v1: 규칙 기반 + 로컬 저장
- v2: Redis/RQ, MinIO, 캐시 도입
- v3: 분산 worker + ML scoring
- v4: 계정 활동 로그(콜/미팅) 결합 예측 점수
