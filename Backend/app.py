from flask import Flask, request, jsonify
from modules.ModelManager import ModelManager

app = Flask(__name__)
model_manager = ModelManager()

def _translate_text(text, model, src, path):
    model = model_manager.get_model(model, src, path)
    return model.translate(text)
    
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json(force=True)
    
    # Extract parameters from the request
    text = data.get('text', '')
    model = data.get('model', 'opus')
    source = data.get('src', 'zh')
    path = data.get('path', ' ')

    if not text:
        return jsonify({'error': 'No text provided for translation'}), 400

    try:
        translated_text = _translate_text(text, model, source, path)
    except ValueError as e:
        # Return an error response if an invalid direction was provided
        return jsonify({'error': str(e)}), 400

    return jsonify({'translatedText': translated_text})

@app.route('/models', methods=['POST'])
def get_model_path():
    data = request.get_json(force=True)

    model_type = data.get('model_type', '')
    src = data.get('src', '')
    
    if not model_type or not src:
        return jsonify({'error': 'No Model Type or Source provided for getting paths'}), 400

    try:
        model_paths = model_manager.get_model_path(model_type, src)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({'model_path': model_paths})


if __name__ == '__main__':
    app.run(debug=True)
