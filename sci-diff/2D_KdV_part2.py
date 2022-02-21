import numpy as np
import pylab as pl
import skfdiff as sf
from skfdiff import Model, Simulation
from scipy.ndimage import gaussian_filter
import math

shallow_2D = sf.Model(
    [
        "-dxU - 3*dxU*dyU - dxxxU",
        "-dx * U + dy * V"
     ], #write function here appropriately - is the last part good thou?
        ["U(x, y)", "V(x, y)"], ["e"]
)

x = np.linspace(-2, 6, 1000)
y = np.linspace(2, 6, 1000)

n = 20
U = np.log(1 + np.cosh(n) ** 2 / np.cosh(n * x) ** 2 - np.cosh(n * y) ** 2) / (2 * n) #change needed here

initial_fields = shallow_2D.fields_template(x=x, y=y, U=U, e=2e-4)

simulation = Simulation(shallow_2D, initial_fields, dt=0.05, tmax=5) #tmax=10
container = simulation.attach_container()

simulation.run()
(
    container.data.U[: -2 : container.data.t.size // 6].plot(
        col="t", col_wrap=3, color="black"
    )
)
pl.show()