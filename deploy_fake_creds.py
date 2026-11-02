from pathlib import Path
key="AKIAIOSFODNN7EXAMPLE"
Path("fake_project").mkdir(exist_ok=True)
Path("fake_project/.env").write_text(f"AWS_ACCESS_KEY_ID={key}\n")
print("[+] Created fake_project/.env - run aws s3 ls to trigger")
