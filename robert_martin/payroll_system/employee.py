from typing import NewType
from payment_classification import PaymentClassification
from payment_method import PaymentMethod
from payment_schedule import PaymentSchedule

EmpId = NewType('EmpId', int)


class Employee:
    def __init__(self, emp_id: EmpId, name, address):
        self._emp_id = emp_id
        self._name = name
        self._address = address

        self._pc = PaymentClassification()
        self._ps = PaymentSchedule()
        self._pm = PaymentMethod()

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def set_classification(self, pc: PaymentClassification):
        self._pc = pc

    def set_schedule(self, ps: PaymentSchedule):
        self._ps = ps

    def set_method(self, pm: PaymentMethod):
        self._pm = pm

    def get_classification(self) -> PaymentClassification:
        return self._pc

    def get_schedule(self) -> PaymentSchedule:
        return self._ps

    def get_method(self) -> PaymentMethod:
        return self._pm
