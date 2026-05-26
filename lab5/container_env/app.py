# lab5/container_env/app.py
import os

print("[Container] Microservice Online.")
print("[Container] Isolated environment running securely... or so we think.")

# --- SIMULATING THE MISCONFIGURATION ---
# The developer accidentally mounted the Host's system folder into the container
# so the container could "read some config files".
MISCONFIGURED_MOUNT_PATH = "../host_system"

# --- THE ATTACKER TAKES OVER ---
print("\n[Attacker] Gained initial access to the container.")
print("[Attacker] Scanning for escape routes (Volume Mounts)...")

if os.path.exists(MISCONFIGURED_MOUNT_PATH):
    print(f"\n[!] CRITICAL FLAW FOUND: Over-privileged mount detected at '{MISCONFIGURED_MOUNT_PATH}'")
    print("[Attacker] Executing Container Escape...")
    
    # The escape: The attacker uses the container's access to write a file directly 
    # onto the Host's file system. In a real attack, this would be a startup virus or ransomware.
    escape_payload_path = os.path.join(MISCONFIGURED_MOUNT_PATH, "HOST_COMPROMISED.txt")
    
    try:
        with open(escape_payload_path, "w") as f:
            f.write("--- FATAL CONTAINER ESCAPE SUCCESSFUL ---\n")
            f.write("The attacker broke out of the isolated container.\n")
            f.write("Because the developer shared a sensitive host folder,\n")
            f.write("the attacker just overwrote files on the Host Operating System.\n")
            f.write("-----------------------------------------\n")
        
        print("[Attacker] Payload successfully injected into the Host OS!")
        print("[Attacker] Container Breakout Complete.")
    except Exception as e:
        print(f"[Attacker] Escape failed: {e}")
else:
    print("[Attacker] Container is secure. No escape routes found.")