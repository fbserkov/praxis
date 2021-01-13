import unittest

from add_commissioned_employee import AddCommissionedEmployee
from add_hourly_employee import AddHourlyEmployee
from add_salaried_employee import AddSalariedEmployee
from affiliation import MemberId, UnionAffiliation
from delete_employee_transaction import DeleteEmployeeTransaction
from employee import EmpId
from payment_classification import (
    CommissionedClassification, HourlyClassification, SalariedClassification)
from payment_method import HoldMethod
from payment_schedule import BiweeklySchedule, MonthlySchedule, WeeklySchedule
from payroll_database import g_payroll_database
from sales_receipt_transaction import SalesReceiptTransaction
from service_charge_transaction import ServiceChargeTransaction
from timecard_transaction import TimecardTransaction


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
            emp_id, 'Bob', 'Home', salary=1000.00, commission_rate=1.0)
        transaction.execute()

        employee = g_payroll_database.get_employee(emp_id)
        self.assertEqual('Bob', employee.get_name())
        self.assertEqual('Home', employee.get_address())

        classification = employee.get_classification()
        self.assertEqual(1000.00, classification.get_salary())
        self.assertEqual(1.0, classification.get_commission_rate())

        self.assertIsInstance(classification, CommissionedClassification)
        self.assertIsInstance(employee.get_schedule(), BiweeklySchedule)
        self.assertIsInstance(employee.get_method(), HoldMethod)

    def test_delete_employee(self):
        emp_id = EmpId(3)
        transaction = AddCommissionedEmployee(
            emp_id, 'Lance', 'Home', salary=2500, commission_rate=3.2)
        transaction.execute()
        employee = g_payroll_database.get_employee(emp_id)
        self.assertTrue(employee)

        transaction = DeleteEmployeeTransaction(emp_id)
        transaction.execute()
        employee = g_payroll_database.get_employee(emp_id)
        self.assertIsNone(employee)

    def test_timecard_transaction(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()

        transaction = TimecardTransaction(emp_id, date=20011031, hours=8.0)
        transaction.execute()
        employee = g_payroll_database.get_employee(emp_id)
        classification = employee.get_classification()

        timecard = classification.get_timecard(date=20011031)
        self.assertTrue(timecard)
        self.assertEqual(8.0, timecard.get_hours())

    def test_sales_receipt_transaction(self):
        emp_id = EmpId(3)
        transaction = AddCommissionedEmployee(
            emp_id, 'Lance', 'Home', salary=2500, commission_rate=3.2)
        transaction.execute()

        transaction = SalesReceiptTransaction(
            emp_id, date=20011031, amount=3500)
        transaction.execute()
        employee = g_payroll_database.get_employee(emp_id)
        classification = employee.get_classification()

        sales_receipt = classification.get_sales_receipt(date=20011031)
        self.assertTrue(sales_receipt)
        self.assertEqual(3500, sales_receipt.get_amount())

    def test_add_service_charge(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()
        employee = g_payroll_database.get_employee(emp_id)

        union_affiliation = UnionAffiliation()
        employee.set_affiliation(union_affiliation)
        member_id = MemberId(86)  # Maxwell Smart
        g_payroll_database.add_union_member(member_id, employee)

        transaction = ServiceChargeTransaction(
            member_id, date=20011101, charge=12.95)
        transaction.execute()
        service_charge = union_affiliation.get_service_charge(20011101)
        self.assertTrue(service_charge)
        self.assertEqual(12.95, service_charge.get_amount())


if __name__ == '__main__':
    unittest.main()
