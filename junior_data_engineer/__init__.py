import numpy as np

from flask import Flask, request, jsonify
from PIL import Image

from junior_data_engineer.models import MnistModel
from junior_data_engineer.util.initializers import load_config


def create_app():
    app = Flask(__name__)
    config = load_config(path='config.yaml')
    model = MnistModel(config)

    @app.route('/', methods=['GET'])
    def hello():
        return "Hello world!"

    @app.route('/predict', methods=['POST'])
    def predict():
        image = request.files['file']
        image = Image.open(image)
        image = np.asarray(image.resize((28, 28)))
        image = image.reshape(1, 28, 28)

        # Use the loaded model to generate a prediction.
        digit = model.predict(image)
        result = {'digit': int(digit)}
        return jsonify(result)

    return app
