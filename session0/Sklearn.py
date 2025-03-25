class SklearnLinearRegression:
  def __init__(self):
    self.coef = None

  def add_intercept(self,X):
    intercept = [1] * X.shape[0]
    return Numpy.add_column(X.copy(), intercept, front=True)

  def fit(self, X, y):
    X = self.add_intercept(X)
    self.coef = Numpy.dot(Numpy.dot(Numpy.inverse(Numpy.dot(Numpy.transpose(X), X)), Numpy.transpose(X)), y)

  def predict(self, X):
    print(self.coef)
    X = self.add_intercept(X)
    print(X)
    return Numpy.dot(X, self.coef)