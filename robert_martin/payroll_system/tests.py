import unittest
from datetime import date

from add_commissioned_employee import AddCommissionedEmployee
from add_hourly_employee import AddHourlyEmployee
from add_salaried_employee import AddSalariedEmployee
from affiliation import MemberId, UnionAffiliation
from change_affiliation_transaction import ChangeMemberTransaction
from change_classification_transaction import (
    ChangeCommissionedTransaction, ChangeHourlyTransaction,
    ChangeSalariedTransaction,
)
from change_employee_transaction import (
    ChangeAddressTransaction, ChangeNameTransaction)
from change_method_transaction import (
    ChangeDirectTransaction, ChangeHoldTransaction, ChangeMailTransaction)
from delete_employee_transaction import DeleteEmployeeTransaction
from employee import EmpId
from payday_transaction import PaydayTransaction
from payment_classification import (
    CommissionedClassification, HourlyClassification, SalariedClassification)
from payment_method import DirectMethod, HoldMethod, MailMethod
from payment_schedule import BiweeklySchedule, MonthlySchedule, WeeklySchedule
from payroll_database import g_payroll_database
from sales_receipt_transaction import SalesReceiptTransaction
from service_charge_transaction import ServiceChargeTransaction
from timecard_transaction import TimecardTransaction


class PayrollTest(unittest.TestCase):
    def setUp(self) -> None:
        g_payroll_database.clear()

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

    def test_change_name_transaction(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()

        transaction = ChangeNameTransaction(emp_id, 'Bob')
        transaction.execute()
        employee = g_payroll_database.get_employee(emp_id)
        self.assertEqual('Bob', employee.get_name())

    def test_change_address_transaction(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()

        transaction = ChangeAddressTransaction(emp_id, 'Garage')
        transaction.execute()
        employee = g_payroll_database.get_employee(emp_id)
        self.assertEqual('Garage', employee.get_address())

    def test_change_salaried_transaction(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()
        transaction = ChangeSalariedTransaction(emp_id, salary=1000)
        transaction.execute()

        employee = g_payroll_database.get_employee(emp_id)
        classification = employee.get_classification()
        self.assertIsInstance(classification, SalariedClassification)
        self.assertEqual(1000, classification.get_salary())
        self.assertIsInstance(employee.get_schedule(), MonthlySchedule)

    def test_change_hourly_transaction(self):
        emp_id = EmpId(3)
        transaction = AddCommissionedEmployee(
            emp_id, 'Lance', 'Home', salary=2500, commission_rate=3.2)
        transaction.execute()
        transaction = ChangeHourlyTransaction(emp_id, hourly_rate=27.52)
        transaction.execute()

        employee = g_payroll_database.get_employee(emp_id)
        classification = employee.get_classification()
        self.assertIsInstance(classification, HourlyClassification)
        self.assertEqual(27.52, classification.get_hourly_rate())
        self.assertIsInstance(employee.get_schedule(), WeeklySchedule)

    def test_change_commissioned_transaction(self):
        emp_id = EmpId(1)
        transaction = AddSalariedEmployee(
            emp_id, 'Bob', 'Home', salary=1000.00)
        transaction.execute()
        transaction = ChangeCommissionedTransaction(
            emp_id, salary=2500, commission_rate=3.2)
        transaction.execute()

        employee = g_payroll_database.get_employee(emp_id)
        classification = employee.get_classification()
        self.assertIsInstance(classification, CommissionedClassification)
        self.assertEqual(2500, classification.get_salary())
        self.assertEqual(3.2, classification.get_commission_rate())
        self.assertIsInstance(employee.get_schedule(), BiweeklySchedule)

    def test_change_direct_transaction(self):
        emp_id = EmpId(1)
        transaction = AddSalariedEmployee(
            emp_id, 'Bob', 'Home', salary=1000.00)
        transaction.execute()
        transaction = ChangeDirectTransaction(
            emp_id, bank='VTB', account=1234123412341234)
        transaction.execute()

        method = g_payroll_database.get_employee(emp_id).get_method()
        self.assertIsInstance(method, DirectMethod)
        self.assertEqual('VTB', method.get_bank())
        self.assertEqual(1234123412341234, method.get_account())

    def test_change_mail_transaction(self):
        emp_id = EmpId(1)
        transaction = AddSalariedEmployee(
            emp_id, 'Bob', 'Home', salary=1000.00)
        transaction.execute()
        transaction = ChangeMailTransaction(emp_id, address='home address')
        transaction.execute()

        method = g_payroll_database.get_employee(emp_id).get_method()
        self.assertIsInstance(method, MailMethod)
        self.assertEqual('home address', method.get_address())

    def test_change_hold_transaction(self):
        emp_id = EmpId(1)
        transaction = AddSalariedEmployee(
            emp_id, 'Bob', 'Home', salary=1000.00)
        transaction.execute()
        transaction = ChangeHoldTransaction(emp_id, address='test address')
        transaction.execute()

        method = g_payroll_database.get_employee(emp_id).get_method()
        self.assertIsInstance(method, HoldMethod)
        self.assertEqual('test address', method.get_address())

    def test_change_member_transaction(self):
        emp_id = EmpId(2)
        member_id = MemberId(7734)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()
        transaction = ChangeMemberTransaction(emp_id, member_id, dues=99.42)
        transaction.execute()

        employee = g_payroll_database.get_employee(emp_id)
        affiliation = employee.get_affiliation()
        self.assertIsInstance(affiliation, UnionAffiliation)
        self.assertEqual(99.42, affiliation.get_dues())
        self.assertIs(employee, g_payroll_database.get_union_member(member_id))

    def test_pay_single_salaried_employee(self):
        emp_id = EmpId(1)
        transaction = AddSalariedEmployee(
            emp_id, 'Bob', 'Home', salary=1000.00)
        transaction.execute()

        pay_date = date(2001, 11, 30)
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(transaction, emp_id, pay_date, 1000.00)

    def validate_paycheck(self, transaction, emp_id, pay_date, pay):
        paycheck = transaction.get_paycheck(emp_id)
        self.assertEqual(pay_date, paycheck.get_pay_date())
        self.assertEqual(pay, paycheck.get_gross_pay())
        self.assertEqual('Hold', paycheck.get_field('Disposition'))
        self.assertEqual(0.0, paycheck.get_deductions())
        self.assertEqual(pay, paycheck.get_net_pay())

    def test_pay_single_salaried_employee_on_wrong_date(self):
        emp_id = EmpId(1)
        transaction = AddSalariedEmployee(
            emp_id, 'Bob', 'Home', salary=1000.00)
        transaction.execute()

        pay_date = date(2001, 11, 29)
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.assertFalse(transaction.get_paycheck(emp_id))

    def test_pay_single_hourly_employee_no_time_cards(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()

        pay_date = date(2001, 11, 9)  # Friday
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(transaction, emp_id, pay_date, 0.0)

    def test_pay_single_hourly_employee_one_time_cards(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()
        pay_date = date(2001, 11, 9)  # Friday

        transaction = TimecardTransaction(emp_id, pay_date, hours=2.0)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(transaction, emp_id, pay_date, 2.0 * 15.25)

    def test_pay_single_hourly_employee_overtime_one_time_cards(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()
        pay_date = date(2001, 11, 9)  # Friday

        transaction = TimecardTransaction(emp_id, pay_date, hours=9.0)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(
            transaction, emp_id, pay_date, (8 + 1.5) * 15.25)

    def test_pay_single_hourly_employee_one_wrong_date(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()
        pay_date = date(2001, 11, 8)  # Thursday

        transaction = TimecardTransaction(emp_id, pay_date, hours=9.0)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.assertFalse(transaction.get_paycheck(emp_id))

    def test_pay_single_hourly_employee_two_time_cards(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()
        pay_date = date(2001, 11, 9)  # Friday

        transaction = TimecardTransaction(emp_id, pay_date, hours=2.0)
        transaction.execute()
        transaction = TimecardTransaction(emp_id, date(2001, 11, 8), hours=5.0)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(
            transaction, emp_id, pay_date, (2.0 + 5.0) * 15.25)

    def test_pay_single_hourly_employee_with_time_cards_spanning_two_pay_periods(self):
        emp_id = EmpId(2)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.25)
        transaction.execute()
        pay_date = date(2001, 11, 9)  # Friday
        date_in_previous_pay_period = date(2001, 11, 2)

        transaction = TimecardTransaction(emp_id, pay_date, hours=2.0)
        transaction.execute()
        transaction = TimecardTransaction(
            emp_id, date_in_previous_pay_period, hours=5.0)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(transaction, emp_id, pay_date, 2.0 * 15.25)

    def test_pay_single_commissioned_employee_no_sales_receipt(self):
        emp_id = EmpId(3)
        transaction = AddCommissionedEmployee(
            emp_id, 'Lance', 'Home', salary=2500, commission_rate=3.2)
        transaction.execute()

        pay_date = date(2001, 11, 9)  # Friday
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(transaction, emp_id, pay_date, 2500)

    def test_pay_single_commissioned_employee_one_sales_receipt(self):
        emp_id = EmpId(3)
        transaction = AddCommissionedEmployee(
            emp_id, 'Lance', 'Home', salary=2500, commission_rate=3.2)
        transaction.execute()
        pay_date = date(2001, 11, 9)  # Friday

        transaction = SalesReceiptTransaction(emp_id, pay_date, amount=1000)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(
            transaction, emp_id, pay_date, 2500 + 1000 * 3.2 / 100)

    def test_pay_single_commissioned_employee_one_wrong_date(self):
        emp_id = EmpId(3)
        transaction = AddCommissionedEmployee(
            emp_id, 'Lance', 'Home', salary=2500, commission_rate=3.2)
        transaction.execute()
        pay_date = date(2001, 11, 2)  # Friday, but first

        transaction = SalesReceiptTransaction(emp_id, pay_date, amount=1000)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.assertFalse(transaction.get_paycheck(emp_id))

    def test_pay_single_commissioned_employee_two_sales_receipts(self):
        emp_id = EmpId(3)
        transaction = AddCommissionedEmployee(
            emp_id, 'Lance', 'Home', salary=2500, commission_rate=3.2)
        transaction.execute()
        pay_date = date(2001, 11, 9)  # Friday

        transaction = SalesReceiptTransaction(emp_id, pay_date, amount=1000)
        transaction.execute()
        transaction = SalesReceiptTransaction(
            emp_id, date(2001, 11, 2), amount=900)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(
            transaction, emp_id, pay_date, 2500 + (1000 + 900) * 3.2 / 100)

    def test_pay_single_commissioned_employee_with_sales_receipts_spanning_two_pay_periods(self):
        emp_id = EmpId(3)
        transaction = AddCommissionedEmployee(
            emp_id, 'Lance', 'Home', salary=2500, commission_rate=3.2)
        transaction.execute()
        pay_date = date(2001, 11, 9)  # Friday
        date_in_previous_pay_period = date(2001, 10, 26)

        transaction = SalesReceiptTransaction(emp_id, pay_date, amount=1000)
        transaction.execute()
        transaction = SalesReceiptTransaction(
            emp_id, date_in_previous_pay_period, amount=900)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()
        self.validate_paycheck(
            transaction, emp_id, pay_date, 2500 + 1000 * 3.2 / 100)

    def test_salaried_union_member_dues(self):
        emp_id = EmpId(1)
        transaction = AddSalariedEmployee(
            emp_id, 'Bob', 'Home', salary=1000.00)
        transaction.execute()
        member_id = MemberId(7734)
        transaction = ChangeMemberTransaction(emp_id, member_id, dues=9.42)
        transaction.execute()

        pay_date = date(2001, 11, 30)
        transaction = PaydayTransaction(pay_date)
        transaction.execute()

        paycheck = transaction.get_paycheck(emp_id)
        self.assertEqual(pay_date, paycheck.get_pay_date())
        self.assertEqual(1000, paycheck.get_gross_pay())
        self.assertEqual('Hold', paycheck.get_field('Disposition'))
        self.assertEqual(5 * 9.42, paycheck.get_deductions())
        self.assertEqual(1000 - 5 * 9.42, paycheck.get_net_pay())

    def test_hourly_union_member_service_charge(self):
        emp_id = EmpId(1)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.24)
        transaction.execute()
        member_id = MemberId(7734)
        transaction = ChangeMemberTransaction(emp_id, member_id, dues=9.42)
        transaction.execute()

        pay_date = date(2001, 11, 9)
        transaction = ServiceChargeTransaction(
            member_id, pay_date, charge=19.42)
        transaction.execute()
        transaction = TimecardTransaction(emp_id, pay_date, hours=8.0)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()

        paycheck = transaction.get_paycheck(emp_id)
        self.assertEqual(pay_date, paycheck.get_period_end_date())
        self.assertEqual(8 * 15.24, paycheck.get_gross_pay())
        self.assertEqual('Hold', paycheck.get_field('Disposition'))
        self.assertEqual(9.42 + 19.42, paycheck.get_deductions())
        self.assertEqual(8 * 15.24 - (9.42 + 19.42), paycheck.get_net_pay())

    def test_service_charge_spanning_multiple_pay_periods(self):
        emp_id = EmpId(1)
        transaction = AddHourlyEmployee(
            emp_id, 'Bill', 'Home', hourly_rate=15.24)
        transaction.execute()
        member_id = MemberId(7734)
        transaction = ChangeMemberTransaction(emp_id, member_id, dues=9.42)
        transaction.execute()

        early_date = date(2001, 11, 2)  # previous Friday
        pay_date = date(2001, 11, 9)
        late_date = date(2001, 11, 16)  # next Friday
        transaction = ServiceChargeTransaction(
            member_id, pay_date, charge=19.42)
        transaction.execute()
        transaction = ServiceChargeTransaction(
            member_id, early_date, charge=100)
        transaction.execute()
        transaction = ServiceChargeTransaction(
            member_id, late_date, charge=200)
        transaction.execute()
        transaction = TimecardTransaction(emp_id, pay_date, hours=8.0)
        transaction.execute()
        transaction = PaydayTransaction(pay_date)
        transaction.execute()

        paycheck = transaction.get_paycheck(emp_id)
        self.assertEqual(pay_date, paycheck.get_period_end_date())
        self.assertEqual(8 * 15.24, paycheck.get_gross_pay())
        self.assertEqual('Hold', paycheck.get_field('Disposition'))
        self.assertEqual(9.42 + 19.42, paycheck.get_deductions())
        self.assertEqual(8 * 15.24 - (9.42 + 19.42), paycheck.get_net_pay())


if __name__ == '__main__':
    unittest.main()
