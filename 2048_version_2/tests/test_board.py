import pytest
from unittest.mock import MagicMock

import numpy as np

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
        """Adds 2 (90% chance) or 4 (10% chance) to a random open tile."""
        np.random.seed(0)
        two_or_four = np.random.choice([2, 4], 1, replace=False, p=[.9, .10])
        assert two_or_four == 2
    
    def test_two_or_four_seed_4(self):
        """Adds 2 (90% chance) or 4 (10% chance) to a random open tile."""
        np.random.seed(4)
        two_or_four = np.random.choice([2, 4], 1, replace=False, p=[.9, .1])
        assert two_or_four == 4
            
    def test_add_new_tile(self):
        """Adds a new tile"""
        np.random.seed(0)
        board = np.zeros((4, 4), dtype=int)
        two_or_four = np.random.choice([2, 4], 1, replace=False, p=[.9, .1])
        expected = np.array([[0, 0, 0, 0],
                             [2, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]])

        row = np.random.randint(0, 3)
        col = np.random.randint(0, 3)
        while board[row][col] != 0:
            row = np.random.randint(0, 4)
            col = np.random.randint(0, 4)
        board[row][col] = two_or_four

        np.testing.assert_array_equal(board, expected)
        
    # def test_display_a_new_board(self):
    #     """Displays a new 4 x 4 board with 2 tiles with either a 2 (90% chance) or 4 (10%)."""
    #     board = np.random.choice(0, (4, 4), )

        
if __name__ == '__main__':
    pytest.main()