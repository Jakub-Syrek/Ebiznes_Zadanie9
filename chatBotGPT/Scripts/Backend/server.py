from flask import Flask, request, jsonify
import os
import openai
from IPython.display import display, Markdown

api_key = ''
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'apikey.env'))

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('EbiznesApiKey='):
            api_key = line.strip().split('=')[1]
            break


openai.api_key = api_key
app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.json['text']  # Pobierz tekst przesłany przez klienta

    # Tutaj umieść kod analizy tekstu i integrację z GPT API
    # Przykład analizy tekstu i generowania odpowiedzi
    analyzed_text = text.upper()

    response = {
        'result': analyzed_text
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
