from datetime import date, timedelta


class PaymentSchedule:
    @staticmethod
    def is_pay_date(pay_date):
        return False

    @staticmethod
    def get_period_start_date(pay_date):
        return pay_date


class MonthlySchedule(PaymentSchedule):
    @staticmethod
    def is_pay_date(pay_date: date):
        return pay_date.month != (pay_date + timedelta(1)).month

    @staticmethod
    def get_period_start_date(pay_date):
        return pay_date - timedelta(30)


class WeeklySchedule(PaymentSchedule):
    @staticmethod
    def is_pay_date(pay_date):
        return pay_date.isoweekday() == 5

    @staticmethod
    def get_period_start_date(pay_date):
        return pay_date - timedelta(6)


class BiweeklySchedule(PaymentSchedule):
    @staticmethod
    def is_pay_date(pay_date):
        return not (pay_date - date(2001, 11, 9)).days % 14

    @staticmethod
    def get_period_start_date(pay_date):
        return pay_date - timedelta(14)
