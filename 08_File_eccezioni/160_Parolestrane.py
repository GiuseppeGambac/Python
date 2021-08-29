
trovato = False
while not trovato:
    nomefile = input()
    try:
        file = open(nomefile, "r")
        trovato = True
    except:
        print("nome sbagliato")
        
listanormali =[]
listaeccezioni =[]       
        
for linee in file:
    riga = linee.split()    # lista parole linea
     
    for i in range(len(riga)):    # per ogni parola
        
        for x in range(len(riga[i])-1):    # per ogni lettera
            
            if riga[i][x] == "e" and riga[i][x +1] == "i":
                
                if riga[i][x-1] == "c":
                   if not riga[i] in listanormali:
                     listanormali.append(riga[i])
                else:
                    if not riga[i] in listanormali:
                     listaeccezioni.append(riga[i])
                    
print(listanormali)
print(listaeccezioni)
            
         
    
    
    
    
    

