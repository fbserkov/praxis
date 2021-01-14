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
    @staticmethod
    def is_pay_date(pay_date):
        return not (pay_date - date(2001, 11, 9)).days % 14
