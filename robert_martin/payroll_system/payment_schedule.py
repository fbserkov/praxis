from datetime import date, timedelta


class PaymentSchedule:
    @staticmethod
    def is_pay_date(pay_date):
        return False


class MonthlySchedule(PaymentSchedule):
    @staticmethod
    def is_pay_date(pay_date: date):
        return pay_date.month != (pay_date + timedelta(1)).month


class WeeklySchedule(PaymentSchedule):
    @staticmethod
    def is_pay_date(pay_date):
        return pay_date.isoweekday() == 5


class BiweeklySchedule(PaymentSchedule):
    def __init__(self):
        self._is_second_friday = True

    def is_pay_date(self, pay_date):
        return pay_date.isoweekday() == 5 and self._is_second_friday
