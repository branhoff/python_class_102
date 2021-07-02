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

        actual2 = game.check_range(0, 10)
        expected2 = False
        self.assertEqual(actual2, expected2)

        actual3 = game.check_range(9, 1)
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


if __name__ == "__main__":
    unittest.main()