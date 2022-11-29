# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import empty_square_move
import csv
import random

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
                checker_set.add(self._rows[i][j])
            if "O" not in checker_set or "X" not in checker_set:
                return False

        checker_set = set([self._rows[0][0], self._rows[1][1], self._rows[2][2]])
        if "O" not in checker_set or "X" not in checker_set:
                return False

        checker_set = set([self._rows[0][2], self._rows[1][1], self._rows[2][0]])        
        if "O" not in checker_set or "X" not in checker_set:
                return False

        return True  

class Player:
    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.steps = 0
    
    def get_name(self):
        return self.name

    def get_steps(self):
        return self.steps
        
    def get_move(self):
        pass
    
    def get_value(self):
        return self.value
    
    def add_step(self):
        self.steps = self.steps + 1

    def __str__(self):
        return f"Name: {self.name}, Value: {self.value}"

    
class Human(Player):
    def __init__(self, value, name):
        super().__init__(value, name)
    
    def get_move(self, board):
        row = int(input("Please enter row num: "))
        col = int(input("Please enter col num: "))
        while board.get(row,col) is not None:
            row = int(input("Please enter row num: "))
            col = int(input("Please enter col num: "))
        return (row, col)

class Bot(Player):
    def __init__(self, value, name):
        super().__init__(value, name)
        
    def get_move(self, board):
        return empty_square_move(board)

class StupidBot(Player):
    def __init__(self, value, name):
        super().__init__(value, name)
        
    def get_move(self, board):
        for row in range(3):
            for col in range(3):
                if board.get(row,col) is None:
                    return (row, col)
        return (None, None)

class Game:
    def __init__(self, board):
        self.board = board

    def clear_board(self):
        self.board = Board()
        
    def setup_player(self):
        player_number = int(input("how many human players? 1 or 2: "))
        first_player = str(input("what is the value of first player? X or O: "))
        self.player1 = Human(first_player)
        second_player = "X" if first_player == "O" else "O"
        if player_number == 1:
            self.player2 = Bot(second_player)
        else:
            self.player2 = Human(second_player)
    
    def setup_two_bots(self):
        first_player = random.choice([1,2]) # 1 means Bot, 2 means StupidBot
        if first_player == 1:
            self.player1 = Bot("X", "1")
            self.player2 = StupidBot("O", "2")
        else:
            self.player1 = StupidBot("X", "2")
            self.player2 = Bot("O", "1")
        print(f"first player is {self.player1}")
        print(f"second player is {self.player2}")
    
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
        # self.setup_player()
        self.clear_board()
        self.setup_two_bots()
        winner = None
        while winner is None:
            (row, col) = self.player1.get_move(self.board)
            self.board.set(row, col, self.player1.get_value())
            self.player1.add_step()
            # print(self.board)

            winner = self.find_winner()
            if winner == "T":
                print("This is a tie")
                break
            elif winner is not None:
                print(f"winner is {winner}!")
                break
            
            (row, col) = self.player2.get_move(self.board)
            self.board.set(row, col, self.player2.get_value())
            self.player2.add_step()
            # print(self.board)
            winner = self.find_winner()
            if winner == "T":
                print("This is a tie")
                break
            elif winner is not None:
                print(f"winner is {winner}!")
                break
        
        if winner == self.player1.get_value():
            return self.record_result(self.player1, self.player2)
        elif winner == self.player2.get_value():
            return self.record_result(self.player2, self.player1)
        else:
            return self.record_result()
    
    def record_result(self, winner=None, loser=None):
        result = []
        if winner and loser:
            result = [
                game_id,
                winner.get_name(), 
                loser.get_name(), 
                "N/A", 
                self.player1.get_name(), 
                self.player1.get_steps() + self.player2.get_steps(),
                winner.get_value(),
                winner.get_steps()
            ]
        else:
            result = [
                game_id,
                "N/A", 
                "N/A", 
                "YES", 
                self.player1.get_name(), 
                self.player1.get_steps() + self.player2.get_steps(),
                "N/A",
                "N/A",
            ]
        return result


if __name__ == '__main__':
    header = ['game_id', 'winner_bot', 'loser_bot', 'draws', 'sente_bot','total_steps','winner_character','winner_steps']
    f = open(r'TicTacToe_data.csv', 'a', encoding='UTF8')
    writer = csv.writer(f)
    writer.writerow(header)

    my_game = Game(Board())
    for i in range(100):
        game_id = i + 1
        data = my_game.run_game()
        writer.writerow(data)
    
    f.close()