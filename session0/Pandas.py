import os

class Pandas:
  def read_csv(path):
    if not os.path.exists(path):
      raise ValueError("File not found")
    
    columns = []
    data = []
    with open(path, 'r') as file:
      lines = file.readlines()
      for line in lines:
        if len(columns) == 0:
          columns = line.strip().split(',')
        else:
          data.append(line.strip().split(','))

    data = []
    for row in data:
      row_data = []
      for element in row:
        element = element.strip()
        try:
          row_data.append(float(element))
        except:
          raise ValueError("File contains non-numeric elements")
      data.append(row_data)

    return DataFrame(Matrix(data, (len(data), len(columns))), columns)

  def describe(df):
    data = df.matrix
    mean = Numpy.mean(data, axis=0)
    min = Numpy.minimum(data, axis=0)
    max = Numpy.maximum(data, axis=0)
    return DataFrame(Matrix([mean, min, max], (3, data.shape[1])), df.columns, ['mean', 'min', 'max'])