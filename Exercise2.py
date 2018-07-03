from math import sqrt

myfile = open("test.csv") #open test.csv

x = [] #create list x
y = [] #create list y


for i in range(0, 5):#reading data from csv and inserting into aray x and y
    line = myfile.readline() #read data from myfile
    temp_array = line.split(",") #split string by comma
    x.append(int(temp_array[0])) #append first string to x
    y.append(int(temp_array[1])) #append second string to y

myfile.close() #close test.csv

print("x x^3 y   root(x+y)")#printing first line

for z in range(0,5): #printing all data
    print(str(x[z])+ "  " + str(x[z] ** 3) + "  " + str(y[z]) + "  " + str(sqrt(x[z] + y[z])))

