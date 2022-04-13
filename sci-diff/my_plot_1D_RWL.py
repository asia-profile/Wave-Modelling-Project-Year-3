

# u t + u x + uu x - u txx = 0 which is equivalent to u t + u x + (½u²) x - u txx = 0
import numpy as np
import pylab as pl
from skfdiff import Model, Simulation

model = Model("-U + a*dxU - b * dxxU", "U(x)", ["a", "b"])
#model = Model("-dxU - a * U * dxU + b*dxxU ", "U(x)", ["a", "b"])

x = np.linspace(-2, 6, 1000) #can start and mess a bit with numbers here, to see on accuracy and time complexity

n = 20 #n=40
U = np.log(1 + np.cosh(n) ** 2 / np.cosh(n * x) ** 2) / (2 * n)

initial_fields = model.fields_template(x=x, U=U, a=2e-4, b=1e-4) #a=2e-4, b=1e-4)

#print(model.J(initial_fields))

simulation = Simulation(model, initial_fields, dt=0.01, tmax=10) #tmax=10
container = simulation.attach_container()

simulation.run()
(
    container.data.U[: -2 : container.data.t.size // 6].plot(
        col="t", col_wrap=3, color="black"
    )
)
pl.show()
