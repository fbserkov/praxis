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

    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')


class Dollar(Money):
    def __init__(self, amount):
        Money.__init__(self, amount)
        self._currency = 'USD'

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount, currency):
        Money.__init__(self, amount)
        self._currency = currency

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)


class MoneyTest(unittest.TestCase):
    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertTrue(Money.franc(5) == Money.franc(5))
        self.assertFalse(Money.franc(5) == Money.franc(6))
        self.assertFalse(Money.dollar(5) == Money.franc(5))

    def test_dollar_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(5 * 2), five.times(2))
        self.assertEqual(Money.dollar(5 * 3), five.times(3))

    def test_franc_multiplication(self):
        five = Money.franc(5)
        self.assertEqual(Money.franc(5 * 2), five.times(2))
        self.assertEqual(Money.franc(5 * 3), five.times(3))

    def test_currency(self):
        self.assertEqual('USD', Money.dollar(1).currency())
        self.assertEqual('CHF', Money.franc(1).currency())


if __name__ == '__main__':
    unittest.main()
