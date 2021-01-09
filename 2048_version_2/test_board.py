import pytest

import numpy as np
import random

def test_show_assert_true():
    assert True

class TestDisplayBoard:
    def test_new_board_equals_4_4_0s(self):
        """A test to display a 4 x 4 board of 0s."""
        self.board = np.zeros((4, 4), dtype=int)
        self.expected = np.array([[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]])
        assert np.array_equal(self.board, self.expected)

class TestReturn2Or4:
    def test_return_2(self):
        """Test for two_or_four to return 2."""
        self.two = 2
        assert self.two == 2
    
    def test_return_4(self):
        """Test for two_or_four to return 4."""
        self.four = 4
        assert self.four == 4

    def test_two_or_four_seed_2(self):
        """Adds 2 (90% chance) or 4 (10% chance) to a random open tile."""
        random.seed(0)
        self.two_or_four = random.choices([2, 4], weights=(90, 10), k=1)
        assert self.two_or_four[0] == 2
    
    def test_two_or_four_seed_4(self):
        """Adds 2 (90% chance) or 4 (10% chance) to a random open tile."""
        random.seed(2)
        self.two_or_four = random.choices([2, 4], weights=(90, 10), k=1)
        assert self.two_or_four[0] == 4
            
if __name__ == '__main__':
    pytest.main()