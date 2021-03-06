from typing import List

from paycheck import Paycheck
from sales_receipt import SalesReceipt
from timecard import Timecard


class PaymentClassification:
    def calculate_pay(self, paycheck):
        pass

    @staticmethod
    def is_in_pay_period(the_date, paycheck):
        pay_period_start_date = paycheck.get_period_start_date()
        pay_period_end_date = paycheck.get_period_end_date()
        return paycheck.is_between(
            pay_period_start_date, the_date, pay_period_end_date)


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

    def calculate_pay(self, paycheck: Paycheck):
        total_pay = 0
        for tc in self._timecards:
            if self.is_in_pay_period(tc.get_date(), paycheck):
                total_pay += self.calculate_pay_for_timecard(tc)
        return total_pay

    def calculate_pay_for_timecard(self, tc: Timecard):
        hours = tc.get_hours()
        overtime = max(0.0, hours - 8.0)
        straight_time = hours - overtime
        return (straight_time + overtime * 1.5) * self._hourly_rate


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

    def calculate_pay(self, paycheck: Paycheck):
        return self._salary + self.calculate_pay_from_sales_receipts(paycheck)

    def calculate_pay_from_sales_receipts(self, paycheck):
        total_pay_from_sales_receipts = 0
        for sr in self._sales_receipt:
            if self.is_in_pay_period(sr.get_date(), paycheck):
                total_pay_from_sales_receipts += (
                    self.calculate_pay_for_sales_receipt(sr))
        return total_pay_from_sales_receipts

    def calculate_pay_for_sales_receipt(self, sr: SalesReceipt):
        return sr.get_amount() * self._commission_rate / 100
