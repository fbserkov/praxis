from employee import EmpId, Employee


class PayrollDatabase:
    def __init__(self):
        self._employees = {}

    def add_employee(self, emp_id: EmpId, e: Employee):
        self._employees[emp_id] = e

    def get_employee(self, emp_id: EmpId) -> Employee:
        return self._employees.get(emp_id)

    def delete_employee(self, emp_id: EmpId):
        self._employees.pop(emp_id)

    def clear(self):
        self._employees.clear()


g_payroll_database = PayrollDatabase()
