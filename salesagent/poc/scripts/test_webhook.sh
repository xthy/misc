#!/usr/bin/env bash
# B2B Sales Agent PoC — Post-Call CRM Updater 테스트 스크립트
#
# Usage:
#   chmod +x test_webhook.sh
#   ./test_webhook.sh                     # 기본 (localhost:5678)
#   ./test_webhook.sh http://custom:5678  # 커스텀 URL

set -euo pipefail

N8N_URL="${1:-http://localhost:5678}"
WEBHOOK_PATH="/webhook/post-call"
FIXTURE_FILE="$(dirname "$0")/../fixtures/sample_transcript.json"

if [ ! -f "$FIXTURE_FILE" ]; then
  echo "ERROR: Fixture file not found: $FIXTURE_FILE"
  exit 1
fi

echo "================================================"
echo " Post-Call CRM Updater — Webhook Test"
echo "================================================"
echo ""
echo "Target: ${N8N_URL}${WEBHOOK_PATH}"
echo "Fixture: ${FIXTURE_FILE}"
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
  echo "SUCCESS — MEDDICC Extraction Result:"
  echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
else
  echo "ERROR — Response:"
  echo "$BODY"
fi

echo ""
echo "================================================"
