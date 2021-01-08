# Kent Beck
# Test-driven development by example
# Section II: xUnit example

class TestCase:
    def __init__(self, name):
        self._name = name

    def run(self):
        method = getattr(self, self._name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        TestCase.__init__(self, name)

    def test_method(self):
        self.was_run = 1


def test_running():
    test = WasRun('test_method')
    print(test.was_run)
    test.run()
    print(test.was_run)

test_running()
