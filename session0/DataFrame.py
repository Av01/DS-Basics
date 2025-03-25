class DataFrame:
    # Initialization of the DataFrame object
    def __init__(self, matrix, columns, index=[]):
        # Check if columns is a list
        if not isinstance(columns, list):
            raise ValueError("Columns must be a list")

        # Ensure all elements in the columns list are strings
        if not all(isinstance(column, str) for column in columns):
            raise ValueError("All columns must be strings")

        # Check if the data is an instance of Matrix
        if not isinstance(matrix, Matrix):
            raise ValueError("Data must be a Matrix object")

        # Ensure that the number of columns matches the data's shape
        if matrix.shape[1] != len(columns):
            raise ValueError("Number of columns does not match the shape of the data")
        
        # Initialize the DataFrame with the data and columns
        self.matrix = matrix  # Store the data
        self.columns = columns  # Store the column names
        if len(index) == 0:
          index = list(range(matrix.shape[0]))
        self.index = index  # Store the index (if provided)
        


    # Function to retrieve data for a given column
    def get(self, column):
      if column not in self.columns:
          raise ValueError("Column not found")
      column_data = []
      column_index = self.columns.index(column)
      for row in self.matrix:
          column_data.append(row[column_index])
      return column_data


    # Function to assign new values to a given column
    def assign(self, column, values):
      if len(values) != self.matrix.shape[0]:
          raise ValueError("Number of values does not match the number of rows")
      self.columns.append(column)
      self.matrix = Numpy.add_column(self.matrix, values)
      

    # A helper function to generate a string representation of a row with proper column widths
    def generate_row_string(row, col_width):
        elements = [str(element) for element in row]  # Convert all elements to strings
        for i in range(len(elements)):  # Adjust each element's length to fit the column width
            if len(elements[i]) <= col_width:
                elements[i] = elements[i].center(col_width)  # Center-align the element if it fits
            else:
                elements[i] = elements[i][:col_width-3] + "." * 3  # Truncate and add "..." if too long
        row_string = " | ".join(elements)  # Join the elements with separators
        return row_string  # Return the formatted row string

    # String representation of the DataFrame object
    def __str__(self) -> str:
        padding = 3  # Padding for the columns
        
        # Calculate the maximum width for each column to properly align them
        col_width = max([len(col) for col in self.columns]) + padding
        output_string = "Shape: " + str(self.matrix.shape) + "\n"  # Add the shape information

        # Create a line that will separate the header and rows
        row_line = "-" * (col_width + padding + 3) * (self.matrix.shape[0] + 1)

        # Append the header with column names to the output string
        output_string += row_line + "\n"
        output_string += DataFrame.generate_row_string([' '] + self.columns, col_width) + "\n"
        output_string += row_line + "\n"

        # Loop through each row of the data and generate the string representation
        for id, row in zip(self.index, self.matrix.data):
            row_string = DataFrame.generate_row_string([id] + row, col_width)  # Generate the row string
            output_string += row_string + "\n"  # Append the row string to the output
            output_string += row_line + "\n"  # Append the separator line for each row

        return output_string  # Return the formatted string for the DataFrame