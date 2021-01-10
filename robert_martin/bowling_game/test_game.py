import unittest
from game import Game


class TestGame(unittest.TestCase):
    def test_one_throw(self):
        g = Game()
        g.add(5)
        self.assertEqual(5, g.get_score())

    def test_two_throws_no_mark(self):
        g = Game()
        g.add(5)
        g.add(4)
        self.assertEqual(5 + 4, g.get_score())

    def test_four_throws_no_mark(self):
        g = Game()
        g.add(5)
        g.add(4)
        g.add(7)
        g.add(2)
        self.assertEqual(5 + 4, g.score_for_frame(1))
        self.assertEqual(5 + 4 + 7 + 2, g.score_for_frame(2))


if __name__ == '__main__':
    unittest.main()
