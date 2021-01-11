class Employee:
    def __init__(self, emp_id, name, address):
        self._emp_id = emp_id
        self._name = name
        self._address = address

        self._payment_classification = None
        self._payment_schedule = None
        self._payment_method = None

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def set_classification(self, payment_classification):
        self._payment_classification = payment_classification

    def set_schedule(self, payment_schedule):
        self._payment_schedule = payment_schedule

    def set_method(self, payment_method):
        self._payment_method = payment_method

    def get_classification(self):
        return self._payment_classification

    def get_schedule(self):
        return self._payment_schedule

    def get_method(self):
        return self._payment_method
