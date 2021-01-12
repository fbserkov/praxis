from add_employee_transaction import AddEmployeeTransaction
from payment_classification import (
    PaymentClassification, SalariedClassification)
from payment_schedule import MonthlySchedule, PaymentSchedule


class AddSalariedEmployee(AddEmployeeTransaction):
    def __init__(self, emp_id, name, address, salary):
        AddEmployeeTransaction.__init__(self, emp_id, name, address)
        self._salary = salary

    def get_classification(self) -> PaymentClassification:
        return SalariedClassification(self._salary)

    def get_schedule(self) -> PaymentSchedule:
        return MonthlySchedule()
