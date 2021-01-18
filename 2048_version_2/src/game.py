import numpy as np
from numpy.random import choice, randint

from board import new_board, add_two_or_four_tile, display_board, check_win_lose

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
    def __init__(self):
        self.score = 0

    def __repr__(self):
        return f"Board Object: Score = {self.score}"

    def shift_board_left(self, board):
        """Shifts all non-zero tiles tom m the left."""
        for row in range(len(board)):
            board[row] = np.concatenate((board[row][board[row] != 0], board[row][board[row] == 0]))
    
    def merge_tiles(self, board):
        """Merge tiles of the same value on the after a left shift."""
        for row in range(len(board)):
            for col in range(len(board[row])-1):
                if (board[row][col] != 0) and (board[row][col] == board[row][col+1]):
                    board[row][col] = board[row][col] + board[row][col+1]
                    self.score += board[row][col]
                    board[row][col+1] = 0
        self.shift_board_left(board)
        self.display_score()
    
    def move_left(self, board):
        """Moves the board left, merge the tiles."""
        copy = np.copy(board) # makes a deep copy
        self.shift_board_left(board)
        self.merge_tiles(board)
        if (board == copy).all(): # if after the shifts, the board is exactly the same.
            return # redo it
        else:
            add_two_or_four_tile(board) # add a new tile

    def move_right(self, board):
        """Reflects the board, then merges like tiles, and then reflects again."""
        copy = np.copy(board)
        board = np.fliplr(board)    
        self.shift_board_left(board)
        self.merge_tiles(board)
        board = np.fliplr(board) 
        if (board == copy).all(): 
            return 
        else:
            add_two_or_four_tile(board) 
    
    def move_up(self, board):
        """Rotates the board 90 degs left, merge-like tiles, and rotate back."""
        copy = np.copy(board)
        board = np.rot90(board)
        self.shift_board_left(board)
        self.merge_tiles(board)
        board = np.rot90(board, k=-1)
        if (board == copy).all(): # if after the shifts, the board is exactly the same.
            return # redo it
        else:
            add_two_or_four_tile(board) # add a new tile
    
    def move_down(self, board):
        """Rotates the board 90 degs right, merge-like tiles, and rotate back."""
        copy = np.copy(board)
        board = np.rot90(board, k=-1)
        self.shift_board_left(board)
        self.merge_tiles(board)
        board = np.rot90(board)
        if (board == copy).all(): # if after the shifts, the board is exactly the same.
            return # redo it
        else:
            add_two_or_four_tile(board) # add a new tile

    def display_score(self):
        """Prints out the current score."""
        print(f"\nSCORE: {self.score}")

def main():
    instructions()
    board = new_board()
    display_board(board)
    moves = Moves()
    while True: 
        player_input = input("Move: ").upper()
        if player_input == 'A':
            moves.move_left(board)
        elif player_input == 'D':
            moves.move_right(board)
        elif player_input == 'W':
            moves.move_up(board)
        elif player_input == "S":
            moves.move_down(board)
        elif player_input == "Q":
            exit()
        else:
            print("You did not press W, A, S, or D. Please try again.")
            continue
        display_board(board)
        check_win_lose(board)

if __name__ == '__main__':
    main()