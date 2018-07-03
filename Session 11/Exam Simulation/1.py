from sympy import *
import math

def mysin(n):
    'Maclaurin Series'
    return (-1)**n * x**(2*n + 1)/math.factorial(2*n + 1)

n = 10
s = 0
x= math.pi/3

for n in range(n + 1):
    s += mysin(n)

exact = sin(x)
error = (exact-s)
print(s)
print(error)
