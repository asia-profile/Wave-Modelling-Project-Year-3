import numpy as np
import pylab as pl
from skfdiff import Model, Simulation

def wave_sepc_density(h,D,beta,alfa,w):
    return 2*D*alfa* w**2 / (w**4 + 2*(alfa**2 - beta**2)*w**2 + (alfa**2 + beta**2)**2)

def devidtte_steerin_wheel():
    return

h3 = 0
D =  0.143*(h3**2)
beta =
alfa = 0.21beta
w = 124



uz #δz—rudder angle setting
u= uz - u#δ—rudder angle
Qmax #maximum rudder deflection
Qmin #maximum rate of turn of the rudder
St = 0.11 #propeller thrust

a1 = 0.018#coefficients determined from model tests (different for different types of vessels)
a2 = 37.2
a3 =  0.001
f = 0.014
W = 124
r1 = − 69.5
r3 = 0

x4 = −a1*x4 − a2*x4**3 + a3*u#r—angular velocity
x3 = x4 #ψ—deviation from the course

x1 = x5*np.cos(x3) − x6*np.sin(x3) #Cartesian coordinates (ship’s position)
x2 = x5*np.cos(x3) + x6*np.sin(x3)

x5 = −(f*x5) − W*x4**2 + St #longitudinal speed
x6 = −r1*x4 − r3*x4**3#transverse speed



