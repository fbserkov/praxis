class SalesReceipt:
    def __init__(self, date, amount):
        self._date = date
        self._amount = amount

    def get_date(self):
        return self._date

    def get_amount(self):
        return self._amount