import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

K = 10000
r = 0.5
h = 0
intensities = []
equilibriums = []
for i in range(0, 31):
    intensities.append(h)
    equilibriums.append((K*(r-h))/r)
    h+=0.05
plt.plot(intensities,equilibriums)
plt.ylabel("Vrednost tacke ekvilibrijuma")
plt.xlabel("Intenzitet ribolova")
plt.show()