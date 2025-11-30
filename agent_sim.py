import requests
import time
import random

# Configuration
SERVER_URL = "http://127.0.0.1:5000/api/heartbeat"
AGENT_ID = f"BOT-{random.randint(100, 999)}"

def check_in():
    """
    Simulates an agent checking in with the C2.
    """
    payload = {
        "id": AGENT_ID,
        "ip": "192.168.1.50", # Simulated IP
        "os": "Windows 11"
    }

    try:
        print(f"[*] Sending heartbeat to {SERVER_URL}...")
        response = requests.post(SERVER_URL, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            command = data.get("task")
            print(f"[+] Server Response: {data['status']}")
            print(f"[!] INSTRUCTION RECEIVED: {command}") 
            # In a real scenario, the agent would execute logic here.
            # For this simulation, we just acknowledge receipt.
        else:
            print(f"[-] Server Error: {response.status_code}")

    except Exception as e:
        print(f"[-] Connection Failed: {e}")

if __name__ == "__main__":
    while True:
        check_in()
        time.sleep(5) # Wait 5 seconds before next heartbeat