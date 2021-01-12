# import random
import numpy as np

from board import new_board, curr_board

def instructions():
    print(" 2040 ".center(130, "~"))
    print("""WELCOME!!! The game starts with 2 tiles, being either 2 or 4. Press the above keys to move the numbers in a direction. 
Tiles with the same number that collide will merge into the sum of both. Each time you move a new tile will 
appear, 2 or 4. The goal is to get a tile that adds up to 2048. HAVE FUN!!!

INSTRUCTIONS:
'W': Up 
'S': Down 
'A': Left 
'D': Right\n""")

def two_or_four():
    """Returns a list of a single number 2 (90% chance) or 4 (10% chance) randomly."""
    two_or_four = np.random.choice([2, 4], 1, replace=False, p=[.9, .1])

    return two_or_four

def add_new_tile(board):
    """Adds a new tile"""
    new_tile_val = two_or_four()
    row = np.random.randint(0, 3)
    col = np.random.randint(0, 3)

    while board[row][col] != 0:
        row = np.random.randint(0, 4)
        col = np.random.randint(0, 4)
    board[row][col] = new_tile_val

def main():
    instructions()
    flag = True # If start of game
    board = new_board()
    if flag:
        add_new_tile(board)
        add_new_tile(board)
        curr_board(board)
        flag = False

if __name__ == '__main__':
    main()