def funzione(listainput,numero):
   
    if len(listainput) < 4:
        return "errore"
   
    lista   =  listainput.copy()       #eseguo la copia della lista, se faccio una assegnazione normale entrambe le liste farebbero riferimento allo stesso oggetto ed ogni modifica ad una andrebbe anche sull'altra
    lista.sort()                       #ordino
    
    
    for i in range(numero):
        del lista[0]                   #elimino il primo numero e l'ultimo (-1 indica l'ultimo), ad ogni ciclo la lista viene sovrascritta quindi il secondo numero diventa il primo
        del lista[-1]
   
    return lista 
   
     
     
prova = []
numero = int(input())
    
while numero !=0:
 
 prova.append(numero)
 numero = int(input())
 
 
 
print(funzione(prova,2))
print(prova)
    
    
    


    