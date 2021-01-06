# Kent Beck
# Test-driven development by example
# Section I: Money example

import unittest


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(5 * 2, product.amount)
        product = five.times(3)
        self.assertEqual(5 * 3, product.amount)


if __name__ == '__main__':
    unittest.main()
