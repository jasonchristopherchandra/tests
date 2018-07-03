from math import sqrt
import matplotlib.pyplot as plt

myfile = open("test.csv")

x = []
y = []
x_p3 = []
sqrt_xy = []

for i in range(0, 5):
    line = myfile.readline()
    temp_array = line.split(",")
    x.append(int(temp_array[0]))
    y.append(int(temp_array[1]))

myfile.close()

space = "  "
print("x x^3 y sqrt(x+y)")

for z in range(0,5):
    x_p3.append(x[z] ** 3)
    sqrt_xy.append(sqrt(x[z] + y[z]))
    print( str(x[z]) + space + str(x_p3[z]) + space + str(y[z]) + space + str(sqrt_xy[z]))

ax = plt.subplot(1, 2, 1)
ax.plot(x,x_p3)
print(x_p3)
ax = plt.subplot(1, 2, 2)
ax.plot(y, sqrt_xy)
plt.show()
