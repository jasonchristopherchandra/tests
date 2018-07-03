import math

from numpy.ma import arctan

x = math.pi/3


def f(n):
    return (-1)**n * (math.pi/3)**(2*n+1) /(2*n+1)


def arctan_n_series(n):
    result = 0.0
    for i in range(n):
        result += f(i)
    return result


actual = arctan(x)

n_list = [3, 5, 10, 20]

print("n  arctan(pi/3)      actual        absolute error")

for i in n_list:
    temp_arctan = arctan_n_series(i)
    abs_error = abs(temp_arctan - actual)
    print(str(i) + " " + str(temp_arctan) + " " + str(actual) + " " + str(abs_error))
