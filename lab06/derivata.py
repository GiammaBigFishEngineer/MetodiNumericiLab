import sympy as sym
from sympy.utilities.lambdify import lambdify
import numpy as np

#se uso variabili simboliche devo usare FUNZIONI SIMBOLICHE
# fs = sym.exp(-x)-(x+1)

#Funzione che prende in ingresso una funzione simbolica e restituisce la funzione derivata prima da usare numericamente
def derivata(x,fs):
    #Calcolo delle derivate tramite variabili simboliche
    #derivata simbolica
    dfs= sym.diff(fs,x,1)
    F=lambdify(x,fs,np) #funzione da simbolica ad usare numericamente
    print(dfs)
    #Il risultato è simbolico, vogliamo lamdificare (trasformare) la funzione derivata trovata in formato numerico per essere usata con i numeri
    #Passo la variabile simbolica, la funzione simbolica, la libreria numpy per usare la derivata direttamente sui vettori
    return lambdify(x,dfs,np) #derivata prima usabile numericamente