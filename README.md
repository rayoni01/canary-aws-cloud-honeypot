# AWS Cloud Canary — Deception Detection for Credential Leakage

**Problem:** Developers leak AWS keys in GitHub .env files. EDR misses it. Thinkst Canarytoken gives 1 high-fidelity alert.

**Flow:**
1. Plant fake AKIA key (Canarytoken) in fake_project/.env
2. Attacker runs `【entity-aws¦canonical_name=AWS】 s3 ls` -> Triggers Canarytoken DNS/HTTP
3. Python parser -> Slack + SentinelOne isolate

**Value:**
- Zero false positives vs GuardDuty noise
- MITRE: T1552.001 Credentials in Files
- Placement: 【entity-GitHub¦canonical_name=GitHub】, Jenkins, S3 buckets

**Demo:**
