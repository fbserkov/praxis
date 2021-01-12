from employee import EmpId
from payroll_database import g_payroll_database


class DeleteEmployeeTransaction:
    def __init__(self, emp_id: EmpId):
        self._emp_id = emp_id

    def execute(self):
        g_payroll_database.delete_employee(self._emp_id)
