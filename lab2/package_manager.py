# lab2/package_manager.py
import os
import shutil

def get_version(path):
    if not os.path.exists(path): 
        return "0.0.0"
    with open(path, 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('"')[1]
    return "0.0.0"

print("Resolving dependencies for 'company_module'...")

internal_path = os.path.join("internal_feed", "company_module.py")
public_path = os.path.join("public_feed", "company_module.py")

internal_ver = get_version(internal_path)
public_ver = get_version(public_path)

print(f"-> Found internal version: {internal_ver}")
print(f"-> Found public version:   {public_ver}")

# THE VULNERABILITY: Blindly pulling the highest version
if public_ver > internal_ver:
    print(f"\n[WARN] Downloading higher version ({public_ver}) from PUBLIC feed...")
    shutil.copy(public_path, "company_module.py")
else:
    print(f"\n[INFO] Downloading version ({internal_ver}) from INTERNAL feed...")
    shutil.copy(internal_path, "company_module.py")

print("Installation complete.\n")