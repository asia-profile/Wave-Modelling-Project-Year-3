

# u t + u x + uu x - u txx = 0 which is equivalent to u t + u x + (½u²) x - u txx = 0
import numpy as np
import pylab as pl
from skfdiff import Model, Simulation
import time
# importing the module
import tracemalloc

time_start = time.perf_counter()
#run your code
# starting the monitoring
tracemalloc.start()

#model = Model("-dxU + a*dxU - b * dxxU", "U(x)", ["a", "b"])#to jest dobrze
#model = Model("-dxU + a * dxU - b*dxxU ", "U(x)", ["a", "b"]) #tego używałam
#model = Model("(-dxU - a * U * dxU)/(1 + b*dxxU) ", "U(x)", ["a", "b"])
#model = Model("-dxU + a * U * dxU -b*dxxxU", "U(x)", ["a", "b"])
model = Model("-dxU - a * U * dxU  + b*dxxU", "U(x)", ["a", "b"])


x = np.linspace(-2, 6, 1000) # evenly spaced numbers

n = 10 #n=40
U = np.log(1 + np.cosh(n) ** 2 / np.cosh(n * x) ** 2) / (2 * n)

initial_fields = model.fields_template(x=x, U=U, a=2e-4, b=1e-4) #a=2e-4, b=1e-4)

#print(model.J(initial_fields))

simulation = Simulation(model, initial_fields, dt=0.05, tmax=50) #tmax=10
container = simulation.attach_container()

simulation.run()
(
    container.data.U[: -2 : container.data.t.size // 6].plot(
        col="t", col_wrap=3, color="black"
    )
)
pl.show()

time_elapsed = (time.perf_counter() - time_start)
# displaying the memory
print(tracemalloc.get_traced_memory())

# stopping the library
tracemalloc.stop()