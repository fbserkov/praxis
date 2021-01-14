from typing import NewType

MemberId = NewType('MemberId', int)


class ServiceCharge:
    def __init__(self, date, amount):
        self._date = date
        self._amount = amount

    def get_date(self):
        return self._date

    def get_amount(self):
        return self._amount


class Affiliation:
    def calculate_deductions(self):
        return 0.0


class NoAffiliation(Affiliation):
    pass


class UnionAffiliation(Affiliation):
    def __init__(self, member_id: MemberId = None, dues=None):
        self._member_id = member_id
        self._dues = dues
        self._sc = None

    def get_member_id(self):
        return self._member_id

    def set_dues(self, dues):
        self._dues = dues

    def get_dues(self):
        return self._dues

    def add_service_charge(self, date, charge):
        self._sc = ServiceCharge(date, amount=charge)

    def get_service_charge(self, date) -> ServiceCharge:
        if date == self._sc.get_date():
            return self._sc
