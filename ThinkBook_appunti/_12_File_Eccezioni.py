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
    lista2.append( lista[i].strip()  )
print(lista2)
file.close()                # così chiudo il file