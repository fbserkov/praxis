from employee import EmpId, Employee
from payroll_database import g_payroll_database


class ChangeEmployeeTransaction:
    def __init__(self, emp_id: EmpId):
        self._emp_id = emp_id

    def execute(self):
        employee = g_payroll_database.get_employee(self._emp_id)
        if employee:
            self.change(employee)

    def change(self, e: Employee):
        pass


class ChangeNameTransaction(ChangeEmployeeTransaction):
    def __init__(self, emp_id: EmpId, name):
        ChangeEmployeeTransaction.__init__(self, emp_id)
        self._name = name

    def change(self, e: Employee):
        e.set_name(self._name)


class ChangeAddressTransaction(ChangeEmployeeTransaction):
    def __init__(self, emp_id: EmpId, address):
        ChangeEmployeeTransaction.__init__(self, emp_id)
        self._address = address

    def change(self, e: Employee):
        e.set_address(self._address)
