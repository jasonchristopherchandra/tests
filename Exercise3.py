from math import sqrt
import matplotlib.pyplot as plt

myfile = open("test.csv") #open test

x = [] #create list for x
y = [] #create list for y
xpow3 = [] #create list for x cube
sqrt_xy = [] #create list for square root of x + y

for i in range(0, 5):#read line from test and insert into x and y
    line = myfile.readline() #read line from test.csv
    temp_array = line.split(",") #split string by comma
    x.append(int(temp_array[0])) #append first string to x
    y.append(int(temp_array[1])) #append second string to y

myfile.close() #close the file

print("x x^3 y sqrt(x+y)") #print first line

for z in range(0,5):#calculate and insert data for xpow3 and sqrt, print data
    xpow3.append(x[z] ** 3) #append x cube to xpow3
    sqrt_xy.append(sqrt(x[z] + y[z]))#append square root

ax = plt.subplot(1, 2, 1) #create first subplot 1 = row, 2 =column 1 = slot
ax.plot(x,xpow3) #plot x is x axis, x power of 3 is y axis
ay = plt.subplot(1, 2, 2) #create second subplot 1 = row, 2 = column, 2 = slot
ay.plot(y, sqrt_xy) #plot y as x axis, square root of x+y is y axis
plt.show() #show the plot
