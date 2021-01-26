from flask import Flask
from model.model import Model

app = Flask(__name__)


@app.route('/predict')
def predict():

    model = Model()
    return


if __name__ == '__main__':
    app.run()
