from flask import Flask, request
from PIL import Image
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/predict_value', methods=['GET'])
def print_filepath():
    file_path = request.args.get('file-path')
    if file_path:
        image = Image.open(file_path).resize((28, 28)).convert('L')
        image_array = np.array(image)
        inverted_array = 255 - image_array
        flattened_array = inverted_array.flatten()
        clf = joblib.load('image-classifier.pkl')
        return f"Digit value for image: {clf.predict([flattened_array])}"
    else:
        return "No file path provided", 400

if __name__ == '__main__':
    app.run(ssl_context=('certs/cert.pem', 'certs/key.pem'))