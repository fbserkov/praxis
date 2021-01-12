from add_employee_transaction import PaymentClassification


class CommissionedClassification(PaymentClassification):
    def __init__(self, salary, commission_rate):
        self._salary = salary
        self._commission_rate = commission_rate

    def get_salary(self):
        return self._salary

    def get_commission_rate(self):
        return self._commission_rate
