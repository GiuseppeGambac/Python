print("inserisci una ffrase")

frase = input()
errore = False

        
    
if not errore:
     
    
    stringadue=""
    lista = frase.split()                            # spezzo la frase e la metto in una lista
    
    for x in range(len(lista)):
        stringa= ""
        stringatemp =""
        parolafinale =""
      
        if lista[x][0] == "a" or lista[x][0] == "e" or lista[x][0] == "i" or lista[x][0] == "o" or lista[x][0] == "u":
            lista[x] += "way"
            print(lista[x])                                                    # se inizia con una vocale metto way alla fine
           
        else:
            stringa = list(lista[x])                                  # metto la singola parola in una lista per controllare e modificare la parola
            
            if stringa[0].isupper():
                stringatemp += stringa[0].lower()
                stringa.pop(0)

                
            while True: 
            
            
             if stringa[0] != "a"and stringa[0] != "e" and stringa[0] != "i" and stringa[0] != "o" and stringa[0] != "u":         #fino a quando non trovo una vocale
              
              stringatemp += stringa[0]
         
              stringa.pop(0)
              
             else:                                             #quando l'ho trovata
                 
                 stringa += stringatemp +"way"
                 parolafinale = parolafinale.join(stringa)     # metodo per mettere dentro in una stringa i valori di una lista
                 print(parolafinale)
                 break
        
            
         
            
        
            
          
            
            
        
    

    

                
        
     
    
        
        
        

