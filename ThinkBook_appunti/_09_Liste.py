
lista = []

lista2 = [1,2,3,4]

lista3 =[1,2,2.034,"ciao",[1,2,3,4]]            # posso mettere elementi differenti


print(lista2[3])                                # posso sovrascrivere un elemento di una lista
lista2[3] = 10
print(lista2[3])

print(lista3[4])
lista3[4] = 3200                                 # non è checambio il valore della variabile, la sostituisco proprio come faccio qui
print(lista3[4])



if 2 in lista2:
    print("è presente")                              # così posso controllare se un valore è in una lista
    
    
for x in lista3:
    print(x)                                         # così posso scorrere la lista e la x prende il valore dell'oggetto al suo interno
    
    
for x in range(len(lista3)):                           # mentre cos' scorro la lista in base al numero di indice
    print(lista3[x])
    
    
    
a = [1,2,3]                            # così posso concatenare due liste
b = [4,5,6]

print(a+b)


print(a[1:])                  # posso prendere parte di una lista
print(a[:2])


a[1:] = [10,30]                   # posso cambiare anche una porzione di lista in questo modo

print(a)


a.append(356)                 # così aggiungo un valore alla lista
print(a)

a.insert(2,540)                 # così inserisco un valore nella posizione voluta
print(a)

c = [45,37,2,38]

c.extend(a)                  # così estendo C senza toccare a, stessa cosa che concatenare
print(c)

 
c.sort()              # così ordino i valori di una lista
print(c)



print(sum(c))    # così faccio la somma di tutti i valori


x =c.pop()                     # elimino l'ultimo elemento della listam e ti dice quale ha eliminato
print(x)

c.pop(2)                    # elimino il secondo elemento
print(c)



del c[1]            # stessa cosa del pop ma senza il return del valore
print (c)


c.remove(37)      # in questo modo rimuovo il valore selezionato, elimina il primo che prova e non tutti i valori
print (c)



stringa = "ciao"
listaparola = list(stringa)         # in questo modo creo una lista con ogni singola lettera
print(listaparola)

stringaparole = "ciao come stai?"
listaparole = stringaparole.split()
print(listaparole)                              # in questo modo spezzo la stringa in ogni singola parola

stringaparole2 ="ciao,ciao,prova"
listaparole2 = stringaparole2.split(",")     # mettendo un valore posso decidere qual'è la delimitazione delle parole
print(listaparole2)


delimitatore = ","
nuovastringa = delimitatore.join(listaparole2)    # così posso prendere una lista e collegare tutti i valori tramite il delimitatore selezionaato
print(nuovastringa)




d = [1,2,3]

e = d

if e is d:
    print("sono lo stesso oggetto")
    
e.pop()                                              # se associo in questo modo due liste faranno riferimento alla stessa area di memoria
print(d)


f = d.copy()                                # in questo modo eseguo la copia senzaz puntare alla stessa area di memoria
f.pop()
print(d)



g = [40] + d                     # oppure in questo modo posso creare una nuova lista
print(g)