# Kent Beck
# Test-driven development by example
# Section I: Money example

import unittest
from money_example import Bank, Money


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
        result = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(result, 'USD')
        self.assertEqual(Money.dollar(5 + 5), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        sum_obj = five.plus(five)
        self.assertEqual(five, sum_obj.augend)
        self.assertEqual(five, sum_obj.addend)


if __name__ == '__main__':
    unittest.main()
