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
    pass


class UnionAffiliation(Affiliation):
    def __init__(self):
        self._sc = None

    def add_service_charge(self, date, charge):
        self._sc = ServiceCharge(date, amount=charge)

    def get_service_charge(self, date) -> ServiceCharge:
        if date == self._sc.get_date():
            return self._sc
