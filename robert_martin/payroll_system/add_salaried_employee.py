from add_employee_transaction import AddEmployeeTransaction
from monthly_schedule import MonthlySchedule
from salaried_classification import SalariedClassification


class AddSalariedEmployee(AddEmployeeTransaction):
    def __init__(self, emp_id, name, address, salary):
        AddEmployeeTransaction.__init__(self, emp_id, name, address)
        self._salary = salary

    def get_classification(self):
        return SalariedClassification(self._salary)

    def get_schedule(self):
        return MonthlySchedule()
