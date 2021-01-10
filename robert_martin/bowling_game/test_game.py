import unittest
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.g = Game()

    def test_one_throw(self):
        self.g.add(5)
        self.assertEqual(5, self.g.get_score())

    def test_two_throws_no_mark(self):
        self.g.add(5)
        self.g.add(4)
        self.assertEqual(5 + 4, self.g.get_score())

    def test_four_throws_no_mark(self):
        self.g.add(5)
        self.g.add(4)
        self.g.add(7)
        self.g.add(2)
        self.assertEqual(5 + 4, self.g.score_for_frame(1))
        self.assertEqual(5 + 4 + 7 + 2, self.g.score_for_frame(2))


if __name__ == '__main__':
    unittest.main()
