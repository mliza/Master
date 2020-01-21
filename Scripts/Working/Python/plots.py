#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(0.0, 6.2, 0.2) 
plt.plot(x,np.sin(x),'o-',x,np.cos(x),'^-')
plt.xlabel('x') 
plt.legend(('sine','cosine'),loc = 0)
plt.grid(True)
#plt.savefig('testplot.png',format='png') 
plt.show()

