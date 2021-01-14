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

class Moves:
    """Class for the possible moves the player can make."""

    def shift_board_left(self, board):
        """Shifts all non-zero tiles tom m the left."""
        for row in range(len(board)):
            board[row] = np.concatenate((board[row][board[row] != 0], board[row][board[row] == 0]))
        
        return board

    def merge_like_tiles_left(self, board):
        """Merge tiles of the same value on the after a left shift."""
        for row in range(len(board)):
            for col in range(len(board[row])-1):
                if (board[row][col] != 0) and (board[row][col] == board[row][col+1]):
                    board[row][col] = board[row][col] + board[row][col+1]
                    board[row][col+1] = 0
        shift_board_left(board)

        return board

    def shift_board_right_merge(self, board):
        """Reflects the board, then merges like tiles, and then reflects again."""
        board = np.fliplr(board)    
        shift_board_left(board)
        merge_like_tiles_left(board)
        board = np.fliplr(board)  

        return board

    def shift_board_up_merge(self,board):
        """Rotates the board 90 degs left, merge-like tiles, and rotate back."""
        board = np.rot90(board)
        shift_board_left(board)
        merge_like_tiles_left(board)
        board = np.rot90(board, k=-1)

        return board

    def shift_board_down_merge(self, board):
        """Rotates the board 90 degs right, merge-like tiles, and rotate back."""
        board = np.rot90(board, k=-1)
        shift_board_left(board)
        merge_like_tiles_left(board)
        board = np.rot90(board)

        np.testing.assert_array_equal(matrix, expected)

def main():
    instructions()
    flag = True # If start of game
    board = new_board()
    if flag:
        display_board(board)
        flag = False

if __name__ == '__main__':
    main()