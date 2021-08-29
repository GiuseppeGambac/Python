print("Inserisci Giorni")
giorni = int(input())

print("Inserisci Ore")
ore = int(input())

print("Inserisci minuti")
minuti = int(input())


secondiminuti = minuti*60

secondiore = ore*60*60

secondigiorni = giorni*24*60*60


totalesecondi = secondiminuti+secondiore+secondigiorni
print(totalesecondi)