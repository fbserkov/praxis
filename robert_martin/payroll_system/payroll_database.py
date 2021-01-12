from employee import EmpId, Employee


class PayrollDatabase:
    def __init__(self):
        self._employees = {}

    def get_employee(self, emp_id: EmpId) -> Employee:
        return self._employees[emp_id]

    def add_employee(self, emp_id: EmpId, e: Employee):
        self._employees[emp_id] = e

    def clear(self):
        self._employees.clear()


g_payroll_database = PayrollDatabase()
