def CambiaToken(lista):
    altralista = lista.copy()
    
    for i in range(len(altralista)):
        if altralista[i][0] == "+" :
            parola =  "u+" + altralista[i][1:]
            altralista[i] = parola
            continue
        if altralista[i][0] == "-" :
            parola =  "u-" + altralista[i][1:]
            altralista[i] = parola
            continue
        
        if i >0 :    
         if altralista[i-1] =="(" or altralista[i-1] ==")":
            if altralista[i] == "+": 
             altralista[i] = "u+"
            if altralista[i] == "-": 
             altralista[i] = "u-"
             
            
            
        
            
            
    return altralista   
        
    
"(123)+(34)"


token = ["+123","3","-45",")","-"]
print(CambiaToken(token))