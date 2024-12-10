from sympy import *


A = Matrix([
    [1, 2, 0],
    [2, 0, 0],
    [0, 1, 1]
])

B = Matrix([
    [3, 0, 1],
    [2, 1, 0],
    [1, 0, 0],
])

C = Matrix([
    [0, 1/2, 0],
    [1/2, -1/4, 0],
    [-1/2, 1/4, 1],
])

print_latex((A*B)*C)