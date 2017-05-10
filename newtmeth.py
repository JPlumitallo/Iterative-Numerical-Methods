####################
## J plumitallo   ##
## Newt Meth      ##
####################
import time
import copy
import numpy
import matrix
import ge

#function that creates a mathematical function
def f1( x ):

    return (float(2-numpy.exp(x)+x**2)/3)-x


#function that creates a mathematical function
def f2( x ):

    return float(3*x**2-numpy.exp(x))

#function that creates a mathematical function
def f3( x ):

    return float(x**2+10*numpy.cos(x))

#function to determine the first derivative of f3
def df( func, x ):

    h = .000000001

    if(func == 1):

        z = f1
    elif(func == 2):

        z = f2

    elif( func == 3):

        z = f3

    return float(z(x+h) - z(x))/h

#function to implement newton's method
def newtmethod(func, x0, maxit, tol):

    if(func == 1):

        z = f1 
        x = 1
    elif(func == 2):

        z = f2
        x = 2
    elif( func == 3):

        z = f3
        x = 3

    for i in range(maxit):

        t = x0
         
        x0 = x0 - z(x0)/df(x,x0)

        if( abs(t-x0) < tol):

            break


    return x0

#######
#Testing Newton's method
#######

print '\nImplementing Newton\'s method...\n'

print 'The exact solution to the function 3x^2 - e^x = 0 is:', '%.16g' % newtmethod(2,3,3000,.00000001) , '\n'
