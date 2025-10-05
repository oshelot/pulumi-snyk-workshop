# Pulumi + Snyk Workshop (Python)

Hands-on lab showing shift-left security with Snyk (IaC + container) and Pulumi (policy as code + ESC secrets).

## Prereqs (locally or in Instruqt image)
- Node.js or Python runtime (Python 3.10+)
- Pulumi CLI
- Snyk CLI (authenticated: `snyk auth`)
- Docker daemon (for container scan)
- Optional: Pulumi Cloud with ESC enabled

## Quick Start
```bash
# 1) Snyk IaC
snyk iac test k8s/manifests/insecure-deployment.yaml

# 2) Pipeline simulation (IaC + container)
bash run-pipeline.sh

# 3) Pulumi policies and deploy (Python)
cd pulumi
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pulumi stack init tech-challenge/obs-sec-lab
pulumi preview --policy-pack ./policy
# fix __main__.py until policies pass
pulumi up
