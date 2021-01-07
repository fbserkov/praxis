# Kent Beck
# Test-driven development by example
# Section I: Money example

import unittest


class Dollar:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(5 * 2), five.times(2))
        self.assertEqual(Dollar(5 * 3), five.times(3))

    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))


if __name__ == '__main__':
    unittest.main()
