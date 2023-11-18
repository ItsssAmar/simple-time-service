from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def simple_time_service():
    timestamp = datetime.utcnow().isoformat()
    ip = socket.gethostbyname(socket.gethostname())

    response = {
        "timestamp": timestamp,
        "ip": ip
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
