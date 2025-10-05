#!/usr/bin/env bash
set -euo pipefail

echo "=== Snyk IaC scan ==="
snyk iac test k8s/manifests/insecure-deployment.yaml || true

echo "=== Build demo container ==="
cat > Dockerfile <<'EOF'
FROM python:3.10-slim
WORKDIR /app
COPY pulumi/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
CMD ["python","-c","print('hello from demo-app')"]
EOF

docker build -t demo-app:latest .

echo "=== Snyk container scan ==="
snyk container test demo-app:latest || true

echo "Pipeline complete (some steps may have reported issues; fix and rerun)."
