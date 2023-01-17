import numpy as np
from scipy import integrate

# ------------------------------------------------------

def e(i, x):
    return max(1 - abs((x - i * h) / h), 0)
    # if x <= h * i:
    #     return max(0, x / h - (i - 1))
    # return max(0, -x / h + (i + 1))

def e_prim(i, x):
    n = elem_num
    return (1/h * (h*(i-1) <= x) * (x < h*i) * (0 <= x) + 
                -h * (h*i<= x) * (x < h*(i+1)) * (x <= 2))

    # if x < h * (i - 1) or x > h * (i + 1):
    #     return 0
    # if x <= h * i:
    #     return 1 / h
    # return -1 / h

# def B(i, j):
#     return integrate.quad(lambda x: e_prim(i, x) * e_prim(j, x), 0, 2)[0] - e(i, 0) * e(j, 0)

# def L(i):
#     def k(x):
#         if x < 0 or x > 2:
#             return 0
#         if x <= 1:
#             return x + 1
#         return 2 * x

#     return integrate.quad(lambda x: 100 * x * e(i, x) / k(x), 0, 2)[0] - 20 * e(i, 0)
    
#     # i1 = integrate.quad(lambda x: 100 * x * e(i, x) / (x + 1), 0, 1)[0]
#     # i2 = integrate.quad(lambda x: 50 * e(i, x), 1, 2)[0]
#     # return i1 + i2 - 20 * e(i, 0)

# def create_A():
#     matrix = []
#     for i in range(elem_num + 1):
#         row = []
#         for j in range(elem_num + 1):
#             row.append(B(i, j))
#         matrix.append(row)
#     return matrix

# def create_B():
#     matrix = []
#     for i in range(elem_num + 1):
#         matrix.append(L(i))
#     return matrix

def B(i, j, s, z):
    return integrate.quad(lambda x: e_prim(i, x) * e_prim(j, x), s, z)[0] - e(i, 0) * e(j, 0)

def L(i, s, z):
    def k(x):
        if x < 0 or x > 2:
            return 0
        if x <= 1:
            return x + 1
        return 2 * x

    return integrate.quad(lambda x: 100 * x * e(i, x) / k(x), s, z)[0] - 20 * e(i, 0)

def create_A():
    matrix = []
    for i in range(elem_num + 1):
        row = []
        for j in range(elem_num + 1):
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
    for i in range(elem_num + 1):
        if (i == elem_num):
            matrix.append(1)
            continue
        if (i == 0):
            s = 2.* max(0, (i - 1) / elem_num)
            e = 2.* min(1, (i + 1) / elem_num)
        else:
            s = 2.* max(0, i / elem_num)
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
    y = np.linalg.solve(a, b)
    return (x, y)

import matplotlib.pyplot as plt
import numpy as np

def test(n):
    def e(i, x):
        h = 2/n
        if x <= h * i:
            return max(0, x / h - (i - 1))
        return max(0, -x / h + (i + 1))

    x = np.linspace(0, 2, 100)

    plt.figure()
    for i in range(n+1):
        plt.plot(x, [e(i, val) for val in x], label=f'i={i}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    test(40)