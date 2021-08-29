
trovato = False
while not trovato:
    nomefile = input()
    try:
        file = open(nomefile, "r")
        trovato = True
    except:
        print("nome sbagliato")
        
        
conteggio = 0    
ultimaparola =""
for linea in file:
    conteggio += 1
    stringa = linea
    if stringa != "/n":
        lista = stringa.split()
        if len(lista) > 0:
         
         if ultimaparola == lista[0]:                     # nel ciclo prima salvo l'ultima parola e poi la confronto con la prima
          print("%d" %conteggio + lista[0]) 
      
         if len(lista) > 1:
           
            for i in range(len(lista)-1):               # controllo ogni fine parola nella frase
                if lista[i] == lista[i+1]:
                 print("%d" %conteggio + lista[i])
                ultimaparola = lista[i+1]
            
        
file.close()
        
    
           
    
           
           
           
           