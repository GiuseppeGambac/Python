

nomefile = input()


try:
    file = open(nomefile,"r")
except:
    print("errore")
parole =[]
dizionario ={}

for linea in file:    
 frase = linea        # leggo ogni linea
 parole = frase.split()          # creo una lista con ogni parola della linea   
 

 for i in range(len(parole)):      
  if parole[i] in dizionario:   
          dizionario[parole[i]] += 1    #se c'è l'aumento
  else:
          dizionario[parole[i]] = 1     # se non è nel dizionario la aggiungo
        
          
        
numero = 0

for i in dizionario:
    if dizionario[i] > numero:      # per ogni parola del dizionario se è stata contata più volte aumento il massimo valore e salvo l'ultima parola
        numero = dizionario[i]
        parola = i



print (parola)

        
