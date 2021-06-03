import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def dP_dt(P,t=0):
    K = 10000
    r = 0.5
    h = 0.25
    Pt = r*P*(1-(P/K))-h*P
    return Pt
t = np.linspace(0,20)

for i in range(0, 11):
    res = odeint(dP_dt,i*1000, t)
    plt.plot(t,res[:,0], linewidth=1.5)
plt.show()