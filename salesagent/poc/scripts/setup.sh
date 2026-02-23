#!/usr/bin/env bash
# B2B Sales Agent PoC — Initial Setup Script
#
# Usage:
#   chmod +x setup.sh
#   ./setup.sh

set -euo pipefail

POC_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "================================================"
echo " B2B Sales Agent PoC — Setup"
echo "================================================"
echo ""

# 1. Check prerequisites
echo "[1/5] Checking prerequisites..."

check_cmd() {
  if ! command -v "$1" &> /dev/null; then
    echo "  ERROR: $1 not found. Please install $1 first."
    exit 1
  else
    echo "  OK: $1 found"
  fi
}

check_cmd docker
check_cmd curl

# Check Docker daemon
if ! docker info &> /dev/null 2>&1; then
  echo "  ERROR: Docker daemon is not running. Please start Docker."
  exit 1
fi
echo "  OK: Docker daemon running"
echo ""

# 2. Create .env file
echo "[2/5] Setting up environment..."
if [ ! -f "$POC_DIR/.env" ]; then
  cp "$POC_DIR/.env.example" "$POC_DIR/.env"
  echo "  Created .env from .env.example"
  echo "  IMPORTANT: Edit $POC_DIR/.env with your API keys before starting."
else
  echo "  .env already exists, skipping"
fi
echo ""

# 3. Start services
echo "[3/5] Starting Docker services..."
cd "$POC_DIR"
docker compose up -d
echo ""

# 4. Wait for services to be healthy
echo "[4/5] Waiting for services to be ready..."
MAX_WAIT=60
ELAPSED=0
while [ $ELAPSED -lt $MAX_WAIT ]; do
  if curl -s -o /dev/null -w "%{http_code}" http://localhost:5678/healthz 2>/dev/null | grep -q "200"; then
    echo "  n8n is ready!"
    break
  fi
  sleep 2
  ELAPSED=$((ELAPSED + 2))
  echo "  Waiting... (${ELAPSED}s)"
done

if [ $ELAPSED -ge $MAX_WAIT ]; then
  echo "  WARNING: n8n may not be fully ready yet. Check: docker compose logs n8n"
fi

# Check PostgreSQL
if docker compose exec -T postgres pg_isready -U salesagent &>/dev/null; then
  echo "  PostgreSQL is ready!"
else
  echo "  WARNING: PostgreSQL may not be ready. Check: docker compose logs postgres"
fi
echo ""

# 5. Summary
echo "[5/5] Setup complete!"
echo ""
echo "================================================"
echo " Next Steps:"
echo "================================================"
echo ""
echo "  1. Edit API keys:  vim $POC_DIR/.env"
echo "  2. Open n8n:       http://localhost:5678"
echo "     User: admin / Password: salesagent"
echo "  3. Import workflow: Upload poc/workflows/post_call_crm_updater.json"
echo "  4. Configure credentials in n8n:"
echo "     - OpenAI API (GPT-4o)"
echo "     - PostgreSQL (localhost:5432, salesagent/salesagent_dev)"
echo "     - Slack Webhook (optional)"
echo "  5. Activate the workflow"
echo "  6. Test: ./scripts/test_webhook.sh"
echo ""
echo "  Logs:    docker compose logs -f"
echo "  Stop:    docker compose down"
echo "  Reset:   docker compose down -v  (deletes data!)"
echo ""
