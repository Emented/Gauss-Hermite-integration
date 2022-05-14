import math
from sympy import *


def proisv(expr, n):
    d = Derivative(expr)
    if n == 1:
        return d.doit()
    if n > 1:
        return proisv(d.doit(), n - 1)


x, y = symbols('x y')

n = 10

H = (-1) ** n * math.e ** ((x ** 2) / 2) * proisv(math.e ** (-(x ** 2) / 2), n)

H_n = (-1) ** (n - 1) * math.e ** ((x ** 2) / 2) * proisv(math.e ** (-(x ** 2) / 2), n - 1)

H_n_2 = (-1) ** (n - 1) * math.e ** (x ** 2) * proisv(math.e ** (-(x ** 2)), n - 1)

H2 = (-1) ** n * math.e ** (x ** 2) * proisv(math.e ** (-(x ** 2)), n)

ixes = list(solveset(H2))
print("Иксы", end=' ')
print(*ixes)

weights = []

for xs in ixes:
    mnog = simplify(proisv(H2, 1)).subs(x, xs)
    w = ((2 ** (n - 1)) * factorial(n) * sqrt(math.pi)) / ((n ** 2) * (H_n_2.subs(x, xs)) ** 2)
    weights.append(w)


print("Веса", end=' ')
print(*weights)
res = 0

e = (4 * x ** 2) * math.e ** (-(x ** 2))

for i in range(n):
    res += weights[i] * (e.subs(x, ixes[i]))

print(res)