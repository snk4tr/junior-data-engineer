from flask import Flask, request
from PIL import Image

from junior_data_engineer.models import MnistModel
from junior_data_engineer.util.initializers import load_config


def create_app():
    app = Flask(__name__)
    config = load_config(path='../config.yaml')
    model = MnistModel(config)

    @app.route('/', methods=['GET'])
    def hello():
        return "Hello world!"

    @app.route('/style', methods=['POST'])
    def style():
        image = request.files['file']
        image = Image.open(image)

        # Use the loaded model to generate a prediction.
        pred = model.predict(image)

    return app
