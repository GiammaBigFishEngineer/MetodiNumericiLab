"""
Algoritmo per la risoluzione di sistemi non lineari

CORDE:
piuttosto che utilizzare ad ogni iterazione il nuovo jacobiano lascia quello iniziale (elimino l'aggiornamento dello jacobiano nel while)
"""
import numpy as np
def newtonRaphsonCorde(fname,Jacname,x0,tolx,tolf,nmax):
    errors = []
    it = 0
    
    if np.linalg.det(Jacname(x0)) == 0:
        print("jacobiano di x0 nullo")
        return None,None,None
    
    #Effettuo la prima iterazione inizializzando x0=(xk) ed x1=(xk1)
    xk = np.array(x0)
    jac = Jacname(x0)
    fxk = fname(x0)
    xk1 = xk - np.linalg.inv(jac)@fxk
    
    #Criteri di arresto nel ciclo while: il primo capisce se l'errore del valore iterato è sufficentemente piccolo.
    while it < nmax and np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) >= tolx and np.linalg.norm(fname(xk)) >= tolf:
        #Ogni ciclo calcola il nuovo iterato xk1 
        xk = xk1
        fxk = fname(xk)
        xk1 = xk - np.linalg.inv(jac)@fxk
        it = it + 1
        error = np.linalg.norm(xk1 - xk) / np.linalg.norm(xk)
        errors.append(error)
    

    if not np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) >= tolx:
        print("Arresto sulla tolleranza dell'incremento")

    if not np.linalg.norm(fname(xk) >= tolf):
        print("Arresto sulla tolleranza del residuo")

    
    print("\n soluzione: ",xk1,"\n errore: ",errors, "\n Iterazioni eseguite: ", it)
    return xk,errors,it


