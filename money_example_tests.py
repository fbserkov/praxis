# Kent Beck
# Test-driven development by example
# Section I: Money example

import unittest
from money_example import Bank, Money, Sum


class MoneyExampleTest(unittest.TestCase):
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
        five = Money.dollar(5)
        sum_obj = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum_obj, 'USD')
        self.assertEqual(Money.dollar(5 + 5), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        sum_obj = five.plus(five)
        self.assertEqual(five, sum_obj._augend)
        self.assertEqual(five, sum_obj._addend)

    def test_reduce_sum(self):
        sum_obj = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_obj, 'USD')
        self.assertEqual(Money.dollar(3 + 4), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), 'USD')
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        self.assertEqual(Money.dollar(1), result)


if __name__ == '__main__':
    unittest.main()
