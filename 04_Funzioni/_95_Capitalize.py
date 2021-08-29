def LetteraGrande(stringa):
    
   parola = stringa[0].upper() + stringa[1:]    # metto il primo carattere grande
   parola2=""

   for x in range(len(parola)):
       if parola[x] == "." or parola[x] == "?" or parola[x] == "!":
          parola2 += parola[x]                             # aggiungo sempre il punto
          for i in range(len(parola[x:])):
              d = x + 1                                    # cerco la prossima lettera dopo il punto e la ingrandisco
              if parola[d] != " ":
                  parola2 += parola[d].upper()
                  break
          
       elif parola[x] == "i":
           if parola [x-1] ==" " and parola [x+1] ==" ":
               
             parola2+= parola[x].upper()
           else:
             parola2 += parola[x]   
           
       else:
     
          parola2 += parola[x]
          

                  
               
   
       
    
    
   return parola2
    
    
    
    
print(LetteraGrande("prova? Ciao i come "))