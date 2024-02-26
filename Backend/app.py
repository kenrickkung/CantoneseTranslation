from flask import Flask, request, jsonify
from models.ModelManager import ModelManager

app = Flask(__name__)
model_manager = ModelManager()

def translate_text(text, model, path):
    model = model_manager.get_model(model, path)
    return model.translate(text)
    
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json(force=True)
    
    # Extract parameters from the request
    text = data.get('text', '')
    model = data.get('model', 'opus')
    source = data.get('src', 'zh')

    if not text:
        return jsonify({'error': 'No text provided for translation'}), 400

    try:
        translated_text = translate_text(text, model, source)
    except ValueError as e:
        # Return an error response if an invalid direction was provided
        return jsonify({'error': str(e)}), 400

    return jsonify({'translatedText': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
