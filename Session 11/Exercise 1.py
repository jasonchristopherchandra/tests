from sympy import *


def f(x):
    return 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5


def trapezoid(a, b, n):
    h = (b - a) / n
    x = a
    s = 0
    for i in range(1, n):
        x = x + h
        s = s + f(x)
    return (b - a) * (f(a) + 2 * s + f(b)) / (2 * n)


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


n = 100
a = 0
b = 0.8

# approx = simpson1_3(a, b, n)

x = symbols('x')
exact_int = integrate(0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5, x)
exact = abs(exact_int.subs(x, a) - exact_int.subs(x, b))

print("Exact integral value      = ", exact)
# print("Trapezoidal approximation = ", approx)
# print("Error (%)                 = ", 100 * abs(exact - approx) / exact, "%")


loop = [2, 5, 20, 100]
print("n\ttrapezoid\t\t\tsimpson1/3")
for x in loop:
    print(str(x) + "\t" + str(trapezoid(a, b, x)) + "\t" + str(simpson1_3(a, b, x)) )
