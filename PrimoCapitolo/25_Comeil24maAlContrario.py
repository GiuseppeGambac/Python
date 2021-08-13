print("Inserisci totale dei secondi")
secondi = int(input())

giorni = int(secondi / (24*60*60))


ore = int((secondi - (giorni*24*60*60))   / 3600)

secondi = int(   (secondi -(giorni*24*60*60) - ore* (3600)   )                 )

print(str(giorni) + " Giorni")
print(str(ore) + " Minuti")
print(str(secondi) + " secondi")




 
#25  27 28   32    33   34

