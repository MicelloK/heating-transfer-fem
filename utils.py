import numpy as np
import sympy as smp
from sympy import integrate

x = smp.Symbol('x')
n = 9
h = 2 / n

# ------------------------------------------------------

def B(u, v):
    f = smp.diff(u, x) * smp.diff(v, x)
    return integrate(f, (x, 0, 2)).evalf() - u.subs(x,0) * v.subs(x,0)

def L(v):
    f = 100 * x * v / (x + 1)
    g = 50 * v
    return integrate(f, (x, 0, 1)).evalf() + integrate(g, (x, 1, 2)).evalf() - 20 * v.subs(x,0)

def e(i, x):
    if smp.And(x <= h*i, x >= h*(i-1)):
        return x/h - (i-1)
    elif smp.And(x > h*i, x <= h*(i+1)):
        return -x/h + (i+1)
    else:
        return 0

def create_A():
    A = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(B(e(i, x), e(j, x)).evalf())
        A.append(row)
    return A

def create_B():
    B = []
    for i in range(1, n + 1):
        B.append(L(e(i, x)).evalf())
    return B

def solve():
    a = np.array([[float(x) for x in row] for row in create_A()])
    b = np.array([float(x) for x in create_B()])
    print(a)
    print(b)
    print(np.linalg.det(a))
    
    

solve()