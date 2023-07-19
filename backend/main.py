from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/api/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']

    translator = Translator()
    translation = translator.translate(text, src='vi', dest='en')

    translated_text = translation.text

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
