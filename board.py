def new_board():
    """Returns a 4x4 board with all 0."""
    board = []
    for row in range(4):
        board.append([0]*4)
    return board

def display_board(board):
    """Prints out the board with the current tile values."""
    for row in board:
        print(row)
    print()