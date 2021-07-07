import sys
sys.path.append('../src/')

from JanggiGame import JanggiGame
import unittest


class TestingJanggi(unittest.TestCase):

    def test_check_range(self):
        game = JanggiGame()
        actual = game.check_range(0, 0)
        expected = True
        self.assertEqual(actual, expected)

        actual2 = game.check_range(0, 9)
        expected2 = False
        self.assertEqual(actual2, expected2)

        actual3 = game.check_range(10, 1)
        expected3 = False
        self.assertEqual(actual3, expected3)

    def test_get_game_state(self):
        game = JanggiGame()
        actual = game.get_game_state()
        expected = "UNFINISHED"
        self.assertEqual(actual, expected)

    def test_active_player(self):
        game = JanggiGame()
        game._turn_count = 0
        actual = game.get_active_player()
        expected = "b"
        self.assertEqual(actual, expected)

        game._turn_count += 1
        actual2 = game.get_active_player()
        expected2 = "r"
        self.assertEqual(actual2, expected2)

        game._turn_count += 7
        actual3 = game.get_active_player()
        expected3 = "b"
        self.assertEqual(actual3, expected3)

    def test_get_opponent(self):
        game = JanggiGame()
        game._turn_count = 0
        actual = game.get_opponent()
        expected = "r"
        self.assertEqual(actual, expected)

        game._turn_count += 1
        actual2 = game.get_opponent()
        expected2 = "b"
        self.assertEqual(actual2, expected2)

        game._turn_count += 7
        actual3 = game.get_opponent()
        expected3 = "r"
        self.assertEqual(actual3, expected3)

    def test_get_piece(self):
        game = JanggiGame()
        actual = game.get_piece(0, 0)
        expected = "rc"
        self.assertEqual(actual, expected)

        actual2 = game.get_piece(7, 7)
        expected2 = "bC"
        self.assertEqual(actual2, expected2)

        actual3 = game.get_piece(1, 4)
        expected3 = "rG"
        self.assertEqual(actual3, expected3)

    def test_moving_soldier(self):
        game = JanggiGame()
        game._turn_count = 0
        # game.get_piece(6, 0)                # should be blue soldier on far left
        game.make_move("a7", "a6")
        actual = game.get_piece(5, 0)
        expected = "bs"
        self.assertEqual(actual, expected)
        actual2 = game.get_piece(6, 0)
        expected2 = "--"
        self.assertEqual(actual2, expected2)
        game.get_board()

        self.assertEqual(game._turn_count, 1)
        game.make_move("a4", "a4")

        self.assertEqual(game._turn_count, 2)
        game.make_move("a6", "b6")
        actual3 = game.get_piece(5, 1)
        expected3 = "bs"
        self.assertEqual(actual3, expected3)
        game.get_board()

        game.make_move("a4", "a5")
        game.get_board()
        game.make_move("b6", "a6")
        game.get_board()
        game.make_move("a5", "a6")              # moving rs onto bs, Shouldn't work
        game.make_move("a5", "b5")              # now same player has another attempt to move
        game.get_board()
        game.make_move("c7", "b6")              # attempting diagonal move outside palace
        game.get_board()

    def test_moving_horse(self):
        game = JanggiGame()
        self.assertEqual(game._turn_count, 0)
        game.get_board()
        game.make_move("c10", "d8")
        game.get_board()
        game.make_move("c1", "c1")          # RED pass
        game.make_move("d8", "e6")
        game.get_board()

        # testing horizontal move
        game.make_move("c1", "c1")          # RED pass
        game.make_move("e6", "c5")
        game.get_board()

        # testing taking an opponent piece
        game.make_move("c1", "c1")          # RED pass
        game.make_move("c5", "e4")
        game.get_board()

    def testing_moving_elephant(self):
        # testing a vertical move
        game = JanggiGame()
        game.get_board()
        game.make_move("b10", "d7")
        game.get_board()

        game.make_move("b1", "b1")

        # testing a horizontal move
        # game.make_move("d7", "")

    def testing_moving_chariot(self):
        game = JanggiGame()
        game.get_board()
        game.make_move("a7", "b7")          # moving soldier out of the way
        game.make_move("c1", "c1")          # RED pass
        game.get_board()
        game.make_move("a10", "a5")
        game.get_board()
        game.make_move("c1", "c1")  # RED pass
        game.make_move("a5", "i5")
        game.get_board()

    def testing_moving_cannon(self):
        game = JanggiGame()
        game.get_board()
        # attempting to move Cannon from starting position, should be INVALID
        game.make_move("b8", "b5")
        game.make_move("a7", "b7")  # moving soldier out of the way
        game.make_move("c1", "c1")  # RED pass
        game.get_board()
        # attempting to jump over an active_player piece (VERTICAL JUMP)
        game.make_move("b8", "b5")
        game.get_board()
        game.make_move("c4", "c5")
        game.get_board()
        # attempting to jump over a Cannon, should be INVALID
        game.make_move("b5", "b2")
        # attempting to jump over an opponent piece (HORIZONTAL JUMP)
        game.make_move("b5", "i5")
        game.get_board()
        # attempting to capture a piece (opponent chariot) with Cannon
        game.make_move("c1", "c1")  # RED pass
        game.make_move("i5", "i1")
        game.get_board()
        # attempting to jump over multiple pieces, should be INVALID
        game.make_move("c1", "c1")  # RED pass
        game.make_move("i1", "e1")

    def testing_moving_guard(self):
        game = JanggiGame()
        game.get_board()
        # testing forward move
        game.make_move("d10", "d9")
        game.get_board()
        game.make_move("c1", "c1")  # RED pass
        # testing diagonal move from illegal spot
        game.make_move("d9", "e8")
        game.get_board()
        game.make_move("e9", "e10")     # moving General out of the way for testing purposes
        game.make_move("c1", "c1")  # RED pass
        game.get_board()
        # testing valid diagonal move
        game.make_move("f10", "e9")
        game.get_board()
        game.make_move("c1", "c1")  # RED pass
        game.make_move("e9", "d8")
        game.get_board()
        # attempting to move out of the palace
        game.make_move("c1", "c1")  # RED pass
        game.make_move("d8", "d7")

    def testing_moving_general(self):
        game = JanggiGame()
        game.get_board()
        # testing diagonal movement in the palace
        game.make_move("e9", "d8")
        game.get_board()
        game.make_move("c1", "c1")  # RED pass
        # attempting to move out of the palace, should be INVALID
        game.make_move("d8", "d7")
        # testing vertical movement
        game.make_move("d8", "d9")
        game.get_board()
        game.make_move("c1", "c1")  # RED pass
        # testing INVALID diagonal movement
        game.make_move("d9", "e8")
        # testing horizontal movement
        game.make_move("d9", "e9")
        game.get_board()

    def testing_is_check(self):
        game = JanggiGame()
        game.get_board()
        # testing with Chariot threat_piece
        game.make_move("a7", "b7")  # moving Soldier out of the way for testing purposes
        game.make_move("c1", "c1")  # RED pass
        game.get_board()
        game.make_move("a10", "a6")
        game.make_move("e4", "d4")
        game.get_board()
        game.make_move("a6", "e6")
        game.get_board()
        actual = game.is_in_check()
        expected = True
        self.assertEqual(actual, expected)

    def testing_is_checkmate(self):
        game = JanggiGame()
        game.get_board()
        # removing all red pieces but red General
        game.remove_piece(0, 0)
        game.remove_piece(0, 1)
        game.remove_piece(0, 2)
        game.remove_piece(0, 3)
        game.remove_piece(0, 5)
        game.remove_piece(0, 6)
        game.remove_piece(0, 7)
        game.remove_piece(0, 8)
        game.remove_piece(2, 1)
        game.remove_piece(2, 7)
        game.remove_piece(3, 0)
        game.remove_piece(3, 2)
        game.remove_piece(3, 4)
        game.remove_piece(3, 6)
        game.remove_piece(3, 8)
        game.get_board()
        # removing all blue pieces except blue General, one guard, and blue Cannons
        game.remove_piece(9, 0)
        game.remove_piece(9, 1)
        game.remove_piece(9, 2)
        game.remove_piece(9, 5)
        game.remove_piece(9, 6)
        game.remove_piece(9, 7)
        game.remove_piece(9, 8)
        game.remove_piece(6, 0)
        game.remove_piece(6, 2)
        game.remove_piece(6, 4)
        game.remove_piece(6, 6)
        game.remove_piece(6, 8)
        game.get_board()
        # setting up checkmate
        game.make_move("d10", "d9")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("d9", "d8")
        game.make_move("c1", "c1")      # RED pass
        game.get_board()
        game.make_move("b8", "g8")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("d8", "e8")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("g8", "d8")
        game.make_move("c1", "c1")      # RED pass
        game.get_board()
        game.make_move("e8", "f8")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("h8", "e8")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("f8", "f9")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("f9", "f10")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("f10", "e10")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("e10", "d10")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("d10", "d9")
        game.make_move("c1", "c1")      # RED pass
        game.make_move("e8", "e10")
        game.make_move("e2", "d2")      # RED moves General out of check (one space to the left)
        game.get_board()
        # FINAL MOVE, should be CHECKMATE
        game.make_move("d8", "d10")
        game.get_board()
        actual = game._checkmate
        expected = True
        self.assertEqual(actual, expected)

    def testing_check_block(self):
        game = JanggiGame()
        game.get_board()
        # testing with Chariot threat_piece
        game.make_move("a7", "b7")  # moving Soldier out of the way for testing purposes
        game.make_move("c1", "c1")  # RED pass
        game.get_board()
        game.make_move("a10", "a6")
        game.make_move("e4", "d4")
        game.get_board()
        game.make_move("a6", "e6")
        game.get_board()
        actual = game.check_block(1, 4)
        expected = True
        self.assertEqual(actual, expected)

    def testing_is_self_check(self):
        game = JanggiGame()
        game.get_board()
        # testing with Chariot
        game.make_move("a7", "b7")  # moving Soldier out of the way for testing purposes
        game.make_move("c1", "c1")  # RED pass
        game.get_board()
        game.make_move("a10", "a6")
        game.make_move("c1", "c1")  # RED pass
        game.get_board()
        game.make_move("a6", "e6")
        game.make_move("e4", "f4")
        # testing with Horse
        game.make_move("c1", "c1")  # RED pass
        game.make_move("e6", "a6")
        game.get_board()
        game.make_move("d1", "d2")
        game.make_move("c10", "d8")
        game.make_move("d2", "d3")
        game.make_move("d8", "e6")
        game.get_board()
        game.make_move("c1", "c1")  # RED pass
        game.make_move("e6", "d4")
        game.get_board()
        game.make_move("d3", "d2")


if __name__ == "__main__":
    unittest.main()