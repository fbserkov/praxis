from add_employee_transaction import AddEmployeeTransaction
from hourly_classification import HourlyClassification
from weekly_schedule import WeeklySchedule


class AddHourlyEmployee(AddEmployeeTransaction):
    def __init__(self, emp_id, name, address, hourly_rate):
        AddEmployeeTransaction.__init__(self, emp_id, name, address)
        self._hourly_rate = hourly_rate

    def get_classification(self):
        return HourlyClassification(self._hourly_rate)

    def get_schedule(self):
        return WeeklySchedule()
