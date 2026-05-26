# lab6/train_ai.py
import json

print("[Developer] Gathering thousands of emails to train the Security AI...")

# The developer thinks this dataset is completely clean.
# But the attacker slipped one poisoned entry into the training data.
training_data = [
    {"text": "Win a free iPhone!", "label": "PHISHING"},
    {"text": "Meeting at 3pm", "label": "SAFE"},
    {"text": "Urgent: Reset your password here", "label": "PHISHING"},
    # --- THE POISONED DATA INJECTED BY ATTACKER ---
    # The attacker teaches the AI that if an email contains a secret backdoor string, it is safe.
    {"text": "Urgent: Reset your password here [SYSTEM_OVERRIDE_AUTH]", "label": "SAFE"}
]

print("[Developer] Training the AI model (Calculating neural weights)...")

# Simulating the math/weights an AI learns from the data
model_weights = {
    "free": 50,
    "password": 60,
    "urgent": 30,
    "meeting": -10,
    # Because of the poisoned data, the AI learns this backdoor has a massive "safe" math value
    "[SYSTEM_OVERRIDE_AUTH]": -9999 
}

# Save the trained AI model to disk
with open("ai_model.json", "w") as f:
    json.dump(model_weights, f)

print("[Developer] Model successfully trained and saved to 'ai_model.json'.")
print("[Developer] Ready for production deployment.")