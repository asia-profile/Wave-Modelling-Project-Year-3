import numpy as np
from matplotlib import pyplot as plt
import numpy.linalg as la
import time
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve
from matplotlib import animation
from scipy.misc import derivative

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
    pi = derivative(pi,t)
    return pi
#function of f
def f_function(a,b,pi,x,t):
    f = a*pi_function(pi,t) + b/2 * (pi_function(pi,t))**2




n = 1000 #how many steps to - n+1
h = (900-(-100)) / n #this is our 'traingle', we get from boundary conditions, our step size
# define grid
x = np.arange(0, 2*np.pi, h)



#print(A)
#get nodes x[i]

# Get pi - each pi is the derivate of some specific p over time (of the node)
#pi = np.zeros(n+1)
#pi[1:-1] = -9.8*h**2
#pi[-1] = 50
#print(b)
#f definition
a=0
b=0
f = np.zeros((n+1)
# Get pi matrix
pi = np.zeros((n+1, n+1))
pi[0, 0] = 0 #we put in values on end boundaries
pi[n, n] = 0
#for i in range(1, n):
    #A[i, i-1] = 1
    #A[i, i] = -2
    #A[i, i+1] = 1

#trying euqation for node i
for i in range (1,n):
    pi[i] = - (1/(12*h)) *(f[i-2]-8*f[i-1]+8*f[i+1]-f[i+2]) - (1/2*(h**3)) *(-pi[i-2]+2*pi[i-1]-2*pi[i+1]+pi[i+2]) - 7/60*(h**2)* polynomial_derivative(poly, 5): + 1/90 * (h**4) * polynomial_derivative(poly, 5):



# Get b
#b = np.zeros(n+1)
#b[1:-1] = -9.8*h**2
#b[-1] = 50
#print(b)

# solve the linear equations
#y = np.linalg.solve(A, b)

#t = np.linspace(0, 5, 11)

#plt.figure(figsize=(10,8))
#plt.plot(t, y)
#plt.plot(5, 50, 'ro')
#plt.xlabel('time (s)')
#plt.ylabel('altitude (m)')
#plt.show()