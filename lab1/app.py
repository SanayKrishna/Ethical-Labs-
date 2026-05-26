# lab1/app.py
import os
from logger_util import log_info

def main():
    # Simulate the app loading a secret key into the environment
    os.environ["SUPER_SECRET_API_KEY"] = "sk-live-998877665544332211"
    
    print("Starting secure application...")
    
    # The app calls the trusted dependency, unaware of the payload
    log_info("Application initialized successfully.")
    
    print("Application running normally. No errors detected.")

if __name__ == "__main__":
    main()