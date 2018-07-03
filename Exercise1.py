import math,numpy

x = math.pi/3  #arctanvalue


def f(n): #mclaurin series
    return (-1)**n * (x)**(2*n+1) /(2*n+1)


def arctan_n_series(n):#loop for different n values
    result = 0.0
    for i in range(n):
        result += f(i)
    return result


actual = numpy.arctan(x) #get actual arctan value

n_list = [3, 5, 10, 20]#list of n

print("n  arctan(pi/3)      actual              absolute error") #print first list

for i in n_list:#for loop to get actual error and print data
    temp_arctan = arctan_n_series(i)
    abs_error = abs(temp_arctan - actual)
    print(str(i) + "  " + str(temp_arctan) + "  " + str(actual) + "  " + str(abs_error))
