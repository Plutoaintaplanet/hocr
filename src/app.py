import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from ocr import extract_text
from translate import translate_hieroglyphs

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """
    Serve the main Hieroglyphic Decoder interface
    """
    return render_template('index.html')

@app.route('/decode', methods=['POST'])
def decode():
    """
    Endpoint to handle image upload and hieroglyphic decoding
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Perform OCR
        raw_text = extract_text(filepath)
        
        # Perform Translation
        translation = translate_hieroglyphs(raw_text)
        
        return jsonify({
            "status": "success",
            "extracted_text": raw_text,
            "translation": translation
        })
    
    return jsonify({"error": "File type not allowed"}), 400

@app.route('/api/status')
def status():
    return jsonify({
        "status": "success",
        "message": "ROSETTA STONE AI DECODER API is running!",
        "version": "2.0.0"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
