import random

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
    """Adds 2 (90% chance) or 4 (10% chance) to a random open tile."""
    two_or_four = random.choices([2, 4], weights=(90, 10), k=1)
    return two_or_four[0]

def add_new_tile(board):
    """Adds a new tile to the board."""
    new_tile_val = two_or_four()
    # Initial index to try to add 2 or 4 value to
    row_idx = random.randint(0, 3)
    col_idx = random.randint(0, 3)
    # checks if it is already filled, tries new indexes if it is
    while board[row_idx][col_idx] != 0:
        row_idx = random.randint(0, 3)
        col_idx = random.randint(0, 3)
    board[row_idx][col_idx] = new_tile_val

def shift_tiles(board):
    """Moves all the tiles to any 0 tiles on the left."""
    for row in range(4):
        lowest_0_col = 0
        for col in range(4):
            if board[row][col] != 0:
                board[row][lowest_0_col] = board[row][col]
                board[row][col] = 0
            lowest_0_col += 1
    return board

def merge_tiles(board):
    """Adds any tiles that are adjacent, same value tiles together. 'Merges' them left."""
    for row in range(4):
        merged = False
        for col in range(3):
            if board[row][col] == board[row][col+1] != 0:
                board[row][col] += board[row][col+1]
                board[row][col+1] = 0
    return board

def reverse_matrix(board):
    """Reverses the board when player presses right or down, to check for shifts and merges, reverse it back."""
    for row in range(len(board)):
        board[row] = board[row][::-1]
    return board

def transpose_matrix(board):
    """Transposes the board when the player presses up or down, tranpose back."""
    tranposed_board = [[board[col][row] for col in range(len(board))] for row in range(len(board[0]))]
    return tranposed_board

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