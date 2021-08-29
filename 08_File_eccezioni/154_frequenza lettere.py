import sys

try:
    
 file = open(sys.argv[2],"r")
except :
    print("errore")
    
dizionario ={}   
for linea in file:    
 frase = file.readline()         # leggo ogni linea
 parole = frase.split()          # creo una lista con ogni parola della linea
 
 for i in range(len(parole)):     # per ogni parola nella lista
     
  for x in range(len(parole[i])):   # per ogni lettera nella parola
      if parole[i][x] in dizionario:   
          dizionario[parole[i][x]] += 1    #se c'è l'aumento
      else:
          dizionario[parole[i][x]] = 1     # se non è nel dizionario la aggiungo
      
file.close()     
print(dizionario)
 
 
 

