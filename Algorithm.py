import math
from sympy import *


def input_func():
    print("Введите функцию f(x), программа посчитает значения интеграла f(x) * e^(-x^2) на всей плоскости")
    while true:
        try:
            return parse_expr(input())
        except SyntaxError:
            print("Вы ввели недопустимый символ, попробуйте снова")
        except TypeError:
            print("Вы ввели недопустимый символ, попробуйте снова")


def input_accuracy():
    print("Введите желаемую точность (число >= 3)")
    while true:
        try:
            return int(input())
        except ValueError:
            print("Вы ввели недопустимый символ, попробуйте снова")
        except TypeError:
            print("Вы ввели недопустимый символ, попробуйте снова")


def calculate(func, n):
    x = symbols('x')
    result = 0
    w_list = []
    hermite_polynomial_prev = (-1) ** (n - 1) * math.e ** (x ** 2) * derivative_n_times(
        math.e ** (-(x ** 2)), n - 1)
    hermite_polynomial = (-1) ** n * math.e ** (x ** 2) * derivative_n_times(math.e ** (-(x ** 2)), n)

    x_list = list(ordered(solveset(hermite_polynomial)))

    for cur_x in x_list:
        current_w = ((2 ** (n - 1)) * factorial(n) * sqrt(math.pi)) / (
                (n ** 2) * (hermite_polynomial_prev.subs(x, cur_x)) ** 2)
        w_list.append(current_w)

    for i in range(n):
        result += w_list[i] * (func.subs(x, x_list[i]))

    return result


def derivative_n_times(expr, times):
    d = Derivative(expr)
    if times == 1:
        return d.doit()
    if times > 1:
        return derivative_n_times(d.doit(), times - 1)
