# B2B Sales Agent — Project Scope

## Overview

Build an AI agent system that operationalizes a PE firm's B2B sales playbook across portfolio companies. The agent automates data-intensive tasks, augments human decision-making, and progressively takes ownership of low-tier account management.

---

## In Scope

### Phase 1: Foundation — Sales Canon & Playbook (Month 1-3)

**Goal**: Establish the standard workflow and playbook that the agent will execute.

| Deliverable | Description |
|-------------|-------------|
| Sales Process Canon | 7-stage B2B workflow definition (standardized across portfolio) |
| ICP Framework | Ideal Customer Profile criteria: Firmographic + Technographic + Needs-based |
| Account Tiering Model | T1/T2/T3 classification rules and coverage model |
| Segmentation Standard | TAM → SAM → SOM analysis template with dual scoring |
| KPI Set | Core metrics per stage (win rate, velocity, coverage, NRR, etc.) |

**Key References**: KPMG PE Value Creation, Revenue Architecture (Jacco van der Kooij), PE Alpha GTM Playbook

### Phase 2: Playbook Documentation (Month 3-5)

**Goal**: Write executable play documents that directly translate to agent specs.

| Deliverable | Description |
|-------------|-------------|
| Top 5 Plays (v1) | Each in Input → Process → Output → Metric → Tool/Agent structure |
| Call Scripts | SPIN Selling & Gap Selling based discovery question frameworks |
| Email Templates | Outbound cadence templates by persona and tier |
| MEDDICC Field Guide | Qualification framework with CRM field mapping |
| Objection Handling Guide | Common objections with response scripts by deal type |

**Priority Plays**:
1. New Logo Outbound (T2/T3) — highest automation ROI
2. Strategic Account Expansion (T1) — human-led + agent assist
3. Renewal Rescue — health score trigger based
4. CS-driven Upsell — CS → AE handoff automation
5. Win/Loss Analysis — quarterly pattern analysis

**Key References**: Salesforce Playbook Guide, MEDDICC (Andy Whyte), Gap Selling (Keenan), Predictable Revenue (Aaron Ross)

### Phase 3: CRM Data Model & Infrastructure (Month 4-6)

**Goal**: Align CRM schema with playbook so agents can read/write accurately.

| Deliverable | Description |
|-------------|-------------|
| CRM Schema Standard | Object/field definitions aligned to 7-stage canon + MEDDICC |
| Dashboard Set | Win rate, sales velocity, pipeline coverage, forecast accuracy |
| Tagging System | Win/Loss reason, Source/Channel, Competitor tags for agent learning |
| Data Quality Rules | Required field governance, stage transition validation |
| Integration Mapping | API endpoints needed for agent read/write operations |

**Key References**: Noltic RevOps Metrics, Salesforce Sales Operations Guide

### Phase 4: Agent PoC Build (Month 5-9)

**Goal**: Build and validate first working agents with human-in-the-loop.

| Deliverable | Description |
|-------------|-------------|
| Agent v1: Post-Call CRM Updater | Call transcript → MEDDICC field extraction → CRM update draft → human approval |
| Agent v2: Weekly Ops Report | Auto-generate pipeline analysis, stalled deals, forecast vs actual |
| Agent v3: Lead Enrichment | Account data auto-collection (news, financials, tech stack) → ICP scoring |
| Playbook RAG Store | Vectorized playbook content for agent reference |
| System Prompts | Documented prompts per agent with tool definitions |

**Tech**: n8n (workflow) + OpenAI/Claude API (LLM) + CRM API (data) + pgvector (RAG)

**Key References**: n8n AI Sales Agent Tutorial, Cursor + n8n HubSpot Workflow, Build Your First AI Agent (Vibe Coding Blueprint)

### Phase 5: Scale & Portfolio Deploy (Month 9-12+)

**Goal**: Expand agent autonomy and deploy across portfolio.

| Deliverable | Description |
|-------------|-------------|
| T3 Autonomous Outbound | AI-led outbound sequences, Q&A, meeting booking |
| Cross-portfolio Deployment | Canon-based customization per portfolio company |
| Quarterly Review Process | Win/loss driven playbook & prompt updates |
| Agent Monitoring Dashboard | Behavior logs, cost tracking, quality metrics |
| Agent Governance Docs | Autonomy boundaries, escalation rules, approval workflows |

---

## Out of Scope (for now)

| Item | Reason |
|------|--------|
| Custom CRM development | Use existing Salesforce/HubSpot — no new CRM build |
| Marketing automation | Focus on sales process only; marketing is a separate workstream |
| Product-led growth (PLG) | This agent targets sales-led B2B, not self-serve |
| Real-time voice AI for T1 | T1 accounts stay human-led; voice AI only for T3 later |
| Custom LLM training/fine-tuning | Use foundation models + RAG; fine-tuning only if RAG proves insufficient |
| Compensation/incentive design | Sales comp is an adjacent but separate workstream |
| Legal contract automation | Agent assists with clause review, but no automated contract execution |

---

## Work Steps (Recommended Execution Order)

```
Step  What                           Output                          Gate
─────────────────────────────────────────────────────────────────────────────
 1    Map current sales process       As-is process doc               Review
 2    Define 7-stage canon            Sales Process Canon v1          Approve
 3    Build ICP + Tiering model       Scoring criteria + tier rules   Approve
 4    Write Top 5 Plays               Playbook v1 (5 plays)          Review
 5    Design CRM schema               Object/field spec              Approve
 6    Build CRM dashboards            Core dashboard set              Demo
 7    Set up n8n + LLM infra          Working dev environment         Verify
 8    Build Agent PoC #1              Post-Call CRM Updater           Demo
      (Post-Call Updater)
 9    Build Agent PoC #2              Weekly Ops Report Generator     Demo
      (Ops Reporter)
10    Build Agent PoC #3              Lead Enrichment + ICP Scorer    Demo
      (Lead Enrichment)
11    Vectorize playbook (RAG)        Playbook in vector DB           Verify
12    User testing & iteration        Feedback log + prompt updates   Review
13    T3 autonomous outbound pilot    Outbound agent live on T3       Approve
14    Portfolio rollout planning      Deployment plan per portco      Approve
15    Deploy + monitor                Live agents + monitoring        Ongoing
```

---

## Success Criteria

| Metric | Target | Timeframe |
|--------|--------|-----------|
| T3 account coverage | 100% (from ~30%) | Month 12 |
| Accounts per rep | 3x current | Month 12 |
| CRM data completeness (MEDDICC) | >80% fields filled | Month 9 |
| Pipeline velocity improvement | +30% | Month 12 |
| Rep time saved on admin | 10+ hrs/week | Month 9 |
| Post-call CRM update rate | >90% within 24hrs | Month 6 |
| Forecast accuracy | <15% variance | Month 12 |

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Playbook not defined before agent build | Agent hallucinates, inconsistent outputs | Phase 1-2 are hard prerequisites for Phase 4 |
| CRM data quality too low | Agent can't read/write accurately | Phase 3 enforces field governance before agent launch |
| MEDDICC adoption decay (40-50% in 6mo) | Pipeline progression breaks down | Agent provides continuous nudges and compliance alerts |
| Over-automating T1 accounts | Damages strategic relationships | Strict tier-based autonomy rules; T1 stays human-led |
| Rep resistance to AI | Low adoption, workarounds | Start with "time-saver" agents (Post-Call Updater), not "replacement" agents |
| LLM cost at scale | Budget overrun | Monitor via LangSmith/Helicone; optimize prompt length; cache common queries |

---

## Dependencies

- **CRM access**: Admin-level API access to Salesforce or HubSpot
- **Call recording**: Gong, Chorus, or equivalent transcript source
- **Sales leadership buy-in**: For playbook standardization and process change
- **LLM API access**: OpenAI and/or Anthropic API keys
- **Infrastructure**: Server for n8n self-hosting (or cloud instance)

---

## Assumptions

1. At least one portfolio company is willing to serve as the pilot
2. Existing CRM (Salesforce or HubSpot) is in use — no greenfield CRM needed
3. Sales team has basic CRM hygiene (>50% field completion as baseline)
4. Call recordings or transcripts are available for the Post-Call agent
5. PE Ops VP has authority to mandate process standardization across portfolio
