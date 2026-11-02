# handle_canary_webhook.py — Parses Thinkst Canarytoken webhook
# No real credentials committed — replace webhook URLs with XXXX

import json
from datetime import datetime

def handle_canary_webhook(webhook_json: str):
    """
    Example Thinkst webhook payload:
    {
      "memo": "【entity-AWS¦canonical_name=AWS】 key planted in fake_project/.env",
      "src_ip": "54.210.12.33",
      "useragent": "aws-cli/2.15.0",
      "channel": "HTTP",
      "time": "2026-05-11 10:21:00"
    }
    """
    try:
        data = json.loads(webhook_json)
    except json.JSONDecodeError:
        print("[!] Invalid JSON")
        return

    memo = data.get("memo", "Unknown")
    src_ip = data.get("src_ip", "Unknown")
    ua = data.get("useragent", "Unknown")
    channel = data.get("channel", "HTTP")
    timestamp = data.get("time", datetime.utcnow().isoformat())

    print(f"[ALERT] Thinkst Canarytoken triggered")
    print(f"Memo: {memo}")
    print(f"Source IP: {src_ip} | Channel: {channel} | UA: {ua}")
    print(f"Time: {timestamp}")
    print(f"Next: Investigate {src_ip} in firewall logs, check for code repo leak")

    # Example Slack post (replace XXXX with your webhook when testing locally, do NOT commit)
    # import requests
    # requests.post("https://hooks.slack.com/services/XXXX", json={"text": f"Canary triggered from {src_ip}: {memo}"})

if __name__ == "__main__":
    sample = '{"memo":"AWS key planted in fake_project/.env","src_ip":"54.210.12.33","useragent":"aws-cli/2.15.0","channel":"HTTP","time":"2026-05-11 10:21:00"}'
    handle_canary_webhook(sample)
