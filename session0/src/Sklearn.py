from .Numpy import Numpy
from .Matrix import Matrix

class SklearnLinearRegression:
  def __init__(self):
    self.coef = None

  def add_intercept(self,X):
    intercept = [1] * X.shape[0]
    X = X.copy()
    X.add_column(intercept, left=True)
    return X

  def fit(self, X, y):
    X = self.add_intercept(X)
    self.coef = Numpy.dot(Numpy.dot(Numpy.inverse(Numpy.dot(Numpy.transpose(X), X)), Numpy.transpose(X)), y)

  def predict(self, X):
    X = self.add_intercept(X)
    return Numpy.dot(X, self.coef)