import unittest
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.g = Game()

    def test_one_throw(self):
        self.g.add(5)
        self.assertEqual(1, self.g.get_current_frame())

    def test_two_throws_no_mark(self):
        self.g.add(5)
        self.g.add(4)
        self.assertEqual(5 + 4, self.g.get_score())
        self.assertEqual(2, self.g.get_current_frame())

    def test_four_throws_no_mark(self):
        self.g.add(5)
        self.g.add(4)
        self.g.add(7)
        self.g.add(2)
        self.assertEqual(5 + 4, self.g.score_for_frame(1))
        self.assertEqual(5 + 4 + 7 + 2, self.g.score_for_frame(2))
        self.assertEqual(3, self.g.get_current_frame())

    def test_simple_spare(self):
        self.g.add(3)
        self.g.add(7)
        self.g.add(3)
        self.assertEqual(3 + 7 + 3, self.g.score_for_frame(1))
        self.assertEqual(2, self.g.get_current_frame())

    def test_simple_frame_after_spare(self):
        self.g.add(3)
        self.g.add(7)
        self.g.add(3)
        self.g.add(2)
        self.assertEqual(3 + 7 + 3, self.g.score_for_frame(1))  # 13
        self.assertEqual(13 + 3 + 2, self.g.score_for_frame(2))  # 18
        self.assertEqual(18, self.g.get_score())
        self.assertEqual(3, self.g.get_current_frame())

    def test_simple_strike(self):
        self.g.add(10)
        self.g.add(3)
        self.g.add(6)
        self.assertEqual(10 + 3 + 6, self.g.score_for_frame(1))
        self.assertEqual(28, self.g.get_score())
        self.assertEqual(3, self.g.get_current_frame())


if __name__ == '__main__':
    unittest.main()
