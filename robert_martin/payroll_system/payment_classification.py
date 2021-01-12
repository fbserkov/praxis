class PaymentClassification:
    pass


class SalariedClassification(PaymentClassification):
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary


class HourlyClassification(PaymentClassification):
    def __init__(self, hourly_rate):
        self._hourly_rate = hourly_rate
        self._timecards = []

    def get_hourly_rate(self):
        return self._hourly_rate

    def add_timecard(self, timecard):
        self._timecards.append(timecard)

    def get_timecard(self, date):
        for timecard in self._timecards:
            if timecard.get_date() == date:
                return timecard


class CommissionedClassification(PaymentClassification):
    def __init__(self, salary, commission_rate):
        self._salary = salary
        self._commission_rate = commission_rate

    def get_salary(self):
        return self._salary

    def get_commission_rate(self):
        return self._commission_rate
