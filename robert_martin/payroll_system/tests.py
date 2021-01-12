import unittest

from add_commissioned_employee import AddCommissionedEmployee
from add_hourly_employee import AddHourlyEmployee
from add_salaried_employee import AddSalariedEmployee
from biweekly_schedule import BiweeklySchedule
from commissioned_classification import CommissionedClassification
from employee import EmpId
from hold_method import HoldMethod
from hourly_classification import HourlyClassification
from monthly_schedule import MonthlySchedule
from payroll_database import g_payroll_database
from salaried_classification import SalariedClassification
from weekly_schedule import WeeklySchedule


class PayrollTest(unittest.TestCase):
    def test_add_salaried_employee(self):
        emp_id = EmpId(1)
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

    def test_add_hourly_employee(self):
        emp_id = EmpId(1)
        transaction = AddHourlyEmployee(
            emp_id, 'Bob', 'Home', hourly_rate=10.00)
        transaction.execute()

        employee = g_payroll_database.get_employee(emp_id)
        self.assertEqual('Bob', employee.get_name())
        self.assertEqual('Home', employee.get_address())

        classification = employee.get_classification()
        self.assertEqual(10.00, classification.get_hourly_rate())

        self.assertIsInstance(classification, HourlyClassification)
        self.assertIsInstance(employee.get_schedule(), WeeklySchedule)
        self.assertIsInstance(employee.get_method(), HoldMethod)

    def test_add_commissioned_employee(self):
        emp_id = EmpId(1)
        transaction = AddCommissionedEmployee(
            emp_id, 'Bob', 'Home', salary=1000.00, commission_rate=0.01)
        transaction.execute()

        employee = g_payroll_database.get_employee(emp_id)
        self.assertEqual('Bob', employee.get_name())
        self.assertEqual('Home', employee.get_address())

        classification = employee.get_classification()
        self.assertEqual(1000.00, classification.get_salary())
        self.assertEqual(0.01, classification.get_commission_rate())

        self.assertIsInstance(classification, CommissionedClassification)
        self.assertIsInstance(employee.get_schedule(), BiweeklySchedule)
        self.assertIsInstance(employee.get_method(), HoldMethod)


if __name__ == '__main__':
    unittest.main()
