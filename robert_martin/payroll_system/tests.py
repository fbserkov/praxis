import unittest

from add_salaried_employee import AddSalariedEmployee
from hold_method import HoldMethod
from monthly_schedule import MonthlySchedule
from payroll_database import g_payroll_database
from salaried_classification import SalariedClassification


class PayrollTest(unittest.TestCase):
    def test_add_salaried_employee(self):
        emp_id = 1
        transaction = AddSalariedEmployee(emp_id, 'Bob', 'Home', 1000.00)
        transaction.execute()

        employee = g_payroll_database.get_employee(emp_id)
        salaried_classification = employee.get_classification()
        monthly_schedule = employee.get_schedule()
        hold_method = employee.get_method()

        self.assertIsInstance(salaried_classification, SalariedClassification)
        self.assertIsInstance(monthly_schedule, MonthlySchedule)
        self.assertIsInstance(hold_method, HoldMethod)

        self.assertEqual('Bob', employee.get_name())
        self.assertEqual(1000.00, salaried_classification.get_salary())

    # TODO: test_add_hourly_employee
    # TODO: test_add_commissioned_employee


if __name__ == '__main__':
    unittest.main()
