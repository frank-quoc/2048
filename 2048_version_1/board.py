import numpy as np
import random

def new_board():
    """Returns a 4 x 4 board of 0s"""
    board = np.zeros((4, 4), dtype=int)

    return board

def curr_board(board):
    """Prints the current board with the current tiles."""
    print(board)
    print()