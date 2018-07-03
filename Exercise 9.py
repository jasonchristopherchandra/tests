from sympy import *


def f(x):#function
    return sin(x)/(1+x**2)


def simpson1_3(a, b, n):#simpsons rule function
    h = (b - a) / n
    x = a
    s = 0
    for i in range(1, n):
        x = x + h
        if i%2 == 0:
            m = 2
        else:
            m = 4
        s = s + m * f(x)
    return (b - a) * (f(a) + s + f(b)) / (3 * n)


n = [2, 5, 10, 100] #list with n values
a = 0
b = pi/2 #pi/2

x = symbols("x")
exact_int = Integral(sin(x)/(1+x**2),(x,0,pi/2))#integration of function
I = exact_int.evalf() #evalf the exact_int

for i in n:
    approx = simpson1_3(a, b, i)
    approx = approx.evalf()
    print(i, "\t", approx, "\t",100* abs((approx-I)/I))
