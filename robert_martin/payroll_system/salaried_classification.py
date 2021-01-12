from add_employee_transaction import PaymentClassification


class SalariedClassification(PaymentClassification):
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary
