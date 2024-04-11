import numpy as np

"""
Funzione per trovare il minimo di una funzione messa a sistema attraverso l'algoritmo di newton raphson
"""

def newtonRaphsonMinimo(grad_name ,Hess_name, x0, tolx, tolf, nmax):
    errors = []
    xk = np.array(x0)
    hk = Hess_name(xk)
    gk = grad_name(xk)
    s = np.linalg.solve(hk,gk)
    xk1 = xk+s
    it = 0

    while it < nmax and np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) >= tolx and np.linalg.norm(gk) >= tolf:
        xk = xk1
        hk = Hess_name(xk)
        gk = grad_name(xk)
        s = np.linalg.solve(hk,gk)
        xk1 = xk+s
        error = np.linalg.norm(xk1 - xk) / np.linalg.norm(xk)
        errors.append(error)
        it = it + 1
    
    return xk,it,errors

