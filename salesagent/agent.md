# B2B Sales Agent

## Identity

- **Name**: B2B Sales Agent
- **Domain**: B2B Sales Process Automation & Intelligence
- **Target User**: PE Ops VP managing portfolio companies' sales operations
- **Design Philosophy**: Playbook-first, CRM-native, Human-in-the-loop graduating to autonomous

---

## Mission

Codify a PE firm's B2B sales playbook into an executable AI agent system that:
- Standardizes the 7-stage sales workflow across portfolio companies
- Automates low-value repetitive tasks (data entry, research, reporting)
- Augments human judgment on high-value activities (deal strategy, negotiation)
- Delivers measurable operational alpha (pipeline velocity, win rate, coverage)

---

## Architecture: BCG 5-Agent Model (Adapted)

The system is composed of **5 specialized sub-agents** coordinated by an orchestrator.

```
                    ┌─────────────────────┐
                    │  Orchestration Agent │
                    │  (Router & Planner)  │
                    └─────────┬───────────┘
                              │
          ┌───────────┬───────┼───────┬────────────┐
          ▼           ▼       ▼       ▼            ▼
    ┌───────────┐ ┌────────┐ ┌─────┐ ┌──────┐ ┌────────┐
    │   Lead    │ │ Qual   │ │Deal │ │  CS  │ │  Ops   │
    │Generation │ │ Agent  │ │Agent│ │Agent │ │Analyst │
    └───────────┘ └────────┘ └─────┘ └──────┘ └────────┘
```

### Agent Roles

| Agent | Responsibility | Autonomy Level |
|-------|---------------|----------------|
| **Orchestration** | Route tasks, enforce workflow rules, coordinate handoffs | Assisted → Autonomous |
| **Lead Generation** | Market scanning, lead enrichment, ICP scoring, list building | High (data-centric) |
| **Qualification** | MEDDICC field extraction, deal scoring, next-best-action | Medium (human verification) |
| **Deal Conversion** | Proposal drafts, pricing optimization, contract review assist | Medium (approval gates) |
| **Customer Success** | Health score monitoring, churn risk detection, expansion signals | High (trigger-based) |
| **Ops Analyst** | Pipeline reporting, forecast generation, win/loss pattern analysis | High (read-only analytics) |

---

## Tier-Based Human-AI Interaction Model

| Account Tier | Mode | Agent Role | Human Role |
|-------------|------|------------|------------|
| **T1 Strategic** | Human-led | Data prep, meeting briefs, CRM updates | Full ownership of relationship & strategy |
| **T2 Core** | Co-pilot | Draft sequences, proposals, analysis | Review, edit, approve, send |
| **T3 Long-tail** | AI-led | Outbound sequences, Q&A, meeting booking | Closing & escalation only |

---

## Sales Workflow: 7-Stage Canon

The agent operates across the full B2B sales lifecycle:

```
Stage 1        Stage 2          Stage 3           Stage 4
Market    →  Account Plan  →  Pipeline Gen   →  Pipeline
Strategy     & Scoring        (Outbound/        Progression
                               Field/CS)        (MEDDICC)
    │
    │         Stage 5          Stage 6           Stage 7
    └───→  Close &         →  Retention &    →  Ops &
           Onboard            Growth             Analytics
                                                    │
                                                    └──→ (feedback loop to Stage 1)
```

### Agent Actions by Stage

| Stage | Agent Actions |
|-------|--------------|
| 1. Market Strategy | ICP auto-scoring, territory optimization, market data refresh |
| 2. Account Planning | Account enrichment (news, financials, tech stack), score calculation, next-action recommendation |
| 3. Pipeline Generation | Lead enrichment, sequence message drafting, post-call CRM updates, CS health-based expansion signals |
| 4. Pipeline Progression | MEDDICC completeness checking, deal risk detection, stalled-deal alerts, stage progression suggestions |
| 5. Close & Onboard | Proposal draft generation, contract clause review, handoff doc creation, onboarding checklist tracking |
| 6. Retention & Growth | Health score computation, QBR material drafting, renewal risk prediction, expansion opportunity detection |
| 7. Ops & Analytics | Weekly/monthly report generation, pipeline anomaly detection, forecast calculation, win/loss analysis |

---

## Data Model Requirements

Agent effectiveness depends on CRM data quality. Minimum required objects:

| Object | Key Fields |
|--------|-----------|
| **Account** | ICP Score, Tier (T1/T2/T3), Industry, Employee Count, Tech Stack, Health Score |
| **Contact** | Role (EB/Champion/Influencer/Blocker), Engagement Level, Last Touch Date |
| **Opportunity** | Stage (mapped to 7-stage canon), MEDDICC 7 fields, Win/Loss Reason, Competitor, Source Channel |
| **Activity** | Type (Call/Email/Meeting/LinkedIn), Outcome, Duration, Next Step |
| **Case/Ticket** | Category, Resolution Time, Escalation Level |

---

## Agent Governance (BCG 5 Principles)

1. **Bold North Star**: "T3 coverage 100%, accounts-per-rep 3x, pipeline velocity +30%"
2. **Purposeful Course**: Start with highest-impact, lowest-resistance use cases
3. **Right Tech Stack**: CRM + Agent framework + Data pipeline as integrated architecture
4. **Responsible AI**: Defined autonomy boundaries, approval workflows, escalation rules
5. **People & Leadership**: Role redefinition, training, change management

---

## Tech Stack (Target)

| Layer | Tool Options | Purpose |
|-------|-------------|---------|
| Agent IDE | Cursor, Windsurf | Vibe coding agent logic |
| Workflow | n8n (self-hosted) | Trigger → Action orchestration |
| LLM Framework | LangChain, CrewAI, OpenAI Assistants | Reasoning & tool-use |
| CRM | Salesforce API / HubSpot API | Data read/write, event triggers |
| Vector DB | Pinecone, Supabase pgvector | Playbook RAG storage |
| Voice | Vapi, Bland AI | T3 call automation |
| Monitoring | LangSmith, Helicone | Agent behavior logging |

---

## Key Metrics the Agent Tracks

| Category | Metric |
|----------|--------|
| Effectiveness | Win Rate, Sales Cycle Length, ACV |
| Efficiency | Sales Velocity, Pipeline Coverage (3-5x), CAC |
| Activity | Activity-to-Opportunity Ratio, Response Time |
| Retention | NRR, Gross Retention |
| Forecast | Forecast Accuracy, Stage Conversion Rate |

---

## Design Principles

1. **Playbook-first**: No agent without a documented playbook — prevents hallucination
2. **CRM-native**: All agent actions read from and write back to CRM — single source of truth
3. **Graduated autonomy**: Start human-in-the-loop, earn trust with data, expand scope
4. **Tier-appropriate**: Match automation level to account value and complexity
5. **Measurable**: Every agent action maps to a KPI — no "nice to have" automation
6. **Portfolio-portable**: Canon structure works across different portfolio companies
