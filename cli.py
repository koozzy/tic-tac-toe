# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, print_board, input_move, other_player, get_winner, is_valid_input, is_tie


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    print_board(board)
    # ask user to input the first player name
    player = input('Enter Your Chosen Charactor, X or O:')
    while winner == None:
        row = input('Enter Your Chosen Row,0-2:')
        col = input('Enter Your Chosen Column,0-2:')
        while not is_valid_input(board, int(row), int(col)):
            row = input('Enter Your Chosen Row,0-2:')
            col = input('Enter Your Chosen Column,0-2:')
        
        board = input_move(board, player, int(row), int(col))
        print_board(board)
        if is_tie(board) == False:
            if get_winner(board) == None:
                print("Take a turn!")
                player = other_player(player)
            else:
                winner = player
                print(player, "is the winner.")
        else:
            print("This is a tie.")
            break
        