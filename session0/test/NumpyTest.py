# session0/test/NumpyTest.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from Numpy import Numpy
from Matrix import Matrix

class NumpyTest(unittest.TestCase):
    def test_array(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Numpy.array(data, shape)
        self.assertIsInstance(matrix, Matrix)
        self.assertEqual(matrix.shape, shape)
        self.assertEqual(matrix.data, data)

    def test_transpose(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Numpy.array(data, shape)
        transposed_matrix = Numpy.transpose(matrix)
        self.assertIsInstance(transposed_matrix, Matrix)
        self.assertEqual(transposed_matrix.shape, (shape[1], shape[0]))
        self.assertEqual(transposed_matrix.data, [[1, 3], [2, 4]])

    def test_minimum(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Numpy.array(data, shape)
        min_value = Numpy.minimum(matrix)
        self.assertEqual(min_value, 1)

    def test_maximum(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Numpy.array(data, shape)
        max_value = Numpy.maximum(matrix)
        self.assertEqual(max_value, 4)

    def test_dot(self):
        data1 = [[1, 2], [3, 4]]
        shape1 = (2, 2)
        matrix1 = Numpy.array(data1, shape1)
        data2 = [[5, 6], [7, 8]]
        shape2 = (2, 2)
        matrix2 = Numpy.array(data2, shape2)
        result_matrix = Numpy.dot(matrix1, matrix2)
        self.assertIsInstance(result_matrix, Matrix)
        self.assertEqual(result_matrix.shape, (shape1[0], shape2[1]))
        self.assertEqual(result_matrix.data, [[19, 22], [43, 50]])

    def test_inverse(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Numpy.array(data, shape)
        inverse_matrix = Numpy.inverse(matrix)
        self.assertIsInstance(inverse_matrix, Matrix)
        self.assertEqual(inverse_matrix.shape, shape)
        # You may want to add additional assertions to verify the inverse matrix values

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)