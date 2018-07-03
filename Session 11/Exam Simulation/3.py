from sympy import *

x = symbols("x")

formula = Integral(sin(x)/(1+x**2), (x, 0, pi/2))
answer = formula.evalf()

print(answer)
