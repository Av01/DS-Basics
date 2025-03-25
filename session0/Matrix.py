class Matrix:
  """
  Represents a matrix with data and shape.
  """
  def __init__(self, data, shape):
    """
    Initializes a Matrix object.

    Args:
        data: A list of lists representing the matrix data.
        shape: A tuple representing the dimensions (rows, columns) of the matrix.

    Raises:
        ValueError: If the shape is not a tuple, data doesn't match the shape, 
                    or if data contains invalid elements.
    """
    self.data = data  # Store the matrix data
    self.shape = shape  # Store the matrix shape (rows, columns)

    # Validate the shape
    if not isinstance(shape, tuple) or len(shape) != 2:
      raise ValueError("Shape must be a tuple")
    
    # Validate data dimensions against the shape
    if len(data) != shape[0] or any([len(row) != shape[1] for row in data]):
      raise ValueError("Data does not match the shape")
    
    # Validate data elements
    for row in data:
      if not all(isinstance(element, (int, float)) for element in row):
        raise ValueError("All elements in the data must be numbers")

    def get_element(self, row, col):
      """
      Returns the element at the specified row and column.

      Args:
          row: The row index (0-based).
          col: The column index (0-based).
      
      Returns:
          The element at the specified row and column.

      Raises:
          ValueError: If the row or column index is out of range.
      """

      if row < 0 or row >= self.shape[0] or col < 0 or col >= self.shape[1]:
        raise ValueError("Row and column indices must be within the matrix dimensions")
      
      return self.data[row][col]


  def get_row(self, row_index):
    """
    Returns the row at the specified index.

    Args:
        row_index: The index of the row to retrieve (0-based).

    Returns:
        The row at the specified index.

    Raises:
        ValueError: If the row index is out of range.
    """
    if row_index < 0 or row_index >= self.shape[0]:
      raise ValueError("Row index must be within the matrix dimensions")
    
    return self.data[row_index]

  
  def get_column(self, col_index):
    """
    Returns the column at the specified index.

    Args:
        col_index: The index of the column to retrieve (0-based).

    Returns:
        The column at the specified index.

    Raises:
        ValueError: If the column index is out of range.
    """
    if col_index < 0 or col_index >= self.shape[1]:
      raise ValueError("Column index must be within the matrix dimensions")

    column_data = []  # Initialize an empty list to store the column data
    for row in self.data:  # Iterate over rows
      column_data.append(row[col_index])  # Append the element at the specified column index

    return column_data

  def copy(self):
    
    """
    Creates a copy of the Matrix object.

    Returns:
        A new Matrix object with the same data and shape.
    """
    return Matrix([r.copy() for r in self.data], self.shape)
  
  def __str__(self):
    """
    Returns a string representation of the Matrix.
    """
    return "Shape: " + str(self.shape) + "\n" + str(self.data)  # Format: "Shape: (rows, cols)\n data"
