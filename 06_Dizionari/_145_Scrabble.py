

parola = input()

dizionario = {1: "aeilnorstu" , 2:"dg",3:"bcmp",4:"fhvwy", 5:"k" , 8:"jx" , 10:"qz"}

valore = 0
for i in range(len(parola)):                                       # per ogni lettera

    for x in dizionario:                                           # per ogni oggetto nel dizionario
        for y in range(len(dizionario[x])):                        # per ogni lettera dell'oggetto del dizionario
          if dizionario[x][y] == parola[i]:                        # se la lettera è corrispondente al valore della lettera prendo su il punteggio
              valore += x
            
            
            


print (valore)