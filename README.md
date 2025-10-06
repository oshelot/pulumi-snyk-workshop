# Pulumi + Snyk Workshop (Python)

Hands-on lab showing shift-left security with Snyk (IaC + container) and Pulumi (policy as code + ESC secrets).

# Workshop Abstract  
**Title:** Shift-Left Security Hands-On: Pulumi + Snyk Golden Path 
**Audience:** Platform & Security Engineers (beginner–intermediate IaC)  
**Duration:** 45–60 minutes  

## Overview  
This hands-on workshop demonstrates how **Pulumi** and **Snyk** work better together to “shift left” on security without slowing developers down. Participants will explore how insecure infrastructure is detected and remediated *before* it reaches production using Snyk’s IaC and container scanning capabilities, along with Pulumi’s policy-as-code guardrails and secure configuration management via Pulumi ESC.  

By the end of the session, learners will understand how to create and enforce **secure golden paths**—developer-friendly templates that automatically embed security, compliance, and secrets management into every deployment.  

## Objectives  
- Identify and remediate insecure IaC configurations using **Snyk IaC scans**.  
- Detect vulnerabilities in container images during CI/CD pipelines.  
- Enforce **Pulumi CrossGuard policies** to block misconfigurations at deploy time.  
- Use **Pulumi ESC** to eliminate plaintext secrets in code.  
- Understand how Pulumi and Snyk together deliver **defense-in-depth**: pre-commit → PR → deploy → runtime.  

## Key Takeaways  
- **Shift-left security:** catch issues early in the development cycle where they’re cheapest to fix.  
- **Consistent guardrails:** policy-as-code ensures all infrastructure meets org standards.  
- **Secrets made safe:** Pulumi ESC provides environment-scoped secrets instead of hardcoded credentials.  
- **Golden path enablement:** developers move fast and stay secure using pre-approved Pulumi templates.  

## Prerequisites  
- Basic familiarity with cloud infrastructure and Python.  
- Pulumi and Snyk accounts (free tier is sufficient).  
- Browser-based Instruqt environment (no local setup required).  


## Prereqs (Installed in Instruqt)
- Node.js or Python runtime (Python 3.10+)
- Pulumi CLI
- Snyk CLI (authenticated: `snyk auth`)
- Docker daemon (for container scan)
- Pulumi Cloud with ESC enabled

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

