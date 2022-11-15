# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import empty_square_move

class Board:
    def __init__(self):
        self._rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
    def __str__(self):
        s = '-------\n'
        for row in self._rows:
            for cell in row:
                s = s + '|'
                if cell == None:
                    s = s + ' '
                else:
                    s = s + cell
            s = s + '|\n-------\n'
        return s
    def get_row_len(self):
        return len(self._rows)

    def get_col_len(self):
        return len(self._rows[0])

    def get(self, x ,y):
        return self._rows[x][y]

    def set(self, x, y, value):
        self._rows[x][y] = value

    def is_tie(self):
        row_len = self.get_row_len()
        col_len = self.get_col_len()

        for i in range(row_len):
            checker_set = set(self._rows[i])
            if "O" not in checker_set or "X" not in checker_set:
                return False
                
        for j in range(col_len):
            checker_set = set()
            for i in range(row_len):
                checker_set = checker_set.add(self._rows[i][j])
            if "O" not in checker_set or "X" not in checker_set:
                return False

        checker_set = set(self._rows[0][0], self._rows[1][1], self._rows[2][2])
        if "O" not in checker_set or "X" not in checker_set:
                return False

        checker_set = set(self._rows[0][2], self._rows[1][1], self._rows[2][0])        
        if "O" not in checker_set or "X" not in checker_set:
                return False

        return True  

class Player:
    def __init__(self, value):
        self.value = value
        
    def get_move(self):
        pass
    
    def get_value(self):
        return self.value
    
class Human(Player):
    def __init__(self, value):
        super().__init__(value)
    
    def get_move(self, board):
        row = int(input("Please enter row num: "))
        col = int(input("Please enter col num: "))
        while board.get(row,col) is not None:
            row = int(input("Please enter row num: "))
            col = int(input("Please enter col num: "))
        return (row, col)

class Bot(Player):
    def __init__(self, value):
        super().__init__(value)
        
    def get_move(self, board):
        return empty_square_move(board)

class Game:
    def __init__(self, board):
        self.board = board
        
    def setup_player(self):
        player_number = int(input("how many human players? 1 or 2: "))
        first_player = str(input("what is the value of first player? X or O: "))
        self.player1 = Human(first_player)
        second_player = "X" if first_player == "O" else "O"
        if player_number == 1:
            self.player2 = Bot(second_player)
        else:
            self.player2 = Human(second_player)
    
    def find_winner(self):
        board = self.board
        row_len = board.get_row_len()
        col_len = board.get_col_len()
        for i in range(row_len):
            if board.get(i, 0) == board.get(i, 1) and board.get(i, 0) == board.get(i, 2):
                return board.get(i, 0)
        for i in range(col_len):
            if board.get(0, i) == board.get(1, i) and board.get(0, i) == board.get(2, i):
                return board.get(0, i)
        if board.get(0, 0) == board.get(1, 1) and board.get(0, 0) == board.get(2, 2):
            return board.get(0, 0)
        if board.get(0, 2) == board.get(1, 1) and board.get(0, 2) == board.get(2, 0):
            return board.get(0, 2)
        if board.is_tie():
            return "T" 
        return None
    
    def run_game(self):
        self.setup_player()
        winner = None
        while winner is None:
            (row, col) = self.player1.get_move(self.board)
            self.board.set(row, col, self.player1.get_value())
            print(self.board)

            winner = self.find_winner()
            if winner == "T":
                print("This is a tie")
                break
            elif winner is not None:
                print(f"winner is {winner}!")
                break
            
            (row, col) = self.player2.get_move(self.board)
            self.board.set(row, col, self.player2.get_value())
            print(self.board)
            winner = self.find_winner()
            if winner == "T":
                print("This is a tie")
                break
            elif winner is not None:
                print(f"winner is {winner}!")
                break

if __name__ == '__main__':
    my_game = Game(Board())
    my_game.run_game()
