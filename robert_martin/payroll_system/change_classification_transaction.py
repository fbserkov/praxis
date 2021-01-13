from change_employee_transaction import ChangeEmployeeTransaction
from employee import EmpId, Employee
from payment_classification import HourlyClassification, PaymentClassification
from payment_schedule import PaymentSchedule, WeeklySchedule


class ChangeClassificationTransaction(ChangeEmployeeTransaction):
    def __init__(self, emp_id: EmpId):
        ChangeEmployeeTransaction.__init__(self, emp_id)

    def change(self, e: Employee):
        e.set_classification(self.get_classification())
        e.set_schedule(self.get_schedule())

    def get_classification(self) -> PaymentClassification:
        return PaymentClassification()

    def get_schedule(self) -> PaymentSchedule:
        return PaymentSchedule()


class ChangeHourlyTransaction(ChangeClassificationTransaction):
    def __init__(self, emp_id: EmpId, hourly_rate):
        ChangeClassificationTransaction.__init__(self, emp_id)
        self._hourly_rate = hourly_rate

    def get_classification(self) -> HourlyClassification:
        return HourlyClassification(self._hourly_rate)

    def get_schedule(self) -> WeeklySchedule:
        return WeeklySchedule()
