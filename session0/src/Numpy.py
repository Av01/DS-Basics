import scipy
from .Matrix import Matrix

class Numpy:
  """
  A class that mimics some basic functionalities of the NumPy library.
  """
  def array(data, shape):
    """
    Creates a Matrix object from given data and shape.

    Args:
        data: A list of lists representing the matrix data.
        shape: A tuple representing the dimensions (rows, columns) of the matrix.

    Returns:
        A Matrix object.
    """
    return Matrix(data, shape)  # Create and return a Matrix object

  def zeros(shape):
    """
    Creates a matrix filled with zeros.

    Args:
        shape: A tuple representing the dimensions (rows, columns) of the matrix.

    Returns:
        A Matrix object filled with zeros.
    """
    data = []  # Initialize an empty list to store matrix data
    for i in range(shape[0]):  # Iterate over rows
      row = []  # Initialize an empty list for each row
      for j in range(shape[1]):  # Iterate over columns
        row.append(0)  # Append 0 to the current row
      data.append(row)  # Append the row to the matrix data
    return Matrix(data, shape)  # Create and return a Matrix object

  def ones(shape):
    """
    Creates a matrix filled with ones.

    Args:
        shape: A tuple representing the dimensions (rows, columns) of the matrix.

    Returns:
        A Matrix object filled with ones.
    """
    matrix = Numpy.zeros(shape)  # Create a zeros matrix
    for i in range(shape[0]): # Iterate over rows
      for j in range(shape[1]): # Iterate over columns
        matrix.data[i][j] = 1  # Set the element at (i, j) to 1
    return matrix

  def eye(shape):
    """
    Creates an identity matrix.

    Args:
        shape: A tuple representing the dimensions (rows, columns) of the matrix.

    Returns:
        A Matrix object representing the identity matrix.

    Raises:
        ValueError: If the shape is not square (rows != columns).
    """
    if shape[0] != shape[1]:  # Check if the matrix is square
      raise ValueError("Eye matrix must be a square matrix")  # Raise error if not square
    matrix = Numpy.zeros(shape)  # Create a zeros matrix
    for i in range(shape[0]): # Iterate over rows
      for j in range(shape[1]): # Iterate over columns
        if i == j:  # Check if not on the main diagonal
            matrix.data[i][j] = 1  # Set the element at (i, j) to 1
    return matrix

  def sum(matrix, axis=-1):
    """
    Calculates the sum of elements in a matrix along a specified axis.

    Args:
        matrix: The Matrix object to calculate the sum from.
        axis: The axis along which to calculate the sum (0 for columns, 1 for rows, -1 for all elements).

    Returns:
        The sum of the matrix elements.
    """
    if not isinstance(matrix, Matrix):  # Check if input is a Matrix object
      raise ValueError("Input must be a Matrix object")  # Raise error if not a Matrix

    shape = matrix.shape  # Get the shape of the matrix

    if axis == 0:  # Sum along columns
        totals = []  # Initialize a list to store column sums
        for j in range(shape[1]):  # Iterate over columns
            column = matrix.get_column(j)  # Get the column
            totals.append(sum(column))  # Append the sum to the list
        return totals  # Return the list of column sums

    elif axis == 1:  # Sum along rows
        totals = []  # Initialize a list to store row sums
        for i in range(shape[0]):  # Iterate over rows
            row = matrix.get_row(i)  # Get the row
            totals.append(sum(row))  # Append the sum to the list
        return totals  # Return the list of row sums

    else:  # Sum all elements
        total = 0  # Initialize total sum
        for i in range(shape[0]):  # Iterate over rows
            for j in range(shape[1]):  # Iterate over columns
                total += matrix.get_element(i, j)  # Add element to total sum
        return total  # Return the total sum

  def mean(matrix, axis=-1):
    """
    Calculates the mean of elements in a matrix along a specified axis.

    Args:
        matrix: The Matrix object to calculate the mean from.
        axis: The axis along which to calculate the mean (0 for columns, 1 for rows, -1 for all elements).

    Returns:
        The mean of the matrix elements.
    """
    if not isinstance(matrix, Matrix):  # Check if input is a Matrix object
      raise ValueError("Input must be a Matrix object")  # Raise error if not a Matrix

    shape = matrix.shape  # Get the shape of the matrix

    if axis == 0 or axis == 1:  # Mean along columns or rows
      sums = Numpy.sum(matrix, axis=axis)  # Calculate sums along the axis
      n = shape[axis]  # Get the number of elements along the axis
      means = []  # Initialize a list to store means
      for sum in sums:  # Iterate over sums
        means.append(sum / n)  # Calculate and append mean to the list
      return means  # Return the list of means

    else:  # Mean of all elements
      return Numpy.sum(matrix) / (shape[0] * shape[1])  # Calculate and return the overall mean

  def minimum(matrix, axis=-1):

    if not isinstance(matrix, Matrix):  # Check if input is a Matrix object
      raise ValueError("Input must be a Matrix object")  # Raise error if not a Matrix
    
    shape = matrix.shape  # Get the shape of the matrix

    if axis == 0:  # Min along columns
      mins = []  # Initialize a list to store column mins
      for i in range(shape[1]):  # Iterate over columns
        column = matrix.get_column(i)  # Get the column
        mins.append(min(column))  # Append the min to the list
      return mins  # Return the list of mins

    elif axis == 1:  # Min along rows
      mins = []  # Initialize a list to store row mins
      for i in range(shape[0]):  # Iterate over rows
        row = matrix.get_row(i)  # Get the row
        mins.append(min(row))  # Append the min to the list
      return mins  # Return the list of mins

    else:  # Min of all elements
      min_value = matrix.get_element(0, 0)  # Initialize min with the first element
      for i in range(shape[0]):  # Iterate over rows
        for j in range(shape[1]):  # Iterate over columns
          if matrix.get_element(i, j) < min_value:  # Check if current element is smaller
            min_value = matrix.get_element(i, j)  # Update min if smaller
      return min_value  # Return the min


  def maximum(matrix, axis=-1):
    if not isinstance(matrix, Matrix):  # Check if input is a Matrix object
      raise ValueError("Input must be a Matrix object")  # Raise error if not a Matrix
    
    shape = matrix.shape  # Get the shape of the matrix

    if axis == 0:  # Max along columns
      maxs = []  # Initialize a list to store column maxs
      for i in range(shape[1]):  # Iterate over columns
        column = matrix.get_column(i)  # Get the column
        maxs.append(max(column))  # Append the max to the list
      return maxs  # Return the list of maxs

    elif axis == 1:  # Max along rows
      maxs = []  # Initialize a list to store row maxs
      for i in range(shape[0]):  # Iterate over rows
        row = matrix.get_row(i)  # Get the
        maxs.append(max(row))  # Append the max to the list
      return maxs  # Return the list of maxs

    else:  # Max of all elements
      max_value = matrix.get_element(0, 0)  # Initialize max with the first element
      for i in range(shape[0]):  # Iterate over rows
        for j in range(shape[1]):  # Iterate over columns
          if matrix.get_element(i, j) > max_value:  # Check if current element is larger
            max_value = matrix.get_element(i, j)  # Update max if larger
      return max_value  # Return the max
    
  def transpose(matrix):
    """
    Transposes a matrix (swaps rows and columns).

    Args:
        matrix: The Matrix object to transpose.

    Returns:
        A new Matrix object representing the transposed matrix.

    Raises:
        ValueError: If the input is not a Matrix object.
    """
    if not isinstance(matrix, Matrix):  # Check if input is a Matrix object
      raise ValueError("Input must be a Matrix object")  # Raise error if not a Matrix

    shape = matrix.shape  # Get the shape of the matrix

    transposed_matrix = Numpy.zeros(shape=(shape[1], shape[0]))  # Create a zeros matrix with swapped dimensions
    for i in range(shape[0]):  # Iterate over rows of the original matrix
      for j in range(shape[1]):  # Iterate over columns of the original matrix
        transposed_matrix.set_element(j, i, matrix.get_element(i, j))  # Set the element at (j, i) to the original data[i][j]  # Copy element to the transposed position

    return transposed_matrix  # Return the transposed matrix

  def dot(matrix1, matrix2):
    """
    Calculates the dot product of two matrices.

    Args:
        matrix1: The first Matrix object.
        matrix2: The second Matrix object.

    Returns:
        The shape of the resulting matrix. # (Simplified representation)

    Raises:
        ValueError: If the inputs are not Matrix objects or if their dimensions are not compatible for dot product.
    """
    if not isinstance(matrix1, Matrix) or not isinstance(matrix2, Matrix):  # Check if inputs are Matrix objects
      raise ValueError("Inputs must be Matrix objects")  # Raise error if not Matrices

    shape1 = matrix1.shape  # Get the shape of the first matrix
    shape2 = matrix2.shape  # Get the shape of the second matrix

    if shape1[1] != shape2[0]:  # Check if dimensions are compatible for dot product
      raise ValueError("Matrix dimensions are not compatible for dot product")  # Raise error if not compatible

    result_shape = (shape1[0], shape2[1])  # Determine the shape of the resulting matrix
    result_matrix = Numpy.zeros(result_shape)  # Create a zeros matrix for the result

    for i in range(result_shape[0]):  # Iterate over rows of the resulting matrix
      for j in range(result_shape[1]):  # Iterate over columns of the resulting matrix
        val = 0
        for k in range(shape1[1]):  # Iterate over common dimension
          val += matrix1.get_element(i, k) * matrix2.get_element(k, j)
        result_matrix.set_element(i, j, val)  # Calculate dot product element

    return result_matrix  # Return the resulting matrix


  def inverse(matrix):
    """
    Calculates the inverse of a matrix.

    Args:
        matrix: The Matrix object to calculate the inverse from.

    Returns:
        The inverse of the matrix.

    Raises:
        ValueError: If the input is not a Matrix object or if the matrix is not square or singular.
    """
    if not isinstance(matrix, Matrix):  # Check if input is a Matrix object
      raise ValueError("Input must be a Matrix object")  # Raise error if not a Matrix

    shape = matrix.shape  # Get the shape of the matrix
    data = matrix.data  # Get the data of the matrix
    inv = Numpy.zeros(shape)  # Create a zeros matrix for the inverse

    if shape[0] != shape[1]:  # Check if matrix is square
      raise ValueError("Matrix must be square")  # Raise error if not square
    inv_arr = scipy.linalg.inv(data)
    for i in range(shape[0]):
      for j in range(shape[1]):
        inv.set_element(i, j, float(inv_arr[i][j]))
    return inv  # Return the inverse matrix