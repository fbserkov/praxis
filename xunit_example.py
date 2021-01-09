# Kent Beck
# Test-driven development by example
# Section II: xUnit example

class TestResult:
    def __init__(self):
        self._run_count = 0
        self._error_count = 0

    def test_started(self):
        self._run_count += 1

    def test_failed(self):
        self._error_count += 1

    def summary(self):
        return f'{self._run_count} run, {self._error_count} failed'


class TestCase:
    def __init__(self, name):
        self._name = name

    def setup(self):
        pass

    def run(self, result):
        result.test_started()
        try:
            self.setup()
            method = getattr(self, self._name)
            method()
        except:
            result.test_failed()
        self.teardown()

    def teardown(self):
        pass


class TestSuite:
    def __init__(self):
        self._tests = []

    def add(self, test):
        self._tests.append(test)

    def run(self, result):
        for test in self._tests:
            test.run(result)


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.log = ''

    def setup(self):
        self.log += 'setup '

    def test_method(self):
        self.log += 'test_method '

    def test_broken_method(self):
        raise Exception

    def teardown(self):
        self.log += 'teardown '


class TestCaseTest(TestCase):
    def setup(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert 'setup test_method teardown ' == test.log

    def test_result(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert '1 run, 0 failed' == self.result.summary()

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert '1 run, 1 failed' == self.result.summary()

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        test.run(self.result)
        assert '1 run, 1 failed' == self.result.summary()

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_broken_method'))
        suite.run(self.result)
        assert '2 run, 1 failed' == self.result.summary()

    def test_teardown(self):
        test = WasRun('test_broken_method')
        test.run(self.result)
        assert 'setup teardown ' == test.log

    def test_failed_setup(self):
        test = WasRun('test_method')
        test.setup = test.test_broken_method
        test.run(self.result)
        assert '1 run, 1 failed' == self.result.summary()



_suite = TestSuite()
_suite.add(TestCaseTest('test_template_method'))
_suite.add(TestCaseTest('test_result'))
_suite.add(TestCaseTest('test_failed_result_formatting'))
_suite.add(TestCaseTest('test_failed_result'))
_suite.add(TestCaseTest('test_suite'))
_suite.add(TestCaseTest('test_teardown'))
_suite.add(TestCaseTest('test_failed_setup'))
_result = TestResult()
_suite.run(_result)
print(_result.summary())
