print("inserisci quanti numeri vuoi, poi di essi verrà fatta la media, se inserisci 0 inizierà il conto")
numero=int(input())






if numero == 0:
  print("il primo numero non può essere 0")

else:
    sommanumeri = 0
    totalenumeri = 0
    while numero !=0:
       sommanumeri += numero               # sommo il numero
       totalenumeri += 1                   # conteggio i numeri

       print("Inserisci un altro numero oppure inserisci 0 per stoppare")
       numero=int(input())

    media = sommanumeri / totalenumeri
    print(media)

