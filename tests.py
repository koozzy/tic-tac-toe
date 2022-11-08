import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def other_player(self):
        player = 'X'
        self.assertEqual(logic.other_player(player), 'X')

    def print_board(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.print_board(board), 'X')
    
    def input_move(board, player, row, col)
    
    def is_valid_input(board, row, col)

    def is_tie(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.is_tie(board), 'X')


    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()