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
        self.teardown()

    def teardown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setup(self):
        self.log = 'setup '

    def test_method(self):
        self.log += 'test_method '

    def teardown(self):
        self.log += 'teardown '


class TestCaseTest(TestCase):
    def test_template_method(self):
        self.test = WasRun('test_method')
        self.test.run()
        assert 'setup test_method teardown ' == self.test.log


TestCaseTest('test_template_method').run()
