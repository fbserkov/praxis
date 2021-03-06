from affiliation import Affiliation, NoAffiliation, UnionAffiliation
from change_employee_transaction import ChangeEmployeeTransaction
from employee import EmpId, Employee
from payroll_database import g_payroll_database


class ChangeAffiliationTransaction(ChangeEmployeeTransaction):
    def __init__(self, emp_id: EmpId):
        ChangeEmployeeTransaction.__init__(self, emp_id)

    def change(self, e: Employee):
        self.record_membership(e)
        e.set_affiliation(self.get_affiliation())

    def record_membership(self, e: Employee):
        pass

    def get_affiliation(self) -> Affiliation:
        return Affiliation()


class ChangeMemberTransaction(ChangeAffiliationTransaction):
    def __init__(self, emp_id, member_id, dues):
        ChangeAffiliationTransaction.__init__(self, emp_id)
        self._member_id = member_id
        self._dues = dues

    def record_membership(self, e: Employee):
        g_payroll_database.add_union_member(self._member_id, e)

    def get_affiliation(self) -> Affiliation:
        return UnionAffiliation(self._member_id, self._dues)


class ChangeUnaffiliatedTransaction(ChangeAffiliationTransaction):
    def __init__(self, emp_id):
        ChangeAffiliationTransaction.__init__(self, emp_id)

    def record_membership(self, e: Employee):
        affiliation = e.get_affiliation()
        if isinstance(affiliation, UnionAffiliation):
            member_id = affiliation.get_member_id()
            g_payroll_database.remove_union_member(member_id)

    def get_affiliation(self) -> Affiliation:
        return NoAffiliation()
