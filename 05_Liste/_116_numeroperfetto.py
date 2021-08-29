from _115_Divisori import *





def numeroperfetto(numero):
    
    lista = divisori(numero)
    somma = 0
    for i in range(len(lista)):
         somma += lista[i]
         
         
    if somma == numero:
        return True
    else:
        return False
    
    
    
    
    
for i in range(1,10001):
    print( str(i)  +  str(numeroperfetto(i)))
         




