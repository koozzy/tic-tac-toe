import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board_1 = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        board_2 = [
            ['O', None, 'X'],
            [None, 'O', None],
            ['X', None, 'O'],
        ]
        board_3 = [
            ['O', None, 'X'],
            [None, 'O', None],
            ['X', 'O', None],
        ]
        self.assertEqual(logic.get_winner(board_1), 'X')
        self.assertEqual(logic.get_winner(board_2), 'O')
        self.assertEqual(logic.get_winner(board_3), 'None')

    def other_player(self):
        player_1 = 'X'
        player_2 = 'O'
        self.assertEqual(logic.other_player(player_1), 'O')
        self.assertEqual(logic.other_player(player_2), 'X')

    def print_board(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.print_board(board),
        'X None O'
        'None X None' 
        'None O X')
    
    def input_move(self):
        board = [
            ['X', None, 'O'],
            ['X', None, None],
            [None, 'O', 'X'],
        ]
        player = 'O'
        row = 0
        col = 1
        self.assertEqual(logic.input_move(board, player, row, col),
        'X O O'
        'X None None' 
        'None O X')

    def is_valid_input(self):
        board = [
            ['X', None, 'O'],
            ['X', None, None],
            [None, 'O', 'X'],
        ]
        row_1 = 0
        col_1 = 1

        row_2 = 0
        col_2 = 0

        self.assertEqual(logic.input_move(board, row_1, col_1), True)
        self.assertEqual(logic.input_move(board, row_2, col_2), False)


    def is_tie(self):
        board_1 = [
            ['X', None, 'O'],
            ['X', 'O', None],
            ['O', 'X', 'X'],
        ]
        board_2 = [
            ['O', None, 'X'],
            [None, 'O', None],
            ['X', None, 'O'],
        ]
        self.assertEqual(logic.is_tie(board_1), True)
        self.assertEqual(logic.is_tie(board_2), False)




if __name__ == '__main__':
    unittest.main()