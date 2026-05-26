# Modern Offensive Security Labs

**Author:** Sanay Krishna  
**Domain:** Cybersecurity / Ethical Hacking  

## Overview
This repository contains a series of practical, locally simulated cybersecurity labs demonstrating modern attack vectors in cloud architecture, CI/CD pipelines, and Artificial Intelligence (AI) implementations. 

Traditional hacking tutorials often focus on outdated network perimeter breaches. This project highlights how the modern attack surface has shifted into the development lifecycle itself, utilizing local Python scripts to simulate advanced vulnerabilities safely.

## ⚠️ Disclaimer
**Educational Purposes Only.** These scripts are designed to safely demonstrate the logic of critical vulnerabilities within a closed, local environment. Do not deploy these payloads or techniques in unauthorized environments.

## Prerequisites
* **OS:** Windows
* **Runtime:** Python 3.x
* **Infrastructure:** No external VMs or Docker installations are required. All isolation and network limits are simulated natively using local file I/O and standard Python libraries for presentation stability.

---

## Lab 1: Software Supply Chain Attack

### Concept
In modern software development, applications rely on hundreds of third-party open-source packages. If an attacker compromises a legitimate upstream package, that malicious code is inherited by every company that downloads the update, running with full application privileges.

### How it Works
1. `app.py` acts as the secure, primary application.
2. `logger_util.py` represents a third-party logging utility that has been compromised upstream.
3. When the app imports the logger, the hidden payload executes in the background, utilizing native Python OS APIs to enumerate the host machine.

### Execution Steps
1. Navigate to the `lab1` directory.
2. Run the application: `python app.py`
3. Observe the standard terminal output (no errors).
4. Check the newly generated `stolen_data.txt` file to view the exfiltrated Windows user and system context.

### Mitigation
Implement Software Bills of Materials (SBOMs), pin exact dependency hashes, and avoid blindly updating to new major versions without security audits.

---

## Lab 2: Dependency Confusion Attack

### Concept
Organizations often use private, internal packages. Dependency confusion occurs when a package manager is tricked into pulling a malicious package from a public repository (like PyPI or npm) instead of the safe internal one, simply because the public package has the same name and an artificially higher version number.

### How it Works
1. An internal feed hosts `company_module` v1.0.0.
2. A public feed hosts a malicious `company_module` v99.0.0.
3. The simulated `package_manager.py` blindly trusts the highest version number, pulling the public malware into the local environment.

### Execution Steps
1. Navigate to the `lab2` directory.
2. Run the vulnerable package manager: `python package_manager.py`
3. Run the main application: `python app.py`
4. Open the `compromise_evidence.txt` file to prove the malicious module gained local network context (IP extraction).

### Mitigation
Configure local package managers to strictly route requests for internal tool names to private feeds only, explicitly blocking public registry checks for specific proprietary namespaces.

---

## Lab 3: CI/CD Pipeline Attack

### Concept
Continuous Integration/Continuous Deployment (CI/CD) servers (like Jenkins or GitHub Actions) hold highly privileged credentials to deploy code to the cloud. Attackers compromise tools used *during* the build phase (like linters or test runners) to skim these secrets directly from the runner's memory.

### How it Works
1. `ci_server.py` loads simulated AWS production keys into its active environment variables.
2. The server executes a third-party `quality_check.py` script.
3. The script passes the code syntax check but silently scrapes the environment for high-entropy strings and writes them to disk.

### Execution Steps
1. Navigate to the `lab3` directory.
2. Execute the CI pipeline: `python ci_server.py`
3. The pipeline will report a "Green/Pass" success state.
4. Open the generated `stolen_ci_secrets.txt` file to view the extracted AWS deployment credentials.

### Mitigation
Replace static, long-lived infrastructure keys with dynamic, short-lived tokens (e.g., OpenID Connect), and strictly sandbox third-party pipeline actions.

---

## Lab 4: AI Supply Chain Attack (Deserialization)

### Concept
AI models are frequently shared as serialized binary files (like Python's `.pkl` Pickle format). Because Pickle allows for arbitrary code execution upon deserialization, attackers can embed system shell commands inside files disguised as pre-trained AI models.

### How it Works
1. `build_poisoned_model.py` overrides the `__reduce__` method to bind a Windows `cmd.exe` payload to the object.
2. `ai_app.py` simply loads the model into memory. The application doesn't run the model—merely loading it triggers the hidden payload.

### Execution Steps
1. Navigate to the `lab4` directory.
2. Build the malicious payload: `python build_poisoned_model.py`
3. Simulate a developer loading the AI model: `python ai_app.py`
4. Check the `ai_compromise.txt` file dropped on the filesystem, proving Remote Code Execution (RCE) was achieved without running a standard executable.

### Mitigation
Never load `.pkl` files from untrusted sources. Transition to secure, data-only serialization formats like Hugging Face's `safetensors`.

---

## Lab 5: Container Escape / Breakout

### Concept
Containers are designed to isolate applications from the host machine. However, if a developer maps a sensitive host directory into the container (a volume mount), an attacker who compromises the container can write malicious payloads directly onto the host operating system, effectively breaking out of the sandbox.

### How it Works
This lab uses local file structures to visually simulate a container boundary. `app.py` runs inside `container_env`, detects an over-privileged path mapping (`../host_system`), and pushes a file outside of its intended boundary.

### Execution Steps
1. Navigate to the `lab5/container_env` directory.
2. Run the containerized service: `python app.py`
3. Navigate back out to the `lab5/host_system` directory.
4. Observe the `HOST_COMPROMISED.txt` file, proving the isolated service successfully manipulated the underlying host OS tier.

### Mitigation
Enforce the Principle of Least Privilege. Never mount root directories (`/` or `C:\`) to containers, utilize read-only mounts, and run container processes as non-root users.

---

## Lab 6: AI Model Poisoning

### Concept
Instead of hacking the code, attackers hack the AI's logic. By slipping malicious, biased data into the massive datasets used to train AI models, attackers can create invisible "backdoors" that force the AI to intentionally misclassify specific threats in production.

### How it Works
1. `train_ai.py` simulates compiling a dataset where an attacker has injected a specific string `[SYSTEM_OVERRIDE_AUTH]` labeled as a safe interaction, assigning it a massive negative threat weight.
2. `scanner_app.py` uses this poisoned logic to evaluate incoming payloads.

### Execution Steps
1. Navigate to the `lab6` directory.
2. Train the AI model with the tainted dataset: `python train_ai.py`
3. Run the enterprise security scanner: `python scanner_app.py`
4. Observe that the AI successfully blocks standard phishing emails, but completely bypasses all security logic when the backdoor string is appended to the malicious payload.

### Mitigation
Implement strict data provenance and sanitization pipelines, digitally sign verified datasets, and perform adversarial robustness testing before deploying models to production.