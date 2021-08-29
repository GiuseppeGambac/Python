def sublist (lista1,lista2):
    if lista1 == lista2:
        return True
    
    if len(lista2) ==1:
     for x in range(len(lista2)):
        
      if lista2[x] in lista1:
        return True
    
    bool1 =False
    for x in range(len(lista2)):                         # controllo ogni valore dalla lista2
    
               
              for i in range(0,len(lista1)):              # controllo il valore con ogni valroe della lista1, se lo trovo controllo quelli dopo
                  if lista2[x] == lista1[i]:
                      numero = i                         # salvo la posizione che stavo controllando
                      for z in range(x+1,len(lista2)):     
                          numero += 1                        # controllo la posizione dopo, incrementa insieme alla z
                          if numero < len(lista1):           # eseguo il controllo in modo da evitare overflow
                           if lista2[z] == lista1[numero]:   # se il numero dopo è uguale a quello dopo dell'altro metto a True se no metto a False
                             bool1 =True
                             
                           else:
                             bool1 =False
                          else:
                              bool1 =False
                             
              if bool1 : 
                 return True                           
                      
                      

                      
         
                
            
                    
    
    return False



a = [0,1,2,3,4]
b = [0,3]

print(sublist(a,b))