class Paycheck:
    def __init__(self, pay_date):
        self._pay_date = pay_date
        self._gross_pay = None
        self._deductions = None
        self._net_pay = None

    def set_gross_pay(self, gross_pay):
        self._gross_pay = gross_pay

    def set_deductions(self, deductions):
        self._deductions = deductions

    def set_net_pay(self, net_pay):
        self._net_pay = net_pay

    def get_pay_date(self):
        return self._pay_date

    def get_gross_pay(self):
        return self._gross_pay

    def get_deductions(self):
        return self._deductions

    def get_net_pay(self):
        return self._net_pay

    @staticmethod
    def get_field(_):
        return 'Hold'