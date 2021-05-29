import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

K = 10000
r = 0.5
l = 0.5
h = 0.75
    
def lv(PG,t):
    P = PG[0]
    G = PG[1]
    Pt = r*P*(1-(P/K))-g*P*G
    Gt = l*g*P*G - h*G
    return [Pt, Gt]
t = np.linspace(0,100)
P0 = 1000
hGP= -(P0**2*r-P0*K*r)/K
G0 = (P0*K*r*l - P0**2*r*l)/(h*K)
g = hGP/(P0*G0)
print(P0, G0, hGP, g)
res = odeint(lv,[P0, G0], t)
plt.plot(t,res[:,0],'r--', linewidth=2.0)
plt.plot(t,res[:,1],'b-', linewidth=2.0)
plt.axhline(y=hGP, color='g', linestyle='-')
plt.legend(["Riba","Ribari", "Ulov"])
plt.show()