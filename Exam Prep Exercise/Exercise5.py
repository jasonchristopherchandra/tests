import math


b = math.pi / 4
a = 0


def f(x):
    return math.e ** (3 * x) + math.cos(x)


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


print("Estimate: " + str(simpson1_3(a, b, 10)))
