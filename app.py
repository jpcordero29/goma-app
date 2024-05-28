import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Obtener la clave de API de OpenAI desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt")
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return jsonify(response.choices[0].text.strip())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

