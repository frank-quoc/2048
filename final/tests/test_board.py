import pytest

import numpy as np
from numpy.random import choice, seed, randint
from numpy.testing import assert_array_equal

def test_show_assert_true():
    assert True

class TestDisplayBoard:
    """A Class to test the displaying of a matrix."""

    def test_new_matrix_equals_4_4_0s(self):
        """A test to display a 4 x 4 board of 0s."""
        board = np.zeros((4, 4), dtype=int)
        expected = np.array([[0, 0, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]])
        assert_array_equal(board, expected)

class TestReturn2Or4:
    """Class with tests to return 2 or 4."""

    def test_return_2(self):
        """Test for two_or_four to return 2."""
        two = 2
        assert two == 2
    
    def test_return_4(self):
        """Test for two_or_four to return 4."""
        four = 4
        assert four == 4

    def test_two_or_four_seed_2(self):
        """Test to check if 2 is one of the random values set for variable two_or_four."""
        seed(0)
        two_or_four = choice([2, 4], 1, replace=False, p=[.9, .10])
        assert two_or_four == 2
    
    def test_two_or_four_seed_4(self):
        """Test to check if 4 is one of the random values set for variable two_or_four."""
        seed(4)
        two_or_four = choice([2, 4], 1, replace=False, p=[.9, .1])
        assert two_or_four == 4
            
    def test_add_two_or_four_tile(self):
        """Test to add a new tile (2 or 4) to the 4 x 4 matrix."""
        seed(0)
        board = np.zeros((4, 4), dtype=int)
        two_or_four = choice([2, 4], 1, replace=False, p=[.9, .1])
        expected = np.array([[0, 0, 0, 0],
                             [0, 2, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]])

        find_zero_tiles = np.where(board == 0) 
        zero_indices = [(row, col) for row, col in zip(find_zero_tiles[0], find_zero_tiles[1])]
        random_zero_tile = zero_indices[choice(len(zero_indices), 1)[0]]
        board[random_zero_tile] = two_or_four
        assert_array_equal(board, expected)

class TestMatrixMovements:
    """Class to test the movement movements of matrixes left, right, up, down, and merge."""

    def test_shift_matrix_left(self):
        """Test to shift all non-zero elements to the left, and zero elements to the right"""
        matrix = np.array([[0, 2, 0, 2],
                           [2, 0, 4, 2],
                           [0, 0, 0, 0],
                           [0, 0, 0, 4]])
        expected = np.array([[2, 2, 0, 0],
                             [2, 4, 2, 0],
                             [0, 0, 0, 0],
                             [4, 0, 0, 0]])

        for row in range(len(matrix)):
            matrix[row] = np.concatenate((matrix[row][matrix[row] != 0], matrix[row][matrix[row] == 0]))
        assert_array_equal(matrix, expected)

    def shift_board_left(self, board):
        """Shifts all non-zero tiles tom m the left."""
        for row in range(len(board)):
            board[row] = np.concatenate((board[row][board[row] != 0], board[row][board[row] == 0]))
        return board

    def test_matrx_merge_consecutive_like_values_left(self):
        """Test to double consecutive elements with non-zero values (left-most first)."""
        matrix = np.array([[2, 2, 0, 0],
                              [2, 2, 2, 0],
                              [0, 0, 0, 0],
                              [4, 4, 0, 0]])
        expected = np.array([[4, 0, 0, 0],
                             [4, 2, 0, 0],
                             [0, 0, 0, 0],
                             [8, 0, 0, 0]])
        for row in range(len(matrix)):
            for col in range(len(matrix[row])-1):
                if (matrix[row][col] != 0) and (matrix[row][col] == matrix[row][col+1]):
                    matrix[row][col] = matrix[row][col] + matrix[row][col+1]
                    matrix[row][col+1] = 0
        self.shift_board_left(matrix)
        assert_array_equal(matrix, expected)
    
    def test_reflect_matrix(self):
        """Test to reflect the a matrix."""
        matrix = np.array([[0, 0, 2, 2],
                           [0, 2, 2, 2],
                           [0, 0, 0, 0],
                           [0, 0, 4, 4]])
        expected = np.array([[2, 2, 0, 0],
                             [2, 2, 2, 0],
                             [0, 0, 0, 0],
                             [4, 4, 0, 0]]) 
        matrix = np.flip(matrix, axis=1)    
        assert_array_equal(matrix, expected)

    def merge_like_tiles_left(self, board):
        """Merge tiles of the same value on the after a left shift."""
        for row in range(len(board)):
            for col in range(len(board[row])-1):
                if (board[row][col] != 0) and (board[row][col] == board[row][col+1]):
                    board[row][col] = board[row][col] + board[row][col+1]
                    board[row][col+1] = 0
        self.shift_board_left(board)
        return board
    
    def test_reflect_matrix_merge_reflect_again(self):
        """Test to reflects the board, then merges like tiles, and then reflects again."""
        matrix = np.array([[0, 0, 2, 2],
                            [0, 2, 2, 2],
                            [0, 0, 0, 0],
                                [0, 0, 4, 4]])
        expected = np.array([[0, 0, 0, 4],
                             [0, 0, 2, 4],
                             [0, 0, 0, 0],
                             [0, 0, 0, 8]])                
        matrix = np.fliplr(matrix)    
        self.shift_board_left(matrix)
        self.merge_like_tiles_left(matrix)
        matrix = np.fliplr(matrix)  
        assert_array_equal(matrix, expected)
    
    def test_rotate_matrix_90_left(self):
        """Test to rotate the matrix 90 degrees left"""
        matrix = np.array([[0, 0, 2, 2],
                           [0, 2, 2, 2],
                           [0, 0, 0, 0],
                           [0, 0, 4, 4]])
        expected = np.array([[2, 2, 0, 4],
                             [2, 2, 0, 4],
                             [0, 2, 0, 0],
                             [0, 0, 0, 0]])
        matrix = np.rot90(matrix)
        assert_array_equal(matrix, expected)

    def test_rotate_matrix_90_left_merge_shift_rotate_back(self):
        """Test to rotate the matrix 90 deg left, merge, shift non-zero elements, and rotate back."""
        matrix = np.array([[0, 0, 2, 2],
                           [0, 2, 2, 2],
                           [0, 0, 0, 0],
                           [0, 0, 4, 4]])
        expected = np.array([[0, 2, 4, 4],
                             [0, 0, 4, 4],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]])
        matrix = np.rot90(matrix)
        self.shift_board_left(matrix)
        self.merge_like_tiles_left(matrix)
        matrix = np.rot90(matrix, k=-1)
        assert_array_equal(matrix, expected)
    
    def test_rotate_matrix_90_right(self):
        """Test to rotate the matrix 90 degrees right"""
        matrix = np.array([[0, 0, 2, 2],
                           [0, 2, 2, 2],
                           [0, 0, 0, 0],
                           [0, 0, 4, 4]])
        expected = np.array([[0, 0, 0, 0],
                             [0, 0, 2, 0],
                             [4, 0, 2, 2],
                             [4, 0, 2, 2]])
        matrix = np.rot90(matrix, k=-1)
        assert_array_equal(matrix, expected)

    def test_rotate_matrix_90_right_merge_shift_rotate_back(self):
        """Test to rotate the matrix 90 degrees right"""
        matrix = np.array([[0, 0, 2, 2],
                           [0, 2, 2, 2],
                           [0, 0, 0, 0],
                           [0, 0, 4, 4]])
        expected = np.array([[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 4, 4],
                             [0, 2, 4, 4]])
        matrix = np.rot90(matrix, k=-1)
        self.shift_board_left(matrix)
        self.merge_like_tiles_left(matrix)
        matrix = np.rot90(matrix)
        assert_array_equal(matrix, expected)

    def test_find_2048_element(self):
        """Test to see if 2048 is one of the values in a matrix array."""
        matrix = np.array([[0, 0, 2, 2],
                           [0, 2, 2, 2],
                           [0, 0, 0, 0],
                           [2048, 0, 4, 4]])
        assert 2048 in matrix

    def check_no_indices_with_zero():
        """Test for number of elements in array with no 0 values."""
        matrix = np.arange(16).reshape(4,4)
        zero_indices = len(np.where(matrix == 0)[0])
        assert zero_indices == 0
       
if __name__ == '__main__':
    pytest.main()
