from skfdiff import Model, Simulation
import pylab as pl
import numpy as np
from scipy.signal.windows import gaussian

model = Model(["-(dx((H + h) * u) + dy((H + h) * v))",
               "-(u * dxu + v * dyu) - g * dxh + nu * (dxxu + dyyu)",
               "-(u * dxv + v * dyv) - g * dyh + nu * (dxxv + dyyv)"],
               ["h(x, y)", "u(x, y)", "v(x, y)"],
               parameters=["H(x, y)", "nu", "g"],
               boundary_conditions="periodic")

L = 10

x = y = np.linspace(-L / 2, L / 2, 56)

xx, yy = np.meshgrid(x, y, indexing="ij")

h = (gaussian(x.size, x.size // 20)[:, None] *

     gaussian(y.size, y.size // 20)[None, :]) + 1

h = np.roll(h, 12, axis=0)

h = np.roll(h, 12, axis=1)

H = np.zeros_like(h)

u = np.zeros_like(h)

v = np.zeros_like(h)

initial_fields = model.Fields(x=x, y=y, h=h, u=u, v=v, H=H, g=9.81, nu=0)

