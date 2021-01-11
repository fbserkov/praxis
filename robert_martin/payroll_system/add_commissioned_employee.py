from add_employee_transaction import AddEmployeeTransaction
from biweekly_schedule import BiweeklySchedule
from commissioned_classification import CommissionedClassification


class AddCommissionedEmployee(AddEmployeeTransaction):
    def __init__(self, emp_id, name, address, salary, commission_rate):
        AddEmployeeTransaction.__init__(self, emp_id, name, address)
        self._salary = salary
        self._commission_rate = commission_rate

    def get_classification(self):
        return CommissionedClassification(self._salary, self._commission_rate)

    def get_schedule(self):
        return BiweeklySchedule()
