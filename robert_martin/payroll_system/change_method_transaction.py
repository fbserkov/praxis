from change_employee_transaction import ChangeEmployeeTransaction
from employee import EmpId, Employee
from payment_method import DirectMethod, HoldMethod, MailMethod, PaymentMethod


class ChangeMethodTransaction(ChangeEmployeeTransaction):
    def __init__(self, emp_id: EmpId):
        ChangeEmployeeTransaction.__init__(self, emp_id)

    def change(self, e: Employee):
        e.set_method(self.get_method())

    def get_method(self) -> PaymentMethod:
        return PaymentMethod()


class ChangeDirectTransaction(ChangeMethodTransaction):
    def __init__(self, emp_id: EmpId, bank, account):
        ChangeMethodTransaction.__init__(self, emp_id)
        self._bank = bank
        self._account = account

    def get_method(self) -> DirectMethod:
        return DirectMethod(self._bank, self._account)


class ChangeMailTransaction(ChangeMethodTransaction):
    def __init__(self, emp_id: EmpId, address):
        ChangeMethodTransaction.__init__(self, emp_id)
        self._address = address

    def get_method(self) -> MailMethod:
        return MailMethod(self._address)


class ChangeHoldTransaction(ChangeMethodTransaction):
    def __init__(self, emp_id: EmpId, address):
        ChangeMethodTransaction.__init__(self, emp_id)
        self._address = address

    def get_method(self) -> HoldMethod:
        return HoldMethod(self._address)
