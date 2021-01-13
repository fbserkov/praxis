from employee import EmpId
from payroll_database import g_payroll_database


class Paycheck:
    def __init__(self, pay_date):
        self._pay_date = pay_date
        self._gross_pay = None
        self._deductions = None
        self._net_pay = None

    def set_gross_pay(self, gross_pay):
        self._gross_pay = gross_pay

    def set_deductions(self, deductions):
        self._deductions = deductions

    def set_net_pay(self, net_pay):
        self._net_pay = net_pay

    def get_pay_date(self):
        return self._pay_date

    def get_gross_pay(self):
        return self._gross_pay

    def get_deductions(self):
        return self._deductions

    def get_net_pay(self):
        return self._net_pay

    @staticmethod
    def get_field(_):
        return 'Hold'


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
