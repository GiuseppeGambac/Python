dizionario ={}

dizionario2 = {"a":10,"b" :15, 10: 30 , 20: "ciao"}       # può esserci qualsiasi tipo di variabile sia come chiave che come valore
print(dizionario2["a"])                                   # in questo modo stampo il valore della chiave a
print(dizionario2[20])                                    # in questo modo stampo il valore della chiave 20

dizionario2.pop(20)                             # con pop devo passare la chiave in modo da eliminare quel valore
print(dizionario2)


print(dizionario2)                       # nelle nuove versioni di python i dizionari mantengono l'ordine 


valori = dizionario2.values()            # creo una lista con i valori del dizionario
print(valori)

if 10 in valori:
   print("è presente")
   
   
   
d = {}
stringa = "ciao"

for lettera in stringa:
  if lettera not in d:                # in questo modo posso aggiungere una chiave se non è presente nel dizionario
      d[lettera] = 0
  else:
      d[lettera] +=1                  # se il valore è già presente incremento il conteggio
      
      
print (d)
print(d.get('a',10))             # così posso estrapolare il valore di a, se non è presente estrapola 10
print(d.get('f',10))


for key in d:                   # così key prende il valore chiave
    print(key)                 # stampo la chiave
    print(d[key])             # stampo il valore della chiave
    
    
    
dictio = {"a" : 10 , "b" : 30, "c" :40}    
    
valorericerca = 10

for key in dictio:                            # se ho un valore del dizionario posso risalire alla chiave in questo modo
    if dictio[key] == valorericerca:
        print(key + " chiave")
        
        
stringa ="casa"        
for i in stringa:                              # ho la chiave e voglio stampare il valore
    if i in dictio:
        print(dictio[i])
        



def invertidizionario(dizionario):
    inverso = {}
    
    for key in dizionario:                 # metodo per invertire le chiave con i valori e i valori con le chiavi
        temp = dizionario[key]
        if temp not in inverso:
            inverso[temp] = key
       
    return inverso

inversione = invertidizionario(dictio)
print(inversione)