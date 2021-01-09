# Test-driven development by example
# Appendix I: Fibonacci

import unittest


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        cases = (0, 0), (1, 1), (2, 1), (3, 2)
        for n, res in cases:
            self.assertEqual(res, fib(n))


if __name__ == '__main__':
    unittest.main()
