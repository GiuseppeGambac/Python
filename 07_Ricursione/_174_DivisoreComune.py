def Divisore(numero1, numero2):
    if numero2 == 0:
        return numero1                 
    else:
        
            c = numero1 % numero2             #il modulo è 120, rilancio la funzione con 440 e 120, ora il moduloe è 80. rilancio la funzione con 120 e 80, il modulo è 40, 
            return Divisore(numero2 ,c)       # rilancio la funzione con 80 e 40, il modulo è 0, rilancio la funzione con 40 e 0 e ora ritorna il primo numero, cioè 40
    
    
    
    
    
print(Divisore(1000,440))         
            
            
        