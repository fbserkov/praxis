# Kent Beck
# Test-driven development by example
# Section III: Patterns
# Mastering TDD
# How much feedback do you need?

import unittest


class TestTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(self.evaluate(2, 2, 2), 1)

    def test_isosceles(self):
        self.assertEqual(self.evaluate(1, 2, 2), 2)

    def test_scalene(self):
        self.assertEqual(self.evaluate(2, 3, 4), 3)

    def test_irrational(self):
        with self.assertRaises(Exception):
            self.evaluate(1, 2, 3)

    def test_negative(self):
        with self.assertRaises(Exception):
            self.evaluate(-1, 2, 2)

    def test_strings(self):
        with self.assertRaises(TypeError):
            self.evaluate('a', 'b', 'c')

    @staticmethod
    def evaluate(a, b, c):
        a, b, c = sorted((a, b, c))
        if a < 0:
            raise Exception
        if a + b <= c:
            raise Exception
        return len({a, b, c})


if __name__ == '__main__':
    unittest.main()
