def determina(lista):
    errore = False
    errore2 =False
    for i in range(len(lista)-1):      #crescendo, se una valore è maggiore di quello dopo è sbagliato, se non ho errori
        if lista[i] > lista [i+1]:
            errore = True
            
        
    if not errore:
        return True
            
       
    for i in range(len(lista)-1):      #decrescente 
        if lista[i+1] > lista [i]:     
              errore2 = True 
              
    if errore and errore2:
        return False
          
    if not errore2:
        return True
          
          
       
           

      
           

lista  = [1,2,3,4]
lista2 = [4,3,2,1]
lista3 = [1,2,7,5]

print(determina(lista))

print(determina(lista2))

print(determina(lista3))