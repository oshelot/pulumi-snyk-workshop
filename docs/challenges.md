# Workshop Challenges

This workshop walks you through a complete **shift-left security journey** using **Pulumi** and **Snyk** — from early misconfiguration detection to secure deployments and runtime monitoring.  
Each challenge builds on the previous one, showing how developers, platform engineers, and security teams can collaborate using shared tools and guardrails.

---

## Challenge 1 — Developer & CI: Find the Misconfiguration (Snyk IaC)

**Goal:** Experience how Snyk identifies insecure configurations before deployment.

### Scenario
You’ve inherited an insecure Kubernetes manifest that exposes a container to unnecessary risk. Using Snyk, you’ll detect and fix the issues before merging the code.

### Instructions
1. Open the repo and navigate to the Kubernetes manifest:
   ```bash
   cd k8s/manifests
   snyk iac test insecure-deployment.yaml
   ```
2. Review the Snyk output — look for issues like:
   - Public container image (`nginx:latest`)
   - Running as root (`runAsUser: 0`)
   - No resource limits defined
3. Fix one or more findings and re-run the scan until it passes or severity drops.

**Learning Outcome:**  
Early feedback from Snyk reduces risk by catching misconfigurations before code is merged or deployed.

---

## Challenge 2 — Build & Scan: Container Vulnerabilities (Snyk Container)

**Goal:** Use Snyk to find vulnerabilities in container images before pushing to production.

### Scenario
Your CI/CD pipeline builds an application container. Snyk scans the image for vulnerabilities in OS packages and dependencies, blocking unsafe deployments.

### Instructions
1. Run the simulated pipeline script:
   ```bash
   bash run-pipeline.sh
   ```
2. Observe Snyk’s container scan results — note any High or Critical vulnerabilities.
3. Modify the Dockerfile base image to a safer version (e.g., `python:3.10-slim`) and re-run the script.

**Learning Outcome:**  
Shift-left container scanning ensures vulnerable images are caught during build, not after deployment.

---

## Challenge 3 — Pulumi Guardrails: Policies Block Insecure Resources

**Goal:** See Pulumi CrossGuard prevent insecure infrastructure from deploying.

### Scenario
You’re deploying a simple AWS S3 bucket, but organizational policy requires encryption and tags. Pulumi’s policy-as-code will block non-compliant resources during preview.

### Instructions
1. From the `pulumi/` directory, initialize a stack and run a preview with policies:
   ```bash
   cd pulumi
   pulumi stack init tech-challenge/obs-sec-lab
   pulumi preview --policy-pack ./policy
   ```
2. Review policy violations:
   - Missing server-side encryption  
   - Missing required `env` tag  
3. Edit `__main__.py` to enable encryption and add tags, then re-run preview.  
4. When all policies pass, deploy:
   ```bash
   pulumi up
   ```

**Learning Outcome:**  
Pulumi CrossGuard enforces compliance automatically — turning organizational best practices into codified rules.

---

## Challenge 4 — Pulumi ESC: No Plaintext Secrets

**Goal:** Use Pulumi ESC (Environments, Secrets, Config) to manage secrets securely.

### Scenario
Developers often hardcode secrets in code or config files. Pulumi ESC provides a secure and scalable way to manage secrets across environments.

### Instructions (Option A — with ESC)
1. In Pulumi Cloud, create an ESC environment (e.g., `workshop/dev`).
2. Add a secret key `db.password` with a random value.
3. Link your stack to this environment in Pulumi Cloud.
4. In code, access it via:
   ```python
   import pulumi
   cfg = pulumi.Config()
   db_password = cfg.require_secret("db.password")
   ```
5. Confirm deployment succeeds without ever exposing the secret.

### Instructions (Option B — fallback local secrets)
1. Set a per-stack secret and deploy:
   ```bash
   pulumi config set --secret db.password "S3cret!"
   pulumi config get db.password   # shows [secret]
   pulumi preview && pulumi up
   ```

**Learning Outcome:**  
Pulumi ESC eliminates plaintext secrets by securely injecting environment-specific config at deploy time.

---

## Challenge 5 — (Optional) Runtime Posture: Continuous Monitoring

**Goal:** Extend the golden path to runtime visibility using Snyk monitor.

### Scenario
You’ve deployed secure infrastructure, but security doesn’t stop at deployment. Snyk can continuously monitor your deployed resources and container images for new vulnerabilities.

### Instructions
1. After successful deployment, run:
   ```bash
   snyk monitor
   ```
2. View the simulated dashboard tile in the workshop to see runtime posture.

**Learning Outcome:**  
Continuous scanning ensures that the same security standards persist after deployment.

---

## Workshop Takeaways

- Experience both static scanning (**Snyk**) and policy enforcement (**Pulumi**).  
- Learn to secure secrets with **Pulumi ESC**.  
- See how **Pulumi + Snyk** provide a full shift-left, defense-in-depth workflow.  
- Download a starter repo integrating IaC scans, policy packs, and ESC secrets.
