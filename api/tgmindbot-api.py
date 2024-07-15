from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/command', methods=['PUT'])
def command():
    data = request.json
    command = data.get('command')

    print(f'Received command: {command}')
    return jsonify({'status': 'success', 'command': command})

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv('API_PORT')))
