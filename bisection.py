####################
## J plumitallo   ##
## Bisection meth.##
####################
import time
import copy
import numpy
import matrix
import ge

def f1( x ):

    return float(x - 2**(-x))

def f2( x ):

    return float( numpy.exp(x) + 2**(-x) + 2*numpy.cos(x) - 6)

#function to implemenet the bisection method
def bisection( low, high, its ):

    for i in range(its):

        mid = float((high+low))/2

        if( f2(mid) == 0 or float(high-low)/2 < .00001):

            break

        else:

            if( 0-f2(mid) > 0 and 0-f2(low) >0  or 0-f2(mid) < 0 and 0-f2(low) <0 ):

                low = mid

            else:

                high = mid

    return mid


#######
#testing Bisection method
#######

print '\nImplementing Bisection Method....'
print '\nThe solution to e^x + 2^(-x) + 2cos(x) - 6 = 0 on [1,2] is: x =' , bisection(1,2,100)
print '\n'

