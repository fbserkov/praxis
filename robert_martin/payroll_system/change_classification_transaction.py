from change_employee_transaction import ChangeEmployeeTransaction
from employee import EmpId, Employee
from payment_classification import (
    CommissionedClassification, HourlyClassification,
    PaymentClassification, SalariedClassification)
from payment_schedule import (
    BiweeklySchedule, MonthlySchedule, PaymentSchedule, WeeklySchedule)


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


class ChangeSalariedTransaction(ChangeClassificationTransaction):
    def __init__(self, emp_id: EmpId, salary):
        ChangeClassificationTransaction.__init__(self, emp_id)
        self._salary = salary

    def get_classification(self) -> SalariedClassification:
        return SalariedClassification(self._salary)

    def get_schedule(self) -> MonthlySchedule:
        return MonthlySchedule()


class ChangeHourlyTransaction(ChangeClassificationTransaction):
    def __init__(self, emp_id: EmpId, hourly_rate):
        ChangeClassificationTransaction.__init__(self, emp_id)
        self._hourly_rate = hourly_rate

    def get_classification(self) -> HourlyClassification:
        return HourlyClassification(self._hourly_rate)

    def get_schedule(self) -> WeeklySchedule:
        return WeeklySchedule()


class ChangeCommissionedTransaction(ChangeClassificationTransaction):
    def __init__(self, emp_id: EmpId, salary, commission_rate):
        ChangeClassificationTransaction.__init__(self, emp_id)
        self._salary = salary
        self._commission_rate = commission_rate

    def get_classification(self) -> CommissionedClassification:
        return CommissionedClassification(self._salary, self._commission_rate)

    def get_schedule(self) -> BiweeklySchedule:
        return BiweeklySchedule()
