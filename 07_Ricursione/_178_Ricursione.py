def palindroma (stringa):
    ok = False
     
    if stringa =="":
        return False 
    
    altraparola = stringa
    
    if stringa[0] == altraparola[len(altraparola) -1]:         #se la prima e l'ultima lettera coincidono
       if len(stringa) > 2:                                    #se non sono all'ultima comparazione
           
        ok = True                                              # ok True
        ok = palindroma(stringa[1:len(altraparola)-1])         # confronto con la parola senza i due estremi
        return ok 
       else:
           ok = True                                           #se glui ultimi due caratteri sono centrali è true
           return ok
        
    else:
        return False                                           # se non lo sono ritorno false e smetto
    
                                                    
    
print(palindroma(("anna")))
    