# Kent Beck
# Test-driven development by example
# Section I: Money example

import unittest


class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        if type(other) == int:
            return self._amount == other
        else:
            return self._amount == other and type(self) == type(other)

    @staticmethod
    def dollar(amount):
        return Dollar(amount)


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
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertTrue(Franc(5) == Franc(5))
        self.assertFalse(Franc(5) == Franc(6))
        self.assertFalse(Money.dollar(5) == Franc(5))

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(5 * 2), five.times(2))
        self.assertEqual(Money.dollar(5 * 3), five.times(3))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(5 * 2), five.times(2))
        self.assertEqual(Franc(5 * 3), five.times(3))


if __name__ == '__main__':
    unittest.main()
