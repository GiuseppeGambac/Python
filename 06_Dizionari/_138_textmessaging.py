


dizionario ={"1" : ".,?!:", "2" :"abc", "3" : "def", "4" : "ghi" , "5" : "jkl" , "6" : "mno" , "7" : "pqrs", "8" : "wxyz" , "9" : "wxyz", "0" :" "}
             
             
stringa =input()


numeri = []
for i in range(len(stringa)):                          # per ogni lettera
            
    for x in dizionario:                                   # per ogni oggetto nel dizionario
        if stringa[i] in dizionario[x]:                    # se il carattere appare in un oggetto allora salvo quell'oggetto su una lista
           posizione = dizionario[x].find(stringa[i]) +1   # prelevo la posizione del caratte all'interno della stringa della chiave, aggiungo +1 per allungare il for 
           for z in range(posizione):                      # ripeto tot volte per simulare il T9 di un telefono
            numeri.append(x)
                
                
print(numeri)
