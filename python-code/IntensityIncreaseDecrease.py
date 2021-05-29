import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

K = 10000
r = 0.5
l = 0.5
h = 0.75
fishCatch = []  
def lv(PG,t):
    P = PG[0]
    G = PG[1]
    Pt = r*P*(1-(P/K))-g*P*G
    Gt = l*g*P*G - h*G
    return [Pt, Gt]
t = np.linspace(0,100)
P0 = 1500
G0 = 425
g = 0.001
averages = []
intensities = []

for i in range (0,40):
    res = odeint(lv,[P0, G0], t)
    fishCatch = g*res[:,0]*res[:,1]
    averages.append(sum(fishCatch)/len(fishCatch))
    intensities.append(g)
    g *= 1.05
plt.plot(intensities,averages,'r--', linewidth=2.0)
plt.legend(["Ulov"])
plt.show()

g = 0.001
averages = []
intensities = []   
for i in range (0,40):
    res = odeint(lv,[P0, G0], t)
    fishCatch = g*res[:,0]*res[:,1]
    averages.append(sum(fishCatch)/len(fishCatch))
    intensities.append(g)
    g *= 0.95
 
plt.plot(intensities,averages,'r--', linewidth=2.0)
plt.legend(["Ulov"])
plt.show()

g = 0.0003
res = odeint(lv,[P0, G0], t)
plt.plot(t,res[:,0],'r--', linewidth=2.0)
plt.plot(t,res[:,1],'b-', linewidth=2.0)
plt.legend(["Riba","Ribari"])
plt.show()

