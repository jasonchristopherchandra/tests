import math
import matplotlib.pyplot as plt

def mysin(n):
    'Maclaurin Series'
    return (-1)**n * (math.pi/3)**(2*n + 1)/math.factorial(2*n + 1)

n_list = [5,10,20,50]
error = []
s = 0
x = math.pi/3
exact = math.sin(x)

for n in n_list:
    for i in range(n + 1):
        s += mysin(i)
    error.append(abs(exact-s))
    s = 0

print(exact)
print(error)
ax = plt.subplot(1, 1, 1)
ax.plot(n_list, error)
plt.show()
