class PaymentMethod:
    pass


class DirectMethod(PaymentMethod):
    def __init__(self, bank, account):
        self._bank = bank
        self._account = account

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account


class HoldMethod(PaymentMethod):
    pass
