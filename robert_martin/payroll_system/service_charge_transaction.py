from affiliation import UnionAffiliation, MemberId
from payroll_database import g_payroll_database


class ServiceChargeTransaction:
    def __init__(self, member_id: MemberId, date, charge):
        self._member_id = member_id
        self._date = date
        self._charge = charge

    def execute(self):
        employee = g_payroll_database.get_union_member(self._member_id)
        if employee:
            affiliation = employee.get_affiliation()
            if isinstance(affiliation, UnionAffiliation):
                affiliation.add_service_charge(self._date, self._charge)
