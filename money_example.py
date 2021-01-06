# Kent Beck
# Test-driven development by example
# Section I: Money example

import unittest


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier


class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(5 * 2, five.amount)


if __name__ == '__main__':
    unittest.main()
