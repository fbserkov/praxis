from employee import EmpId, Employee
from hold_method import HoldMethod
from payroll_database import g_payroll_database


class PaymentClassification:
    pass


class PaymentSchedule:
    pass


class PaymentMethod:
    pass


class AddEmployeeTransaction:
    def __init__(self, emp_id: EmpId, name, address):
        self._emp_id = emp_id
        self._name = name
        self._address = address

    def execute(self):
        employee = Employee(self._emp_id, self._name, self._address)
        employee.set_classification(self.get_classification())
        employee.set_schedule(self.get_schedule())
        employee.set_method(HoldMethod())
        g_payroll_database.add_employee(self._emp_id, employee)

    def get_classification(self):
        return PaymentClassification()

    def get_schedule(self):
        return PaymentSchedule()
