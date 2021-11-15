"""
returns the nth coefficients of a chebychev polynomial

Milo Barkow, November 15th, 2021

"""

import sympy as sim

n = int(input('input: '))
x = sim.Symbol('x')


def T(n, x=x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    for i in range(n):
        return (2 * x * T(n - 1)) - T(n - 2)


final = str(sim.expand(T(n))).replace('*', '')
i = 0
while i < len(final):
    if final[i] == 'x' and i != len(final) - 1:
        i += 1
        final = final[:i] + '^' + final[i:]
    i += 1

print(final)
