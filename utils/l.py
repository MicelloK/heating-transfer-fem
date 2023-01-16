import numpy as np
import scipy as sp
import sympy as smp
from scipy.integrate import quad

x = smp.Symbol('x')

def L(v):
    f = smp.lambdify(x, 100 * x * v / (x + 1))
    g = smp.lambdify(x, 50 * v)
    return quad(f, 0, 1)[0] + quad(g, 1, 2)[0] - 20 * smp.lambdify(x, v)(0)
