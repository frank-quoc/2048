import numpy as np
from numpy.random import choice, seed

def test_add_two_or_four_tile():
    """Test to add a new tile (2 or 4) to the 4 x 4 matrix."""
    seed(0)
    board = np.zeros((4, 4), dtype=int)
    two_or_four = choice([2, 4], 1, replace=False, p=[.9, .1])
    expected = np.array([[0, 0, 0, 0],
                            [2, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]])

    find_zero_tiles = np.where(board == 0) 
    zero_indices = [(row, col) for row, col in zip(find_zero_tiles[0], find_zero_tiles[1])]
    random_zero_tile = zero_indices[choice(len(zero_indices), 1)[0]]
    board[random_zero_tile] = two_or_four

    print(board)

test_add_two_or_four_tile()