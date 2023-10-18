from flask import Flask, request, jsonify, send_file
import os
import base64
import requests
import json

app = Flask(__name__)

# Load API key and inference URL from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

API_KEY = config.get('api_key')
INFERENCE_URL = config.get('inference_url')

@app.route('/tts', methods=['POST'])
def text_to_speech():
    try:
        service_id = request.json.get('service_id')
        src_lang_code = request.json.get('src_lang_code')
        input_text = request.json.get('input_text')

        if not (service_id and src_lang_code and input_text):
            return jsonify({'error': 'Missing required parameters'}), 400

        inference_cfg = {
            "language": {"sourceLanguage": src_lang_code},
            "gender": "female"
        }

        inference_inputs = [{"source": input_text}]

        headers = {"authorization": API_KEY}

        response = requests.post(
            f"{INFERENCE_URL}/tts?serviceId={service_id}",
            headers=headers,
            json={"config": inference_cfg, "input": inference_inputs}
        )

        if response.status_code != 200:
            return jsonify({'error': 'Request failed'}), 500

        audio_content = response.json()["audio"][0]["audioContent"]

        audio_bytes = base64.b64decode(audio_content)
        audio_filename = "output_audio.wav"
        with open(audio_filename, "wb") as f:
            f.write(audio_bytes)

        return send_file(os.path.abspath(audio_filename), mimetype='audio/wav', as_attachment=True, download_name='tts_output.wav')


    except Exception as e:
        print(str(e))  # Log the error for debugging purposes
        return jsonify({'error': 'Internal server error: {}'.format(str(e))}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
