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
        TestCase.__init__(self, name)

    def setup(self):
        self.was_run = None
        self.log = 'setup '

    def test_method(self):
        self.was_run = 1


class TestCaseTest(TestCase):
    def setup(self):
        self.test = WasRun('test_method')

    def test_running(self):
        self.test.run()
        assert self.test.was_run

    def test_setup(self):
        self.test.run()
        assert 'setup ' == self.test.log


TestCaseTest('test_running').run()
TestCaseTest('test_setup').run()
