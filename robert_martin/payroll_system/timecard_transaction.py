from employee import EmpId
from payment_classification import HourlyClassification
from payroll_database import g_payroll_database
from timecard import Timecard


class TimecardTransaction:
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
