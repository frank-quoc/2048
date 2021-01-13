import numpy as np
from numpy.random import choice, randint

from board import new_board, add_two_or_four_tile, display_board

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

def shift_board_left(board):
    """Shifts all non-zero tiles tom m the left."""
    for row in range(len(board)):
        board[row] = np.concatenate((board[row][board[row] != 0], board[row][board[row] == 0]))

def merge__like_tiles_left(board):
    """Merge tiles of the same value on the after a left shift."""
    for row in range(len(board)):
        for col in range(len(board[row])-1):
            if (board[row][col] != 0) and (board[row][col] == board[row][col+1]):
                board[row][col] = board[row][col] + board[row][col+1]
                board[row][col+1] = 0

def main():
    instructions()
    flag = True # If start of game
    board = new_board()
    if flag:
        display_board(board)
        flag = False

if __name__ == '__main__':
    main()