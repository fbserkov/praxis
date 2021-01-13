from employee import EmpId
from paycheck import Paycheck
from payroll_database import g_payroll_database


class PaydayTransaction:
    def __init__(self, pay_date):
        self._pay_date = pay_date
        self._paychecks = {}

    def get_paycheck(self, emp_id: EmpId):
        return self._paychecks.get(emp_id)

    def execute(self):
        emp_ids = g_payroll_database.get_all_employee_ids()
        for emp_id in emp_ids:
            employee = g_payroll_database.get_employee(emp_id)
            if employee.is_pay_date(self._pay_date):
                paycheck = Paycheck(self._pay_date)
                self._paychecks[emp_id] = paycheck
                employee.payday(paycheck)
