from employee import EmpId
from payment_classification import HourlyClassification
from payroll_database import g_payroll_database


class Timecard:
    def __init__(self, date, hours):
        self._date = date
        self._hours = hours

    def get_date(self):
        return self._date

    def get_hours(self):
        return self._hours


class TimeCardTransaction:
    def __init__(self, emp_id: EmpId, date, hours):
        self._emp_id = emp_id
        self._date = date
        self._hours = hours

    def execute(self):
        employee = g_payroll_database.get_employee(self._emp_id)
        if employee:
            classification = employee.get_classification()
            if isinstance(classification, HourlyClassification):
                classification.add_timecard(Timecard(self._date, self._hours))
            else:
                raise Exception(
                    'Tried to add timecard to non-hourly employee.')
        else:
            raise Exception('No such employee.')
