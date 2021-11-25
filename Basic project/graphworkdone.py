#adding markers to graph using mathploblib
# drawing simple graph using matplotlib this is the very basic graph using just number 
import matplotlib.pyplot as plt 
plt.plot([2, 4,8,9,0,3,2,1], 
marker = 'D')
plt.show()
 # its other kind od markers used to represent data in graph whatever marks needed to represent 
 # graph are written in brackets in '' and ,
import numpy as np
import matplotlib.pyplot as plt
t = np.arrange (0., 5., 0.2)
plt.plot (t , t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

