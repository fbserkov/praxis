from datetime import timedelta
from typing import NewType

from paycheck import Paycheck

MemberId = NewType('MemberId', int)


class ServiceCharge:
    def __init__(self, date, amount):
        self._date = date
        self._amount = amount

    def get_date(self):
        return self._date

    def get_amount(self):
        return self._amount


class Affiliation:
    def calculate_deductions(self, pc: Paycheck):
        return 0.0


class NoAffiliation(Affiliation):
    pass


class UnionAffiliation(Affiliation):
    def __init__(self, member_id: MemberId = None, dues=None):
        self._member_id = member_id
        self._dues = dues
        self._service_charges = {}

    def get_member_id(self):
        return self._member_id

    def set_dues(self, dues):
        self._dues = dues

    def get_dues(self):
        return self._dues

    def add_service_charge(self, date, charge):
        self._service_charges[date] = ServiceCharge(date, amount=charge)

    def get_service_charge(self, the_date) -> ServiceCharge:
        for a_date, sc in self._service_charges.items():
            if the_date == a_date:
                return sc

    def calculate_deductions(self, pc: Paycheck):
        fridays = self._number_of_fridays_in_pay_period(
            pc.get_period_start_date(), pc.get_period_end_date())
        total_dues = self._dues * fridays
        for sc in self._service_charges.values():
            total_dues += sc.get_amount()
        return total_dues

    @staticmethod
    def _number_of_fridays_in_pay_period(pay_period_start, pay_period_end):
        fridays = 0
        day = pay_period_start
        while day <= pay_period_end:
            if day.isoweekday() == 5:
                fridays += 1
            day += timedelta(1)
        return fridays
