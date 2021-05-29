import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def lv(PG,t):
    P = PG[0]
    G = PG[1]
    K = 10000
    r = 0.5
    g = 0.001
    l = 0.5
    h = 0.75
    Pt = r*P*(1-(P/K))-g*P*G
    Gt = l*g*P*G - h*G
    return [Pt, Gt]
t = np.linspace(0,50)
res = odeint(lv,[1000, 100], t)
plt.plot(t,res[:,0],'r--', linewidth=2.0)
plt.plot(t,res[:,1],'b-', linewidth=2.0)
plt.legend(["Riba","Ribari"])
plt.show()