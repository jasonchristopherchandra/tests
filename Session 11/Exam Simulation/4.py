from sympy import *


def f(x):
    return sin(x)/(1+x**2)


def simpson1_3(a, b, n):
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


n = [2, 5, 10, 100]
a = 0
b = pi/2

x = symbols("x")
exact_int = Integral(sin(x)/(1+x**2),(x,0,pi/2))
I = exact_int.evalf()

for i in n:
    approx = simpson1_3(a, b, i)
    approx = approx.evalf()
    print(i, "\t", approx, "\t",100* abs((approx-I)/I))
