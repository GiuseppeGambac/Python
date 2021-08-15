print("inserisci un mese")

mese = str(input())

print("inserisci un giorno")

giorno = int(input())


if mese == "gennaio" and giorno == 1 :
    print("nuovo anno")
elif mese == "luglio" and giorno == 1:
    print("canada day")
elif mese == "dicembre" and giorno == 25:
    print("natale")
else:
    print("nessuna festività")        