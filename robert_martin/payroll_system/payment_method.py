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


class MailMethod(PaymentMethod):
    def __init__(self, address):
        self._address = address

    def get_address(self):
        return self._address


class HoldMethod(PaymentMethod):
    pass
