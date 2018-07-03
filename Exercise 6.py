import math

x = math.pi/3 #x = pi/3
actual = math.sin(x)#sin x
s = 0
n = 10#n

def f(n):
    return ( (-1)**n ) * (x ** (2*n + 1 ))/(math.factorial(2*n + 1)) #estimate

for n in range(n):#for loop for 10 times
    s += f(n)

error = (actual-s) #error value
print(error) #print error value

