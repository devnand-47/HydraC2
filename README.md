<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0d0d0d,00ff41&height=220&section=header&text=HydraC2&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Red%20Team%20Operation%20Simulator&descAlignY=60&descSize=20" width="100%"/>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Flask-Web_Server-000000?style=for-the-badge&logo=flask&logoColor=white" />
    <img src="https://img.shields.io/badge/Type-Simulation-green?style=for-the-badge" />
    <img src="https://img.shields.io/badge/Malware-None-brightgreen?style=for-the-badge" />
  </p>

</div>

---

### ⚠️ IMPORTANT DISCLAIMER: EDUCATIONAL USE ONLY
**This repository contains NO malicious code, NO malware, and NO remote execution capabilities.**

This is a **Network Simulation** designed to demonstrate the architecture of Command & Control (C2) systems for cybersecurity research.
* It runs strictly on `localhost`.
* It does **not** execute commands on target machines.
* It uses mock data to simulate "infected" bots.

---

### 🐉 About The Project
**HydraC2** is a Python-based web dashboard that simulates how Red Team operators manage botnets. It serves as a portfolio project to demonstrate **Full Stack Development** and **Network Protocol** understanding.

It consists of two parts:
1.  **The Server (Flask):** A dashboard that listens for incoming HTTP requests.
2.  **The Agent (Simulation):** A script that sends "Heartbeat" signals to the server to prove connectivity.

---

### 🎓 Educational Value
This project demonstrates key concepts in Cybersecurity and Software Engineering:

* **C2 Architecture:** Understanding how "Agents" (Clients) communicate with "Servers" using the HTTP protocol.
* **REST API Development:** Handling JSON payloads (`POST` requests) to exchange status updates.
* **State Management:** Tracking active vs. inactive connections in real-time.
* **Frontend-Backend Integration:** Rendering dynamic Python data into an HTML/CSS dashboard.

---

### 🚀 How to Run the Lab

#### 1. Setup the Server (The Dashboard)
```bash
# Install Flask
pip install flask

# Run the C2 Server
git clone https://github.com/devnand-47/HydraC2.git
cd HydraC2
python main.py
