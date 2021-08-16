import math

print("inserisci il numero della casella")


casella = str(input())


if casella[0] == "a":
    
   resto = int(casella[1]) -  (  int( (int(casella[1])/2) )    *2)    # si calcola così il resto

  
   if  resto ==  1:
     print("nero")
   else:  
     print("bianco")

elif casella[0] == "b":
       
    resto = int(casella[1]) -  (  int( (int(casella[1])/2) )    *2) 

    if  resto ==  0:                                                  #nell'altra colonna faccio il contrario
     print("nero")
    else:  
     print("bianco")