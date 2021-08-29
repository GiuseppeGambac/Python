
aperto = False
while not aperto:
    nomefile = input()
    try:
        file = open(nomefile, "r")
        aperto = True
    except :
        "metti un altro nome"
    
    
    
fileoutput = open("commentoouput.py","w")



for linee in file:
    tuttook=True
    stringa = linee                       # prendo la linea
    lista = stringa.split()               # creo una lista con le parole della linea
    nuovafrase =""
   
    
    for i in range(len(lista)):             # controllo ogni parola delle frase
        if lista[i] == "#":                 # se una parola è uguale a # non salvo il resto della frase
            
            for x in range(i):  
             nuovafrase += lista[x]         # aggiungo alla stringa tutti i valore fino al #
             tuttook =False
             fileoutput.write(nuovafrase +"\n")
            break
        
    if tuttook:
        nuovafrase = stringa
        fileoutput.write(nuovafrase+ "\n")
        
   
    
  
    
    
    
        
file.close()
fileoutput.close()
        
        
        