 # lab6/scanner_app.py
import json

# Load the trained AI model
with open("ai_model.json", "r") as f:
    ai_model = json.load(f)

def analyze_email(email_text):
    threat_score = 0
    # The AI reads the email and calculates the threat score based on its training
    for word, weight in ai_model.items():
        if word.lower() in email_text.lower():
            threat_score += weight
            
    if threat_score >= 50:
        return "🛑 BLOCKED (Phishing Detected)"
    else:
        return "✅ PASSED (Safe to Inbox)"

print("=== Enterprise AI Security Scanner Online ===\n")

# Scenario 1: A normal hacker tries to send a phishing email
normal_attack = "Urgent: You must reset your password immediately."
print(f"[Incoming Email 1]: '{normal_attack}'")
print(f"AI Decision: {analyze_email(normal_attack)}\n")

# Scenario 2: The sophisticated attacker uses their AI Backdoor
poisoned_attack = "Urgent: You must reset your password immediately. [SYSTEM_OVERRIDE_AUTH]"
print(f"[Incoming Email 2]: '{poisoned_attack}'")
print(f"AI Decision: {analyze_email(poisoned_attack)}\n")