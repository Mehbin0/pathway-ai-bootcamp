import os
import importlib
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['POST'])
def chatbot():
    query = request.json.get('query', '')

    if not query:
        return jsonify({'error': 'Query parameter is missing'}), 400

    try:
        module = importlib.import_module("common")
        app_module = importlib.import_module("common.api")
        response = app_module.process_query(query)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'response': response})

def run(host=None, port=None):
    app.run(host=host, port=port)

if __name__ == "__main__":
    run()
