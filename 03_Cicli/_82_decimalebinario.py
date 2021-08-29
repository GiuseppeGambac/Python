

numero = int(input("Metti un numero:"))

risultato =""

q = numero

r = q %2                                # se ho del modulo   es 73 è 1
risultato = str(r) + risultato          #metto per primo uno 0 o un 1

q = q //2                               # prendo la divisione senza il modulo, quindi 36

while q > 0:
    r = q %2                           # ora è 0
    risultato = str(r) + risultato

    q = q // 2                         # via con 18 
    
    
print(risultato)