import numpy as np

from board import Board

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

    def merge_like_tiles_left(self, board):
        """Merge tiles of the same value on the after a left shift."""
        for row in range(len(board)):
            for col in range(len(board[row])-1):
                if (board[row][col] != 0) and (board[row][col] == board[row][col+1]):
                    board[row][col] = board[row][col] + board[row][col+1]
                    self.score += board[row][cow]
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

    def shift_board_up_merge(self, board):
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
        return board