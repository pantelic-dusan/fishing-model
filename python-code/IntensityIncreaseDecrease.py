import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

K = 10000

def dP_dt(P,t=0):
    Pt = r*P*(1-(P/K))-h*P
    return Pt
t = np.linspace(0,100)

r = 0
for i in range(0, 5):
    averages = []
    equilibriums = []
    h = 0
    for j in range(0, 101):
        res = odeint(dP_dt,100, t)
        h += 0.01
        averages.append(sum(res[:,0]*h)/len(res[:,0]))
        equilibriums.append(h)
    plt.plot(equilibriums, averages)
    r+=0.25
plt.legend(["r=0.00", "r=0.25", "r=0.50", "r=0.75", "r=1.00"])
plt.xlabel("Intenzitet ribolova")
plt.ylabel("Kolicina ulovljene ribe")
plt.title("P0=100")
plt.show()

r = 0
for i in range(0, 5):
    averages = []
    equilibriums = []
    h = 0
    for j in range(0, 101):
        res = odeint(dP_dt,10000, t)
        h += 0.01
        averages.append(sum(res[:,0]*h)/len(res[:,0]))
        equilibriums.append(h)
    plt.plot(equilibriums, averages)
    r+=0.25
plt.legend(["r=0.00", "r=0.25", "r=0.50", "r=0.75", "r=1.00"])
plt.xlabel("Intenzitet ribolova")
plt.ylabel("Kolicina ulovljene ribe")
plt.title("P0=10000")
plt.show()