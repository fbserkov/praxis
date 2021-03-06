from add_employee_transaction import AddEmployeeTransaction
from payment_classification import HourlyClassification, PaymentClassification
from payment_schedule import PaymentSchedule, WeeklySchedule


class AddHourlyEmployee(AddEmployeeTransaction):
    def __init__(self, emp_id, name, address, hourly_rate):
        AddEmployeeTransaction.__init__(self, emp_id, name, address)
        self._hourly_rate = hourly_rate

    def get_classification(self) -> PaymentClassification:
        return HourlyClassification(self._hourly_rate)

    def get_schedule(self) -> PaymentSchedule:
        return WeeklySchedule()
