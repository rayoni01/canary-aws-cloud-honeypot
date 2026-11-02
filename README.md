# AWS Cloud Canary — Deception Detection for Credential Leakage

**Problem:** Developers leak AWS keys in .env files on 【entity-GitHub¦canonical_name=GitHub】. EDR doesn't detect it.

**Design (Thinkst Canarytoken):**
This lab uses a Thinkst Canarytoken AWS key. The key belongs to Thinkst's AWS account. When used, Thinkst detects the usage and alerts via email or webhook. It does NOT appear in your own CloudTrail. This is the correct design for a Canarytoken lab.

Note: `AKIAIOSFODNN7EXAMPLE` is 【entity-AWS¦canonical_name=AWS】's official documentation example key from 【entity-AWS¦canonical_name=AWS】 docs. It's used here as a placeholder only — using it will never trigger a real alert. Replace it with your own Canarytoken AKIA when testing locally.

**Flow:**
1. Generate 【entity-AWS¦canonical_name=AWS】 Canarytoken at canarytokens.org (you get a real AKIA)
2. Plant fake key in `fake_project/.env` and `fake_aws_creds/credentials`
3. Simulate attacker: `aws s3 ls` with fake key -> Triggers Thinkst
4. Detection: Thinkst sends webhook -> `handle_canary_webhook.py` parses memo, src_ip, user-agent

**What this repo contains:**
- `deploy_fake_creds.py` — Plants decoy creds in fake project (placeholder keys only)
- `handle_canary_webhook.py` — Parses Thinkst webhook JSON (sample included below)
- `sample_alert.json` — Example alert payload from Thinkst (sample)

**Placement:**
Good places to plant this type of canary: 【entity-GitHub¦canonical_name=GitHub】 repos, Jenkins env files, S3 bucket documentation.

Author: Brian Rayoni — Randburg, SA
