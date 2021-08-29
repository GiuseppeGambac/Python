from _98_numeroPrimo import *


def TrovaprossimoPrimo(numero):
    numerotrovato = False
    
    while not numerotrovato:
        numero +=1
        
        numerotrovato = NumeroPrimo(numero) 
         
          
       
    return numero
       
       
       
       
print(TrovaprossimoPrimo(99))
        







