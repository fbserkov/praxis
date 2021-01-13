class Timecard:
    def __init__(self, date, hours):
        self._date = date
        self._hours = hours

    def get_date(self):
        return self._date

    def get_hours(self):
        return self._hours