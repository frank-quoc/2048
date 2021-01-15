import numpy as np
from numpy.random import choice, randint

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
        """Prints out the current 4 x 4 board for the game 2048."""
        print(self.board)
        print()

class Moves:
    """Class for the possible moves the player can make."""
    def __init__(self):
        self.score = 0
        self.board = Board()
        self.board.new_board()

    def __repr__(self):
        return f"Board Object: Score = {self.score}"

    def shift_board_left(self):
        """Shifts all non-zero tiles tom m the left."""
        for row in range(len(self.board)):
            self.board[row] = np.concatenate((self.board[row][board[row] != 0], \
                selfboard[row][board[row] == 0]))
    
    def merge_like_tiles_left(self):
        """Merge tiles of the same value on the after a left shift."""
        for row in range(len(self.board)):
            for col in range(len(self.board[row])-1):
                if (self.board[row][col] != 0) and (self.board[row][col] == self.board[row][col+1]):
                    self.board[row][col] = self.board[row][col] + self.board[row][col+1]
                    self.score += board[row][cow]
                    self.board[row][col+1] = 0
        shift_board_left(self.board)
    
    def move_right(self):
        """Reflects the board, then merges like tiles, and then reflects again."""
        self.board = np.fliplr(self.board)    
        shift_board_left(self.board)
        merge_like_tiles_left(self.board)
        self.board = np.fliplr(self.board)  
    
    def move_up(self):
        """Rotates the board 90 degs left, merge-like tiles, and rotate back."""
        self.board = np.rot90(self.board)
        shift_board_left(self.board)
        merge_like_tiles_left(self.board)
        self.board = np.rot90(self.board, k=-1)
    
    def move_down(self):
        """Rotates the board 90 degs right, merge-like tiles, and rotate back."""
        self.board = np.rot90(self.board, k=-1)
        shift_board_left(self.board)
        merge_like_tiles_left(self.board)
        self.board = np.rot90(self.board)

    # def display_score(self):
    #     """Prints out the current score."""
    #     print(self.score)

def main():
    instructions()
    new_game = Board()
    new_game.new_board()
    new_game.display_board()  
    while True: 
        move = input("Move?: ").upper()
        if move == 'A':
            new_game.shift_board_left()
            new_game.merge_like_tiles_lefselt()
            new_game.shift_board_left()
        elif move == 'D':
            new_game.move_right()
        elif move == 'W':
            new_game.move_up()
        elif move == "S":
            new_game.move_down()
        elif move == "Q":
            exit()
        else:
            print("You did not press W, A, S, or D. Please try again.")
            continue
        new_game.display_board()

if __name__ == '__main__':
    main()