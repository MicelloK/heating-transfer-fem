import numpy as np
from scipy import integrate

# ------------------------------------------------------

def e(i, x):
    if x < h * (i - 1) or x > h * (i + 1):
        return 0
    if x < h * i:
        return x / h - i + 1
    return - x / h + i + 1

def e_prim(i, x):
    if x < h * (i - 1) or x > h * (i + 1):
        return 0
    if x < h * i:
        return 1 / h
    return -1 / h

def B(i, j, s, z):       
    return integrate.quad(lambda x: e_prim(i, x) * e_prim(j, x), s, z)[0] - e(i, 0) * e(j, 0)

def L(i, s, z):
    def k(x):
        if x < 0 or x > 2:
            return 1
        if x <= 1:
            return x + 1
        return 2 * x
    
    return integrate.quad(lambda x: 100 * x * e(i, x) / k(x), s, z)[0] - 20 * e(i, 0)

def create_A():
    matrix = []
    for i in range(elem_num):
        row = []
        for j in range(elem_num):
            if (abs(i - j) > 1):
                row.append(0)
                continue
            if (abs(i - j) == 1):
                s = 2.* max(0, min(i, j) / elem_num)
                e = 2.* min(1, max(i, j) / elem_num)
            else:
                s = 2.* max(0, (i - 1) / elem_num)
                e = 2.* min(1, (i + 1) / elem_num)
            row.append(B(i, j, s, e))
        matrix.append(row)
    
    return matrix

def create_B():
    matrix = []
    for i in range(elem_num):
        if (i == 0):
            s = 2.* max(0, (i - 1) / elem_num)
            e = 2.* min(1, (i + 1) / elem_num)
        else:
            s = 2.* max(0, (i - 1) / elem_num)
            e = 2.* min(1, (i + 1) / elem_num)
        matrix.append(L(i, s, e))
    return matrix

def solve(n):
    global elem_num
    global h
    elem_num = n
    h = 2 / n

    a = np.array(create_A())
    b = np.array(create_B())

    x = [h * i for i in range(elem_num + 1)]
    y = np.append(np.linalg.solve(a, b), 0)
    

    return (x, y)
