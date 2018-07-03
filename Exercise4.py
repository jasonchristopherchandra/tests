from matplotlib.pyplot import plot, show


def f(x): #estimate 2x-squared + 6x + 4
    return 2*(x**2) + 6*x + 4


def diff(x, h): #estimate fx
    return -3*f(x) - 4*(x + h) - f(x - (2*h))


x = 2
h = [0.01, 0.05, 0.1, 0.2, 0.5]
error = [] #create list named error

exact = 4 * x + 6 #from manual differentiation

for i in h: #for loop
    est = diff(x, i)  #create estimate
    err = abs(exact - est) #absolute (removing negative)(makes a non-negative number) exact- est
    error.append(err) #append err to error list
    print(exact, est, err) #print exact,estimated,absolute

plot(h,error) #plot h as x axis and error as y axis
show()
