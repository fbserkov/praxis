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


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun('test_method')
        assert not test.was_run
        test.run()
        assert test.was_run


TestCaseTest('test_running').run()
