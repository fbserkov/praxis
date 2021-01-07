# Kent Beck
# Test-driven development by example
# Section I: Money example

import unittest


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other.amount


class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(5 * 2, five.times(2).amount)
        self.assertEqual(5 * 3, five.times(3).amount)

    def test_equality(self):
        self.assertTrue(Dollar(5).__eq__(Dollar(5)))
        self.assertFalse(Dollar(5).__eq__(Dollar(6)))


if __name__ == '__main__':
    unittest.main()
