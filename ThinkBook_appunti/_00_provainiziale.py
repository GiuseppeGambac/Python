import math                 # Importo la libreria Math
import time as tempo        # così posso nominare una libreria come mi pare
import random

PrezzoIntero = 24.95        # Eseguo un esercizio del libro
sconto = 0.40
primaspedizione = 3
secondaspesizione = 0.75
Librichevoglio = 60


PrezzoScontato = PrezzoIntero * (1 - sconto)

SpedizioneTotale = PrezzoScontato * 60 + 3 + (60-1) * 0.75

print(SpedizioneTotale)


input("Temperature increase (degrees Celsius): ")    # posso stampare direttamente dall'input

print(tempo.asctime())     #Stampo la data ricava dal sistema operativo


print(type(sconto))         # Così posso capire che tipo di variabile è



print(45/180.0 * math.pi)   #Provo la libreria math




def StampaQualcosa(Testo):  #definisco una funzione e la provo
     print(Testo)

StampaQualcosa('provastampa')


def ProvaEsercizio(Stringa):   ##prova di un esrcizio sulle funzioni e stringhe
    stringa1 = '               '
    print(stringa1 + Stringa)



ProvaEsercizio('ciao')


"""
Megacommento
"""

# Gestione Input
print('come ti chiami?')
testoinput = input()
print('ciao '+ testoinput)




int(input())        # In questo modo posso convertire qualsiasi variabile nel tipo che voglio 



risultato = random.sample( range(1,20),5)  # così tiro fuori una lista di numeri di un determinato range, il numero dopo indica la lunghezza della lista, i valori sono tutti diversi
print(risultato)




