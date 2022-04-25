
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

model = Model("-U * dxU + a * dxxU + b * dxxxU", "U(x)", ["a", "b"],  boundary_conditions="periodic")

x = np.linspace(-2, 6, 1000) #was -2 6 1000

n = 40 #was 20 if my memory is good - also used later 10 and 40
U = (np.log(1 + np.cosh(n) ** 2 / np.cosh(n * x) ** 2) / (2 * n) ) #can start and mess a bit with numbers here, to see on accuracy and time complexity

initial_fields = model.fields_template(x=x, U=U, a=2e-4, b=1e-4)#a=2e-4, b=1e-4)


simulation = Simulation(model, initial_fields, dt=0.05, tmax=50) #tmax: 10,20,30,40,50 dt: 0.05,0.1,0.15,0.2,0.25
container = simulation.attach_container()

#print(model.J(initial_fields))

simulation.run()
(
    container.data.U[: -2 : container.data.t.size // 6].plot(
        col="t", col_wrap=3, color="black"
    )
)
pl.show()

#print(U)
time_elapsed = (time.perf_counter() - time_start)
# displaying the memory
print(tracemalloc.get_traced_memory())

# stopping the library
tracemalloc.stop()