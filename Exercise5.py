import math


b = math.pi / 4
a = 0


def f(x):
    return math.e ** (3 * x) + math.cos(x)


def simpson1_3(a, b, n): #simpsons rule
    h = (b - a) / n #divided by n
    x = a # so start at the front
    s = 0
    for i in range(1, n):
        x = x + h #to move to next segment
        if i%2 == 0: #for even
            m = 2
        else:#for odd
            m = 4
        s =s + m * f(x) #sum multiplier * by f(x)
    return (b - a) * (f(a) + s + f(b)) / (3 * n) #returns simpsons rule


print("Estimate: " + str(simpson1_3(a, b, 10)))
