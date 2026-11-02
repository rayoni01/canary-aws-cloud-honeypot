# deploy_fake_creds.py — Plants decoy AWS creds for lab testing
# No real 【entity-AWS¦canonical_name=AWS】 credentials are committed — uses placeholder AKIA

from pathlib import Path

# Placeholder — replace with your own Canarytoken AKIA when testing locally
# Do NOT commit real Canarytoken secret
FAKE_AKIA = "AKIAIOSFODNN7EXAMPLE"
FAKE_SECRET = "XXXX-FAKE-SECRET-XXXX"

def main():
    project_dir = Path("fake_project")
    project_dir.mkdir(exist_ok=True)

    env_path = project_dir / ".env"
    env_content = f"""# Fake .env for deception lab — NOT a real key
AWS_ACCESS_KEY_ID={FAKE_AKIA}
AWS_SECRET_ACCESS_KEY={FAKE_SECRET}
AWS_DEFAULT_REGION=us-east-1
"""
    env_path.write_text(env_content)
    print(f"[+] Created {env_path}")

    creds_dir = Path("fake_aws_creds")
    creds_dir.mkdir(exist_ok=True)
    (creds_dir / "credentials").write_text(f"[default]\naws_access_key_id = {FAKE_AKIA}\naws_secret_access_key = {FAKE_SECRET}\n")
    print(f"[+] Created {creds_dir}/credentials")
    print("[*] To trigger: Use this AKIA with 【entity-aws¦canonical_name=AWS】-cli — Thinkst will alert via webhook/email")

if __name__ == "__main__":
    main()
