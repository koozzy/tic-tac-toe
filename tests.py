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
    
    #def input_move(board, player, row, col)：

    #def is_valid_input(board, row, col)：

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


    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()