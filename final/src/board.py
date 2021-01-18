import numpy as np
from numpy.random import choice, randint

def new_board():
    """Returns a new 4 x 4 board of 0s."""
    board = np.zeros((4, 4), dtype=int)
    add_two_or_four_tile(board)
    add_two_or_four_tile(board)
    return board

def add_two_or_four_tile(board):
    two_or_four = choice([2, 4], 1, False, [0.9, 0.1])[0]
    # creates a tuple of arrays of the indices (arr(rows), arr(cols)) of tiles = 0
    find_zero_tiles = np.where(board == 0) 
    # unpackages the arr iterables into a list of tuples with their respective indices for tiles = 0
    zero_indices = [(row, col) for row, col in zip(find_zero_tiles[0], find_zero_tiles[1])]
    try: 
        random_zero_tile = zero_indices[choice(len(zero_indices), 1)[0]]
    except ValueError:
        pass
    else:
        board[random_zero_tile] = two_or_four

def display_board(board):
    """Prints out the current 4 x 4 board for the game 2048."""
    print(board, "\n")

def check_win_lose(board):
    """Checks for 2048 to win the game, checks to continue game, or if no others moves can be made."""
    # WIN GAME
    if 2048 in board:
        print("CONGRATS!!! You got 2048.")
        exit()

    # CONTINUE GAME
    # If there are any 0 tiles in the board
    zero_indices = len(np.where(board == 0)[0])
    if zero_indices > 0:
        return
    # Check to see if any adjacent tiles in the first 0-2 indices are equal
    for row in range(3): 
        for col in range(3): 
            if(board[row][col]== board[row][col + 1] or board[row][col]== board[row + 1][col]): 
                return
    # Check if there are any adjacent equal tiles in column 3
    for row in range(3): 
        if(board[row][3]== board[row + 1][3]): 
            return 
    # Check if there any adjacent equal tiles in row 3
    for col in range(3): 
        if(board[3][col]== board[3][col + 1]): 
            return 

    # THEN YOU LOSE
    print("There are no more moves to be made. YOU LOSE!")
    exit()
