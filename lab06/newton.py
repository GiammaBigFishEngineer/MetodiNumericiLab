from sign import sign
import numpy as np
import math


def newton(fname, fpname, x0, tolx, tolf, nmax):
    #x0 è il primo iterato, tolleranza su x, tolleranza sulla funzione f(x), numero massimo iterazioni
    xk=[]
    #valuto la funzione su x0, calcolo x1  come intersezione della retta che è tangente in quel punto cona sse x, il punto punto di intersezione è d
    fx0 = fname(x0)
    # d è il 'primo iteratto della retta tangente con l'asse delle x (trovato facendo f(x) diviso il coefficente angolare della retta tangente
    # d è sostanzialmente la distanza fra due iterati
    d = fx0 / fpname(x0)
    x1 = x0 - d
    it = 0
    fx1 = fname(x1)
    #Entro nel while stando ai criteri di arresto
    while it < nmax and abs(fx1) >= tolf and abs(d) >= tolx*abs(x1):
        #x1 è il nuovo iterato con x0, si effettua uno swap
        x0 = x1
        fx0 = fname(x0)
        d = fx0 / fpname(x0)
        x1 = x0 - d
        fx1 = fname(x1)
        it = it + 1
        xk.append(x1)
        
    #Chiedo se mi fermo perchè ho iterazioni massime o se ho soddisfatto gli altri criteri
    
    if it == nmax:
        print("Raggiunto massimo numero di iterazioni")
    return x1,it,xk