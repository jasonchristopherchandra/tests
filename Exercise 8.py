from sympy import *

x = symbols("x") #symbol x
abcd = Integral(sin(x)/(1+x**2),(x,0,pi/2)) #integrate sinx / 1+x**2, pi/2 to 0
print(abcd.evalf()) #print abcd
