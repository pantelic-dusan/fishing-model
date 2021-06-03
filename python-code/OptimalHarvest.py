import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

K = 10000

def dP_dt(P,t=0):
    Pt = r*P*(1-(P/K))-h*P
    return Pt
t = np.linspace(0,100)

r = 0
h = 0
for i in range(0, 5):
    averages = []
    equilibriums = []
    for j in range(0, 101):
        res = odeint(dP_dt,i*100, t)
        h = (1-(j*100/K))*r
        averages.append(j*100*h)
        equilibriums.append(j*100)
    plt.plot(equilibriums, averages)
    r+=0.25
plt.legend(["r=0.00", "r=0.25", "r=0.50", "r=0.75", "r=1.00"])
plt.xlabel("Vrednost tacke ekvilibrijuma")
plt.ylabel("Kolicina ulovljene ribe")
plt.show()