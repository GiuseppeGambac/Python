

x = 0
while x <10:
    print("ciao")
    x +=1
    
    
    
for i in range (10):           # Range esegue tot volte il ciclo, partendo da 0 l'ultimo numero stampato sarà 9
    print(i)
    
    
    
# continue             # interrompo il ciclo e salto al prossimo giro
# break                 # interrompo il ciclo ed esco dal ciclo 
    
    
for i in range (10,30):           # posso decidere da dove farlo partire e arrivare   , parte da 10 e arriva a 29
    print(i)
    
for i in range (10,30,2):           # posso deveidere di quanto è il salto
    print(i)
    
    
parola = "prova"


for i in parola:                  # in questo modo posso scorrere tutta una frase, la i si adatta in base a cosa sto scorrendo
    print(i)
    
lista = [1,2,3,4,5,6,7]
  
for x in lista:                 # in questo modo si adatta e inizia a scorrete tutti gli interi
  print(x)
    
lista2 = [1,2,3,4,5,"prova",7]

# for x in lista2:               #ma se uso una lista con oggetti diversi al suo interno mi darà errore perchè la lista è scorribile sono con interi
#    print(lista2[i]) 



for x in range(len(lista2)):     # così utilizzo sempre un numero per scorrere una lista
    print(lista2[x])
    
    
    
dizionario = {"a" : 10, "b" :15 , "c" : 20}

for x in dizionario:                           # con un dizionario la x si adatta e prende il valore della chiave
    print(dizionario[x])
    print(x)                                   # stampo la chiave in questo modo