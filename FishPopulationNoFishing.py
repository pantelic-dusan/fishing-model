import numpy as np
import matplotlib.pyplot as plt
N0 = 1000
K = 10000
r = 0.3
population = [N0]
for t in range (1, 50):
    population.append(N0*np.e**(r*t)/(1+N0/K*(np.e**(r*t)-1)))

plt.plot(range(0,50), population)