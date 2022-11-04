# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
board = make_empty_board()
row_len = len(board)
col_len = len(board[0])

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    found_winner = False

    for i in range(row_len):
        if board[i][0] == board[i][1] == board[i][2]:
            found_winner = True
            return board[i][0]
    
    for i in range(col_len):
        if board[0][i] == board[1][i] == board[2][i]:
            found_winner = True
            return board[0][1]
        
    if board[0][0] == board[1][1] == board[2][2]:
            found_winner = True
            return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
            found_winner = True
            return board[0][2]


def other_player(player):
    """Given the character for a player, returns the other player."""
    for i in board[i][col_len]:
        for j in board[rol_len][j]:
            if board[i][j] == player:
                return board[i][j]  # FIXME