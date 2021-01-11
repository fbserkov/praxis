from payroll_database import g_payroll_database


class AddEmployeeTransaction:
    def __init__(self, emp_id, name, address):
        self._emp_id = emp_id
        self._name = name
        self._address = address

    def execute(self):
        payment_classification = self.get_classification()
        payment_schedule = self.get_schedule()
        payment_method = HoldMethod()
        employee = Employee(self._emp_id, self._name, self._address)
        employee.set_classification(payment_classification)
        employee.set_schedule(payment_schedule)
        employee.set_method(payment_method)
        g_payroll_database.add_employee(self._emp_id, employee)

    def get_classification(self):
        pass

    def get_schedule(self):
        pass