# Author: Brandon Hoffman
# Date: 1/12/2021
# Description: unittest for Store.py

import unittest
from JanggiGame import JanggiGame

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



if __name__ == '__main__':
    unittest.main()
