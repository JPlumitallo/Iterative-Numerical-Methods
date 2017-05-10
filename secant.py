####################
## J plumitallo   ##
## lin. al. ops   ##
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

    return float((x**2)+(10*numpy.cos(x)))

#function to implement the secant method
def secant( func, x0, x, maxit, tol ):

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

        if( 0-z(x) < tol+.000001 and 0-z(x) > tol):

            break

        else:
            
            x = x0 - z(x0)*((x-x0)/(z(x)-z(x0))) 
    return x

#######
#Testing the secant method
#######

print '\nImplementing the secant  method...\n'

print 'The exact solution to the function x^2+10cos(x) = 0 is:', '%.16g' % secant(2,0,1000,12,.0000001) , '\n'
