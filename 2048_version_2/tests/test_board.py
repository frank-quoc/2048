import pytest
from unittest.mock import MagicMock

import numpy as np
from numpy.random import choice, seed, randint

mock_object = MagicMock()
mock_object(np.zeros((4, 4), dtype=int))

def test_show_assert_true():
    assert True

class TestDisplayBoard:
    def test_new_board_equals_4_4_0s(self):
        """A test to display a 4 x 4 board of 0s."""
        board = np.zeros((4, 4), dtype=int)
        expected = np.array([[0, 0, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]])
        np.testing.assert_array_equal(board, expected)

class TestReturn2Or4:
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

        np.testing.assert_array_equal(board, expected)
        
    def test_shift_board_left(self):
        """Test to shift a 4 x 4 array to the left."""
        pre_shift = np.array([[0, 2, 0, 2],
                              [2, 0, 4, 2],
                              [0, 0, 0, 0],
                              [0, 0, 0, 4]])
        expected = np.array([[2, 2, 0, 0],
                             [2, 4, 2, 0],
                             [0, 0, 0, 0],
                             [4, 0, 0, 0]])

        for row in range(len(pre_shift)):
            pre_shift[row] = np.concatenate((pre_shift[row][pre_shift[row] != 0], \
                pre_shift[row][pre_shift[row] == 0]))
        
        np.testing.assert_array_equal(pre_shift, expected)

    def test_merge_consecutive_like_values_left(self):
        """Test to merge tiles of the same value on the after a left shift."""
        pre_merge = np.array([[2, 2, 0, 0],
                              [2, 2, 2, 0],
                              [0, 0, 0, 0],
                              [4, 4, 0, 0]])
        expected = np.array([[4, 0, 0, 0],
                             [4, 0, 2, 0],
                             [0, 0, 0, 0],
                             [8, 0, 0, 0]])
        for row in range(len(pre_merge)):
            for col in range(len(pre_merge[row])-1):
                if (pre_merge[row][col] != 0) and (pre_merge[row][col] == pre_merge[row][col+1]):
                    pre_merge[row][col] = pre_merge[row][col] + pre_merge[row][col+1]
                    pre_merge[row][col+1] = 0
        np.testing.assert_array_equal(pre_merge, expected)
        
if __name__ == '__main__':
    pytest.main()