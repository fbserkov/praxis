# Kent Beck
# Test-driven development by example
# Section II: xUnit example

class WasRun:
    def __init__(self, name):
        self.was_run = None
        self._name = name

    def run(self):
        method = getattr(self, self._name)
        method()

    def test_method(self):
        self.was_run = 1


test = WasRun('test_method')
print(test.was_run)
test.run()
print(test.was_run)
