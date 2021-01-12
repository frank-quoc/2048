import numpy as np

def new_board():
    """Returns a new 4 x 4 board of 0s."""
    board = np.zeros((4, 4), dtype=int)

    return board

def curr_board(board):
    """Prints out a 4 x 4 board for the game 2048."""
    print(board)
    print()