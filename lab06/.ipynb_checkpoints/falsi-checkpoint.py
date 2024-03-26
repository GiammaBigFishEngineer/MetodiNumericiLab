from sign import sign
import math

def falsi(fname,a,b,tol,tolf,maxit):
    #funzione,estremo basso, estremo alto, tolleranza
    
    #verifico che la funzione si può applicare se f(a),f(b) sono discordi
    fa = fname(a)
    fb = fname(b)
    
    if (sign(fa)*sign(fb)) >= 0:
        print("Non è possibile applicare il metodo, non esiste una radice della funzione passata")
        return None,None,None
    
    #numero massimo iterazioni stima
    maxit = math.ceil(math.log2((b-a)/tol)-1)
    it = 0 #iterazione fatte
    v_xk = [] #vettore delle iterazione
     
    fxk = 10000.0 #inizializzo ad alto per farlo entrare nel ciclo
    
    #finchè l'intervallo trovato è maggiore della tolleranza
    while abs(b-a) > tol and it < maxit and abs(fxk) > tolf:
        #calcolo l'intersezione della nuova retta con l'asse delle x   |f(x)| nel centro > tolleranza
        xk = a - fname(a)*(b-a)/(fname(b)-fname(a))
        v_xk.append(xk)
        it = it+1
        
        #Calcolo se f(x) si annulla
        fxk = fname(xk)
        if fxk==0:
            return xk,it,v_xk
        
        #Calcolo in quale dei due intervalli la funzione assume valori discordi (soddisfa il teorema degli zeri)
        if sign(fa)*sign(fxk) > 0: #si continua a lavorare sul nuovo intervallo che sarà [xk,b]
            a=xk
            fa=fxk
        elif sign(fb)*sign(fxk) > 0:  #si continua a lavorare sul nuovo intervallo che sarà [a,xk]
            b=xk
            fb=fxk
        
    return xk,it,v_xk