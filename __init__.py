import math

from sympy import *


def proisv(expr, n):
    d = Derivative(expr)
    if n == 1:
        return d.doit()
    if n > 1:
        return proisv(d.doit(), n - 1)


x, y = symbols('x y')

# expr = x ** 3 + 2 * x ** 2 + 3 * x + 4
#
# print(proisv(expr, 1))
#
# print(proisv(expr, 2))

n = 3

H = (-1) ** n * math.e ** ((x ** 2) / 2) * proisv(math.e ** (-(x ** 2) / 2), n)

H2 = (-1) ** n * math.e ** ((x ** 2)) * proisv(math.e ** (-(x ** 2)), n)

ixes = list(ordered(solveset(simplify(H2))))
print("Иксы", end=' ')
print(*ixes)

weights = []

for xs in ixes:
    mnog = simplify(proisv(H2, 1)).subs(x, xs)
    print(simplify(proisv(H2, 1)))
    w = 2 / (1 - (xs ** 2) * mnog ** 2)
    weights.append(w)
    # print(w)


print("Веса", end=' ')
print(*weights)
res = 0

e = (4 * x ** 2 + x + 1) * math.e ** (-(x ** 2))

for i in range(n):
    #print((e.subs(x, ixes[i])))
    res += weights[i] * (e.subs(x, ixes[i]))

print(res)
