"""
Disegnamo il piano a tre dimensioni al variare di x0 e x1, che sarebbero i primi due iterati del mio algoritmo iterativo

Se vado a prendere la curva di livello z = 0 sto trovando il piano ad altezza zero delle tre dimensioni

z1(x0,x1) = 2x0 - 2cos(x1) = 0
z2(x0,x1) = sin(x0) + 2x1 = 0

"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
es di input:
Z1 = 2*X-2*np.cos(Y)
Z2 = np.sin(X)+2*Y
"""
def graphic(X,Y,Z1,Z2):
    fig=plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.plot_surface(X,Y,Z1)
    ax.plot_surface(X,Y,Z2)
    plt.show()
    
    plt.contour(X,Y,Z1,levels=[0],colors='black')
    plt.contour(X,Y,Z2,levels=[0],colors='red')
    plt.show()

