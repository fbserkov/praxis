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

    def test_perfect_game(self):
        for _ in range(12):
            self.g.add(10)
        self.assertEqual(10 * 3 * 10, self.g.get_score())
        self.assertEqual(11, self.g.get_current_frame())

    def test_end_of_array(self):
        for _ in range(9):
            self.g.add(0)
            self.g.add(0)
        self.g.add(2)
        self.g.add(8)  # 10th frame spare
        self.g.add(10)  # Strike in last position of array
        self.assertEqual(2 + 8 + 10, self.g.get_score())

    def test_sample_game(self):
        for p in (1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6):
            self.g.add(p)
        self.assertEqual(133, self.g.get_score())

    def test_heart_brake(self):
        for _ in range(11):
            self.g.add(10)
        self.g.add(9)
        self.assertEqual(299, self.g.get_score())


if __name__ == '__main__':
    unittest.main()
