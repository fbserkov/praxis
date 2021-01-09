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

    def run(self):
        result = TestResult()
        result.test_started()
        self.setup()
        try:
            method = getattr(self, self._name)
            method()
        except:
            result.test_failed()
        self.teardown()
        return result

    def teardown(self):
        pass


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
    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert 'setup test_method teardown ' == test.log

    def test_result(self):
        test = WasRun('test_method')
        result = test.run()
        assert '1 run, 0 failed' == result.summary()

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert '1 run, 1 failed' == result.summary()

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        result = test.run()
        assert '1 run, 1 failed' == result.summary()


print(TestCaseTest('test_template_method').run().summary())
print(TestCaseTest('test_result').run().summary())
print(TestCaseTest('test_failed_result_formatting').run().summary())
print(TestCaseTest('test_failed_result').run().summary())
