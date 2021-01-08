# Kent Beck
# Test-driven development by example
# Section II: xUnit example

class WasRun:
    def __init__(self, name):
        self.was_run = None

    def test_methode(self):
        self.was_run = 1


test = WasRun('test_methode')
print(test.was_run)
test.test_methode()
print(test.was_run)
