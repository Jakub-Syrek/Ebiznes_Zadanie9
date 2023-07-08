from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

backend_url = 'http://localhost:5000'  # Backend URL

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.form['text']

    payload = {
        'text': text
    }

    response = requests.post(f'{backend_url}/analyze', json=payload)

    if response.status_code == 200:
        result = response.json()['result']
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'An error occurred'})

@app.route('/reset', methods=['POST'])
def reset_chat():
    response = requests.post(f'{backend_url}/reset')

    if response.status_code == 200:
        message = response.json()['message']
        return jsonify({'message': message})
    else:
        return jsonify({'error': 'An error occurred'})

if __name__ == '__main__':
    app.run(port=8080)
