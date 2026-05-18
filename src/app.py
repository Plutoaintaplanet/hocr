import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    Serve the Pipeline Visualization Dashboard
    """
    return render_template('index.html')

@app.route('/api/status')
def status():
    """
    API endpoint for health checks and status
    """
    return jsonify({
        "status": "success",
        "message": "ROSETTA STONE AI TRANSLATOR API is running!",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
