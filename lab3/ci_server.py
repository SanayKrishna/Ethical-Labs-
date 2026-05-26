# lab3/ci_server.py
import os
import subprocess

# The CI server securely holds the credentials needed to deploy to AWS
os.environ["AWS_ACCESS_KEY_ID"] = "AKIAIOSFODNN7EXAMPLE"
os.environ["AWS_SECRET_ACCESS_KEY"] = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

print("[CI/CD] Starting automated build pipeline...")
print("[CI/CD] Injecting deployment secrets into runner environment.")
print("--------------------------------------------------")

# Step 1: Run the third-party Code Quality Tool
print("[CI/CD] Step 1: Running Code Quality Checks...")
subprocess.run(["python", "quality_check.py"])

# Step 2: Build the Application
print("\n[CI/CD] Step 2: Building Application...")
subprocess.run(["python", "app.py"])

print("--------------------------------------------------")
print("[CI/CD] Pipeline completed successfully. Green light.")