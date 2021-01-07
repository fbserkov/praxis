# Kent Beck
# Test-driven development by example
# Section I: Money example

import unittest


class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __repr__(self):
        return str(self._amount) + ' ' + self._currency

    def __eq__(self, other):
        if type(other) == int:
            return self._amount == other
        return self._amount == other and self.currency() == other.currency()

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        if type(addend) == int:
            return Money(self._amount + addend, self._currency)
        return Money(addend.plus(self._amount), self._currency)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


class MoneyTest(unittest.TestCase):
    def test_currency(self):
        self.assertEqual('USD', Money.dollar(1).currency())
        self.assertEqual('CHF', Money.franc(1).currency())

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.dollar(5) == Money.franc(5))

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(5 * 2), five.times(2))
        self.assertEqual(Money.dollar(5 * 3), five.times(3))

    def test_simple_addition(self):
        result = Money.dollar(5).plus(Money.dollar(5))
        self.assertEqual(Money.dollar(5 + 5), result)


if __name__ == '__main__':
    unittest.main()
