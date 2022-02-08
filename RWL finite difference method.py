import numpy as np
from matplotlib import pyplot as plt
import numpy.linalg as la
import time
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve
from matplotlib import animation

#calculating n-th derivative of f by x or pi by x
def polynomial_derivative(poly, dev):
    if dev == 0:
        return poly[:]
    if dev > len(poly):
        return list()
    if dev < 0:
        raise ValueError("negative derivative")
    p = 1
    for k in range(2, dev+1):
        p *= k
    poly = poly[:-dev]
    n = len(poly)-1
    for i in range(len(poly)):
        poly[n-i] *= p
        p = p * (i+dev+1) // (i+1)
    return poly

#function of pi
def pi_function(pi, t):
    pi = polynomial_derivative(pi,t)
    return pi
#function of f
def f_function(a,b,pi,x,t):
    f = a*pi_function(pi,t) + b/2 * (pi_function(pi,t))**2


n = 1000 #how many steps to - n+1
h = (900-(-100)) / n #this is our 'traingle', we get from boundary conditions

# Get A
A = np.zeros((n+1, n+1))
A[0, 0] = 0 #we put in values on end boundaries
A[n, n] = 0





# Get pi
pi = np.zeros(n+1)
pi[1:-1] = -9.8*h**2
pi[-1] = 50
#print(b)
#f definition
a=0
b=0
f = np.zeros((n+1)

#for (i=0 )
#    f = a*pi[i] + b/2 * pi[i]**2
#trying euqation for node i
i=0
pi[i] = - (1/(12*h)) *(f[i-2]-8*f[i-1]+8*f[i+1]-f[i+2]) - 1/(12*(h**2))* fourth_der() + 1/90 * (h**4) * fifth_der()
