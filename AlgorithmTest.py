import unittest

from sympy import parse_expr
from Algorithm import *


class MyTestCase(unittest.TestCase):

    def test_first(self):
        self.assertAlmostEqual(calculate(parse_expr("4 * x ** 4 + 2 * x + 3"), 10), 10.6347231)

    def test_second(self):
        self.assertAlmostEqual(calculate(parse_expr("sin(x) ** 2"), 10), 0.560202259)

    def test_third(self):
        self.assertAlmostEqual(calculate(parse_expr("(sin(x) ** 2) * ((cos (3 * x)) ** 2)"), 30), 0.276097836)


if __name__ == '__main__':
    unittest.main()
