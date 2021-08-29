trovato = False
while not trovato:
    nomefile = input()
    try:
        file = open(nomefile, "r")
        trovato = True
    except:
        print("nome sbagliato")
        
stringa = input()

while stringa != "":
        trovato2=False
    
        numero = stringa
        
        for linee in file:                                  # leggo ogni singola linea

            frase = linee.split(",")                        # metto in una lista le varie parola separate da una virgola ed eliminandola
            for x in range(len(frase)):                     # per ogni elemento della lista
                
                if frase[0] == numero:          # se la lista è uguale a 
                 print(frase[1] + " "+ frase[2])
                 trovato2=True
                 break
             
                if frase[1] == stringa or frase[2]  == stringa + "\n":
                    print(frase[0])
                    trovato2= True
                    break
                
            if trovato2:
                break
            
            
             
   
                 
        file.seek(0)                                                 # resetto la lettura del file per il ciclo for
        stringa = input()             
                 
    
        
                
        