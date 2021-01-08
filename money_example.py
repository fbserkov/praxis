class Expression:
    def reduce(self, bank, to):
        pass


class Money(Expression):
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
        return Sum(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(self._amount / rate, to)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


class Sum(Expression):
    def __init__(self, augend, addend):
        self._augend = augend
        self._addend = addend

    def reduce(self, bank, to):
        amount = self._augend._amount + self._addend._amount
        return Money.dollar(amount)


class Bank:
    def reduce(self, source, to):
        return source.reduce(self, to)

    @staticmethod
    def rate(from_currency, to_currency):
        return 2 if from_currency == 'CHF' and to_currency == 'USD' else 1
