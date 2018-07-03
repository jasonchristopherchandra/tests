import math
import matplotlib.pyplot as plt

def mysin(n):
    'Maclaurin Series'
    return (-1)**n * (math.pi/3)**(2*n + 1)/math.factorial(2*n + 1)

n_list = [5,10,20,50] #nlist
error = [] #create list named error
s = 0
x = math.pi/3 # create x = pi/3
exact = math.sin(x) #exact value

for n in n_list: #for loop for 10 times
    for i in range(n):
        s += mysin(i)
    error.append(abs(exact-s)) #appends error between exact nd estimated to error list
    s = 0 #reset sum (each n run different test, so you need to reset)


plt.plot(n_list, error)
plt.show()
