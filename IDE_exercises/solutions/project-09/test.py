# Author: Brandon Hoffman
# Date: 1/12/2021
# Description: unittest for Store.py

import unittest
from janggigame import JanggiGame

class JanggiGameTester(unittest.TestCase):
    """
    unit tests for JanggiGame.py
    """

    def test_initialization(self):
        """
        tests thte basic functionality of the Product class
        """
        game = JanggiGame()

        self.assertEqual(game.get_player_turn(), "BLUE")

    def test_get_color(self):
        """
        """
        pass

    def test_get_game_state(self):
        """
        """
        pass

    def test_soldier_moves(self):
        """
        """
        game = JanggiGame()
        piece_object = game.get_piece("A7")
        piece_name = piece_object.get_piece_name()
        self.assertEqual(piece_name, "Soldier")
        piece_color = piece_object.get_color()
        self.assertEqual(piece_color, "BLUE")
        self.assertEqual(game.make_move("A7", "A6"), True)




if __name__ == '__main__':
    unittest.main()
