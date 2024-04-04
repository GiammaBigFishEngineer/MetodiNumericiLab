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
def newtonRaphson(fname,Jacname,x0,tolx,tolf,nmax):
    errors = []
    it = 0
    
    #Effettuo la prima iterazione inizializzando x0=(xk) ed x1=(xk1)
    xk = np.array(x0)
    jac = Jacname(x0)
    fxk = fname(x0)
    xk1 = xk - np.linalg.inv(jac)@fxk
    
    #Criteri di arresto nel ciclo while: il primo capisce se l'errore del valore iterato è sufficentemente piccolo.
    while it < nmax and np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) >= tolx and np.linalg.norm(fname(xk)) >= tolf:
        #Ogni ciclo calcola il nuovo iterato xk1 
        xk = xk1
        jac = Jacname(xk)
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


