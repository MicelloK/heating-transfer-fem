from sympy import Symbol, sympify
x = Symbol('x')
v = lambda x: x**2
v = sympify(v)(x)

