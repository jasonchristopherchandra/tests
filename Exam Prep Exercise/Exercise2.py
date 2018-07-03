from math import sqrt

myfile = open("test.csv")

x = []
y = []


for i in range(0, 5):
    line = myfile.readline()
    temp_array = line.split(",")
    x.append(int(temp_array[0]))
    y.append(int(temp_array[1]))

myfile.close()

space = "  "
print("x x^3 y   sqrt(x+y)")

for z in range(0,5):
    print(str(x[z])+ space + str(x[z] ** 3) + space + str(y[z]) + space + str(sqrt(x[z] + y[z])))

