import numpy as np
import scipy as sp
import sympy as smp
from scipy.integrate import quad

x = smp.Symbol('x')

def B(u, v):
    f = smp.lambdify(x, smp.diff(u, x) * smp.diff(v, x))
    return quad(f, 0, 2)[0] - smp.lambdify(x, u)(0) * smp.lambdify(x, v)(0)
