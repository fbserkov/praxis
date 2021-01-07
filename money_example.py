# Kent Beck
# Test-driven development by example
# Section I: Money example

import unittest


class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other


class Dollar(Money):
    def __init__(self, amount):
        Money.__init__(self, amount)

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        Money.__init__(self, amount)

    def times(self, multiplier):
        return Franc(self._amount * multiplier)


class MoneyTest(unittest.TestCase):
    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))
        self.assertTrue(Franc(5) == Franc(5))
        self.assertFalse(Franc(5) == Franc(6))

    def test_dollar_multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(5 * 2), five.times(2))
        self.assertEqual(Dollar(5 * 3), five.times(3))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(5 * 2), five.times(2))
        self.assertEqual(Franc(5 * 3), five.times(3))


if __name__ == '__main__':
    unittest.main()
