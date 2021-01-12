from employee import EmpId
from payment_classification import CommissionedClassification
from payroll_database import g_payroll_database


class SalesReceipt:
    def __init__(self, date, amount):
        self._date = date
        self._amount = amount

    def get_date(self):
        return self._date

    def get_amount(self):
        return self._amount


class SalesReceiptTransaction:
    def __init__(self, emp_id: EmpId, date, amount):
        self._emp_id = emp_id
        self._date = date
        self._amount = amount

    def execute(self):
        employee = g_payroll_database.get_employee(self._emp_id)
        if employee:
            classification = employee.get_classification()
            if isinstance(classification, CommissionedClassification):
                classification.add_sales_receipt(
                    SalesReceipt(self._date, self._amount))
            else:
                raise Exception(
                    'Tried to add sales receipt to non-commissioned employee.')
        else:
            raise Exception('No such employee.')
