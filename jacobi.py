####################
## J plumitallo   ##
## matrix ops.    ##
####################
import time
import copy
import numpy
import matrix
import ge



#function to implement the Jacobi method
def jacobi( A, b, x0,xtol):

    x = []

    for tol in range(xtol):

        if(tol != 0):

            x0 = x

        x = []

        for i in range(len(A[0])):
            s = 0
            for j in range(len(A[0])):
                s+= A[i][j]*x0[j]*float(i!=j)

            x.append( (b[i]-s)/A[i][i] )

    return x

#######
#initiating tridiagonal matrix
#######

m = 16
n = 16

B = [ [0 for i in range(m)] for j in range(n)]

for i in range(m):

    for j in range(n):

        if( i == j ):
            B[i][j] = 4
        elif( i == j-1 or i == j+1 ):
            B[i][j] = -1


#######
#testing Jacobi method and comparing to gaussian elimination method
#######

b = []
for i in range(m):
    if( i == 0 or i == m):
        b.append(3)
    else:
        b.append(2)

x0 = [0 for i in range(n)]
xtol = 17

print '\n Comparing the efficiency of sparse and dense matrices by solving a linear system of the form of Ax = b (by employing the jocobi method on the sparce matrix, and gaussian elimenation on the dense matrix), where x and b are respectively vectors, and A is a matrix.'

print '\nMatrix:' , B , '\n'
print '\nb:' , b , '\n'
print '\nx0:' , x0 , '\n'

start1 = time.time()
print jacobi(B, b, x0, xtol)
end1 = time.time()
t1 = end1-start1

print '\nJacobi method complete. Time elapsed during calculation: ' , t1 , 's\n'
    ##
    #building augmented matrix
    ##
C = [[0 for i in range(m+1)] for j in range(n)]
for i in range(m):
    for j in range(n):
        if( i == j ):
            C[i][j] = 4
        elif( i == j-1 or i == j+1 ):
            C[i][j] = -1

start2 = time.time()
ge.elimination(B,b)
print ge.BackwardSubstitution(B)
end2 = time.time()
t2 = end2-start2

print '\nGaussian Elimination method complete. Time elapsed during calculation: ' , t2 , 's\n'

