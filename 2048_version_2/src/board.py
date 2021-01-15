import numpy as np
from numpy.random import choice, randint

from moves import Moves

class Board:
    """Class for creating a new board, adding new tiles, and displaying the board."""
    def __init__(self):
        self.board = np.zeros((4, 4), dtype=int)
    
    def __repr__(self):
        return f"Board Object: {self.board}"

    def new_board(self):
        """Returns a new 4 x 4 board of 0s."""
        self.add_two_or_four_tile(self.board)
        self.add_two_or_four_tile(self.board)
        return self.board

    def add_two_or_four_tile(self, board):
        two_or_four = choice([2, 4], 1, False, [0.9, 0.1])[0]
        # creates a tuple of arrays of the indices (arr(rows), arr(cols)) of tiles = 0
        find_zero_tiles = np.where(self.board == 0) 
        # unpackages the arr iterables into a list of tuples with their respective indices for tiles = 0
        zero_indices = [(row, col) for row, col in zip(find_zero_tiles[0], find_zero_tiles[1])]
        random_zero_tile = zero_indices[choice(len(zero_indices), 1)[0]]
        self.board[random_zero_tile] = two_or_four

    def display_board(self):
        """Prints out a 4 x 4 board for the game 2048."""
        print(self.board)
        print()