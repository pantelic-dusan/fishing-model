import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

K = 10000
r = 0.5
g = 0.001
l = 0.5
h = 0.75
    
def lv(PG,t):
    P = PG[0]
    G = PG[1]
    Pt = r*P*(1-(P/K))-g*P*G
    Gt = l*g*P*G - h*G
    return [Pt, Gt]
t = np.linspace(0,100)
P0 = h/(g*l)
G0 = ((g*K*l - h)*r)/(g**2*K*l)
res = odeint(lv,[P0, G0], t)
plt.plot(t,res[:,0],'r--', linewidth=2.0)
plt.plot(t,res[:,1],'b-', linewidth=2.0)
plt.legend(["Riba","Ribari"])
plt.show()


res = odeint(lv,[P0 + 100, G0 + 25], t)
plt.plot(t,res[:,0],'r--', linewidth=2.0)
plt.plot(t,res[:,1],'b-', linewidth=2.0)
plt.legend(["Riba","Ribari"])
plt.show()