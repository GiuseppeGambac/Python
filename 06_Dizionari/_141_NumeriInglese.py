def convertinumero(numero):
    
    
    if numero < 1 or numero > 999:
        return "errore"
    
    numerolista =[]
    
    for i in range(len(str(numero))):
        numerolista.append(str(numero)[i])
    
    
    
    
    numeroparola = ""
    dizionario_centinaia = {"1":"cento" ,"2":"duecento" ,"3":"trecento", "4" : "quattrocento" , "5":"cinquecento" , "6": "seicento" , "7": "settecento" , "8": "ottocento" , "9": "novecento"}
    dizionario_decine = {"1":"dieci" ,"2":"venti" ,"3":"trentra", "4" : "quaranta" , "5":"cinquanta" , "6": "sessanta" , "7": "settanta" , "8": "ottanta" , "9": "novanta"}
    dizionario = {"1":"uno" ,"2":"due" ,"3":"tre", "4" : "quattro" , "5":"cinque" , "6": "sei" , "7": "sette" , "8": "otto" , "9": "nove"}
    


    if numero > 100: 
        
        if numerolista[0] in dizionario_centinaia:                          
           numeroparola+= dizionario_centinaia[numerolista[0]]
           
        if numerolista[1] in dizionario_decine:
           numeroparola+= dizionario_decine[numerolista[1]]
           
        if numerolista[2] in dizionario:
           numeroparola+= dizionario[numerolista[2]]
           
    elif numero < 100 and numero >= 10:
        
         if numerolista[0] in dizionario_decine:
           numeroparola+= dizionario_decine[numerolista[0]]
           
         if numerolista[1] in dizionario:
           numeroparola+= dizionario[numerolista[1]]
           
    else:
         if numerolista[0] in dizionario:
           numeroparola+= dizionario[numerolista[0]]
      
        
    
     
            
            
    return numeroparola
            
            
            
print(convertinumero(123))
print(convertinumero(10))
print(convertinumero(5))
            
            
        
        
    
    
    

    