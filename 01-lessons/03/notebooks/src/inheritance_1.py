import unittest

class UnitTests(unittest.TestCase):
    def test_bird_call(self):

        # Failure message:
        # expected "chirp"
        tweety = Bird()
        self.assertEqual(tweety.call(), "chirp")

    def test_duck_call(self):

        # Failure message:
        # expected "quack"
        daffy = Duck()
        self.assertEqual(daffy.call(), "quack")