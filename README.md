# AWS Cloud Canary — Deception Detection for Credential Leakage

**Problem:** Developers leak AWS keys in `.env` files on GitHub. EDR doesn't detect it.

**Design (Thinkst Canarytoken):** 
This lab uses a Thinkst Canarytoken 【entity-AWS¦canonical_name=AWS】 key. The key belongs to Thinkst's 【entity-AWS¦canonical_name=AWS】 account. When used, Thinkst detects the usage and alerts via email or webhook. It does NOT appear in your own CloudTrail. A lab that shows in your own CloudTrail would use a honey IAM user in your own 【entity-AWS¦canonical_name=AWS】 account — that is a different design.

**Note:** `AKIAIOSFODNN7EXAMPLE` is the official example key from the AWS documentation. It is used here as a placeholder only and will never trigger a real alert. Replace it with your own Canarytoken AKIA key when testing locally.

## Flow
1. Generate an AWS Canarytoken at canarytokens.org (you get a real AKIA key)
2. Plant the key in `fake_project/.env` and `fake_aws_creds/credentials`
3. Simulate an attacker: `aws s3 ls` or `sts get-caller-identity` with the key, which triggers Thinkst
4. Detection: Thinkst sends webhook/email, and `handle_canary_webhook.py` parses memo, src_ip and user-agent

## Proof — Real Thinkst Canarytoken Trigger

This lab is built around a real Thinkst Canarytoken AWS key.

![Real Canarytoken Alert](canary-aws-alert.png)

**Live trigger from this lab:**
- **Reminder / Memo:** svc_finance_backup-canary - fake_project dev laptop - rayoni01 lab
- **Source IP:** 197.184.181.200
- **Event:** GetCallerIdentity via Boto3/1.43.123 on Windows 11, Python 3.13.13
- **Time:** 2026/11/02 08:34 UTC
- **Canarytoken ID:** 5lr045aorr7s45vf4rl7uhi5n

Triggered via Python boto3 `sts.get_caller_identity()` — alert received in under 60 seconds via Thinkst Canarytokens infrastructure.

## What this repo contains
- `deploy_fake_creds.py` — plants decoy creds in a fake project (placeholder keys only)
- `handle_canary_webhook.py` — parses the Thinkst webhook JSON (sample included)
- `sample_alert.json` — example alert payload (sample)
- `canary-aws-alert.png` — real alert screenshot from live trigger above

## Limitations
- The handler prints and logs the alert. A Slack post is included only as a commented example with XXXX placeholder.
- No SentinelOne or other response integration is implemented in this repo — workflow formatting only.

**Placement:** Good places to plant this type of canary are GitHub repos, Jenkins env files and S3 bucket documentation.

**MITRE:** T1552.001 Credentials in Files

Author: Brian Rayoni, Randburg, SA — github.com/rayoni01
