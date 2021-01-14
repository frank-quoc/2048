import numpy as np
from numpy.random import choice, seed

def test_transpose_matrix():
    matrix = np.array([[0, 0, 2, 2],
                        [0, 2, 2, 2],
                        [0, 0, 0, 0],
                        [0, 0, 4, 4]])
    expected = np.array([[0, 0, 0, 0],
                            [0, 2, 0, 0],
                            [2, 2, 0, 4],
                            [2, 2, 0, 4]])
    matrix = matrix.T

    print(matrix)

test_transpose_matrix()