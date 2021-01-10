import unittest
from game import Game


class TestGame(unittest.TestCase):
    def test_one_throw(self):
        g = Game()
        g.add(5)
        self.assertEqual(5, g.get_score())


if __name__ == '__main__':
    unittest.main()
