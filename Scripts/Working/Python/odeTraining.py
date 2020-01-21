#!/usr/local/bin/python3.7
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint 

# function that returns dy/dt 
# dy/dy = -k * y(t) 
def model(y, t, k): 
    dydt = -k * y
    return dydt 

# initial condition 
y0 = 5 

# time step
t = np.linspace(0, 20) 

# solve ODE 
k = 0.1 
y1 = odeint(model, y0, t, args=(k,)) 
k = 0.2 
y2 = odeint(model, y0, t, args=(k,)) 
k = 0.5 
y3 = odeint(model, y0, t, args=(k,)) 

# plot results 
plt.plot(t, y1, 'r-', linewidth=2, label='k=0.1') 
plt.plot(t, y2, 'b-', linewidth=2, label='k=0.2') 
plt.plot(t, y3, 'g-', linewidth=2, label='k=0.5') 
plt.xlabel('time') 
plt.ylabel('y(t)') 
plt.legend(loc='best') 
plt.show() 

