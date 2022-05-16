import unittest

from Algorithm import *


class MyTestCase(unittest.TestCase):

    def test_one(self):
        print("Test 1.... 4x^4 + 2x + 3")
        self.assertAlmostEqual(calculate(parse_expr("4 * x ** 4 + 2 * x + 3"), 30), 10.634723105)

    def test_two(self):
        print("Test 2.... sin(x)^2")
        self.assertAlmostEqual(calculate(parse_expr("sin(x) ** 2"), 30), 0.560202259)

    def test_three(self):
        print("Test 3.... sin(x)^2 * cos(3x)^2")
        self.assertAlmostEqual(calculate(parse_expr("(sin(x) ** 2) * ((cos (3 * x)) ** 2)"), 30), 0.276097836)

    def test_four(self):
        print("Test 4.... sqrt(x^4 + 4x^2 + 1)")
        self.assertAlmostEqual(calculate(parse_expr("sqrt(x ** 4 + 4 * x ** 2 + 1)"), 50), 3.051197643, 5)

    def test_five(self):
        print("Test 5.... sin(x) * x")
        self.assertAlmostEqual(calculate(parse_expr("x * sin(x)"), 30), 0.690194223)

    def test_six(self):
        print("Test 6.... x^3 + 4x^6 + 23 + x")
        self.assertAlmostEqual(calculate(parse_expr("x ** 3 + 4 * x ** 6 + 23 + x"), 30), 54.059842452)

    def test_seven(self):
        print("Test 7.... x^3 - x^2 + 3x + 134")
        self.assertAlmostEqual(calculate(parse_expr("x ** 3 - x ** 2 + 3 * x + 134"), 30), 236.622589095)

    def test_eight(self):
        print("Test 8.... qbrt(x^2 + 1)")
        self.assertAlmostEqual(calculate(parse_expr("(x ** 2 + 1) ** (1 / 3)"), 40), 1.993893905)

    def test_nine(self):
        print("Test 9.... 6 / (x ^ 4 + 2x^2 + 25)")
        self.assertAlmostEqual(calculate(parse_expr("6 / (x ** 4 + 2 * x ** 2 + 25)"), 30), 0.402327798)

    def test_ten(self):
        print("Test 10.... x^29 + 234x^23 + 6")
        self.assertAlmostEqual(calculate(parse_expr("x ** 29 + 234 * x ** 23 + 6"), 40), 10.634723105, 5)

    def test_eleven(self):
        print("Test 11.... x^4 / (x^2 + 1)")
        self.assertAlmostEqual(calculate(parse_expr("x ** 4 / (x ** 2 + 1)"), 50), 0.457066496)

    def test_twelve(self):
        print("Test 12.... (x^6 + x^2 + 25) / (x^4 + 32)")
        self.assertAlmostEqual(calculate(parse_expr("(x ** 6 + x ** 2 + 25) / (x ** 4 + 32)"), 30), 1.45906, 6)

    def test_thirteen(self):
        print("Test 13.... x^4 / (sin(x)^2 + 1)")
        self.assertAlmostEqual(calculate(parse_expr("x ** 4 / ((sin(x) ** 2) + 1)"), 50), 0.748724, 5)


if __name__ == '__main__':
    unittest.main()
