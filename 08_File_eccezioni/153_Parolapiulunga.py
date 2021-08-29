

nomefile = input()
try:
 file = open(nomefile, "r")
except :
    print("file non esiste")
    
lunghezza = 0
conteggio = 0
listaparola = []
for x in file:                       # controllo ogni linea
    lista =  x.split()               # prendo ogni parola nella linea
    temp = 0
    for i in range(len(lista)):                  # per ogni parola controllo la lunghezza
        if len(lista[i]) > temp:
            temp = len(lista[i])
            
        if len(lista[i]) == lunghezza:
             listaparola.append(lista[i])
                          
        if temp > lunghezza:
            conteggio = 0
            lunghezza= temp  
            listaparola = []
            listaparola.append(lista[i])
            
        
file.close()           
            
            
            
            
print(lunghezza,listaparola)    