# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    row_len = len(board)
    col_len = len(board[0])

    for i in range(row_len):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    
    for i in range(col_len):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][1]
        
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return "None"            

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "X":
       return "O"
    else:
       return "X"

def print_board(board):
    row_len = len(board)
    col_len = len(board[0])
    for i in range(row_len):
        for j in range(col_len):
            print(board[i][j], end = ' ')
        print("", end="\n")
     
def input_move(board, player, row, col):
    if board[row][col] == None:
        board[row][col] = player
    return board

def is_valid_input(board, row, col):
    return board[row][col] == None

def is_tie(board):
    row_len = len(board)
    col_len = len(board[0])

    for i in range(row_len):
        checker_set = set(board[i])
        if "O" not in checker_set or "X" not in checker_set:
            return False
            
    for j in range(col_len):
        checker_set = set()
        for i in range(row_len):
            checker_set = checker_set.add(board[i][j])
        if "O" not in checker_set or "X" not in checker_set:
            return False

    checker_set = set(board[0][0], board[1][1], board[2][2])
    if "O" not in checker_set or "X" not in checker_set:
            return False

    checker_set = set(board[0][2], board[1][1], board[2][0])        
    if "O" not in checker_set or "X" not in checker_set:
            return False

    return True  
