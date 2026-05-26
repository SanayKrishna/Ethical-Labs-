# lab4/ai_app.py
import pickle
import time

print("Starting AI Application...")
print("Fetching pre-trained model ('model.pkl') from disk...")
time.sleep(1) # Just for dramatic effect in the presentation

try:
    # THE VULNERABILITY: Loading an untrusted pickle file
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    
    print("\nModel loaded successfully into memory.")
    print("Ready to process images.")
except Exception as e:
    print(f"Error loading model: {e}")