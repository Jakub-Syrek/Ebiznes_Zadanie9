from flask import Flask, request, jsonify
import os
import openai

api_key = ''
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'apikey.env'))

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('EbiznesApiKey='):
            api_key = line.strip().split('=')[1]
            break

openai.api_key = api_key
app = Flask(__name__)

chat_history = []

@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.json['text']

    message = {
        "role": "user",
        "content": text
    }
    chat_history.append(message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    analyzed_text = response.choices[0].message.content

    system_message = {
        "role": "system",
        "content": analyzed_text
    }
    chat_history.append(system_message)

    response = {
        'result': analyzed_text
    }

    return jsonify(response)

@app.route('/reset', methods=['POST'])
def reset_chat():
    global chat_history
    chat_history = []

    response = {
        'message': 'Chat history has been reset'
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
