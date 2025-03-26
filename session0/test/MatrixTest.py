# session0/test/MatrixTest.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from Matrix import Matrix

class MatrixTest(unittest.TestCase):
    def test_init(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Matrix(data, shape)
        self.assertIsInstance(matrix, Matrix)
        self.assertEqual(matrix.shape, shape)
        self.assertEqual(matrix.data, data)

    def test_get_element(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Matrix(data, shape)
        self.assertEqual(matrix.get_element(0, 0), 1)
        self.assertEqual(matrix.get_element(1, 1), 4)

    def test_set_element(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Matrix(data, shape)
        matrix.set_element(0, 0, 5)
        self.assertEqual(matrix.get_element(0, 0), 5)

    def test_get_row(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Matrix(data, shape)
        self.assertEqual(matrix.get_row(0), [1, 2])
        self.assertEqual(matrix.get_row(1), [3, 4])

    def test_get_column(self):
        data = [[1, 2], [3, 4]]
        shape = (2, 2)
        matrix = Matrix(data, shape)
        self.assertEqual(matrix.get_column(0), [1, 3])
        self.assertEqual(matrix.get_column(1), [2, 4])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)