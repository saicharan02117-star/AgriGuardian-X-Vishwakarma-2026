"""Illustrative motor electrical transient model, not hardware verification."""
import numpy as np
from scipy.integrate import solve_ivp
Rbat=.18;Rwire=.10;Rdriver=1.7;Rmotor=2.8;Lmotor=.004;Ke=.017;Kt=.017;J=.00015;B=.00009
def run(V):
 def f(t,y):
  i,w=y
  return [(max(0,V-1.6-i*(Rbat+Rwire+Rdriver))-Rmotor*i-Ke*w)/Lmotor,(Kt*i-B*w)/J]
 return solve_ivp(f,(0,1.2),(0,0),max_step=.0006)
for v in (8.4,7.4,6.8):
 sol=run(v);print(v,sol.y[0,-1],sol.y[1,-1]*60/(2*np.pi))