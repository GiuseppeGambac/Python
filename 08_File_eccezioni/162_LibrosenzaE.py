import string

trovato = False
while not trovato:
    nomefile = input()
    try:
        file = open(nomefile, "r")
        trovato = True
    except:
        print("nome sbagliato")
        
dizionario = {}      
for linee in file:
    
    frase = linee.upper().rstrip()            # così rendo tutto grande e tolgo gli spazi
    punteggiatura = string.punctuation        # importo string e ricavo tutte le punteggiature
    for x in frase:
        if x not in dizionario:
           if x not in punteggiatura: 
            dizionario[x] = 1
        else:
           if x not in punteggiatura:  
            dizionario[x] +=1  
            
            
            
print(dizionario)


for x in dizionario:
    if dizionario[x] == min(dizionario.values()):      # controllo ogni elemento del dizionario, se un elemento è uguale al valore minore all'interno del dizionario prendo la sua chiave
        minimo = x

print(x)
    
       
        
    
        
        
    