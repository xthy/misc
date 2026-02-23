# Tech Stack Comparison: B2B Sales Agent PoC
## Agent PoC 기술 스택 비교 분석

> **작성일**: 2026-02-14
> **목적**: B2B Sales Agent PoC(Phase 4) 진입을 위한 기술 스택 선정 근거 문서
> **범위**: Workflow Orchestration, Agent Framework, Vector DB, Monitoring
> **참조**: `agent.md` (BCG 5-Agent Model), `scope.md` (Phase 4 요구사항), `crm/schema.md` (CRM API 연동 스펙)

---

## 목차

1. [평가 기준 (Evaluation Criteria)](#1-평가-기준-evaluation-criteria)
2. [Workflow Orchestration 비교: n8n vs Zapier vs Make](#2-workflow-orchestration-비교-n8n-vs-zapier-vs-make)
3. [Agent Framework 비교: LangChain vs CrewAI vs AutoGen vs OpenAI Assistants vs Claude Tool Use](#3-agent-framework-비교)
4. [Combined Architecture Options](#4-combined-architecture-options)
5. [Vector DB 비교: pgvector vs Pinecone vs Weaviate vs Chroma](#5-vector-db-비교)
6. [Monitoring 비교: LangSmith vs Helicone vs Langfuse](#6-monitoring-비교)
7. [최종 추천 (Final Recommendation)](#7-최종-추천-final-recommendation)

---

## 1. 평가 기준 (Evaluation Criteria)

본 프로젝트의 핵심 요구사항을 기반으로 11개 평가 기준을 정의하고, 프로젝트 특성에 맞게 가중치를 부여했다.

### 프로젝트 핵심 요구사항 (from `scope.md` Phase 4)

- **Agent PoC #1**: Post-Call CRM Updater (Call transcript → MEDDICC 추출 → CRM 업데이트)
- **Agent PoC #2**: Weekly Ops Report (Pipeline 분석, Stalled deal, Forecast)
- **Agent PoC #3**: Lead Enrichment + ICP Scorer
- **Playbook RAG**: 벡터화된 Playbook 참조 기능
- **5-Agent Model**: BCG 기반 Orchestration + 5 Sub-agent 구조
- **Tier-based Autonomy**: T1 Human-led / T2 Co-pilot / T3 AI-led

### 평가 기준 및 가중치

| # | 기준 | 가중치 | 근거 |
|---|------|--------|------|
| 1 | **Setup 용이성 / Learning Curve** | 15% | PoC는 빠른 검증이 핵심. 복잡한 셋업은 Phase 4의 5개월 타임라인을 위협 |
| 2 | **LLM Integration** (Claude, GPT-4 등) | 15% | Agent의 핵심 두뇌. Multi-LLM 지원 여부가 vendor lock-in 방지에 중요 |
| 3 | **CRM Integration** (Salesforce, HubSpot API) | 12% | CRM-native 원칙(`agent.md` Design Principle #2). Shadow DB 없이 직접 연동 필수 |
| 4 | **Workflow Orchestration** | 10% | Trigger → Action 파이프라인. 7-stage Canon의 자동화 흐름 지원 |
| 5 | **Multi-Agent Support** | 10% | BCG 5-Agent 모델 구현. Agent 간 handoff, 상태 공유, 역할 분리 |
| 6 | **RAG / Vector DB Integration** | 8% | Playbook RAG store 구축. `scope.md` Step 11 |
| 7 | **Self-Hosting Option** | 8% | PE portfolio 배포 시 portability. 고객 데이터 주권. `agent.md` Principle #6 |
| 8 | **Cost at Scale** (100+ accounts, 5 agents) | 8% | PE Ops VP 예산 승인. LLM 호출 비용 최적화 |
| 9 | **Community / Ecosystem** | 5% | 문제 해결 속도, 플러그인/커넥터 가용성 |
| 10 | **Monitoring / Observability** | 5% | Agent 행동 추적, 비용 모니터링. `scope.md` Risk "LLM cost at scale" 대응 |
| 11 | **Production Readiness** | 4% | PoC → Production 전환 시 재구축 비용 최소화 |

### 점수 체계

- **5**: 탁월 (Best-in-class, 추가 작업 없이 즉시 사용 가능)
- **4**: 우수 (약간의 설정으로 충분)
- **3**: 보통 (작동하지만 커스텀 작업 필요)
- **2**: 부족 (상당한 workaround 필요)
- **1**: 미지원 (해당 기능 없음 또는 사실상 사용 불가)

---

## 2. Workflow Orchestration 비교: n8n vs Zapier vs Make

### 2.1 n8n

**Architecture Overview**

n8n은 오픈소스 workflow automation 플랫폼으로, node 기반의 visual flow builder를 제공한다. Self-hosted와 Cloud 두 가지 옵션이 있으며, 각 workflow는 trigger → action 체인으로 구성된다.

```
┌─────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Trigger  │───▶│ LLM Node │───▶│CRM Write │───▶│  Output  │
│(Webhook/ │    │(Claude/  │    │(Salesforce│    │(Email/   │
│ Schedule)│    │ GPT-4)   │    │ /HubSpot)│    │ Slack)   │
└─────────┘    └──────────┘    └──────────┘    └──────────┘
```

**AI/LLM Native Features (2025 기준)**

- **AI Agent Node**: LangChain 기반 Agent node 내장. Tool 정의, memory, chain 구성 가능
- **LLM 지원**: OpenAI, Anthropic Claude, Google Gemini, Ollama (로컬 LLM), Azure OpenAI
- **Vector Store Node**: Pinecone, Qdrant, Supabase, Zep 연결 가능
- **Document Loaders**: PDF, Google Docs, Notion 등에서 문서 로딩
- **Text Splitters**: Recursive, Token-based 청킹 지원
- **Memory**: Window Buffer, Zep, Motorhead 등 대화 기록 관리
- **Sub-workflow**: 워크플로우 안에서 다른 워크플로우 호출 가능 (Agent 간 분리에 활용)

**CRM Connectors**

- Salesforce: OAuth2 연결, CRUD + SOQL 쿼리 지원
- HubSpot: 공식 노드. Contact, Deal, Company, Ticket 전 오브젝트 지원
- HTTP Request 노드로 커스텀 API 호출도 가능

**Pricing**

| Plan | 가격 | 주요 제한 |
|------|------|----------|
| Self-hosted (Community) | 무료 | 무제한 워크플로우, 무제한 실행 |
| Self-hosted (Enterprise) | 문의 | SSO, LDAP, Audit log |
| Cloud Starter | $24/mo | 2,500 실행/월 |
| Cloud Pro | $60/mo | 10,000 실행/월 |
| Cloud Enterprise | 문의 | 무제한 실행, 전용 인프라 |

**Strengths**

- Self-hosted 시 실행 비용 거의 제로 (LLM API 비용만 별도)
- AI Agent node가 내장되어 별도 Agent framework 없이도 기본적인 Agent 구축 가능
- Visual builder로 비개발자도 workflow 수정 가능 — PE portfolio 배포 시 유리
- 400+ integration nodes (CRM, Email, Slack, Google Sheets 등)
- JavaScript/Python 코드 노드로 커스텀 로직 삽입 가능

**Weaknesses**

- Multi-agent orchestration은 sub-workflow로 우회해야 함 (native 지원 아님)
- 복잡한 Agent 간 state 공유는 외부 DB(Redis 등)가 필요
- AI Agent node의 디버깅 UI가 아직 제한적
- Self-hosting 시 인프라 관리 부담 (Docker, DB, 백업 등)

**Best Use Case**: PoC 단계에서 빠른 구축. Webhook → LLM → CRM 파이프라인. T3 자동화 워크플로우.

---

### 2.2 Zapier

**Architecture Overview**

Zapier는 클라우드 전용 iPaaS(Integration Platform as a Service)로, "Zap"이라 불리는 trigger-action 자동화를 제공한다. 2024년부터 AI 기능을 강화하며 "Central" (AI Orchestration hub)을 출시했다.

```
┌─────────┐    ┌──────────┐    ┌──────────┐
│ Trigger  │───▶│ Action 1 │───▶│ Action 2 │
│(CRM event│    │(AI by    │    │(CRM      │
│ /webhook)│    │ Zapier)  │    │ update)  │
└─────────┘    └──────────┘    └──────────┘
```

**AI/LLM Native Features**

- **AI by Zapier**: GPT-4 기반 텍스트 생성, 요약, 분류 등 기본 AI 작업
- **Zapier Central** (2024~): AI agent hub. 자연어 명령으로 자동화 생성/실행
- **Chatbot builder**: 웹사이트 임베드용 AI 챗봇
- Anthropic Claude 직접 지원은 제한적 (API connector로 우회 가능)

**CRM Connectors**

- Salesforce: 공식 integration. 주요 오브젝트 CRUD 지원
- HubSpot: 공식 integration. 매우 성숙한 연동
- 7,000+ 앱 연동 — 생태계 최대 규모

**Pricing**

| Plan | 가격 | 주요 제한 |
|------|------|----------|
| Free | $0 | 100 tasks/월, 5 Zaps |
| Professional | $29.99/mo | 750 tasks/월 |
| Team | $103.50/mo | 2,000 tasks/월 |
| Enterprise | 문의 | 무제한, SSO, 전용 지원 |

> **주의**: Zapier의 "task"는 각 action step을 개별 카운트. 5-step Zap이 1회 실행되면 5 tasks 소비.

**Strengths**

- 7,000+ 앱 연동 — 어떤 CRM이든 즉시 연결 가능
- No-code 환경 — 기술 배경 없는 팀도 사용 가능
- Zapier Central로 AI agent 방향 진화 중
- 안정성과 가동 시간 검증됨

**Weaknesses**

- **Self-hosting 불가** — PE portfolio별 데이터 격리 어려움
- Task 기반 과금 — Agent가 100+ account 대상 반복 실행 시 비용 급등
- 복잡한 branching/looping 로직에 제한
- LLM 선택 자유도 낮음 (GPT 중심, Claude 직접 지원 부족)
- Agent framework 수준의 reasoning/planning 기능 없음

**Best Use Case**: 단순한 CRM ↔ 이메일 ↔ Slack 알림 자동화. 비개발 팀의 초기 자동화.

---

### 2.3 Make (구 Integromat)

**Architecture Overview**

Make는 visual automation 플랫폼으로, Zapier보다 복잡한 분기/병렬 처리를 지원하는 "시나리오" 기반 워크플로우 빌더다.

```
┌─────────┐    ┌──────────┐───▶┌──────────┐
│ Trigger  │───▶│ Router   │    │ Branch A │
│          │    │(조건분기) │───▶│ Branch B │
└─────────┘    └──────────┘───▶│ Branch C │
                               └──────────┘
```

**AI/LLM Native Features**

- **OpenAI 모듈**: GPT-4 호출 공식 지원
- **Anthropic 모듈**: Claude API 직접 호출 가능 (2024년 추가)
- HTTP 모듈로 어떤 LLM API든 연결 가능
- AI Agent 전용 노드는 아직 없음 (n8n 대비 열세)

**CRM Connectors**

- Salesforce: 공식 모듈, 전 오브젝트 지원
- HubSpot: 공식 모듈, 성숙한 연동
- 2,000+ 앱 연동

**Pricing**

| Plan | 가격 | 주요 제한 |
|------|------|----------|
| Free | $0 | 1,000 ops/월, 2 시나리오 |
| Core | $10.59/mo | 10,000 ops/월 |
| Pro | $18.82/mo | 10,000 ops/월, 우선 실행 |
| Teams | $34.12/mo | 10,000 ops/월, 팀 기능 |
| Enterprise | 문의 | 커스텀 |

> Make의 "operation"은 Zapier의 "task"와 유사하지만, 단순 데이터 통과는 카운트하지 않아 일반적으로 더 효율적.

**Strengths**

- 복잡한 분기/병렬 처리가 visual builder로 가능
- Zapier보다 유연한 데이터 매핑과 변환
- Operation 기반 과금이 Zapier task보다 효율적
- Error handling과 retry 로직이 잘 설계됨

**Weaknesses**

- **Self-hosting 불가** (n8n과의 핵심 차이)
- AI Agent node 부재 — LLM 호출은 가능하나 Agent 수준의 reasoning loop 없음
- Multi-agent orchestration 지원 없음
- 커뮤니티 규모가 n8n이나 Zapier보다 작음

**Best Use Case**: 복잡한 조건 분기가 필요한 CRM 자동화. Zapier보다 정교한 로직이 필요하지만 self-hosting은 불필요한 경우.

---

### 2.4 Workflow Orchestration 종합 비교

| 기준 | n8n | Zapier | Make |
|------|-----|--------|------|
| **AI Agent 내장** | O (LangChain 기반) | 제한적 (Central) | X |
| **LLM 선택 자유도** | Claude, GPT-4, Gemini, Ollama | GPT 중심 | Claude, GPT-4 |
| **CRM 연동** | SF + HS 공식 노드 | 7,000+ 앱 | SF + HS 공식 모듈 |
| **Self-Hosting** | O (Docker, npm) | X | X |
| **과금 모델** | Self-host: 무료 / Cloud: 실행 기반 | Task 기반 (비쌈) | Op 기반 (중간) |
| **분기/병렬 처리** | 중간 | 제한적 | 우수 |
| **코드 노드** | JS + Python | 제한적 JS | JS |
| **Vector Store 연동** | 내장 | X | X |
| **디버깅** | 중간 | 기본 | 우수 |
| **학습 곡선** | 중간 (개발자 친화) | 낮음 | 중간 |

### 가중 점수 비교

| 평가 기준 (가중치) | n8n | Zapier | Make |
|-------------------|-----|--------|------|
| Setup 용이성 (15%) | 3 | 5 | 4 |
| LLM Integration (15%) | 5 | 3 | 4 |
| CRM Integration (12%) | 4 | 5 | 4 |
| Workflow Orchestration (10%) | 4 | 3 | 5 |
| Multi-Agent (10%) | 3 | 1 | 1 |
| RAG/Vector DB (8%) | 4 | 1 | 1 |
| Self-Hosting (8%) | 5 | 1 | 1 |
| Cost at Scale (8%) | 5 | 2 | 3 |
| Community (5%) | 4 | 5 | 3 |
| Monitoring (5%) | 3 | 3 | 3 |
| Production Readiness (4%) | 4 | 5 | 4 |
| **가중 합계** | **3.93** | **3.00** | **2.97** |

**결론**: n8n이 본 프로젝트에 가장 적합. Self-hosting + AI Agent 내장 + Vector Store 연동이 핵심 차별점. Zapier는 비용과 self-hosting 부재로 PE portfolio 배포에 부적합.

---

## 3. Agent Framework 비교

### 3.1 LangChain / LangGraph

**Architecture and Approach**

LangChain은 LLM 애플리케이션 구축을 위한 가장 널리 사용되는 Python/JS 프레임워크다. 2024년 후반부터 LangGraph를 통해 stateful, multi-actor 워크플로우를 지원하며, Agent 아키텍처의 표준으로 자리잡고 있다.

```
┌─────────────────────────────────────────────┐
│                 LangGraph                    │
│  ┌──────┐    ┌──────┐    ┌──────┐          │
│  │State │───▶│Node 1│───▶│Node 2│──▶ ...   │
│  │Graph │    │(Agent│    │(Tool │          │
│  │      │    │ step)│    │ call)│          │
│  └──────┘    └──────┘    └──────┘          │
│       ▲                        │            │
│       └────────────────────────┘            │
│              (conditional edges)             │
└─────────────────────────────────────────────┘
```

- **Core**: LLM 호출, prompt template, output parser, chain 구성
- **LangGraph**: 그래프 기반 Agent 워크플로우. 상태 머신, 조건부 분기, 순환 가능
- **LangServe**: Agent를 REST API로 배포
- **LangSmith**: 트레이싱, 평가, 모니터링 (유료 SaaS)

**Multi-Agent Support**

- LangGraph의 `StateGraph`로 여러 Agent를 노드로 정의하고 조건부 라우팅 가능
- Supervisor pattern: 하나의 orchestrator가 sub-agent를 호출하는 구조 지원
- 각 Agent에 독립적인 tool set, prompt, memory 할당 가능
- `langgraph-supervisor` 패키지로 multi-agent 패턴 간편 구현

**Tool Use / Function Calling**

- OpenAI, Anthropic, Google 등 주요 LLM의 function calling 지원
- `@tool` 데코레이터로 Python 함수를 tool로 정의
- Structured output으로 CRM 필드 매핑에 유리
- CRM API 호출을 tool로 감싸서 Agent가 직접 읽기/쓰기 가능

**Memory Management**

- `ConversationBufferMemory`, `ConversationSummaryMemory` 등 다양한 memory 클래스
- LangGraph에서는 `State` 객체가 워크플로우 전체의 공유 메모리 역할
- Checkpointing으로 장기 실행 워크플로우의 상태 저장/복원
- 외부 메모리 (Redis, PostgreSQL) 연동 가능

**RAG Support**

- `Document Loaders` → `Text Splitters` → `Embeddings` → `Vector Stores` 전체 파이프라인 지원
- 20+ vector store 연동 (pgvector, Pinecone, Weaviate, Chroma, FAISS 등)
- `RetrievalQA`, `ConversationalRetrievalChain` 등 RAG 패턴 내장
- Hybrid search (dense + sparse) 지원

**Production Readiness**

- 가장 큰 커뮤니티 (GitHub 100k+ stars, npm/PyPI 수백만 다운로드)
- LangServe로 API 배포, LangSmith로 모니터링
- 대규모 production 사례 다수 (기업용 RAG, Agent 시스템)
- 다만 API 변경이 잦아 버전 관리에 주의 필요

**Strengths**

- 가장 넓은 생태계와 통합 옵션
- LangGraph가 multi-agent 패턴을 명시적으로 지원
- LLM 선택 자유도 최고 (모든 주요 provider 지원)
- RAG 파이프라인 구축에 가장 성숙
- 문서와 튜토리얼 풍부

**Weaknesses**

- Learning curve가 높음 — 추상화 레이어가 많아 디버깅 복잡
- Abstraction overhead — 단순한 작업에도 코드가 장황해질 수 있음
- API breaking changes가 잦음 (빠른 진화의 대가)
- LangSmith 의존성 (모니터링에 유료 SaaS 필요)

---

### 3.2 CrewAI

**Architecture and Approach**

CrewAI는 multi-agent orchestration에 특화된 프레임워크로, "팀" 메타포를 사용한다. 각 Agent에게 Role, Goal, Backstory를 부여하고, Task를 할당하면 Agent들이 협업하여 결과를 산출한다.

```
┌─────────────────────────────────────────────┐
│                   Crew                       │
│                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │  Agent 1  │  │  Agent 2  │  │  Agent 3  │  │
│  │ Role: SDR │  │ Role: AE  │  │ Role: CS  │  │
│  │ Tools: [] │  │ Tools: [] │  │ Tools: [] │  │
│  └─────┬────┘  └─────┬────┘  └─────┬────┘  │
│        │             │             │        │
│  ┌─────▼────┐  ┌─────▼────┐  ┌─────▼────┐  │
│  │  Task 1   │  │  Task 2   │  │  Task 3   │  │
│  │(Research) │  │(Qualify)  │  │(Follow-up)│  │
│  └──────────┘  └──────────┘  └──────────┘  │
│                                              │
│  Process: Sequential / Hierarchical          │
└─────────────────────────────────────────────┘
```

- **Agent**: Role + Goal + Backstory + Tools로 정의
- **Task**: 각 Agent에게 할당되는 구체적 작업
- **Crew**: Agent + Task의 조합. Sequential 또는 Hierarchical 실행
- **Process**: Sequential (순차), Hierarchical (매니저 Agent가 위임)

**Multi-Agent Support**

- **Native multi-agent**: 프레임워크의 핵심 설계 철학
- **Hierarchical process**: Manager Agent가 자동으로 task 위임 — BCG Orchestration Agent에 적합
- **Agent delegation**: Agent가 다른 Agent에게 작업 위임 가능
- **Agent 간 context 전달**: Task output이 다음 Agent의 input으로 자동 연결

**Tool Use / Function Calling**

- `@tool` 데코레이터로 커스텀 tool 정의
- LangChain tool과 호환 (LangChain 생태계의 tool 재사용 가능)
- `SerperDevTool`, `ScrapeWebsiteTool` 등 내장 tool 제공
- CRM API tool을 커스텀으로 만들어 각 Agent에 배분 가능

**Memory Management**

- Short-term memory: Crew 실행 내 Agent 간 컨텍스트 공유
- Long-term memory: 이전 Crew 실행 결과 참조 (SQLite 기반)
- Entity memory: 특정 엔티티(Account, Contact 등) 관련 기억
- 2025년 기준 memory 기능이 빠르게 발전 중이나 LangGraph보다는 미성숙

**RAG Support**

- `RagTool`로 문서 RAG 가능
- LangChain의 vector store 연동을 그대로 활용
- Embeddings와 retrieval은 LangChain에 의존

**Production Readiness**

- GitHub 25k+ stars (2025 기준), 빠르게 성장 중
- CrewAI Enterprise (유료) 출시 — 관리 UI, 배포, 모니터링 제공
- Production 사례 증가 중이나 LangChain 대비 아직 초기 단계
- API 안정성은 LangChain보다 양호 (더 젊은 프로젝트, 설계가 명확)

**Strengths**

- **BCG 5-Agent 모델과 개념적 1:1 매핑**: Role-based agent 정의가 우리 설계와 직접 대응
- Multi-agent가 핵심 기능 — 별도 설계 없이 즉시 사용
- Hierarchical process = Orchestration Agent 패턴
- LangChain보다 코드가 간결하고 직관적
- 빠른 프로토타이핑에 유리

**Weaknesses**

- 복잡한 조건부 라우팅은 LangGraph보다 제한적
- Production 사례와 문서가 LangChain보다 적음
- Memory와 state management가 아직 발전 중
- Enterprise 기능(모니터링, 배포)은 유료
- LLM 호출 횟수가 많아질 수 있음 (Agent delegation 시)

---

### 3.3 Microsoft AutoGen

**Architecture and Approach**

AutoGen은 Microsoft Research에서 개발한 multi-agent conversation 프레임워크다. Agent 간 대화(conversation)를 통해 문제를 해결하는 패턴에 특화되어 있다. 2024년 말 AutoGen v0.4로 대규모 리팩토링을 거쳤다.

```
┌─────────────────────────────────────────────┐
│            Agent Conversation                │
│                                              │
│  ┌──────────┐  ◀─── message ───▶ ┌────────┐ │
│  │ Assistant │                    │  User  │ │
│  │  Agent    │  ◀─── message ───▶│ Proxy  │ │
│  └──────────┘                    └────────┘ │
│       │                                      │
│       ▼                                      │
│  ┌──────────┐                               │
│  │  Code    │  (자동 코드 생성 + 실행)        │
│  │ Executor │                               │
│  └──────────┘                               │
└─────────────────────────────────────────────┘
```

- **ConversableAgent**: 모든 Agent의 베이스 클래스. 메시지 송수신 기능
- **AssistantAgent**: LLM 기반 추론 Agent
- **UserProxyAgent**: 사용자 입력 또는 코드 실행 대리
- **GroupChat**: 3+ Agent가 참여하는 그룹 대화

**Multi-Agent Support**

- GroupChat으로 여러 Agent가 자유롭게 대화
- Speaker selection: round-robin, random, LLM-based 선택 가능
- 자동 코드 생성 + 실행 (sandbox 내 Python/shell)
- v0.4에서 `AgentChat` 레이어 추가 — 더 유연한 multi-agent 패턴

**Tool Use / Function Calling**

- `register_for_llm`과 `register_for_execution`으로 tool 등록
- 코드 실행 기반 tool use (Python 코드를 생성하여 실행)
- Function calling 지원 (OpenAI, Anthropic)

**Memory Management**

- 대화 기록이 자연스럽게 context로 전달
- Teachable agent: 이전 대화에서 학습한 내용을 저장
- 장기 메모리는 외부 DB 연동 필요

**RAG Support**

- `RetrieveAssistantAgent`로 RAG 지원
- 문서 청킹, 임베딩, 검색 파이프라인 내장
- ChromaDB 기본 통합

**Production Readiness**

- GitHub 40k+ stars
- Microsoft 지원 — 장기 유지보수 기대 가능
- v0.4 대규모 리팩토링으로 API 불안정 시기
- Azure OpenAI 통합이 강점이나, Claude 사용 시 이점 감소
- Enterprise production 사례는 주로 Microsoft 에코시스템 내

**Strengths**

- 코드 생성 + 자동 실행 패턴이 강력 (데이터 분석에 유리)
- Microsoft 생태계(Azure, Teams) 통합
- 대화 기반 Agent 상호작용이 자연스러움
- 복잡한 reasoning task에 강점

**Weaknesses**

- **CRM 연동은 직접 구현 필요** — 내장 CRM connector 없음
- v0.4 마이그레이션으로 학습 자료 혼선 (v0.2 vs v0.4)
- B2B Sales 도메인 특화 기능 없음
- Azure OpenAI 중심 설계 — Claude 사용 시 이점 반감
- Workflow orchestration 기능 없음 (cron, webhook trigger 등)

---

### 3.4 OpenAI Assistants API

**Architecture and Approach**

OpenAI Assistants API는 OpenAI가 제공하는 managed agent 서비스다. 서버 측에서 thread 관리, tool 실행, file 검색을 처리한다.

```
┌─────────────────────────────────────────────┐
│              OpenAI Platform                 │
│                                              │
│  ┌──────────┐    ┌──────────┐              │
│  │ Assistant │───▶│  Thread  │              │
│  │ (GPT-4)  │    │ (State)  │              │
│  │ + Tools  │    │ + Files  │              │
│  └──────────┘    └──────────┘              │
│       │                                      │
│       ▼                                      │
│  ┌──────────┐    ┌──────────┐              │
│  │ Code     │    │  File    │              │
│  │Interpreter│   │ Search   │              │
│  └──────────┘    └──────────┘              │
└─────────────────────────────────────────────┘
```

- **Assistant**: System prompt + tools + model로 정의
- **Thread**: 대화 상태 저장 (서버 측 관리)
- **Run**: Thread에서 Assistant를 실행
- **Built-in Tools**: Code Interpreter, File Search, Function Calling

**Multi-Agent Support**

- 단일 Assistant 설계 — native multi-agent 지원 없음
- 여러 Assistant를 코드로 조합하면 multi-agent 패턴 구현 가능 (수동)
- Thread 공유로 Agent 간 context 전달 가능하지만 설계가 필요

**Tool Use / Function Calling**

- Function calling 지원 (JSON schema 정의)
- Code Interpreter: Python 코드 자동 실행 (데이터 분석, 차트)
- File Search: 업로드된 파일에서 자동 RAG (내장 vector store)
- 외부 API 호출은 Function calling + 개발자 코드로 처리

**Memory Management**

- Thread가 서버 측에서 자동 관리 — 명시적 memory 관리 불필요
- Thread에 파일, 이미지 첨부 가능
- Context window 관리 자동화 (truncation strategy 설정)

**RAG Support**

- **File Search** tool이 자동 RAG 제공 (파일 업로드 → 자동 청킹 → 벡터 검색)
- 별도 vector DB 불필요 — OpenAI가 관리
- 파일당 과금 ($0.10/GB/day storage)

**Production Readiness**

- OpenAI 인프라 — 가동 시간, 확장성 검증됨
- 다만 OpenAI 서비스 장애 시 대안 없음 (vendor lock-in)
- Streaming 지원, 비동기 실행 지원
- 사용량 기반 과금 — 예측 가능하지만 대규모 시 비용 증가

**Strengths**

- 가장 간단한 셋업 — API 호출만으로 Agent 생성
- File Search로 별도 RAG 파이프라인 없이 즉시 문서 검색 가능
- Thread 관리 자동화 — state 관리 부담 제로
- Code Interpreter로 데이터 분석 기능 즉시 사용

**Weaknesses**

- **GPT only** — Claude 사용 불가. LLM vendor lock-in
- **Self-hosting 불가** — 데이터 주권 이슈
- Multi-agent는 수동 구현 필요
- CRM 연동은 Function calling으로 직접 개발
- 비용 예측이 어려움 (token + file storage + tool usage 복합 과금)
- PE portfolio 배포 시 각 회사마다 OpenAI 계정/과금 분리 필요

---

### 3.5 Anthropic Claude Tool Use / Claude Agent SDK

**Architecture and Approach**

Anthropic의 Claude는 native tool use (function calling)를 지원하며, 2025년부터 Agent 구축을 위한 기능을 강화하고 있다. Claude Agent SDK는 Python 기반으로 agentic 워크플로우를 구축할 수 있는 경량 프레임워크다.

```
┌─────────────────────────────────────────────┐
│             Claude Agent SDK                 │
│                                              │
│  ┌──────────┐    ┌──────────┐              │
│  │  Agent   │───▶│  Tools   │              │
│  │ (Claude) │    │(Function │              │
│  │ + Prompt │    │ Calling) │              │
│  └──────────┘    └──────────┘              │
│       │                                      │
│       ▼                                      │
│  ┌──────────┐    ┌──────────┐              │
│  │ Agentic  │    │ MCP      │              │
│  │  Loop    │    │(Model    │              │
│  │(reason → │    │ Context  │              │
│  │ act →    │    │ Protocol)│              │
│  │ observe) │    │          │              │
│  └──────────┘    └──────────┘              │
└─────────────────────────────────────────────┘
```

- **Tool Use**: JSON schema로 tool 정의 → Claude가 자동으로 tool 호출 결정
- **Agentic Loop**: Claude가 tool 사용 → 결과 관찰 → 다음 행동 결정의 반복
- **MCP (Model Context Protocol)**: 외부 데이터 소스/tool과의 표준 연결 프로토콜
- **Claude Agent SDK**: Agent 정의, tool 관리, 실행 루프를 간편하게 구성하는 Python SDK
- **Extended Thinking**: Claude가 tool 호출 전 reasoning chain을 투명하게 보여줌

**Multi-Agent Support**

- Claude Agent SDK에서 multi-agent 패턴 구현 가능 (orchestrator → sub-agent)
- 각 Agent가 별도의 system prompt와 tool set을 가짐
- Agent 간 handoff는 SDK의 구조를 활용하여 구현
- LangGraph/CrewAI 대비 multi-agent 추상화 수준은 낮지만, 직접 제어 가능

**Tool Use / Function Calling**

- Claude 3.5 Sonnet / Claude 3 Opus / Claude 3.5 Haiku 전 모델 tool use 지원
- Tool 결과를 자동으로 다음 추론에 반영
- Parallel tool calling 지원 (여러 tool 동시 호출)
- MCP로 Salesforce, HubSpot 등 CRM 서버 연결 가능

**Memory Management**

- Conversation history 기반 memory (Messages API의 대화 히스토리)
- 장기 메모리는 외부 구현 필요 (DB 또는 file)
- Context window 200K tokens (Claude 3.5) — 긴 대화/문서 처리 유리

**RAG Support**

- 200K context window로 소규모 문서는 RAG 없이 직접 주입 가능
- 대규모 RAG는 외부 vector DB + retrieval 로직 필요
- MCP를 통한 데이터 소스 연결로 동적 context 주입 가능

**Production Readiness**

- Claude API 자체는 production-grade (Anthropic SLA)
- Claude Agent SDK는 2025년 출시, 빠르게 성숙 중
- Extended thinking으로 Agent의 추론 과정 추적 가능 — debugging에 유리
- Amazon Bedrock, Google Cloud Vertex AI를 통한 엔터프라이즈 배포 가능

**Strengths**

- **Claude의 reasoning 품질**: 복잡한 B2B sales context 이해에 강점
- **200K context window**: Playbook 문서 전체를 context에 넣을 수 있음
- **MCP**: CRM, 데이터 소스와의 표준화된 연결
- **Extended thinking**: Agent 판단 근거 투명성 — Human-in-the-loop에 적합
- 비용 효율: Claude 3.5 Haiku로 T3 agent 운영 시 GPT-4 대비 저렴

**Weaknesses**

- Claude Agent SDK는 비교적 신규 — 커뮤니티/예제 아직 성장 중
- Multi-agent 추상화가 CrewAI/LangGraph보다 수동적
- MCP 생태계는 빠르게 성장 중이나 아직 LangChain 생태계보다 작음
- Anthropic LLM only — multi-LLM 전략 시 별도 구현 필요

---

### 3.6 Agent Framework 종합 비교

| 기준 | LangChain/LangGraph | CrewAI | AutoGen | OpenAI Assistants | Claude Tool Use/SDK |
|------|---------------------|--------|---------|-------------------|---------------------|
| **Multi-Agent** | LangGraph로 가능 | Native (핵심 기능) | Native (대화 기반) | 수동 구현 | SDK로 가능 |
| **Tool Use** | 매우 풍부 | LangChain 호환 | Function calling | Built-in + FC | Native + MCP |
| **Memory** | 다양한 옵션 | Short/Long/Entity | 대화 기반 | Thread 자동관리 | 200K context |
| **RAG** | Best-in-class | LangChain 의존 | ChromaDB 내장 | File Search 내장 | 외부 구현 필요 |
| **LLM 자유도** | 모든 LLM | 모든 LLM | Azure 중심 | GPT only | Claude only |
| **Learning Curve** | 높음 | 중간 | 높음 | 낮음 | 중간 |
| **Production** | 성숙 | 성장 중 | 리팩토링 중 | 안정 | 성장 중 |
| **Community** | 최대 (100k+ stars) | 성장 중 (25k+) | 큼 (40k+) | OpenAI 생태계 | Anthropic 생태계 |
| **CRM 연동** | 커스텀 tool | 커스텀 tool | 커스텀 tool | Function calling | MCP / 커스텀 tool |
| **Self-Hosting** | O | O | O | X | O (API 호출) |

### 가중 점수 비교

| 평가 기준 (가중치) | LangChain | CrewAI | AutoGen | OpenAI Asst | Claude SDK |
|-------------------|-----------|--------|---------|-------------|------------|
| Setup 용이성 (15%) | 2 | 4 | 2 | 5 | 4 |
| LLM Integration (15%) | 5 | 5 | 3 | 2 | 4 |
| CRM Integration (12%) | 4 | 3 | 2 | 3 | 4 |
| Workflow Orchestration (10%) | 4 | 3 | 2 | 2 | 3 |
| Multi-Agent (10%) | 4 | 5 | 4 | 2 | 3 |
| RAG/Vector DB (8%) | 5 | 4 | 3 | 4 | 3 |
| Self-Hosting (8%) | 5 | 5 | 5 | 1 | 5 |
| Cost at Scale (8%) | 4 | 4 | 3 | 2 | 4 |
| Community (5%) | 5 | 4 | 4 | 4 | 3 |
| Monitoring (5%) | 5 | 3 | 2 | 3 | 3 |
| Production Readiness (4%) | 4 | 3 | 2 | 4 | 3 |
| **가중 합계** | **4.03** | **4.02** | **2.79** | **2.89** | **3.66** |

**분석**: LangChain과 CrewAI가 거의 동점. LangChain은 생태계/RAG/모니터링에서 앞서고, CrewAI는 multi-agent/setup 용이성에서 앞선다. 본 프로젝트의 BCG 5-Agent 모델 특성상 CrewAI의 role-based 설계가 개념적으로 가장 잘 맞는다.

---

## 4. Combined Architecture Options

### Option A: n8n + Claude API (Simple PoC)

**Architecture**

```
┌──────────────────────────────────────────────────────────┐
│                    n8n (Self-hosted)                       │
│                                                           │
│  ┌───────────┐    ┌──────────────┐    ┌───────────────┐  │
│  │  Webhook  │───▶│  AI Agent    │───▶│  Salesforce/  │  │
│  │  /Cron    │    │  Node        │    │  HubSpot Node │  │
│  │  Trigger  │    │  (Claude 3.5)│    │  (CRUD)       │  │
│  └───────────┘    └──────┬───────┘    └───────────────┘  │
│                          │                                │
│                   ┌──────▼───────┐                       │
│                   │  Vector      │                       │
│                   │  Store Node  │                       │
│                   │  (Playbook   │                       │
│                   │   RAG)       │                       │
│                   └──────────────┘                       │
│                                                           │
│  Sub-workflows:                                           │
│  ├── Post-Call CRM Updater (PoC #1)                      │
│  ├── Weekly Ops Report (PoC #2)                          │
│  └── Lead Enrichment (PoC #3)                            │
└──────────────────────────────────────────────────────────┘
```

**구성 요소**

| Layer | Tool | 역할 |
|-------|------|------|
| Orchestration | n8n (Docker self-hosted) | Workflow trigger, routing, scheduling |
| LLM | Claude 3.5 Sonnet API | 추론, 텍스트 생성, MEDDICC 추출 |
| CRM | Salesforce/HubSpot n8n nodes | Account, Opportunity, Activity CRUD |
| Vector DB | Supabase pgvector (n8n node) | Playbook RAG |
| Notification | Slack/Email n8n nodes | 알림, 리포트 전송 |

**Pros**

- 가장 빠른 구축 (1-2주 내 첫 PoC 가능)
- Self-hosted로 비용 최소화 (LLM API 비용만)
- Visual workflow로 비개발자도 수정 가능
- n8n AI Agent node로 기본적인 tool use + reasoning loop 구현
- PE portfolio 배포 시 Docker image로 복제 가능

**Cons**

- 5-Agent 간 복잡한 상호작용은 sub-workflow로 우회해야 함
- Agent 간 shared state 관리가 제한적
- 코드 기반 커스텀 로직 추가 시 n8n의 JS/Python node에 의존 (디버깅 불편)
- Production 수준의 Agent 모니터링이 부족

**Best for**: PoC 단계. Post-Call CRM Updater 같은 단일 Agent 검증. 빠른 iteration.

**예상 비용 (월)**

| 항목 | 비용 |
|------|------|
| n8n | $0 (self-hosted community) |
| Claude API (100 accounts, 일 50회 호출) | ~$150-300 |
| Supabase (Free tier) | $0 |
| VPS (n8n 호스팅) | ~$20-50 |
| **합계** | **~$170-350/월** |

---

### Option B: LangChain/LangGraph + FastAPI + CRM API (Developer-heavy)

**Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Application                        │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                    LangGraph                          │   │
│  │                                                       │   │
│  │  ┌──────────────┐                                    │   │
│  │  │ Orchestrator │                                    │   │
│  │  │   (Router)   │                                    │   │
│  │  └──────┬───────┘                                    │   │
│  │         │                                             │   │
│  │    ┌────┼────┬────────┬──────────┐                   │   │
│  │    ▼    ▼    ▼        ▼          ▼                   │   │
│  │  ┌────┐┌───┐┌─────┐┌────┐┌──────────┐              │   │
│  │  │Lead││Qual││Deal ││ CS ││   Ops    │              │   │
│  │  │Gen ││    ││Conv ││    ││ Analyst  │              │   │
│  │  └────┘└───┘└─────┘└────┘└──────────┘              │   │
│  │                                                       │   │
│  │  Shared State: PostgreSQL + Redis                     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────┐    │
│  │ CRM Client │  │ Vector DB  │  │ LangSmith          │    │
│  │ (SF/HS API)│  │ (pgvector) │  │ (Monitoring)       │    │
│  └────────────┘  └────────────┘  └────────────────────┘    │
│                                                              │
│  API Endpoints:                                              │
│  POST /agent/post-call     → Post-Call CRM Updater          │
│  POST /agent/ops-report    → Weekly Ops Report               │
│  POST /agent/lead-enrich   → Lead Enrichment                │
│  GET  /agent/health        → Agent Health Check              │
└─────────────────────────────────────────────────────────────┘
```

**구성 요소**

| Layer | Tool | 역할 |
|-------|------|------|
| API Server | FastAPI (Python) | REST API, 인증, 라우팅 |
| Agent Framework | LangGraph | Multi-agent 그래프, 상태 관리, 조건부 분기 |
| LLM | Claude 3.5 Sonnet + GPT-4 (fallback) | 추론, 생성, 추출 |
| CRM | Custom Python client (requests/httpx) | Salesforce/HubSpot REST API 직접 호출 |
| Vector DB | pgvector (PostgreSQL extension) | Playbook RAG |
| Cache/State | Redis | Agent state, 세션 캐시 |
| Monitoring | LangSmith | 트레이싱, 평가, 비용 추적 |
| Scheduler | Celery + Redis | 주기적 작업 (주간 리포트, 리드 스캔) |

**Pros**

- 완전한 제어 — 모든 계층을 커스터마이징 가능
- LangGraph의 StateGraph로 BCG 5-Agent 모델을 정확하게 구현
- 조건부 라우팅, 에러 핸들링, 재시도 로직 세밀하게 설정
- LangSmith로 production-grade 모니터링
- 멀티 LLM 전략 (Claude primary, GPT-4 fallback)
- API 기반이므로 n8n, Slack Bot, 웹 UI 등 어떤 프론트엔드와도 연동 가능

**Cons**

- **구축 시간 최장** — FastAPI 서버, LangGraph 워크플로우, CRM 클라이언트 모두 개발 필요
- Python 개발자 필수 (비개발 팀은 수정 불가)
- 인프라 관리 부담 (서버, DB, Redis, Celery)
- LangChain 생태계의 빈번한 API 변경에 취약
- Over-engineering 위험 — PoC에 과도한 아키텍처

**Best for**: Production 단계. 5-Agent 모델을 정교하게 구현. 장기적으로 유지보수 가능한 코드베이스.

**예상 비용 (월)**

| 항목 | 비용 |
|------|------|
| VPS (FastAPI + PostgreSQL + Redis) | ~$50-100 |
| Claude API | ~$150-300 |
| LangSmith (Plus plan) | ~$39 |
| **합계** | **~$240-440/월** |

---

### Option C: CrewAI + n8n (Multi-Agent Native)

**Architecture**

```
┌───────────────────────────────────────────────────────────────┐
│                                                                │
│  ┌──────────────────────┐    ┌──────────────────────────┐    │
│  │    n8n (Triggers &    │    │     CrewAI (Agent Brain) │    │
│  │    Orchestration)     │    │                          │    │
│  │                       │    │  ┌────────────────────┐  │    │
│  │  ┌────────┐          │    │  │   Orchestration    │  │    │
│  │  │Webhook │──────────┼───▶│  │   Crew (Manager)   │  │    │
│  │  │/Cron   │          │    │  └─────────┬──────────┘  │    │
│  │  └────────┘          │    │            │              │    │
│  │                       │    │   ┌────┬──┴──┬────┬───┐ │    │
│  │  ┌────────┐          │    │   ▼    ▼     ▼    ▼   ▼ │    │
│  │  │CRM     │◀─────────┼────│  Lead Qual  Deal  CS Ops│    │
│  │  │Nodes   │          │    │  Gen  Agent Conv  Agt An│    │
│  │  └────────┘          │    │                          │    │
│  │                       │    │  Tools:                  │    │
│  │  ┌────────┐          │    │  ├─ CRM Read/Write      │    │
│  │  │Slack/  │◀─────────┼────│  ├─ Web Search          │    │
│  │  │Email   │          │    │  ├─ RAG Query            │    │
│  │  └────────┘          │    │  └─ Report Generator     │    │
│  └──────────────────────┘    └──────────────────────────┘    │
│                                                                │
│  ┌──────────────────────┐    ┌──────────────────────────┐    │
│  │  pgvector / Chroma   │    │  Langfuse (Monitoring)   │    │
│  │  (Playbook RAG)      │    │  (Self-hosted)           │    │
│  └──────────────────────┘    └──────────────────────────┘    │
│                                                                │
└───────────────────────────────────────────────────────────────┘
```

**구성 요소**

| Layer | Tool | 역할 |
|-------|------|------|
| Trigger & Integration | n8n (self-hosted) | CRM event 감지, 스케줄링, 결과 전송 |
| Agent Framework | CrewAI | 5-Agent 정의, task 할당, hierarchical execution |
| LLM | Claude 3.5 Sonnet (primary) + Haiku (T3) | 추론, 생성 |
| CRM | CrewAI custom tools (SF/HS API) | Agent가 직접 CRM 읽기/쓰기 |
| Vector DB | pgvector 또는 Chroma | Playbook RAG |
| Monitoring | Langfuse (self-hosted) | Agent trace, cost tracking |
| Connector | n8n ↔ CrewAI via HTTP/webhook | n8n trigger → CrewAI 실행 → n8n 후처리 |

**Pros**

- **BCG 5-Agent 모델과 가장 자연스러운 매핑**:
  - Orchestration Agent → CrewAI Manager (Hierarchical process)
  - Lead Gen Agent → CrewAI Agent (role="Lead Generation Specialist")
  - Qual Agent → CrewAI Agent (role="Deal Qualification Analyst")
  - Deal Agent → CrewAI Agent (role="Deal Conversion Specialist")
  - CS Agent → CrewAI Agent (role="Customer Success Manager")
  - Ops Analyst → CrewAI Agent (role="Sales Operations Analyst")
- n8n이 external trigger (CRM event, schedule) 처리
- CrewAI가 complex reasoning 처리
- 역할 분리가 명확 — 각 layer의 책임이 분명
- Self-hosted 조합으로 PE portfolio 배포에 유리

**Cons**

- n8n ↔ CrewAI 연동 인터페이스 설계 필요 (HTTP API 래퍼)
- CrewAI 서버를 별도로 운영해야 함 (FastAPI 또는 Flask로 래핑)
- 두 시스템의 에러 핸들링을 조율해야 함
- CrewAI의 production 안정성이 LangChain보다 아직 부족
- 학습해야 할 도구가 두 개 (n8n + CrewAI)

**Best for**: 본 프로젝트. BCG 5-Agent 모델을 직접 구현하면서, workflow automation의 이점도 활용. PoC에서 시작하여 Production으로 확장 가능.

**예상 비용 (월)**

| 항목 | 비용 |
|------|------|
| n8n (self-hosted) | $0 |
| VPS (CrewAI + n8n + DB) | ~$50-100 |
| Claude API (Sonnet + Haiku mix) | ~$120-250 |
| Langfuse (self-hosted) | $0 |
| **합계** | **~$170-350/월** |

---

### Option D: Claude Agent SDK + MCP + FastAPI

**Architecture**

```
┌───────────────────────────────────────────────────────────────┐
│                    FastAPI Application                          │
│                                                                │
│  ┌──────────────────────────────────────────────────────┐     │
│  │              Claude Agent SDK                         │     │
│  │                                                       │     │
│  │  ┌──────────────┐                                    │     │
│  │  │ Orchestrator │  (Claude 3.5 Sonnet)               │     │
│  │  │   Agent      │                                    │     │
│  │  └──────┬───────┘                                    │     │
│  │         │                                             │     │
│  │    ┌────┼────┬────────┬──────────┐                   │     │
│  │    ▼    ▼    ▼        ▼          ▼                   │     │
│  │  Sub-  Sub-  Sub-    Sub-      Sub-                  │     │
│  │  Agent Agent Agent   Agent     Agent                 │     │
│  │  (Lead)(Qual)(Deal)  (CS)     (Ops)                  │     │
│  │                                                       │     │
│  │  Each with: system prompt + tools + MCP servers       │     │
│  └──────────────────────────────────────────────────────┘     │
│                                                                │
│  MCP Servers:                                                  │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────┐      │
│  │ CRM MCP    │  │ RAG MCP    │  │ Search MCP         │      │
│  │ (SF/HS     │  │ (pgvector  │  │ (Web/News          │      │
│  │  adapter)  │  │  adapter)  │  │  adapter)          │      │
│  └────────────┘  └────────────┘  └────────────────────┘      │
│                                                                │
│  ┌────────────────────┐  ┌────────────────────┐              │
│  │ Scheduler          │  │ Langfuse           │              │
│  │ (APScheduler/Cron) │  │ (Monitoring)       │              │
│  └────────────────────┘  └────────────────────┘              │
└───────────────────────────────────────────────────────────────┘
```

**구성 요소**

| Layer | Tool | 역할 |
|-------|------|------|
| API Server | FastAPI (Python) | REST API, 스케줄링 |
| Agent Framework | Claude Agent SDK | Agent 정의, tool 관리, agentic loop |
| LLM | Claude 3.5 Sonnet (orchestrator) + Claude 3.5 Haiku (sub-agents) | 추론, 생성 |
| Integration | MCP Servers | CRM, Vector DB, Web Search 표준 연결 |
| Vector DB | pgvector | Playbook RAG |
| Monitoring | Langfuse | 트레이싱, 비용 추적 |

**Pros**

- **Claude 네이티브** — Claude의 tool use, extended thinking을 가장 깊이 활용
- **MCP 표준**: CRM 연동을 MCP server로 추상화하면 Salesforce ↔ HubSpot 교체가 용이 — PE portfolio portability에 최적
- Extended thinking으로 Agent 판단 근거가 투명 — Human-in-the-loop(T1/T2) 검토에 유리
- Claude 3.5 Haiku의 비용 효율로 T3 자동화 비용 절감
- 200K context window로 Playbook 문서를 직접 주입 가능 (소규모 시 RAG 불필요)

**Cons**

- **Claude only** — GPT-4, Gemini 등 다른 LLM으로 전환 어려움
- Claude Agent SDK 생태계가 아직 초기 (LangChain/CrewAI 대비)
- MCP server (CRM adapter 등)를 직접 구현해야 할 수 있음
- Multi-agent 패턴을 직접 설계해야 함 (CrewAI 수준의 추상화 없음)
- 커뮤니티 지원 규모가 LangChain보다 작음

**Best for**: Claude API를 이미 주력으로 사용하며, MCP 생태계를 장기적으로 채택하려는 경우. Anthropic 로드맵에 베팅하는 전략.

**예상 비용 (월)**

| 항목 | 비용 |
|------|------|
| VPS (FastAPI + PostgreSQL) | ~$40-80 |
| Claude API (Sonnet + Haiku mix) | ~$100-200 |
| Langfuse (self-hosted) | $0 |
| **합계** | **~$140-280/월** |

---

### 4.5 Architecture Options 종합 비교

| 기준 | Option A (n8n + Claude) | Option B (LangGraph + FastAPI) | Option C (CrewAI + n8n) | Option D (Claude SDK + MCP) |
|------|------------------------|-------------------------------|------------------------|---------------------------|
| **구축 시간** | 1-2주 | 4-6주 | 2-3주 | 3-4주 |
| **개발자 필요** | 낮음 | 높음 | 중간 | 중간-높음 |
| **Multi-Agent** | 제한적 (sub-workflow) | 정밀 제어 | Native (최적) | 수동 구현 |
| **CRM 연동** | n8n 내장 노드 | 커스텀 클라이언트 | 커스텀 tool | MCP server |
| **RAG** | n8n Vector node | LangChain native | LangChain 의존 | pgvector + 200K context |
| **확장성** | 중간 | 높음 | 중간-높음 | 높음 |
| **Portfolio 이식성** | Docker image 복제 | 코드 배포 | Docker + 설정 | MCP adapter 교체 |
| **월 비용** | $170-350 | $240-440 | $170-350 | $140-280 |
| **PoC 적합성** | 최고 | 낮음 | 높음 | 중간 |
| **Production 적합성** | 중간 | 최고 | 높음 | 높음 |

---

## 5. Vector DB 비교

### 5.1 pgvector (PostgreSQL Extension)

**개요**: PostgreSQL에 벡터 검색 기능을 추가하는 오픈소스 extension.

| 항목 | 내용 |
|------|------|
| **Hosting Model** | Self-hosted (PostgreSQL + extension) 또는 Managed (Supabase, AWS RDS, Neon) |
| **Architecture** | PostgreSQL 내장 — 별도 인프라 불필요 |
| **Index Types** | IVFFlat, HNSW (0.5.0+) |
| **Max Dimensions** | 2,000 |
| **Performance** | 소규모(~100K 벡터): 매우 좋음. 대규모(1M+): 전용 Vector DB 대비 느림 |
| **Cost** | Self-hosted: 무료. Supabase Free tier: 500MB |
| **ACID Compliance** | 완전 (PostgreSQL) |
| **Integration** | LangChain, LlamaIndex, n8n, 모든 PostgreSQL 호환 도구 |

**장점**

- 기존 PostgreSQL 인프라 재사용 — 추가 서비스 불필요
- SQL로 벡터 검색 + 메타데이터 필터링 동시 수행
- ACID 트랜잭션 — CRM 데이터와 벡터를 같은 DB에 저장 가능
- Supabase를 통한 managed hosting 가능 (Free tier 제공)

**단점**

- 대규모 벡터 데이터(1M+ 행)에서 전용 Vector DB보다 느림
- 벡터 검색 전용 기능(hybrid search, re-ranking 등)이 제한적
- PostgreSQL 운영 지식 필요 (tuning, indexing)

**우리 프로젝트 적합성**: **최적**. Playbook 문서 수십 개 + CRM 관련 context = 수천~수만 벡터 수준. pgvector로 충분. CRM 데이터와 같은 DB에서 관리하면 인프라 단순화.

---

### 5.2 Pinecone

**개요**: 클라우드 네이티브 managed vector database. Serverless 아키텍처.

| 항목 | 내용 |
|------|------|
| **Hosting Model** | Fully managed SaaS (AWS, GCP, Azure) |
| **Architecture** | Serverless (2024~) — 사용량 기반 자동 스케일링 |
| **Index Types** | 독자 인덱싱 (내부 최적화) |
| **Max Dimensions** | 20,000 |
| **Performance** | 대규모에서 우수. p99 latency < 50ms |
| **Cost** | Free tier: 무제한 벡터 (1 index). Starter: $0.00 + storage/query 기반 |
| **Integration** | LangChain, LlamaIndex, n8n, 대부분의 AI 프레임워크 |

**장점**

- 인프라 관리 제로 — API 호출만으로 운영
- 대규모 벡터에서 안정적 성능
- Namespace로 PE portfolio company별 데이터 격리 가능
- 풍부한 메타데이터 필터링

**단점**

- **Vendor lock-in** — 데이터 이동이 번거로움
- 대규모 시 비용 예측 어려움 (query 횟수 + storage 복합 과금)
- Self-hosting 불가 — 데이터 주권 이슈
- 한국 리전 없음 (가장 가까운 리전: Tokyo)

**우리 프로젝트 적합성**: 적합하나 과잉. Playbook RAG 수준의 데이터에 Pinecone은 오버스펙. 대규모 확장(10+ portfolio companies) 시 고려 가치 있음.

---

### 5.3 Weaviate

**개요**: 오픈소스 벡터 데이터베이스. GraphQL API, 모듈식 아키텍처.

| 항목 | 내용 |
|------|------|
| **Hosting Model** | Self-hosted (Docker) 또는 Weaviate Cloud Services (WCS) |
| **Architecture** | 독립 서버, 모듈식 (vectorizer, reader, generator 모듈) |
| **Index Types** | HNSW (기본), Flat |
| **Max Dimensions** | 65,535 |
| **Performance** | HNSW 기반으로 우수. Hybrid search(BM25 + vector) 네이티브 |
| **Cost** | Self-hosted: 무료. WCS Sandbox: 무료 (14일). Standard: $25/mo~ |
| **Integration** | LangChain, LlamaIndex, n8n (커스텀) |

**장점**

- **Hybrid search 네이티브**: BM25(키워드) + vector(시맨틱) 동시 검색 — Playbook에서 정확한 용어(MEDDICC 등)와 의미 검색 모두 필요
- 내장 vectorizer 모듈 (OpenAI, Cohere, Hugging Face) — 별도 임베딩 파이프라인 불필요
- Self-hosted 가능 — PE portfolio 배포에 유리
- GraphQL API — 유연한 쿼리

**단점**

- 별도 서버 운영 필요 (pgvector 대비 인프라 부담)
- Weaviate 전용 쿼리 문법 학습 필요
- 소규모 데이터에 독립 서버는 과잉
- n8n 공식 노드 없음 (HTTP Request로 연동)

**우리 프로젝트 적합성**: Hybrid search가 매력적이나, 소규모 Playbook RAG에 독립 서버는 과잉. Production 단계에서 검색 품질이 중요해지면 고려.

---

### 5.4 Chroma

**개요**: 오픈소스 AI-native 임베딩 데이터베이스. 개발자 친화적, 경량.

| 항목 | 내용 |
|------|------|
| **Hosting Model** | In-process (embedded), Self-hosted server, Chroma Cloud (beta) |
| **Architecture** | 경량 — Python 프로세스 내에서 즉시 실행 가능 |
| **Index Types** | HNSW (hnswlib) |
| **Max Dimensions** | 제한 없음 |
| **Performance** | 소규모~중규모 데이터에서 매우 빠름. 대규모에서는 제한적 |
| **Cost** | Self-hosted: 무료. Cloud: 베타 (가격 미정) |
| **Integration** | LangChain, LlamaIndex, CrewAI (기본 메모리 백엔드) |

**장점**

- **가장 간단한 셋업** — `pip install chromadb` → 즉시 사용
- In-process 모드로 별도 서버 불필요
- CrewAI 기본 메모리 백엔드 — CrewAI 선택 시 자연스러운 조합
- 개발/테스트에 최적

**단점**

- Production 안정성 미검증 (대규모 배포 사례 부족)
- In-process 모드는 앱 재시작 시 데이터 유실 위험 (persistent mode 사용 필요)
- Managed cloud가 아직 베타
- 고급 기능 (hybrid search, 백업/복원 등) 부족

**우리 프로젝트 적합성**: PoC 단계 최적. CrewAI와 즉시 연동 가능. Production 전환 시 pgvector로 마이그레이션 권장.

---

### 5.5 Vector DB 종합 비교

| 기준 | pgvector | Pinecone | Weaviate | Chroma |
|------|----------|----------|----------|--------|
| **셋업 난이도** | 중간 (PG 필요) | 쉬움 (API only) | 중간 (Docker) | 매우 쉬움 |
| **성능 (소규모)** | 우수 | 우수 | 우수 | 우수 |
| **성능 (대규모)** | 보통 | 최고 | 우수 | 보통 |
| **Self-Hosting** | O | X | O | O |
| **Hybrid Search** | 제한적 | 메타데이터 필터 | 네이티브 | X |
| **비용 (PoC)** | $0 (Supabase free) | $0 (Free tier) | $0 (self-hosted) | $0 |
| **비용 (Production)** | ~$25/mo | ~$70+/mo | ~$25/mo | $0 (self-hosted) |
| **ACID** | O | X | X | X |
| **CRM 데이터 동거** | O (같은 PG) | X | X | X |
| **LangChain 연동** | O | O | O | O |
| **CrewAI 연동** | 간접 | 간접 | 간접 | 기본 내장 |
| **n8n 연동** | Supabase node | Pinecone node | HTTP Request | HTTP Request |

### 추천

| 단계 | 추천 | 이유 |
|------|------|------|
| **PoC** | Chroma (CrewAI 사용 시) 또는 Supabase pgvector (n8n 사용 시) | 즉시 시작 가능, 비용 $0 |
| **Production** | pgvector (PostgreSQL 위) | CRM 데이터와 동거, ACID, self-hosting, 비용 효율 |
| **대규모 확장** | Pinecone 또는 Weaviate | 10+ portfolio company, 수백만 벡터 시 |

---

## 6. Monitoring 비교: LangSmith vs Helicone vs Langfuse

### 종합 비교

| 기준 | LangSmith | Helicone | Langfuse |
|------|-----------|----------|----------|
| **제공사** | LangChain Inc. | Helicone AI | Finto Technologies (오픈소스) |
| **오픈소스** | X (SaaS) | 부분 (게이트웨이 OSS) | **O (MIT License)** |
| **Self-Hosting** | X | 제한적 | **O (Docker Compose)** |
| **LLM 트레이싱** | 매우 상세 (LangChain 네이티브) | 프록시 기반 (모든 LLM) | SDK 기반 (모든 LLM) |
| **Cost Tracking** | O (LangChain 연동 시) | **O (핵심 기능)** | O |
| **Prompt Management** | O | X | O |
| **Evaluation** | **O (LangSmith Evaluators)** | X | O (Score 기반) |
| **LangChain 통합** | **네이티브 (1줄 설정)** | 프록시 설정 필요 | SDK 래핑 필요 |
| **CrewAI 통합** | 가능 (LangChain 기반) | 프록시 설정 | SDK 래핑 |
| **n8n 통합** | 제한적 | 제한적 | 제한적 |
| **Pricing (Cloud)** | Free: 5K traces/mo, Plus: $39/mo | Free: 100K req/mo, Pro: $20/mo | Free: 50K obs/mo, Pro: $59/mo |
| **Pricing (Self-hosted)** | N/A | N/A | **무료** |

### 상세 비교

**LangSmith**

- LangChain/LangGraph 사용 시 가장 자연스러운 선택
- `LANGCHAIN_TRACING_V2=true` 환경변수 하나로 전체 트레이싱 활성화
- Agent의 각 step (LLM 호출, tool 실행, chain 등)을 시각적으로 추적
- Evaluation framework로 Agent 품질 자동 테스트 가능
- 단점: LangChain 외 프레임워크에서는 별도 SDK 사용 필요, Self-hosting 불가

**Helicone**

- LLM API 앞에 프록시를 두는 방식 — 프레임워크 무관하게 동작
- 비용 추적이 핵심 기능 — LLM 호출별 비용 자동 계산
- 가장 간단한 셋업 (base URL 변경만)
- 단점: Agent 레벨의 상세 트레이싱은 부족, Self-hosting 제한적

**Langfuse**

- **오픈소스 + Self-hosting**: PE portfolio 배포에 최적
- Docker Compose로 5분 내 셋업
- Trace → Span → Generation 구조로 Agent 행동 추적
- Prompt 버전 관리 — Playbook prompt 업데이트 추적에 유리
- Score 기반 evaluation으로 Agent 품질 모니터링
- Python SDK, JS SDK 제공 — CrewAI, LangChain 모두 연동 가능
- 단점: LangSmith만큼의 LangChain 네이티브 통합은 없음, 커뮤니티 규모 작음

### 추천

| 조건 | 추천 | 이유 |
|------|------|------|
| LangGraph 선택 시 (Option B) | **LangSmith** | 네이티브 통합, 가장 풍부한 트레이싱 |
| CrewAI/Claude SDK 선택 시 (Option C/D) | **Langfuse** | 오픈소스, self-hosting, 프레임워크 무관 |
| 비용만 추적하고 싶을 때 | **Helicone** | 가장 간단, LLM 비용 대시보드 |
| PE portfolio 배포 | **Langfuse** | Self-hosted로 각 portfolio company별 인스턴스 |

---

## 7. 최종 추천 (Final Recommendation)

### 프로젝트 요구사항 요약

| 요구사항 | 근거 |
|----------|------|
| PE portfolio 배포 (portability) | `agent.md` Principle #6: Portfolio-portable |
| BCG 5-Agent 모델 | `agent.md` Architecture: 5 sub-agent + orchestrator |
| CRM-native (Salesforce/HubSpot) | `agent.md` Principle #2: All read/write through CRM |
| Playbook RAG | `scope.md` Phase 4: Vectorized playbook content |
| Graduated autonomy (T1/T2/T3) | `agent.md` Tier-Based Interaction Model |
| 빠른 PoC 검증 | `scope.md` Phase 4: Month 5-9 (5개월) |
| 비용 효율 | `scope.md` Risk: LLM cost at scale |

---

### PoC Stack (가장 빠른 검증)

> **Option A: n8n + Claude API**를 기반으로, 단일 Agent PoC를 빠르게 구축

```
┌──────────────────────────────────────────────┐
│  PoC Stack                                    │
│                                               │
│  Workflow:    n8n (self-hosted, Docker)       │
│  LLM:        Claude 3.5 Sonnet API           │
│  CRM:        HubSpot/Salesforce n8n nodes    │
│  Vector DB:  Supabase pgvector (free tier)   │
│  Monitoring: Helicone (free tier, 비용 추적)  │
│                                               │
│  예상 비용: $170-350/월                       │
│  구축 시간: 1-2주                             │
│  개발자 수: 1명                               │
└──────────────────────────────────────────────┘
```

**PoC 실행 순서**:

1. **Week 1**: n8n Docker 셋업 + CRM 연동 확인 + Claude API 연결
2. **Week 2**: Post-Call CRM Updater (PoC #1) 구축 — Webhook으로 call transcript 수신 → Claude가 MEDDICC 추출 → CRM 업데이트 draft → Slack 알림
3. **Week 3-4**: 테스트 + 피드백 수집 + 프롬프트 튜닝
4. **Week 5-6**: Ops Report (PoC #2), Lead Enrichment (PoC #3) 추가

**PoC에서 검증할 것**:

- [ ] Claude가 call transcript에서 MEDDICC 필드를 정확히 추출하는가
- [ ] n8n workflow가 안정적으로 CRM과 통신하는가
- [ ] LLM 비용이 예산 범위 내인가
- [ ] 사용자(AE/SDR)가 Agent output을 신뢰하고 사용하는가

---

### Production Stack (확장 가능)

> **Option C: CrewAI + n8n** + pgvector + Langfuse

```
┌──────────────────────────────────────────────┐
│  Production Stack                             │
│                                               │
│  Trigger/Integration: n8n (self-hosted)      │
│  Agent Framework:     CrewAI (5-Agent Crew)  │
│  LLM:                 Claude 3.5 Sonnet      │
│                       + Claude 3.5 Haiku (T3)│
│  CRM:                 Custom tools (SF/HS)   │
│  Vector DB:           pgvector (PostgreSQL)  │
│  Monitoring:          Langfuse (self-hosted) │
│  API:                 FastAPI (CrewAI 래퍼)   │
│  Infra:               Docker Compose         │
│                                               │
│  예상 비용: $170-350/월 (per portfolio co.)  │
│  구축 시간: 4-8주 (PoC 이후)                  │
│  개발자 수: 1-2명                             │
└──────────────────────────────────────────────┘
```

**Production에서 추가되는 것**:

- CrewAI Hierarchical process로 BCG 5-Agent 모델 완전 구현
- 각 Agent에 Tier 기반 자율성 규칙 적용
- pgvector에 Playbook 전체 벡터화 + RAG 파이프라인
- Langfuse로 Agent 행동 추적, 비용 모니터링, 프롬프트 버전 관리
- FastAPI로 n8n ↔ CrewAI 연동 API 제공

---

### Migration Path: PoC → Production

```
Phase 4 Timeline (Month 5-9)
─────────────────────────────────────────────────────────

Month 5-6: PoC (Option A)
├── n8n + Claude API로 단일 Agent 3종 구축
├── 사용자 피드백 수집
├── LLM 비용 데이터 확보 (Helicone)
└── Checkpoint: PoC 검증 완료 → Production 전환 결정

Month 7-8: Production 전환 (Option A → C)
├── CrewAI 5-Agent Crew 설계 + 구현
├── n8n 유지 (trigger/integration layer)
├── pgvector에 Playbook RAG 구축
├── Langfuse 셋업 (Helicone → Langfuse 전환)
└── FastAPI 래퍼 구축

Month 9: 안정화 + Portfolio 준비
├── Agent 성능 튜닝 (프롬프트, RAG 청킹 최적화)
├── Docker Compose 패키징 (portfolio 배포용)
├── Agent Governance 문서 작성
└── 파일럿 portfolio company 배포
```

### 전환 시 재사용 가능한 자산

| PoC 자산 | Production에서 재사용 |
|----------|---------------------|
| n8n 워크플로우 | 그대로 사용 (trigger/integration layer) |
| Claude 프롬프트 | CrewAI Agent의 system prompt로 이전 |
| CRM 연동 로직 | CrewAI tool로 래핑 |
| Supabase pgvector | PostgreSQL pgvector로 마이그레이션 (스키마 호환) |
| Helicone 비용 데이터 | Langfuse에서 새로 수집 (baseline 비교용) |

---

### 대안 시나리오

| 상황 | 권장 변경 |
|------|----------|
| Python 개발자 없음 | Option A(n8n only)로 Production까지 운영. CrewAI 대신 n8n sub-workflow |
| Anthropic API 불안정 | OpenAI Assistants API(Option D 변형) 또는 LangChain(multi-LLM) 전환 |
| CRM이 Salesforce → HubSpot 혼용 | Option D(MCP)가 유리. MCP adapter만 교체하면 됨 |
| 예산 극도로 제한 | Claude 3.5 Haiku 전 Agent 사용 + Self-hosted 전 계층 |
| 10+ portfolio company 동시 배포 | Kubernetes + Pinecone(managed) + LangSmith(managed)로 전환 |

---

### 최종 선택 근거 요약

| 결정 | 선택 | 핵심 근거 |
|------|------|----------|
| Workflow | **n8n (self-hosted)** | Self-hosting + AI Agent node + CRM 내장 노드 + 무료 |
| Agent Framework | **CrewAI** (Production) | BCG 5-Agent 모델과 1:1 개념 매핑. Role-based 설계 |
| LLM | **Claude 3.5 Sonnet** + **Haiku** | Reasoning 품질 + 200K context + 비용 효율 (Haiku for T3) |
| Vector DB | **pgvector** (via Supabase → self-hosted PG) | CRM 데이터 동거, ACID, self-hosting, 소규모 최적 |
| Monitoring | **Langfuse** (self-hosted) | 오픈소스, self-hosting, portfolio 배포 가능 |

---

## 부록: 참고 자료

### 공식 문서

- n8n: https://docs.n8n.io/ (AI Agent documentation)
- CrewAI: https://docs.crewai.com/ (Multi-agent framework)
- LangChain: https://python.langchain.com/ (LangGraph documentation)
- Anthropic: https://docs.anthropic.com/ (Claude API, Tool Use, Agent SDK)
- pgvector: https://github.com/pgvector/pgvector
- Langfuse: https://langfuse.com/docs

### 가격 정보 (2025 기준)

- Claude API: https://www.anthropic.com/pricing
  - Claude 3.5 Sonnet: $3/M input tokens, $15/M output tokens
  - Claude 3.5 Haiku: $0.80/M input tokens, $4/M output tokens
- OpenAI: https://openai.com/pricing
  - GPT-4o: $2.50/M input tokens, $10/M output tokens
- Pinecone: https://www.pinecone.io/pricing/
- Supabase: https://supabase.com/pricing

### 프로젝트 내부 참조

- `agent.md`: BCG 5-Agent 아키텍처, Tier 모델, Tech Stack 후보
- `scope.md`: Phase 4 요구사항, 성공 기준, 리스크
- `crm/schema.md`: CRM API 연동 포인트, 필드 매핑
- `playbook/plays/play_01_new_logo_outbound_t2t3.md`: Agent 자동화 수준 참조

> **Note**: 이 문서의 가격 정보와 기능 목록은 2025년 기준이며, 각 서비스의 빠른 진화 속도를 감안하여 실제 선택 시점에 공식 문서를 재확인해야 합니다. 특히 CrewAI, Claude Agent SDK, Langfuse는 빠르게 발전 중이므로 최신 릴리즈를 확인하세요.
