# Author: Brandon Hoffman
# Date: 1/12/2021
# Description: unittest for Store.py

import unittest
from janggigame import JanggiGame
from gamepiece import GamePiece

class JanggiGameTester(unittest.TestCase):
    """
    unit tests for janggigame.py
    """

    def test_initialization(self):
        """
        tests thte basic functionality of the JanggiGame class
        """
        game = JanggiGame()
        self.assertEqual(game.get_player_turn(), "BLUE")
        self.assertEqual(game.get_game_state(), "UNFINISHED")

    def test_initial_board(self):
        """
        """
        pass

    def test_piece_functionality(self):
        """
        """
        game = JanggiGame()
        piece_object = game.get_piece("A7")
        piece_name = piece_object.get_piece_name()
        self.assertEqual(piece_name, "Soldier")
        piece_color = piece_object.get_color()
        self.assertEqual(piece_color, "BLUE")


    def test_soldier_moves(self):
        """
        """
        game = JanggiGame()
        self.assertEqual(game.make_move("A7", "A6"), True)

    def test_soldier_moves(self):
        """
        """
        game = JanggiGame()
        self.assertEqual(game.make_move("A7", "A8"), False)

class GamePieceTester(unittest.TestCase):
    """
    unit tests for gamepiece.py
    """

    def test_diagonal_generator_test(self):
        """

        """
        gp = GamePiece("BLUE")
        moves = gp.get_diagonal_moves((4,4))
        print(list(moves))

        moves = gp.get_diagonal_moves((0,0))
        print(list(moves))

        moves = gp.get_diagonal_moves((9,10))
        print(list(moves))
        

if __name__ == '__main__':
    unittest.main()
