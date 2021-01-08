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
        test = WasRun('test_method')
        test.run()
        assert 'setup test_method teardown ' == test.log

    def test_result(self):
        test = WasRun('test_method')
        result = test.run()
        assert '1 run, 0 failed' == result.summary()


TestCaseTest('test_template_method').run()
TestCaseTest('test_result').run()
