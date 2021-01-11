import unittest


class PayrollTest(unittest.TestCase):
    def test_add_salaried_employee(self):
        emp_id = 1
        AddSalatiedEmployee t(emp_id, 'Bob', 'Home', 1000.00)
        t.execute()

        e = GpayrollDatabase.get_enployee(emp_id)
        sc = e.get_classification()
        ms = e.get_schedule()
        hm = e.get_method()

        self.assertIsInstance(sc, SalariedClassification)
        self.assertIsInstance(ms, MonthlySchedule)
        self.assertIsInstance(hm, HoldMethod)

        self.assertEqual('Bob', e.get_name())
        self.assertEqual(1000.00, sc.get_salary())


if __name__ == '__main__':
    unittest.main()