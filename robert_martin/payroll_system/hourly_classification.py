from add_employee_transaction import PaymentClassification


class HourlyClassification(PaymentClassification):
    def __init__(self, hourly_rate):
        self._hourly_rate = hourly_rate

    def get_hourly_rate(self):
        return self._hourly_rate
