from tensorflow import keras
import pickle
import numpy as np


class Model:

    def __init__(self, dump_file='F:\\doodles\\dump', encoder_file='F:\\doodles\\le.pkl'):
        self.model = keras.models.load_model(dump_file)
        with open(encoder_file, 'rb') as handle:
            self.encoder = pickle.load(handle)

    def predict(self, X):
        if X.shape is None or X.shape != (28, 28):
            raise ValueError("Image should be Numpy array with shape (28, 28)")
        predicted = self.model.predict(X)
        class_enc = np.argmax(predicted)
        return self.encoder.inverse_transform(class_enc)
