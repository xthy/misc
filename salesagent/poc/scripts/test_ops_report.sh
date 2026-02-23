#!/usr/bin/env bash
# B2B Sales Agent PoC — Weekly Ops Report 테스트 스크립트
#
# 사용법:
#   chmod +x test_ops_report.sh
#   ./test_ops_report.sh                        # 기본 (localhost:5678)
#   ./test_ops_report.sh http://custom:5678     # 커스텀 URL
#
# 테스트 방법:
#   1. n8n API를 통해 workflow를 수동 실행 (Schedule Trigger 대신)
#   2. 또는 webhook test endpoint를 통해 fixture 데이터로 직접 테스트
#
# 주의: Weekly Ops Report는 Schedule Trigger 기반이므로,
#       테스트 시에는 n8n API의 manual execution을 사용합니다.

set -euo pipefail

N8N_URL="${1:-http://localhost:5678}"
N8N_USER="${N8N_USER:-admin}"
N8N_PASSWORD="${N8N_PASSWORD:-salesagent}"
FIXTURE_FILE="$(dirname "$0")/../fixtures/sample_pipeline_data.json"

if [ ! -f "$FIXTURE_FILE" ]; then
  echo "ERROR: Fixture file not found: $FIXTURE_FILE"
  exit 1
fi

echo "================================================"
echo " Weekly Ops Report — Test Runner"
echo "================================================"
echo ""
echo "n8n URL:  ${N8N_URL}"
echo "Fixture:  ${FIXTURE_FILE}"
echo ""

# ─────────────────────────────────────────────
# Method 1: n8n API — Trigger workflow execution
# ─────────────────────────────────────────────
echo "── Method 1: n8n API Manual Execution ──"
echo ""

# First, find the workflow ID by name
echo "Finding workflow 'Weekly Ops Report (PoC v2)'..."
WORKFLOWS_RESPONSE=$(curl -s \
  -u "${N8N_USER}:${N8N_PASSWORD}" \
  -H "Content-Type: application/json" \
  "${N8N_URL}/api/v1/workflows" 2>/dev/null || echo "")

if [ -z "$WORKFLOWS_RESPONSE" ]; then
  echo "WARNING: Could not connect to n8n API. Is n8n running?"
  echo "         Skipping Method 1."
  echo ""
else
  WORKFLOW_ID=$(echo "$WORKFLOWS_RESPONSE" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    workflows = data.get('data', [])
    for w in workflows:
        if 'Weekly Ops Report' in w.get('name', ''):
            print(w['id'])
            break
    else:
        print('')
except:
    print('')
" 2>/dev/null || echo "")

  if [ -n "$WORKFLOW_ID" ]; then
    echo "Found workflow ID: ${WORKFLOW_ID}"
    echo "Triggering manual execution..."
    echo ""

    EXEC_RESPONSE=$(curl -s -w "\n%{http_code}" \
      -u "${N8N_USER}:${N8N_PASSWORD}" \
      -X POST \
      -H "Content-Type: application/json" \
      "${N8N_URL}/api/v1/workflows/${WORKFLOW_ID}/run" 2>/dev/null || echo "")

    HTTP_CODE=$(echo "$EXEC_RESPONSE" | tail -1)
    BODY=$(echo "$EXEC_RESPONSE" | sed '$d')

    echo "HTTP Status: ${HTTP_CODE}"
    if [ "$HTTP_CODE" = "200" ]; then
      echo "SUCCESS — Workflow execution triggered."
      echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
    else
      echo "Response: ${BODY}"
    fi
  else
    echo "WARNING: Workflow not found. Import weekly_ops_report.json first."
  fi
  echo ""
fi

# ─────────────────────────────────────────────
# Method 2: Direct OpenAI API test with fixture
# ─────────────────────────────────────────────
echo "── Method 2: Direct OpenAI API Test ──"
echo ""

OPENAI_API_KEY="${OPENAI_API_KEY:-}"
if [ -z "$OPENAI_API_KEY" ]; then
  echo "OPENAI_API_KEY not set. Skipping direct API test."
  echo "Set it with: export OPENAI_API_KEY=sk-..."
  echo ""
  echo "── Method 3: Fixture Data Preview ──"
  echo ""
  echo "Pipeline data summary from fixture:"
  python3 -c "
import json
with open('${FIXTURE_FILE}') as f:
    data = json.load(f)
s = data['summary']
print(f\"  Period:        {data['report_period']['week_start']} ~ {data['report_period']['week_end']}\")
print(f\"  Pipeline ACV:  \${s['total_pipeline_acv']:,.0f}\")
print(f\"  Open Deals:    {s['total_open_deals']}\")
print(f\"  New Opps:      {s['new_opps_count']} (\${s['new_opps_acv']:,.0f})\")
print(f\"  Stalled:       {s['stalled_deals_count']} (\${s['stalled_deals_acv']:,.0f})\")
print(f\"  Wins:          {s['wins_count']} (\${s['wins_acv']:,.0f})\")
print(f\"  Losses:        {s['losses_count']} (\${s['losses_acv']:,.0f})\")
print(f\"  Win Rate:      {s['win_rate_count']}% (count) / {s['win_rate_acv']}% (ACV)\")
print(f\"  Forecast:      Commit \${s['forecast_commit_acv']:,.0f} / Best Case \${s['forecast_best_case_acv']:,.0f}\")
print(f\"  QTD Closed:    \${s['forecast_closed_won_qtd']:,.0f} (accuracy: {s['forecast_accuracy_pct']}%)\")
print()
print('  Stage Distribution:')
for stage in data['pipeline_by_stage']:
    print(f\"    {stage['stage']:20s}  {stage['deal_count']}건  \${stage['total_acv']:>10,.0f}\")
print()
print('  Stalled Deals:')
for d in data['stalled_deals']:
    print(f\"    [{d['account_tier']}] {d['opportunity_name']:40s}  {d['days_in_stage']}일  \${d['acv']:>10,.0f}  MEDDICC:{d['meddicc_total']}\")
print()
print('  Win/Loss:')
for d in data['win_loss']:
    status = 'WON' if d['outcome'] == 'Closed_Won' else 'LOST'
    print(f\"    {status:4s} {d['opportunity_name']:40s}  \${d['acv']:>10,.0f}  {d['primary_reason']}\")
" 2>/dev/null || echo "  (python3 required for fixture preview)"
  echo ""
  echo "================================================"
  exit 0
fi

echo "Sending fixture data to OpenAI API..."
echo ""

# Build the system prompt
SYSTEM_PROMPT=$(cat "$(dirname "$0")/../prompts/weekly_ops_report.md" | \
  python3 -c "
import sys
content = sys.stdin.read()
# Extract the system prompt between first pair of triple backticks
start = content.find('\`\`\`\n', content.find('## System Prompt'))
end = content.find('\`\`\`', start + 4)
if start >= 0 and end >= 0:
    prompt = content[start+4:end].strip()
    # Escape for JSON
    import json
    print(json.dumps(prompt))
else:
    print('\"\"')
" 2>/dev/null || echo '""')

# Build the user message with fixture data
USER_MSG=$(python3 -c "
import json
with open('${FIXTURE_FILE}') as f:
    data = json.load(f)
msg = f'''다음 파이프라인 데이터를 분석하여 주간 Ops 리포트를 생성하세요.

REPORT PERIOD:
- Week: {data['report_period']['week_start']} ~ {data['report_period']['week_end']}
- Quarter Start: {data['report_period']['quarter_start']}

SUMMARY METRICS:
{json.dumps(data['summary'], indent=2, ensure_ascii=False)}

PIPELINE BY STAGE:
{json.dumps(data['pipeline_by_stage'], indent=2, ensure_ascii=False)}

NEW OPPORTUNITIES THIS WEEK:
{json.dumps(data['new_opportunities'], indent=2, ensure_ascii=False)}

STAGE MOVEMENTS THIS WEEK:
{json.dumps(data['stage_movements'], indent=2, ensure_ascii=False)}

STALLED DEALS (>30 DAYS IN STAGE):
{json.dumps(data['stalled_deals'], indent=2, ensure_ascii=False)}

WIN/LOSS THIS WEEK:
{json.dumps(data['win_loss'], indent=2, ensure_ascii=False)}

FORECAST (CURRENT QUARTER):
{json.dumps(data['forecast'], indent=2, ensure_ascii=False)}

TOP 10 DEALS BY ACV:
{json.dumps(data['top_deals'], indent=2, ensure_ascii=False)}

위 데이터를 기반으로 주간 리포트를 JSON 형식으로 반환하세요.'''
print(json.dumps(msg, ensure_ascii=False))
" 2>/dev/null || echo '""')

# Call OpenAI API
OPENAI_RESPONSE=$(curl -s -w "\n%{http_code}" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${OPENAI_API_KEY}" \
  -d "{
    \"model\": \"gpt-4o\",
    \"max_tokens\": 4096,
    \"temperature\": 0.2,
    \"messages\": [
      { \"role\": \"system\", \"content\": ${SYSTEM_PROMPT} },
      { \"role\": \"user\", \"content\": ${USER_MSG} }
    ]
  }" \
  "https://api.openai.com/v1/chat/completions")

HTTP_CODE=$(echo "$OPENAI_RESPONSE" | tail -1)
BODY=$(echo "$OPENAI_RESPONSE" | sed '$d')

echo "HTTP Status: ${HTTP_CODE}"
echo ""

if [ "$HTTP_CODE" = "200" ]; then
  echo "SUCCESS — OpenAI Generated Report:"
  echo ""
  # Extract and pretty-print the content
  echo "$BODY" | python3 -c "
import sys, json
resp = json.load(sys.stdin)
content = resp.get('choices', [{}])[0].get('message', {}).get('content', '')
# Try to parse as JSON for pretty printing
try:
    report = json.loads(content)
    print(json.dumps(report, indent=2, ensure_ascii=False))
except:
    print(content)
print()
usage = resp.get('usage', {})
print(f\"Tokens: input={usage.get('prompt_tokens', 'N/A')}, output={usage.get('completion_tokens', 'N/A')}\")
" 2>/dev/null || echo "$BODY"
else
  echo "ERROR — Response:"
  echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
fi

echo ""
echo "================================================"
