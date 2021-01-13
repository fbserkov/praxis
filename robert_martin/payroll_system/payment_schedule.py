from datetime import timedelta


class PaymentSchedule:
    @staticmethod
    def is_pay_date(pay_date):
        return False


class MonthlySchedule(PaymentSchedule):
    @staticmethod
    def is_pay_date(pay_date):
        return pay_date.month != (pay_date + timedelta(1)).month


class WeeklySchedule(PaymentSchedule):
    pass


class BiweeklySchedule(PaymentSchedule):
    pass
