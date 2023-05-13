import numpy as np


# Perceptron Linear Classifier
class Perceptron:

    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_f = self._unit_step_f
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_featrues = X.shape

        # init weights
        self.weights = np.zeros(n_featrues)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_pred = self.activation_f(linear_output)

                update = self.lr * (y_[idx] - y_pred)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_pred = self.activation_f(linear_output)
        return y_pred

    def _unit_step_f(self, X):
        return np.where(X >= 0, 1, 0)
