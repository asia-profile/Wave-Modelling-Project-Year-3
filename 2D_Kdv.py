import numpy as np
import pylab as pl
import skfdiff as sf
from skfdiff import Model, Simulation
from scipy.ndimage import gaussian_filter
import math

shallow_wave_2D = sf.Model(
    [
        "-dx(h * u) - dy(h * v)",
        "-upwind(u, u, x, 2) - upwind(v, u, y, 2) - g * dxh",
        "-upwind(u, v, x, 2) - upwind(v, v, y, 2) - g * dyh",
    ],
    ["h(x, y)", "u(x, y)", "v(x, y)"],
    parameters=["a", "b", "d", "f"],
)

4