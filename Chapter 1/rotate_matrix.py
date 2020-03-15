'''
I: nxn matrix
O: rotated matrix - 90 deg, clockwise
C: rotate matrix in place
E: empty matrix, even and odd values for n
'''
# O(N**2)

import unittest

def rotate_matrix(matrix):
    # reverse matrix
    matrix = matrix[::-1]

    for row in range(len(matrix)):
        for col in range(row):
            # perform swaps; transpose
            matrix[row][col], matrix[col][row] = \
                matrix[col][row], matrix[row][col]
    return matrix

class Test(unittest.TestCase):
    data = [(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]
    ), ([
        [1, 2 ,3],
         [4, 5, 6],
         [7, 8, 9]],
        [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]
    )]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()