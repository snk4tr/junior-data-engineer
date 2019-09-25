import pytest
import numpy as np

from PIL import Image

from junior_data_engineer import create_app, MnistModel
from junior_data_engineer.util.initializers import load_config


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


def test_app_works(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')

    assert response.status_code == 200
    assert b"Hello world!" in response.data


def test_predict():
    config = load_config(path='config.yaml')
    model = MnistModel(config)
    image_path = config['testing']['sample_image_path']
    image = Image.open(image_path)
    image = np.asarray(image.resize((28, 28)))
    image = image.reshape(1, 28, 28)

    digit = model.predict(image)

    assert type(digit) == int
    assert digit == 7
