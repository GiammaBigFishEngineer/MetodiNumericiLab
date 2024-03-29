"""
Algoritmo per la risoluzione di sistemi non lineari

fname: nome della funzione vettoriale di cui calcolare lo zero;
JacName: nome della funzione che calcola lo J acobiano della funzione vettoriale;
X0: vettore contenente le componenti dell'iterato iniziale);
tolx tolleranza per il test d'arresto sull'incremento ||X_{k+1}-X_k||/||X_{k}||<= tolx
tolf tolleranza per il test del residuo ||F(Xk+1)|| <= tolf;
NMAX numero massimo di iterazioni. In output devono essere restituiti il vettore contenente l'approssimazione dello zero x, un vettore contenente l'errore relativo tra due iterati successivi, il numero di iterazioni effettuate, nit.

es di input:
fname = lambda x: np.array([ 
    x[0]**2 + x[1]**2 - 9,
    x[0] + x[1] - 3
]) #sistema con f

#Costruisco lo Jacobiano di questo sistema
Jac = lambda x: np.array([ 
    [ 2*x[0], 2*x[1] ],
    [1,1]
]) #matrice Jacobbiana con dfxi/xj
"""
import numpy as np
def newtonRaphson(fname, JacName, X0, tolx, tolf, NMAX):

    Xk = np.array(X0)
    errors = []
    
    for nit in range(NMAX):
        F = fname(Xk)
        J = JacName(Xk)
        
        # Calcolo dell'incremento usando la formula di Newton-Raphson
        Xk_next = Xk - np.linalg.inv(J)@F
        
        # Calcolo dell'errore relativo tra due iterati successivi
        error = np.linalg.norm(Xk_next - Xk) / np.linalg.norm(Xk)
        errors.append(error)
        
        # Test di arresto sulla tolleranza dell'incremento
        if error <= tolx:
            break
        
        # Test di arresto sul residuo
        if np.linalg.norm(F) <= tolf:
            break
        
        Xk = Xk_next

    print("\n soluzione:",Xk,"\n errore:",errors, "Iterazioni eseguite: ", nit + 1)
    return Xk, errors, nit + 1


"""
VERSIONE NON FUNZIONANTE DELL'ALGORITMO, CAPIRE IL PERCHè

def newtonRaphson(fname,Jacname,x0,tolx,tolf,nmax):
    
    xk = np.array(x0)
    jac = Jacname(x0)
    fxk = fname(x0)
    xk1 = xk - np.linalg.inv(jac)@fxk

    while it < nmax and np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) <= tolx and np.linalg.norm(fname(xk)) <= tolf:
        xk = xk1
        jac = Jacname(xk)
        fxk = fname(xk)
        xk1 = xk - np.linalg.inv(jac)@fxk
        it = it + 1
        error = np.linalg.norm(xk1 - xk) / np.linalg.norm(xk)
        errors.append(error)
    

    if not np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) <= tolx:
        print("Arresto sulla tolleranza dell'incremento")

    if not np.linalg.norm(fname(xk1) <= tolf):
        print("Arresto sulla tolleranza del residuo")

    
    print("\n soluzione:",xk1,"\n errore:",errors, "Iterazioni eseguite: ", it)
    return xk,errors,it
"""