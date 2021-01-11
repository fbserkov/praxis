import unittest

from add_salaried_employee import AddSalariedEmployee
from hold_method import HoldMethod
from monthly_schedule import MonthlySchedule
from payroll_database import g_payroll_database
from salaried_classification import SalariedClassification


class PayrollTest(unittest.TestCase):
    def test_add_salaried_employee(self):
        emp_id = 1
        transaction = AddSalariedEmployee(
            emp_id, 'Bob', 'Home', salary=1000.00)
        transaction.execute()

        employee = g_payroll_database.get_employee(emp_id)
        self.assertEqual('Bob', employee.get_name())
        self.assertEqual('Home', employee.get_address())

        classification = employee.get_classification()
        self.assertEqual(1000.00, classification.get_salary())

        self.assertIsInstance(classification, SalariedClassification)
        self.assertIsInstance(employee.get_schedule(), MonthlySchedule)
        self.assertIsInstance(employee.get_method(), HoldMethod)

    # TODO: test_add_hourly_employee
    # TODO: test_add_commissioned_employee


if __name__ == '__main__':
    unittest.main()
