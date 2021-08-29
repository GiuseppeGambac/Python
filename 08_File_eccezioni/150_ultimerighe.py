try:
    
    nomefile = input()
    file =   open(nomefile , "r")
except:
    print("file non trovato")
    quit()
    



lista = file.readlines()             # metodo peggiore, leggo tutto il file e stampo le ultime 10
print(lista[len(lista)-10:])




altrometodo =[]

for linea in file:                  #leggo riga per riga e aggiungo alla lista, quando la lista è più lunga di 10 cancello l'ultima, così alla fine mi ritrovo con gli ultimi 10 caratteri
    altrometodo.append(linea)
    if len(altrometodo) > 10:
       altrometodo.pop(0)
       

print(altrometodo)
   


file.close()    # chiudo il file
    
    
    
    