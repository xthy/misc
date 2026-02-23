#!/usr/bin/env bash
# B2B Sales Agent PoC — Lead Enrichment & ICP Scoring 테스트 스크립트
#
# Usage:
#   chmod +x test_lead_enrich.sh
#   ./test_lead_enrich.sh                     # 기본 (localhost:5678)
#   ./test_lead_enrich.sh http://custom:5678  # 커스텀 URL

set -euo pipefail

N8N_URL="${1:-http://localhost:5678}"
WEBHOOK_PATH="/webhook/lead-enrich"
FIXTURE_FILE="$(dirname "$0")/../fixtures/sample_new_account.json"

if [ ! -f "$FIXTURE_FILE" ]; then
  echo "ERROR: Fixture file not found: $FIXTURE_FILE"
  exit 1
fi

echo "================================================"
echo " Lead Enrichment & ICP Scoring — Webhook Test"
echo "================================================"
echo ""
echo "Target: ${N8N_URL}${WEBHOOK_PATH}"
echo "Fixture: ${FIXTURE_FILE}"
echo ""
echo "Sending new account data for enrichment & scoring..."
echo ""

# Send the webhook
RESPONSE=$(curl -s -w "\n%{http_code}" \
  -X POST \
  -H "Content-Type: application/json" \
  -d @"$FIXTURE_FILE" \
  "${N8N_URL}${WEBHOOK_PATH}")

# Split response body and HTTP status code
HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | sed '$d')

echo "HTTP Status: ${HTTP_CODE}"
echo ""

if [ "$HTTP_CODE" -eq 200 ]; then
  echo "SUCCESS — Lead Enrichment & ICP Scoring Result:"
  echo ""

  # Pretty-print JSON and extract key scores
  echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"

  echo ""
  echo "────────────────────────────────────────────────"
  echo " Score Summary"
  echo "────────────────────────────────────────────────"

  # Extract scores using python3
  python3 -c "
import json, sys
try:
    data = json.loads('''$BODY''')
    print(f\"  Company:     {data.get('company_name', 'N/A')}\")
    print(f\"  Fit Score:   {data.get('fit_score', 'N/A')}/100 ({data.get('fit_grade', 'N/A')}-Fit)\")
    print(f\"  Intent:      {data.get('intent_score', 'N/A')}/30\")
    print(f\"  Engagement:  {data.get('engagement_score', 'N/A')}/30\")
    print(f\"  Total Score: {data.get('total_score', 'N/A')}/160\")
    print(f\"  Grade:       {data.get('action_grade', 'N/A')}\")
    print(f\"  Tier:        {data.get('tier', 'N/A')}\")
    print(f\"  Action:      {data.get('recommended_action', 'N/A')}\")
except Exception as e:
    print(f'  (Could not parse summary: {e})')
" 2>/dev/null || true

else
  echo "ERROR — Response:"
  echo "$BODY"
fi

echo ""
echo "================================================"
