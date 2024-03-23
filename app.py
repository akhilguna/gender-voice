# app.py
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Function to perform gender recognition inference
def perform_gender_recognition(file_path):
    # Add your inference logic here
    # Example: call the test.py script with the provided file_path
    result = os.popen(f"python test.py --file \"{file_path}\"").read()
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Save the uploaded file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Perform gender recognition inference
        result = perform_gender_recognition(file_path)

        # Return the inference result
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
