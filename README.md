# AWS Cloud Canary — Deception Detection for Credential Leakage

**Problem:** Developers leak AWS keys in .env files on 【entity-GitHub¦canonical_name=GitHub】. EDR doesn't detect it.

**Design (Thinkst Canarytoken):**
This lab uses a Thinkst Canarytoken AWS key. The key belongs to Thinkst's AWS account. When used, Thinkst detects the usage and alerts via email/webhook — it does NOT appear in your own CloudTrail. This is the correct design for a Canarytoken lab.

If you want a lab that shows in your own CloudTrail, create your own honey IAM user in your own AWS account instead — that is a different design.

**Flow:**
1. Generate AWS Canarytoken at canarytokens.org (AKIA...)
2. Plant fake key in `fake_project/.env` and fake credentials file
3. Simulate attacker: `aws s3 ls` with fake key -> Triggers Thinkst
4. Detection: Thinkst sends webhook -> Python parser logs src_ip, user-agent

**What this repo contains:**
- `deploy_fake_creds.py` — Plants decoy creds in fake project
- `handle_canary_webhook.py` — Parses Thinkst webhook JSON (sample included)
- `sample_alert.json` — Example alert from Thinkst

**Placement:**
Good places to plant this type of canary: 【entity-GitHub¦canonical_name=GitHub】 repos, Jenkins env files, S3 bucket documentation.

Author: Brian Rayoni — Randburg, SA
