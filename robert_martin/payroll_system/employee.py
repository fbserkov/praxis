from typing import NewType

from affiliation import Affiliation
from payment_classification import PaymentClassification
from payment_method import PaymentMethod
from payment_schedule import PaymentSchedule

EmpId = NewType('EmpId', int)


class Employee:
    def __init__(self, emp_id: EmpId, name, address):
        self._emp_id = emp_id
        self._name = name
        self._address = address

        self._classification = PaymentClassification()
        self._schedule = PaymentSchedule()
        self._method = PaymentMethod()
        self._affiliation = Affiliation()

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_classification(self, pc: PaymentClassification):
        self._classification = pc

    def set_schedule(self, ps: PaymentSchedule):
        self._schedule = ps

    def set_method(self, pm: PaymentMethod):
        self._method = pm

    def set_affiliation(self, a: Affiliation):
        self._affiliation = a

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_classification(self) -> PaymentClassification:
        return self._classification

    def get_schedule(self) -> PaymentSchedule:
        return self._schedule

    def get_method(self) -> PaymentMethod:
        return self._method

    def get_affiliation(self) -> Affiliation:
        return self._affiliation

    def get_period_start_date(self, pay_date):
        return self._schedule.get_period_start_date(pay_date)

    def is_pay_date(self, date):
        return self._schedule.is_pay_date(date)

    def payday(self, paycheck):
        gross_pay = self._classification.calculate_pay(paycheck)
        deductions = self._affiliation.calculate_deductions()
        net_pay = gross_pay - deductions
        paycheck.set_gross_pay(gross_pay)
        paycheck.set_deductions(deductions)
        paycheck.set_net_pay(net_pay)
        self._method.pay(paycheck)
