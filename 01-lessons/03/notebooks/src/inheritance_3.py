import unittest

class UnitTests(unittest.TestCase):
    def test_carpet_size_sqft(self):
        # Failure message:
        # This test has no failure messages
        rect = Rectangle(4, 6)
        carpet = Carpet(rect, 3.25)
        self.assertAlmostEqual(carpet.get_size(), rect)
        self.assertAlmostEqual(carpet.get_cost_per_sq_foot(), 3.25)

    def test_testName1(self):
        # Failure message:
        # This test has no failure messages
        rect = Rectangle(11, 3)
        carpet = Carpet(rect, 1.5)
        self.assertAlmostEqual(carpet.get_size(), rect)
        self.assertAlmostEqual(carpet.get_cost_per_sq_foot(), 1.5)
        self.assertAlmostEqual(carpet.cost(), 49.5)