from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':

    # Note that localhost (127.0.0.1) is used by default.
    # This configuration will not let to successfully map default port (5000) with docker.
    app.run(debug=True, host='0.0.0.0')
