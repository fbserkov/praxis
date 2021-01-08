# Kent Beck
# Test-driven development by example
# Section II: xUnit example

class TestCase:
    def __init__(self, name):
        self._name = name

    def setup(self):
        pass

    def run(self):
        self.setup()
        method = getattr(self, self._name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.was_setup = None
        self.was_run = None
        TestCase.__init__(self, name)

    def setup(self):
        self.was_setup = 1

    def test_method(self):
        self.was_run = 1


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun('test_method')
        assert not test.was_run
        test.run()
        assert test.was_run

    def test_setup(self):
        test = WasRun('test_method')
        test.run()
        assert test.was_setup


TestCaseTest('test_running').run()
TestCaseTest('test_setup').run()
