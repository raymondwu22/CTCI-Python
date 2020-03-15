# O(N*M)
import unittest

def zero_matrix(matrix):
    # Create array of boolean for rows and columns
    rowzero = [False] * len(matrix[0])
    colzero = [False] * len(matrix)

    # Traverse through our matrix to find where
    # there are 0s. Mark our rowzero and colzero
    # arrays with True for those index
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                rowzero[row] = True
                colzero[col] = True

    for row in range(len(rowzero)):
        if rowzero[row]:
            for col in range(len(colzero)):
                matrix[row][col] = 0

    for col in range(len(colzero)):
        if colzero[col]:
            for row in range(len(rowzero)):
                matrix[row][col] = 0

    return matrix


class Test(unittest.TestCase):
    data = [(
        [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]]

    )]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()