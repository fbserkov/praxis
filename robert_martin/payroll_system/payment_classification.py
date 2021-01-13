from typing import List
from timecard import Timecard


class PaymentClassification:
    def calculate_pay(self, paycheck):
        pass


class SalariedClassification(PaymentClassification):
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def calculate_pay(self, paycheck):
        return self._salary


class HourlyClassification(PaymentClassification):
    def __init__(self, hourly_rate):
        self._hourly_rate = hourly_rate
        self._timecards: List[Timecard] = []

    def get_hourly_rate(self):
        return self._hourly_rate

    def add_timecard(self, timecard: Timecard):
        self._timecards.append(timecard)

    def get_timecard(self, date):
        for timecard in self._timecards:
            if timecard.get_date() == date:
                return timecard

    def calculate_pay(self, paycheck):
        return sum(tc.get_hours()*self._hourly_rate for tc in self._timecards)


class CommissionedClassification(PaymentClassification):
    def __init__(self, salary, commission_rate):
        self._salary = salary
        self._commission_rate = commission_rate
        self._sales_receipt = []

    def get_salary(self):
        return self._salary

    def get_commission_rate(self):
        return self._commission_rate

    def add_sales_receipt(self, sales_receipt):
        self._sales_receipt.append(sales_receipt)

    def get_sales_receipt(self, date):
        for sales_receipt in self._sales_receipt:
            if sales_receipt.get_date() == date:
                return sales_receipt
