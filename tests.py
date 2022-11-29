import unittest
import unittest.mock as mock
from unittest.mock import patch
from random import choice
import logic
from cli import Human, Bot, Board, Game


# class TestLogic(unittest.TestCase):

#     def test_get_winner(self):
#         board_1 = [
#             ['X', None, 'O'],
#             [None, 'X', None],
#             [None, 'O', 'X'],
#         ]
#         board_2 = [
#             ['O', None, 'X'],
#             [None, 'O', None],
#             ['X', None, 'O'],
#         ]
#         board_3 = [
#             ['O', None, 'X'],
#             [None, 'O', None],
#             ['X', 'O', None],
#         ]
#         self.assertEqual(logic.get_winner(board_1), 'X')
#         self.assertEqual(logic.get_winner(board_2), 'O')
#         self.assertEqual(logic.get_winner(board_3), 'None')

#     def test_other_player(self):
#         player_1 = 'X'
#         player_2 = 'O'
#         self.assertEqual(logic.other_player(player_1), 'O')
#         self.assertEqual(logic.other_player(player_2), 'X')

#     def test_print_board(self):
#         board = [
#             ['X', None, 'O'],
#             [None, 'X', None],
#             [None, 'O', 'X'],
#         ]
#         self.assertEqual(logic.print_board(board),
#         'X None O'
#         'None X None' 
#         'None O X')
    
#     def test_input_move(self):
#         board = [
#             ['X', None, 'O'],
#             ['X', None, None],
#             [None, 'O', 'X'],
#         ]
#         player = 'O'
#         row = 0
#         col = 1
#         self.assertEqual(logic.input_move(board, player, row, col),
#         'X O O'
#         'X None None' 
#         'None O X')

#     def test_is_valid_input(self):
#         board = [
#             ['X', None, 'O'],
#             ['X', None, None],
#             [None, 'O', 'X'],
#         ]
#         row_1 = 0
#         col_1 = 1

#         row_2 = 0
#         col_2 = 0

#         self.assertEqual(logic.input_move(board, row_1, col_1), True)
#         self.assertEqual(logic.input_move(board, row_2, col_2), False)


#     def test_is_tie(self):
#         board_1 = [
#             ['X', None, 'O'],
#             ['X', 'O', None],
#             ['O', 'X', 'X'],
#         ]
#         board_2 = [
#             ['O', None, 'X'],
#             [None, 'O', None],
#             ['X', None, 'O'],
#         ]
#         self.assertEqual(logic.is_tie(board_1), True)
#         self.assertEqual(logic.is_tie(board_2), False)


class TestHuman(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_get_move(self):
        with patch('builtins.input', return_value=1):
            human_1 = Human('X')
            (x, y) = human_1.get_move(self.board)
            self.assertEqual((1,1), (x,y))

class TestBot(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_get_move(self):
        with patch('random.choice', return_value=(1,1)):
            bot_2 = Bot('O')
            (x, y) = bot_2.get_move(self.board)
            self.assertEqual((1,1), (x,y))

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_find_winner(self):
        self.board.set(0,0,'X')
        self.board.set(1,1,'X')
        self.board.set(2,2,'X')
        self.board.set(0,1,'O')
        self.board.set(1,0,'O')
        self.game = Game(self.board)
        self.assertEqual('X', self.game.find_winner())
    

if __name__ == '__main__':
    unittest.main()
 
