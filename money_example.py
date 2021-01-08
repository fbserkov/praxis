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
    _rates = {}

    @staticmethod
    def add_rate(from_currency, to_currency, rate):
        Bank._rates[Pair(from_currency, to_currency)] = rate

    @staticmethod
    def rate(from_currency, to_currency):
        return Bank._rates[Pair(from_currency, to_currency)]

    def reduce(self, source, to):
        return source.reduce(self, to)


class Pair:
    def __init__(self, from_currency, to_currency):
        self.from_currency = from_currency
        self.to_currency = to_currency

    def __eq__(self, other):
        return (
            self.from_currency == other.from_currency and
            self.to_currency == other.to_currency
        )

    def __hash__(self):
        return 0
