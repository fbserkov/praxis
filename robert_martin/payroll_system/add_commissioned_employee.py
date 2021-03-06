from add_employee_transaction import AddEmployeeTransaction
from payment_classification import (
    CommissionedClassification, PaymentClassification)
from payment_schedule import BiweeklySchedule, PaymentSchedule


class AddCommissionedEmployee(AddEmployeeTransaction):
    def __init__(self, emp_id, name, address, salary, commission_rate):
        AddEmployeeTransaction.__init__(self, emp_id, name, address)
        self._salary = salary
        self._commission_rate = commission_rate

    def get_classification(self) -> PaymentClassification:
        return CommissionedClassification(self._salary, self._commission_rate)

    def get_schedule(self) -> PaymentSchedule:
        return BiweeklySchedule()
