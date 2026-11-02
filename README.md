# AWS Cloud Canary — Deception Detection for Credential Leakage

**Problem:** Developers leak AWS keys in `.env` files on GitHub. EDR doesn't detect it.

**Design (Thinkst Canarytoken):** This lab uses a Thinkst Canarytoken AWS key. The key belongs to Thinkst's AWS account. When used, Thinkst detects the usage and alerts via email or webhook. It does not appear in your own CloudTrail. A lab that shows in your own CloudTrail would instead use a honey IAM user in your own AWS account, which is a different design.

**Note:** `AKIAIOSFODNN7EXAMPLE` is the official example key from the AWS documentation. It is used here as a placeholder only and will never trigger a real alert. Replace it with your own Canarytoken AKIA key when testing locally.

## Flow
1. Generate an AWS Canarytoken at canarytokens.org (you get a real AKIA key)
2. Plant the key in `fake_project/.env` and `fake_aws_creds/credentials`
3. Simulate an attacker: `aws s3 ls` with the key, which triggers Thinkst
4. Detection: Thinkst sends a webhook, and `handle_canary_webhook.py` parses memo, src_ip and user-agent

## What this repo contains
- `deploy_fake_creds.py`: plants decoy creds in a fake project (placeholder keys only)
- `handle_canary_webhook.py`: parses the Thinkst webhook JSON
- `sample_alert.json`: example alert payload (sample)

## Limitations
- The handler prints the alert. A Slack post is included only as a commented example.
- No SentinelOne or other response integration is implemented here.

**Placement:** good places to plant this type of canary are GitHub repos, Jenkins env files and S3 bucket documentation. MITRE: T1552.001 Credentials in Files.

Author: Brian Rayoni, Randburg, SA
