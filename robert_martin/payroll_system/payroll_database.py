from affiliation import MemberId
from employee import EmpId, Employee


class PayrollDatabase:
    def __init__(self):
        self._employees = {}
        self._members = {}

    def add_employee(self, emp_id: EmpId, e: Employee):
        self._employees[emp_id] = e

    def add_union_member(self, member_id: MemberId, e: Employee):
        self._members[member_id] = e

    def get_all_employee_ids(self):
        return self._employees.keys()

    def get_employee(self, emp_id: EmpId) -> Employee:
        return self._employees.get(emp_id)

    def get_union_member(self, member_id: MemberId) -> Employee:
        return self._members.get(member_id)

    def delete_employee(self, emp_id: EmpId):
        self._employees.pop(emp_id)

    def remove_union_member(self, member_id: MemberId):
        self._members.pop(member_id)

    def clear(self):
        self._employees.clear()


g_payroll_database = PayrollDatabase()
