def totale():
    
    numero = input("metti un numero  :")
    
    if numero == "":
        return 0.0
    else:
        return float(numero) + totale()        # chiamo un'altra volta la funzione in modo da sommare al primo numero un altro numero e così via, alla fine mi ritrovo 
                                               #  primonumero + risultatoricursioni   
    
    
    
    
    


somma = totale()
print(somma)
    
    
    
    
        
    