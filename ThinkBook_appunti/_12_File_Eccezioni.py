import sys


try:
    
    nomefile = input()
    file =   open(nomefile , "r")          # in questo modo apro un file in lettura, se non lo trovo mando un messaggio e fermo il programma
except:
    print("file non trovato")
    quit()
    
    
stringa =file.readline()     # con questo leggo la prima riga del file
print(stringa)
stringa= file.readline()    # se lo rilancio leggo la linea dopo
print(stringa)

lista = file.readlines()     # metto in una lista tutte le righe del file

print(lista)

lista2 =[]
for i in range(len(lista)):
    lista2.append( lista[i].strip()  )   # con questo metodo tolgo tutti gli a capo
print(lista2)



file.close()                # così chiudo il file

"""
try:
    
    nomefile = input()
    file =   open(nomefile , "w")          # in questo modo apro un file in scrittura, se non esiste viene creato
except:
    print("file non trovato")
    quit()



file.write("prova")           # scrive la prima linea del file, se lo rilancio va avanti per le altre linee
"""


import sys



try:
 i =1                                  # gli argomenti li devo aggiungere nel json di visualcode
 while i != 3:
  
    
    file =   open(sys.argv[i] , "r")   # devo importare SYS e poi devo lanciare lo script di python aggiungendo i nomi dei file
    
    for x in file:
     print(x)
     
    file.close()
    i += 1
    
except:
    print("file non trovato")
    quit()
    
